
#--------------------------------------------------------------------------------------

from fastapi import FastAPI,HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
import json
from typing import Annotated,Literal,Optional
app = FastAPI()

class Patient(BaseModel):
    
    id: Annotated[str,Field(...,description='ID of the patient',examples=['P001'])]
    name: Annotated[str,Field(...,description='name of the patient',examples=['String'])]
    city:Annotated[str,Field(...,description='city of the patient',examples=['String'])]
    age:Annotated[int,Field(...,gt=0,lt=120,description='Age of the patient')]
    gender:Annotated[Literal['Male', 'Female', 'Other', 'male', 'female', 'other'],Field(...,description='Gender of the patient')]
    height:Annotated[float,Field(...,gt=0,description='Height of the patient in Meters')]
    weight:Annotated[float,Field(...,gt=0,description='Weight of the patient in Kgs')]
    
    
    
    @computed_field
    @property
    def bmi(self)-> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obessed'
        



class Patient_Update(BaseModel):
    
    
    name: Annotated[Optional[str],Field(default=None)]
    city: Annotated[Optional[str],Field(default=None)]
    age: Annotated[Optional[int],Field(default=None,gt=0)]
    gender: Annotated[Optional[Literal['Male', 'Female', 'Other', 'male', 'female', 'other']],Field(default=None)]
    height: Annotated[Optional[float],Field(default=None,gt=0)]
    weight: Annotated[Optional[float],Field(default=None,gt=0)]
        







import json

from fastapi import FastAPI,Path, HTTPException,Query

app= FastAPI()

def load_data():
    with open("pateint.json", "r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('pateint.json','w') as f:
        json.dump(data,f)

@app.get("/")
def hello():
    return {"message": "patient Management System api"}

@app.get("/about")
def about():
    return {"message": "A fully Functional patient management system api to manage your patients records"}

@app.get("/view")
def view():
    data=load_data()
    return data


@app.get("/patient/{patient_id}")

def get_patient(patient_id:str = Path(..., description="The ID of the patient to retrieve", example="P001")):
    data = load_data()
    if patient_id in data:
            return data[patient_id]
    # return {"error": "Patient not found"}# do not give the correct status code 
    raise HTTPException(status_code=404, detail="Patient not found")



@app.get("/sort")
def sort_patients(sort_by:str=Query(..., description="sort on the basis of height, weight, BMI"),order:str=Query('Asc',description='sort in ascending or descending order')):
    
    valid_fields = ['height', 'weight', 'BMI']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"invalid sort_by value. Must be one of {valid_fields}")
    
    if order not in ['Asc', 'Desc']:
        raise HTTPException(status_code=400, detail="invalid order value. Must be 'Asc' or 'Desc'")
    
    data=load_data()
    
    sort_order =True if order =='desc' else False
    
    sorted_data= sorted(data.values(),key=lambda x: x.get(sort_by,0), reverse=sort_order)
    
    return sorted_data



@app.post('/create')
def create_patient(patient:Patient_Update):
    # load existing data 
    data=load_data()
    
    # check if the patient Already Exists
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient Already exists')
    
    # new patient added to DataBase
    data[patient.id]=patient.model_dump(exclude=['id'])
    
    #save into the json file 
    save_data(data)
    
    return JSONResponse(status_code=201,content={'message':'patient created successfully'})
    
    
    
    
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError


@app.put("/edit/{patient_id}")
def update_patient(
    patient_id: str,
    patient_update: Patient_Update
):
    
    # Load data
    data = load_data()

    # Check patient exists
    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Patient '{patient_id}' not found"
        )

    try:
        # Existing patient data
        existing_patient = data[patient_id].copy()

        # Add id because Patient model requires it
        existing_patient["id"] = patient_id

        print("\n========== UPDATE REQUEST ==========")
        print("Patient ID:", patient_id)
        print("Existing Data:", existing_patient)

        # Get only fields sent by user
        updates = patient_update.model_dump(
            exclude_unset=True
        )

        print("Incoming Updates:", updates)

        # Merge updates into existing data
        existing_patient.update(updates)

        print("Merged Data:", existing_patient)

        # Validate with full Patient model
        validated_patient = Patient(**existing_patient)

        # Convert back to dictionary
        patient_dict = validated_patient.model_dump(
            exclude={"id"}
        )

        print("Validated Data:", patient_dict)

        # Save updated patient
        data[patient_id] = patient_dict
        save_data(data)

        print("Patient updated successfully.")

        return JSONResponse(
            status_code=200,
            content={
                "message": "Patient updated successfully",
                "patient": patient_dict
            }
        )

    except ValidationError as e:

        print("\n========== VALIDATION ERROR ==========")
        print(e)

        raise HTTPException(
            status_code=422,
            detail=e.errors()
        )

    except Exception as e:

        print("\n========== UNEXPECTED ERROR ==========")
        print(str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
        
        
        
        
        
        
@app.delete("/delete/{patient_id}")
def delete_patient(patient_id:str):
    
    #Load data 
    data = load_data()
    
    
    if patient_id not in data:
        raise HTTPException(status_code=404,detail='pateint not found')
    
    del data[patient_id]
    
    save_data(data)
    
    return JSONResponse(status_code=200,content={'Message':'patient deleted'})
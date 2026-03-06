import json

from fastapi import FastAPI,Path, HTTPException,Query

app= FastAPI()

def load_data():
    with open("pateint.json", "r") as f:
        data = json.load(f)
    return data

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
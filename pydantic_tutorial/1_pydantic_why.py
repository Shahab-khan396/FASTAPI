# def insert_patient_data(name:str,age:int,):
#     if type(name)==str and type(age)==int:
#         if age<0:
#             raise ValueError ("age can't be negative ")
#         return {"message": f"Patient {name} of age {age} inserted successfully"}
#     else:
#         return TypeError("Invalid input types")
    
    
# def update_patient_data(name:str,age:int,):
#     if type(name)==str and type(age)==int:
#         return {"message": f"Patient {name} of age {age} updated successfully"}
#     else:
#         return TypeError("Invalid input types")
    
    
# insert_patient_data("shahab",22)
# # update_patient_data("shahab",21)

from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='name of the patient',description='give the name of the patient in less the 50 char',examples=['shahab','yasir'])]
    email:EmailStr
    linkedin:AnyUrl
    age:int
    weight:float=Field(gt=0,lt=120)
    married:Annotated[bool,Field(default=None,description='Is the pateint married')]
    allergies:Annotated[Optional[list[str]],Field(default=None,max_length=5)]
    contact:Optional[dict[str,str]]=None
    


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('inserted')
    
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print('updated')
    
patient_info={'name':'Shahab','email':"abc@gmail.com",'linkedin':"https://linkedin.com",'age':22,'weight':68.5,'married':True,'allergies':['polen','dust'],'contact':{'email':'abc@gmail.com','phone':'123131'}}
patient1=Patient(**patient_info)

update_patient_data(patient1)

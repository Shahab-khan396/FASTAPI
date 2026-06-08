from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float #kg
    height:float #mtr
    married:bool
    allergies:list[str]
    contact:dict[str,str]
    
    
    
    
    @computed_field
    @property
    def BMI(self)-> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact:
            raise ValueError ("patient older than 60 must have emergency contact")
        return model
    
    
    
    
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        
        valid_domains=['hbl.com','bok.com']
        #abc@gmail.com
        domain_names=value.split('@')[-1]
        
        if domain_names not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    
    @field_validator('name',mode='after')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age')
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value 
        else:
            raise ValueError("age should be in between 0 and 100")
    
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    # print(patient.linkedin)
    print(patient.age)
    # print(patient.weight)
    # print(patient.height)
    print("BMI : ",patient.BMI)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print('updated')
    
patient_info={'name':'Shahab','email':"abc@bok.com",'linkedin':"https://linkedin.com",'age':22,'weight':68.5,'height':1.73,'married':True,'allergies':['polen','dust'],'contact':{'email':'abc@gmail.com','phone':'123131'}}


patient1=Patient(**patient_info)

update_patient_data(patient1)

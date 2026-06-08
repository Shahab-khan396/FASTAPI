from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient (BaseModel):
    
    
    name: str
    gender: str='male'
    age : int
    address : Address
    
    
Address_dict ={'city':'peshawar', 'state':'KPK' , 'pin':'25000' }
address1=Address(**Address_dict)
    
Patient_dict={'name':'shahab','age':22, 'address':address1}    
Patient1=Patient(**Patient_dict)
    
temp=Patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))
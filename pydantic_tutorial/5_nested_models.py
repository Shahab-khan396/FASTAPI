from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient (BaseModel):
    
    
    name: str
    gender: str
    age : int
    address : Address
    
    
Address_dict ={'city':'peshawar', 'state':'KPK' , 'pin':'25000' }
address1=Address(**Address_dict)
    
Patient_dict={'name':'shahab','gender':'male','age':22, 'address':address1}    
Patient1=Patient(**Patient_dict)
    
print(Patient1)
print(Patient1.name)
print(Patient1.address.city)
print(Patient1.address.state)
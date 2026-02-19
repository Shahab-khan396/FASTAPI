# def get_name(full_name: str, last_name:str):
#     full_name = full_name.title()+ " " +last_name.title()
#     return full_name
# print(get_name("john", "doe")) 


def get_name_age(full_name: str, age:int):
    name_with_age =full_name.title()+ "is this age " + str(age)
    return name_with_age
print(get_name_age("john", "15")) 
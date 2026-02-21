import json

from fastapi import FastAPI

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
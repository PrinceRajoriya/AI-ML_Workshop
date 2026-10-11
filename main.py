from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

@app.get("/students/{student_id}")
def get_student(student_id: int, course: str = "Python"):
    return {"student_id": student_id, "course": course}

class Student(BaseModel):
    name: str
    email: EmailStr
    age: int
@app.post("/students/")
def create_student(student: Student):
    return{
        "message": "Student created successfully",
        "student": student.model_dump()
    }

class Product(BaseModel):
    name: str
    price: float
products = []

@app.post("/products/")
def create_product(product: Product):
    products.append(product)
    return {"message": "Product created successfully", "product": product.model_dump()}

@app.get("/products/")
def get_products():
    return {"products": [product.model_dump() for product in products]}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    if 0 <= product_id < len(products):
        return {"product": products[product_id].model_dump()}
    return {"error": "Product not found"}
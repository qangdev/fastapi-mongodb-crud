import motor.motor_asyncio

from bson import ObjectId
from decouple import config

# MONGO_URL = "mongodb://root:root@0.0.0.0:27017"
MONGO_URL = config("MONGO_URL")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

database = client.studens

student_col = database.get_collection("students")


def student_helper(student) -> dict:
    return {"id": str(student["_id"]),
            "fullname": student["fullname"],
            "email": student["email"],
            "course_of_study": student["course_of_study"],
            "year": student["year"],
            "gpa": student["gpa"]}


async def get_students():
    students = []
    async for student in student_col.find():
        students.append(student_helper(student))
    return students

async def get_student(id: str) -> dict:
    student = await student_col.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)

async def add_student(student_data: dict) -> dict:
    student = await student_col.insert_one(student_data)
    new_student = await student_col.find_one({"_id": student.inserted_id})
    return student_helper(new_student)

async def update_student(id: str, data: dict) -> bool:
    if len(data) < 1:
        return False
    student = await student_col.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await student_col.update_one({"_id": ObjectId(id)}, {"$set": data})
        return updated_student

async def delete_student(id: str) -> bool:
    student = await student_col.find_one({"_id": ObjectId(id)})
    if student:
        await student_col.delete_one({"_id": ObjectId(id)})
        return True
    else:
        return False
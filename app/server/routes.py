from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (add_student,
                                 delete_student,
                                 get_student,
                                 get_students,
                                 update_student)

from app.server.schemas import (Student,
                                UpdateStudent)

router = APIRouter()

@router.post("/", response_description="Student data added into the database")
async def route_add_student_data(student: Student = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return {"data": [new_student]}, 201

@router.get("/", response_description="Students returned")
async def route_get_students():
    students = await get_students()
    if students:
        return {"data": students}, 200
    return {"data": []}, 200

@router.get("/{id}", response_description="Students returned")
async def route_get_student(id):
    student = await get_student(id)
    if student:
        return {"data": [student]}, 200
    return {"data": []}, 200

@router.put("/{id}")
async def route_update_student(id: str, req: UpdateStudent = Body(...)):
    data = {k: v for k, v in req.dict().items() if v != None}
    updated_student = await  update_student(id, data)
    if updated_student:
        return {"message": "Student updated"}, 200
    return {"message": "An error occurred"}, 404

@router.delete("/{id}", response_description="Student has been deleted form the database")
async def route_delete_student(id):
    del_student = await delete_student(id)
    if del_student:
        return {"message": "Student deleted"}, 200
    return {"message": "An error occurred"}, 404

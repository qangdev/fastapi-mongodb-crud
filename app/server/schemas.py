from typing import Optional

from pydantic import BaseModel, EmailStr, Field



class Student(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {"example": {"fullname": "John Doe",
                                    "email": "jdie@example.com",
                                    "course_of_study": "SE",
                                    "year": 2,
                                    "gpa": 3.0}}


class UpdateStudent(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {"example": {"fullname": "John Doe",
                                    "email": "jdie@example.com",
                                    "course_of_study": "SE",
                                    "year": 2,
                                    "gpa": 3.0}}


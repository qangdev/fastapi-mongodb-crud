from fastapi import FastAPI

from app.server.routes import router as StudentRouter

app = FastAPI()
app.include_router(StudentRouter, tags=["Student"], prefix="/student")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome!"}

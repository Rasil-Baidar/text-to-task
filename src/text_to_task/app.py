import uvicorn
from fastapi import FastAPI
from text_to_task.api.main import api_router

app = FastAPI()
app.include_router(api_router)

def run()-> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI,File,UploadFile
from celery import Celery
import time
import whisper

app = FastAPI()

celery_app = Celery(
    'worker',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

model = whisper.load_model("base")

@app.get("/")
def read_root():
    return {"message": "Docker está funcionando! O ambiente está pronto."}

@app.post("/")
def post_root(myFile: UploadFile):
    path = f"uploads/{myFile.filename}"

    with open(path,"wb") as f:
        f.write(myFile.file.read())

    result = process.delay(path)
    return {"id" : result.id}

@app.get("/result/{taskId}")
def request_status(taskId: str):
    task = celery_app.AsyncResult(taskId)
    return {
        "state" : task.state,
        "result" : task.result
    }

@celery_app.task
def process(filePath: str):
    try:
        print("Resumindo...")
        result = model.transcribe(filePath) 
        transcription = result["text"].lower()
        print("Fim.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return {"transcription" : transcription}

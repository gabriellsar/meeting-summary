from fastapi import FastAPI,UploadFile
from celery import Celery
import time
import whisper
from google import genai
import os

app = FastAPI()
celery_app = Celery(
    'worker',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

API_KEY = os.getenv("GEMINI_API_KEY")

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
    result = model.transcribe(filePath)
    transcription = result["text"].lower()

    if API_KEY:
        try:
            client = genai.Client(api_key=API_KEY)
            summary = client.models.generate_content(
                model="gemini-2.5-flash",
                contents= f"""
                Você é um secretário executivo eficiente.
                Analise a seguinte transcrição de reunião e gere um resumo estruturado contendo:
                    - Tópicos Principais discutidos.
                    - Decisões tomadas.
                    - Ações futuras (To-Do list).

                Transcrição:
                {transcription}
            """)
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"Error": "Erro ao gerar resposta"}
    else:
        print("Erro ao carregar API_KEY")
        return {"Error": "Erro na API_KEY"}

    return {
        "transcription" : transcription,
        "summary": summary.text
        }

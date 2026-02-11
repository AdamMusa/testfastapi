from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home()->dict:
    return {"status": "Hello this test is done by Komguep"}

@app.get("/up")
def healthcheck()->dict:
    return {"status": "success"}
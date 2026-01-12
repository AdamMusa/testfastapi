from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home()->dict:
    return {"status": "success"}

@app.get("/up")
def healthcheck()->dict:
    return {"status": "success"}
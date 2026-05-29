from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home()->dict:
    return {"status": "This is a demo for YC"}

@app.get("/up")
def healthcheck()->dict:
    return {"status": "success"}

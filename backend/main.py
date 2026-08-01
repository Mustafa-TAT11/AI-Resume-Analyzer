from fastapi import FastAPI

app = FastAPI(title="AI Resume Analyzer API")

@app.get("/")
def read_root():
    return {"message": "AI Resume Analyzer API is running"}

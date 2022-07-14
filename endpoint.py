from fastapi import FastAPI
from uvicorn import run

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hi there!"}

if __name__ == "__main__":
    run(app=app, log_level='debug', host='0.0.0.0', port=8000)
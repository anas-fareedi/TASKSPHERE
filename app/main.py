from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def get_check():
    return {"message": "check!"}
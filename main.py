from fastapi import FastAPI
import uvicorn
app = FastAPI()

async def get_users():
    return {"user1": 1, "user2": 2, "user3": 3}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")
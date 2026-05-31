from fastapi import FastAPI,Request

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}

@app.post("/Questions")
async def Questions(req : Request):
    data = await req.json()
    prompt = data["prompt"]

    return{
        "message" : "Promt received",
        "prompt" : prompt
    }


from fastapi import FastAPI,Request

app = FastAPI()

@app.post("/Qustions")
async def Questions(req : Request):
    data = await req.json()
    prompt = data["prompt"]

    return{
        "message" : "Promt received",
        "prompt" : prompt
    }


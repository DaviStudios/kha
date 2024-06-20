from fastapi import FastAPI
import khaea


api = FastAPI()

@app.get("/val?={string}")
def hashapi(string):
    return {"hash": khaea.kha(string)}

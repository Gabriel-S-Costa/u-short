from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def heath_checker():
    return {'message': "I'm Alive."}

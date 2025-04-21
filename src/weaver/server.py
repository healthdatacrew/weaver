from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict:
    """Root endpoint that returns a simple message."""
    return {"message": "Hello World"}

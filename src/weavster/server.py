import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/api/helloworld")
async def root() -> dict:
    """Root endpoint that returns a simple message."""
    return {"message": "Hello World"}


# Static assets (JS, CSS, etc.)
app.mount("/assets", StaticFiles(directory="ui/build/client/assets"), name="ui-assets")


# Catch-all route for UI (React SPA)
@app.get("/")
@app.get("/{full_path:path}")
async def serve_ui(full_path: str) -> FileResponse:
    index_path = os.path.join("ui", "build", "client", "index.html")
    return FileResponse(index_path)

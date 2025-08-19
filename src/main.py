from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import httpx

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("src/templates/index.html") as f:
        return f.read()

@app.post("/test")
async def test_url(request: Request):
    data = await request.form()
    url = data.get("url")
    if url:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url)
                return {"status": "success", "message": f"POST request sent to {url}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    return {"status": "error", "message": "No URL provided"}

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from core import orchestrate_pipeline

app = FastAPI()

templates = Jinja2Templates(directory="src/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/sentiment-api", response_class=HTMLResponse)
def sentiment(request: Request, url: str = Form(...)):
    result = orchestrate_pipeline(url)
    return HTMLResponse(content=f"<div>Result: {result}</div>")

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from core import orchestrate_pipeline
from utils import authenticate_reddit, get_comments

app = FastAPI()
reddit = authenticate_reddit()
templates = Jinja2Templates(directory="src/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/sentiment-api", response_class=HTMLResponse)
def sentiment(request: Request, url: str = Form(...)):
    comments = get_comments(reddit, url)
    if isinstance(comments, dict):
        return HTMLResponse(content=f"<div>Result: {comments}</div>")
    else:
        result = orchestrate_pipeline(comments)
        context = {"overall_result": result[0:2], 
                   "result": result[2], 
                   "comments": comments}
        return templates.TemplateResponse(
            request=request,
            name="result_update.html",
            context=context
        )

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
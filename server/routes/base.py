from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request

templates = Jinja2Templates(directory="templates")

BaseRouter = APIRouter()
@BaseRouter.get("/", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    print("fsdf")
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

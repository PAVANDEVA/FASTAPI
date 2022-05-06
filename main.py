from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from server.routes.user import router as UsersRouter
# from server.routes.base import BaseRouter as deafult
from fastapi.responses import HTMLResponse

app = FastAPI()

# app.include_router(deafult,prefix="/index")
app.include_router(UsersRouter, tags=["Users"], prefix="/users")

# templates = Jinja2Templates(directory="templates")


# @app.get("/index/", response_class=HTMLResponse)
# async def read_item(request:Request):
#     return templates.TemplateResponse("index.html", {"request": request, "id": 56})
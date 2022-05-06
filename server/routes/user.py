from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from server.database.database import (
    retrieve_users
)
from server.models.user import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema
)

templates = Jinja2Templates(directory="templates")
router = APIRouter()
@router.get("/")
async def get_users(request:Request):
    users = await retrieve_users()
    if users:
        return templates.TemplateResponse("index.html", {"request": request,'data':users, "id": 56})
        # return ResponseModel(users, "Users data retrieved successfully")
        # return "Hello world"
    return ResponseModel(users, "Empty list returned")
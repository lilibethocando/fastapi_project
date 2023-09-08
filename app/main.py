from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import datetime
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

#models.Base.metadata.create_all(bind=engine) -- we commented this one after installing alembic.

app = FastAPI(debug=True)
app.mount("/static", StaticFiles(directory="/Users/default-admin/Desktop/fast_api/fastapi/app/static"), name="static")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

templates = Jinja2Templates(directory="/Users/default-admin/Desktop/fast_api/fastapi/app/templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    current_year = datetime.datetime.now().year
    return templates.TemplateResponse("home.html", {"request": request, "current_year": current_year})






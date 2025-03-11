import fastapi
import fastapi.staticfiles

import os

import fastapi.templating

app = fastapi.FastAPI()
templates = fastapi.templating.Jinja2Templates(os.path.abspath("templates"))

app.mount("/static", fastapi.staticfiles.StaticFiles(directory=os.path.abspath("static")), "static")
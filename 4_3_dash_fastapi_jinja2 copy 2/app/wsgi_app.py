import os
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import RedirectResponse

#from fastapi import Depends
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.dash_app import create_dash_app
#from routers import model_get

urlPath_dash = '/dash'
port_dash = 8050
app_dash = create_dash_app(requests_pathname_prefix=urlPath_dash)

#------------------
app_fastapi = FastAPI()
app_fastapi.mount(urlPath_dash, WSGIMiddleware(app_dash.server))

#app_fastapi.include_router(model_get.router)
@app_fastapi.get("/")
def redirect_root():
    url = "http://0.0.0.0:" + str(port_dash) + urlPath_dash
    response = RedirectResponse(url)
    return response

script_dir = os.path.dirname(__file__)
script_dir_abs_file_path = os.path.join(script_dir, "static/")
template_dir_abs_file_path = os.path.join(script_dir, 'templates/')
app_fastapi.mount("/static", StaticFiles(directory=script_dir_abs_file_path), name="static")
#app_fastapi.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=template_dir_abs_file_path)
#templates = Jinja2Templates(directory="templates")

@app_fastapi.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app_fastapi.get("/status")
def get_status():
    return {"status": "ok"}


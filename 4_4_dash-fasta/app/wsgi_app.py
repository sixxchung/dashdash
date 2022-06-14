from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from fastapi.middleware.wsgi import WSGIMiddleware
from app.app_dash import dash_app

from routers import model_get

urlPath_dash = '/dash'
port_dash = 8050

app_fastapi = FastAPI()
app_fastapi.mount("/dash", WSGIMiddleware(dash_app.server))

app_fastapi.include_router(model_get.router)

@app_fastapi.get("/")
async def redirect_root():
    url = "http://127.0.0.1:8888/dash"
    response = RedirectResponse(url)
    return response


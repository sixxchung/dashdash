# from app.wsgi_app import app_fastapi
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import RedirectResponse

#from app.dash_app import create_dash_app
from . import dash_app 
#from routers import model_get

urlPath_dash = '/dash'
port_dash = 8050

#------------------
app_dash = dash_app.create_dash_app(requests_pathname_prefix=urlPath_dash)
#------------------
app_fastapi = FastAPI()
app_fastapi.mount(urlPath_dash, WSGIMiddleware(app_dash.server))
#app_fastapi.include_router(model_get.router)
@app_fastapi.get("/")
def redirect_root():
    url= "http://127.0.0.1:8888/dash"
    #url = "http://0.0.0.0:" + str(port_dash) + urlPath_dash
    response = RedirectResponse(url)
    return response


@app_fastapi.get("/status")
def get_status():
    return {"status": "ok"}


port_dash = 8050
reload_fastapi = True
#------------------

if __name__ == "__main__":
    uvicorn.run("main:app_fastapi",
                #host="0.0.0.0",
                #port=port_dash,
                #reload=reload_fastapi,
                #workers=2
                )

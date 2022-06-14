import uvicorn
#from app.app_dash import dash_app

#from app.routers import model_get
from app.wsgi_app import app_fastapi

if __name__ == "__main__":
    uvicorn.run("main:app_fastapi", port=8888)

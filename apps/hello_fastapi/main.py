from fastapi import FastAPI
from database import Base, engine
from api import router
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

app = FastAPI(docs_url="/")
origins = [
    "http://localhost",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

app.include_router(router)

openapi_schema = get_openapi(
    title="Library Management API",
    version="1.0",
    description="This is a simple API to manage books in a library",
    routes=app.routes,
)
app.openapi_schema = openapi_schema

if __name__ == "__main__":
    run("main:app", host="localhost", reload=True, port=8000)

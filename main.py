from fastapi import FastAPI
from contextlib import asynccontextmanager

# from core.database import create_tables
from fastapi.middleware.cors import CORSMiddleware
from api.v1.api import router as api_router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up application...")
    # create_tables()
    print("Database tables created successfully!")
    yield
    print("Shutting down application...")


app = FastAPI(
    title="Simple API",
    version="1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*",
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Hello API"}


@app.get("/health")
async def helath():
    return {"message": "Healthy"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

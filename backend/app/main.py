from fastapi import FastAPI

from app.routes.upload import router as upload_router
from app.routes.chat import router as chat_router
from app.routes.summary import router as summary_router 

app = FastAPI(
    title="Intelligent Documentation Assistant",
    description="An AI-powered platform for understanding and interacting with technical documentation.",
    version="1.0.0"
)

# Register routers
app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(summary_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Intelligent Documentation Assistant API",
        "docs": "/docs"
    }
# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import structlog

# تنظیم لاگر برای محیط تولید/توسعه
structlog.configure()
logger = structlog.get_logger()

app = FastAPI(title="Vohu API", version="0.1.0")

# تنظیم CORS برای ارتباط با فرانت‌اند React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    logger.info("Health check requested")
    return {"status": "online", "service": "Vohu-Core"}

# مسیرهای API در آینده در اینجا mount می‌شوند
# from app.api.routes import router
# app.include_router(router, prefix="/api")

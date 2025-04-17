from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import Video

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# health-check
@app.get("/")
async def health_check():
    return {"status": "ok"}

# Include routers
app.include_router(Video.router, prefix="/api")

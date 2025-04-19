from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import Analysis

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

async def get_progress():
    # Placeholder for progress logic
    return {"progress": 50}  # Example progress value

# Include routers
app.include_router(Analysis.router, prefix="/api")


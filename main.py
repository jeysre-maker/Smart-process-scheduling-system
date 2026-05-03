from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import process_routes, scheduling_routes, analysis_routes, history_routes
from utils.db import init_db

app = FastAPI(title="Smart Process Scheduling System", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database on startup
@app.on_event("startup")
def startup_event():
    init_db()

# Register routes
app.include_router(process_routes.router, prefix="/api/processes", tags=["Processes"])
app.include_router(scheduling_routes.router, prefix="/api/scheduling", tags=["Scheduling"])
app.include_router(analysis_routes.router, prefix="/api/analysis", tags=["Analysis"])
app.include_router(history_routes.router, prefix="/api/history", tags=["History"])

@app.get("/")
def root():
    return {"message": "Smart Process Scheduling System API", "status": "running"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}

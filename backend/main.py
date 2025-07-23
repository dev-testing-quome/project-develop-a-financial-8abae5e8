import uvicorn
from fastapi import FastAPI, Request, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os

from database import SessionLocal, engine
from models import Base
from routers import users, portfolio, trading  # Add more routers as needed

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Replace with your allowed origins in production
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Dependency Injection for Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Router Inclusion
app.include_router(users.router)
app.include_router(portfolio.router)
app.include_router(trading.router)

# Health Check Endpoint
@app.get('/health')
def health_check():
    return {'status': 'ok'}

# Exception Handling
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse({'detail': exc.detail}, status_code=exc.status_code)

# Static File Serving and Frontend Routing
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
    
    @app.get("/{{"file_path:path}}")
    async def serve_frontend(file_path: str):
        if file_path.startswith("api/") or file_path == "":
            return None # Let API routes handle it or return 404 for root
        static_file = os.path.join("static", file_path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse("static/index.html") # SPA routing

# OpenAPI Documentation
app.docs_url = '/docs'
app.redoc_url = '/redoc'

# Start the application (for local development)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

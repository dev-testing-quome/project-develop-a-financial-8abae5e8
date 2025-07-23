import uvicorn
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os

from database import SessionLocal, engine
from models import Base
from routers import users, portfolio, trading, market_data # Add other routers as needed

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Replace with your allowed origins in production
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Dependency injection for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Router inclusion
app.include_router(users.router)
app.include_router(portfolio.router)
app.include_router(trading.router)
app.include_router(market_data.router) # Add other routers as needed

# Health check endpoint
@app.get('/health')
def health_check():
    return {'status': 'OK'}

# Static file serving
if os.path.exists('static'):
    app.mount('/static', StaticFiles(directory='static'), name='static')

    @app.get('/{path:path}')
    async def serve_frontend(path: str):
        if path.startswith('api'):
            return None
        file_path = os.path.join('static', path)
        if os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(os.path.join('static', 'index.html')) # SPA routing

# Exception handling
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={'detail': exc.detail})

# OpenAPI documentation
app.openapi_url = '/openapi.json'

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

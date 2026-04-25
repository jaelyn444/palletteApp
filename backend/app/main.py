from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload, mixing

app = FastAPI(title="Paint Palette API") #The title shows up in the auto-generated docs.

app.add_middleware(
    CORSMiddleware, #CROSS ORIGIN RESOURCE SHARING 
    allow_origins=["http://localhost:5173"], #Allow request from React
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api")
app.include_router(mixing.router, prefix="/api")

@app.get("/") #GET request 
def root():
    return {"message": "Paint Palette API is running"}
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, categories

app= FastAPI(title="WebCourse")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(categories.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
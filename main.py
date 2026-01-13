from fastapi import FastAPI
from routes.brcyptname import router as bcrypt_router

app = FastAPI(title="FastAPI GitHub Actions Demo")

@app.get("/")
def root():
    return {
        "status": "running",
        "message": "FastAPI is up and working 🚀"
    }

# register bcrypt router
app.include_router(bcrypt_router)

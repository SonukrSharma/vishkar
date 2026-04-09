from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import blueprint

app = FastAPI(
    title="DevBlueprint AI",
    description="Generate complete, developer-ready project blueprints from your app idea.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular dev server — expand in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blueprint.router)


@app.get("/")
def root():
    return {"message": "DevBlueprint AI is running", "version": "0.1.0"}


@app.get("/health")
def health():
    return {"status": "ok"}

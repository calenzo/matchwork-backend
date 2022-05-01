from fastapi import FastAPI
from matchworklib.routes import user_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(app_name="matchwork")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router)

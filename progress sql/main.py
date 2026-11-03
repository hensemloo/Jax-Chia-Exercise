from fastapi import FastAPI
from routers import right_windows, left_windows

app=FastAPI()

app.include_router (
right_windows.router,
prefix="/right",
tags=["Right Window Buttons"]
)

app.include_router(
left_windows.router,
prefix="/left",
tags=["Left Window Buttons"]
)
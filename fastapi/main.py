from fastapi import FastAPI
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware 

from lessons.l1_basic_get import router as basic_get_router # type: ignore
from lessons.l2_path_params import router as path_param_router 
from lessons.l3_query_params import router as query_param_router 
from lessons.l4_post_basics import router as post_router   
# from lessons.l5_post_params import router as post_param_router

# for UI lessons
from ui_practice.ui_script import router as ui_router  

app = FastAPI(title="FastAPI Learning Project")

# for UI lessons
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(basic_get_router)
app.include_router(path_param_router)
app.include_router(query_param_router)
app.include_router(post_router) 
app.include_router(ui_router)
# app.include_router(post_param_router)

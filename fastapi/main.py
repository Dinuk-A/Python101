from fastapi import FastAPI
from typing import Optional

from lessons.lesson1_basic_get import router as basic_get_router
from lessons.lesson2_path_params import router as path_param_router
from lessons.lesson3_query_params import router as query_param_router
from lessons.lesson4_post_basics import router as post_router  

app = FastAPI(title="FastAPI Learning Project")

app.include_router(basic_get_router)
app.include_router(path_param_router)
app.include_router(query_param_router)
app.include_router(post_router) 






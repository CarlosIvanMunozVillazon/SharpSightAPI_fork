from fastapi import FastAPI
import menu
from data import *
from data.ComparaisonList import ComparisonList

'''
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

'''


def __init__():
    menu.startMenu()


__init__()

import os
import openai
import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/create")
async def create(json_file):
    data = json.load(json_file)
    generate_doc(data)

@app.get("/get_ai_response")
async def get_ai_response(field_name, data):
    raise NotImplementedError

@app.get("/generate_doc")
async def generate_doc(data, template):
    raise NotImplementedError
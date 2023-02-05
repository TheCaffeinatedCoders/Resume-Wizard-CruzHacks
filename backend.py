import os
import openai
import subprocess
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from jinja2 import FileSystemLoader
from latex.jinja2 import make_env
from pdflatex import PDFLaTeX
from urllib.parse import unquote

openai.api_key = os.getenv("OPENAI_API_KEY")


app = FastAPI()

prompt = "I am a highly intelligent resume builder bot. When provided with a basic description from the user about a particular section on a resume, I generate a more beautifully written response that would look good on a resume. I make sure that in my responses I am not inventing any information or using any information that was not explicitly provided by the user. My responses are concise, accurate, and clearly represent the same meaning as the user's input, but written in a more beautiful, reputable way. My responses use exclusively user provided information, without inventing or using any information that was not explicitly provided by the user."

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return { "message": "Hello root" }

@app.get("/get-ai-response")
async def get_ai_response(field_name : str, data : str):
    field_name = unquote(field_name)
    data = unquote(data)
    print(field_name, data)
    return openai.Completion.create(
        model = 'text-davinci-003',
        prompt = f'{prompt}\n{field_name}: {data}',
        max_tokens = 150,
        temperature = 0.4
    ).choices[0].text

@app.post("/generate-doc")
async def generate_doc(data: dict):
    data = json.loads(data)
    env = make_env(loader=FileSystemLoader('.'))
    with open('template.tex', 'r') as f:
        template_text = f.read()
        #template = env.from_string(template_text)
    
    for key in data.keys():
        # get section text from start and end
        sub1 = 'start_'+key
        sub2 = 'end_'+key

        idx1 = template_text.index(sub1)
        idx2 = template_text.index(sub2)

        section_text = ''
        new_template_text = template_text
        for idx in range(idx1 + len(sub1) + 1, idx2 - 1):
            section_text += template_text[idx]
            new_template_text = new_template_text[:idx1 + len(sub1) + 1] + new_template_text[idx1 + len(sub1) + 2:]
        template_text = new_template_text

        section_template = env.from_string(section_text)

        prev_insert_idx = idx1 + len(sub1) + 1

        # check length of list of instances of section and add/render to template
        for i in range(len(data[key])):
            # add it to template underneath previous instance of section
            section_template_text = section_template.render(**data[key][i])
            template_text = template_text[:prev_insert_idx] + section_template_text + template_text[prev_insert_idx - 1:]
            prev_insert_idx += len(section_template_text) + 1
        
    response = JSONResponse(content=template_text)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return PDFLaTeX.from_string(template_text).getpdf()

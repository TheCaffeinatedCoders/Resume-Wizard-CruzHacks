import os
import openai
import json
from fastapi import FastAPI, File, UploadFile

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()
prompt = "I am a highly intelligent resume builder bot. When provided with a basic description from the user about a particular section on a resume, I generate a more beautifully written response that would look good on a resume. I make sure that in my responses I am not inventing any information or using any information that was not explicitly provided by the user. My responses are concise, accurate, and clearly represent the same meaning as the user's input, but written in a more beautiful, reputable way. My responses use exclusively user provided information, without inventing or using any information that was not explicitly provided by the user."

@app.get("/")
async def root():
    return { "message": "Hello root" }

@app.get("/get-ai-response/{field_name}/{data}")
async def get_ai_response(field_name : str, data : str):
    return openai.Completion.create(
        model = 'text-davinci-003',
        prompt = f'{prompt}\n{field_name}: {data}',
        max_tokens = 150,
        temperature = 1
    ).choices[0].text

@app.get("/generate-doc")
async def generate_doc(data: str):
    data = json.loads(data)
    with open("template.tex") as template_file:
        template_text = template_file.read()

    print(data)
    final_text = template_text.format(**data)

    return final_text
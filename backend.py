import os
import io
import openai
import subprocess
import json
# from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Response
from jinja2 import FileSystemLoader
from latex.jinja2 import make_env
from pdflatex import PDFLaTeX
from urllib.parse import unquote
from fastapi import FastAPI
from pylatex import Document, NoEscape

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
    return {"message": "Hello root"}


@app.get("/get-ai-response")
async def get_ai_response(field_name: str, data: str):
    field_name = unquote(field_name)
    data = unquote(data)
    print(field_name, data)
    return openai.Completion.create(
        model='text-davinci-003',
        prompt=f'{prompt}\n{field_name}: {data}',
        max_tokens=150,
        temperature=0.4
    ).choices[0].text


@app.post("/generate-doc")
async def generate_doc(data: dict):
    try:
        # data = json.loads(data)
        print(data)
        env = make_env(loader=FileSystemLoader('.'))
        with open('template.tex', 'r') as f:
            template_text = f.read()
            # template = env.from_string(template_text)

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
                new_template_text = new_template_text[:idx1 + len(
                    sub1) + 1] + new_template_text[idx1 + len(sub1) + 2:]
            template_text = new_template_text

            section_template = env.from_string(section_text)

            prev_insert_idx = idx1 + len(sub1) + 1

            # check length of list of instances of section and add/render to template
            for i in range(len(data[key])):
                # add it to template underneath previous instance of section
                section_template_text = section_template.render(**data[key][i])
                template_text = template_text[:prev_insert_idx] + \
                    section_template_text + template_text[prev_insert_idx - 1:]
                prev_insert_idx += len(section_template_text) + 1
        # doc = Document()
        # doc.append(NoEscape(template_text))
        # doc.generate_pdf('out', clean_tex=False)
        # Return the PDF file as a response to the client as a byte array
        # with open('out.pdf', 'rb') as f:
            # pdf = f.read()
        # Delete the PDF file
        # os.remove('out.pdf')
        # os.remove('out.tex')
        # return Response(content=pdf, media_type="application/pdf")
        # return Response(content=template_text, media_type="application/pdf")

        return template_text
        # response = JSONResponse(content=template_text)
        # response.headers["Access-Control-Allow-Origin"] = "*"
        # return PDFLaTeX.from_string(template_text).getpdf()
        # return Response(content=template_text, media_type="application/pdf")
        # pdfl = PDFLaTeX.from_jinja_template(env.from_string(template_text))
        # pdf, log, cp = pdfl.create_pdf()
        # return Response(content=pdf, media_type="application/pdf")
        # pdf, log, cp = pdfl.create_pdf();
        # headers = {'Content-Disposition': 'attachment; filename="out.pdf"'}
        # headers = {'Content-Disposition': 'inline; filename="out.pdf"'}
        # return Response(pdf, headers=headers, media_type='application/pdf')
        
    except Exception as e:
        print(e)
        return JSONResponse(content={"error": str(e)}, status_code=400)

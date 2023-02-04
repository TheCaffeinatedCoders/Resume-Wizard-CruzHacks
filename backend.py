import os
import openai
import json

def create(json_file):
    data = json.load(json_file)
    generate_doc(data)

def generate_doc(data, template):
    raise NotImplementedError
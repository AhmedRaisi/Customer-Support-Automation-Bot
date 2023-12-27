# rpa_tasks.py
import json
import random
import os

def safe_format(template, **kwargs):
    class SafeDict(dict):
        def __missing__(self, key):
            return '{' + key + '}'
    
    replacements = SafeDict(**kwargs)
    return template.format_map(replacements)

# Load templates
current_dir = os.path.dirname(__file__)
templates_dir = os.path.join(current_dir, '..', 'templates')
with open(os.path.join(templates_dir, 'general_responses.json')) as file:
    templates = json.load(file)

def generate_response(intent, context):
    # Choose a random template for the given intent
    template = random.choice(templates[intent])

    # Safely replace placeholders with context information
    response = safe_format(template, **context)

    return response

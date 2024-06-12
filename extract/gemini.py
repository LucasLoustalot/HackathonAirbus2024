import json
import google.generativeai as genai

from os import getenv

getenv('GOOGLE_API_KEY')

# Gets the list of models that support the 'generateContent' method
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

certifications = genai.protos.Schema(
    type = genai.protos.Type.ARRAY,
    items = genai.protos.Schema(type=genai.protos.Type.STRING)
)

customers = genai.protos.Schema(
    type = genai.protos.Type.ARRAY,
    items = genai.protos.Schema(type=genai.protos.Type.STRING)
)

skills = genai.protos.Schema(
    type = genai.protos.Type.ARRAY,
    items = genai.protos.Schema(type=genai.protos.Type.STRING)
)

data = genai.protos.FunctionDeclaration(
    name = "company_data",
    parameters = genai.protos.Schema(
        type = genai.protos.Type.OBJECT,
        properties = {
            'name': genai.protos.Schema(type=genai.protos.Type.STRING),
            'location': genai.protos.Schema(type=genai.protos.Type.STRING),
            'link' : genai.protos.Schema(type=genai.protos.Type.STRING),
            'contact' : genai.protos.Schema(type=genai.protos.Type.STRING),
            'turnover': genai.protos.Schema(type=genai.protos.Type.STRING),
            'size' : genai.protos.Schema(type=genai.protos.Type.STRING),
            'certifications': certifications,
            'skills': skills,
            'main_sector': genai.protos.Schema(type=genai.protos.Type.STRING),
            'main_customers': customers
        },
    )
)

model = genai.GenerativeModel('gemini-1.5-flash', tools=[data])

def get_company_data(url : str, language : str = 'en'):
    prompt = open(language + '.txt', 'r').read()
    print(f"{url} {prompt}")
    result = model.generate_content(f"{url} {prompt}", tool_config={'function_calling_config':'ANY'})
    fc = result.candidates[0].content.parts[0].function_call
    return json.dumps(type(fc).to_dict(fc), indent=4)
import os
from google.genai.client import Client 
from google.genai.errors import APIError 

print("ai_api.py loaded")
os.environ['GEMINI_API_KEY'] = "AIzaSyA7ewADKHUMhxXQQ_k-UYQzkl0lEhM2lIk"

async def _connect_llm(model_name, prompt ):    
    client = Client() 

    try:
        response = await client.aio.models.generate_content(
            model=model_name,
            contents=prompt
        )
        return response.text

    except APIError as e:
        print(f"*** (APIError) ***")
        print(f"error:  {e}")
    except Exception as e:
        print(f"***error: {e} ***")
        

async def generate_story_llm(prompt):
    model_name = 'models/gemini-2.5-flash'
    result= await _connect_llm(model_name, prompt)
    return result
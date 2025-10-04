from google.genai import Client
from google.genai.errors import APIError 

print("ai_api.py loaded")
def _connect_llm(model_name, prompt ):    
    client = Client(api_key="AIzaSyA7ewADKHUMhxXQQ_k-UYQzkl0lEhM2lIk") 
    
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        print(response.text)
        
    except APIError as e:
        print(f"*** (APIError) ***")
        print(f"error:  {e}")
    except Exception as e:
        print(f"***error: {e} ***")

def generate_story_llm(prompt):
    model_name = 'models/gemini-2.5-flash' 
    _connect_llm(model_name, prompt)
from google.genai import Client
from google.genai.errors import APIError 

def connect_llm():    
    client = Client(api_key="AIzaSyA7ewADKHUMhxXQQ_k-UYQzkl0lEhM2lIk") 
    model_name = 'models/gemini-2.5-flash' 
    
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=["Hello, can you please help me?"]
        )
        print(response.text)
        
    except APIError as e:
        print(f"*** (APIError) ***")
        print(f"error:  {e}")
    except Exception as e:
        print(f"***error: {e} ***")

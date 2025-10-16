from .prompts import build_image_prompt
from .ai_api import generate_image_async

async def image_generation(story_text, age):
    print(story_text)
    print("image_generation called") 
    for i, paragrafh in enumerate(story_text):
        prompt= build_image_prompt(story_text, age, i)
        result= await generate_image_async(prompt,i,"images")
     
    

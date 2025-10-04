from .prompts import build_story_prompt
from .ai_api import generate_story_llm
from .utils import split_by_hash_number

print("story_generator.py loaded")
async def story_generator(topic,age):
    print("Story generator")
    prompt= build_story_prompt(topic,age)
    story= await generate_story_llm(prompt)
    story_split= split_by_hash_number(story)
    for r in story_split:
        print(r)
        print("---")

    
    
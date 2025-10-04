from .prompts import build_story_prompt
from .ai_api import generate_story_llm

print("story_generator.py loaded")
def story_generator(topic,age):
    print("Story generator")
    prompt= build_story_prompt(topic,age)
    story= generate_story_llm(prompt)
    print(story)
    
    
from ast import Return
from .prompts import build_story_prompt
from .ai_api import generate_story_llm
from .utils import split_story_to_lists

print("story_generator.py loaded")
async def story_generator(topic,age):
    print("Story generator")
    prompt= build_story_prompt(topic,age)
    story= await generate_story_llm(prompt)
    print("story received:")
    hebrew_sentences, english_sentences = split_story_to_lists(story)
    return hebrew_sentences, english_sentences
    
    
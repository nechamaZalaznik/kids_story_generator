import re


def split_story_to_lists(text):

    hebrew_parts = re.split(r'#\d+\s*', text)
    hebrew_sentences = [part.strip().splitlines()[0] for part in hebrew_parts if part.strip()]

    english_parts = re.split(r'\*\d+\s*', text)
    english_sentences = [part.strip().splitlines()[0] for part in english_parts[1:] if part.strip()]  # מתחילים מ-1

    return hebrew_sentences, english_sentences

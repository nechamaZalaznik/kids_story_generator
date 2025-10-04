import re

def split_by_hash_number(text):
    parts = re.split(r'#\d+\s*', text)
    return [part.strip() for part in parts if part.strip()]

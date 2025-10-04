print("prompts.py loaded")
def build_story_prompt(topic, age):
    pages, lines_per_page = _story_length_by_age(age)

    prompt = f"""
כתוב סיפור לילד בגיל {age} בנושא "{topic}".
הסיפור צריך להיות חיובי, פשוט, ברור ומותאם לילדים בגיל הזה.
אין לכלול תוכן מפחיד, אלים או עצוב.
הסיפור יכיל ערך חינוכי עדין, למשל חברות, עזרה או סבלנות, ויכלול תיאורים קלים של צבעים, רגשות או מקומות.

מבנה:
- הסיפור יהיה באורך כ-{pages} עמודים.
- בכל עמוד יהיו כ-{lines_per_page} משפטים.
- סמני את תחילת כל עמוד עם #1, #2 וכו', כך שכל עמוד ניתן לפיצול קל לאחר מכן.
- כתבי בשפה טבעית וברורה, שמתאימה לילדים בגיל זה.
"""
    return prompt


def _story_length_by_age(age):
    """
    מחזירה מספר עמודים ושורות בכל עמוד לפי גיל הילד
    """
    if age <= 3:
        pages = 6      # 6-7 עמודים
        lines_per_page = 1  # 1-2 משפטים לעמוד
    elif 4 <= age <= 6:
        pages = 9      # 9-10 עמודים
        lines_per_page = 4  # 4-5 משפטים לעמוד
    else:
        pages = 15
        lines_per_page = 5  # 5-6 משפטים לעמוד
    
    return pages, lines_per_page
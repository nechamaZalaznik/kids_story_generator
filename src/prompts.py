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


**ביקוש לתרגום באנגלית:**
- כתבי כל עמוד פעמיים: קודם בעברית, אחר כך באנגלית.
- סמני את העמודים באנגלית עם *1, *2, *3 … באופן תואם למשפטים בעברית.
- התרגום לאנגלית צריך לשקף את המשמעות, האווירה והקונטקסט של המשפט המקורי, 
  כך שיתאים גם לשימוש ליצירת תמונה.
- אין לקצר או לשנות את המשמעות.
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

def build_image_prompt(story, age, paragraph_index):
    """
    story: רשימה של פסקאות באנגלית
    age: גיל הילד
    paragraph_index: אינדקס הפסקה ברשימה, מתחיל מ-0
    """
    if paragraph_index < 0 or paragraph_index >= len(story):
        raise ValueError("Paragraph index out of range.")

    paragraph = story[paragraph_index].strip()

    # Combine full story into one readable string
    full_story_text = " ".join(s.strip() for s in story)

    prompt = f"""generate a image
      Current scene to illustrate:
{paragraph}

Art style: light, cheerful, minimal elements.
Do not add unnecessary objects or characters.
Focus on clarity, warm colors, and gentle emotions suitable for a {age}-year-old child.

The illustration should reflect the overall mood and atmosphere of the full story:
{full_story_text}
"""
    return prompt
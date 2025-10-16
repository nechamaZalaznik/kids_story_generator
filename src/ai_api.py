import os
import aiohttp
import asyncio
from google.genai.client import Client  # type: ignore
from google.genai.errors import APIError  # type: ignore

print("ai_api.py loaded")
os.environ['GEMINI_API_KEY'] = "AIzaSyA7ewADKHUMhxXQQ_k-UYQzkl0lEhM2lIk"

async def _connect_llm(model_name, prompt ):    
    client = Client() 

    try:
        response = await client.aio.models.generate_content(
            model=model_name,
            contents=prompt
        )
        return response.text

    except APIError as e:
        print(f"*** (APIError) ***")
        print(f"error:  {e}")
    except Exception as e:
        print(f"***error: {e} ***")
        

async def generate_image_async(prompt: str, index: int, output_dir: str = "images"):
    """
    יוצרת תמונה דרך Pollinations.ai ושומרת לקובץ מקומי עם אינדקס.
    השימוש אסינכרוני (aiohttp) עם טיפול בשגיאות.
    """
    os.makedirs(output_dir, exist_ok=True)
    filename = f"scene_{index:03d}.jpg"
    output_path = os.path.join(output_dir, filename)

    url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=30) as response:
                if response.status != 200:
                    raise Exception(f"Status {response.status}")
                content = await response.read()

        with open(output_path, "wb") as f:
            f.write(content)

        print(f"✅ Saved scene {index}: {output_path}")
        return output_path

    except asyncio.TimeoutError:
        print(f"⚠️ Timeout while generating image {index}")
    except aiohttp.ClientError as e:
        print(f"⚠️ Network error on image {index}: {e}")
    except Exception as e:
        print(f"⚠️ Failed to generate image {index}: {e}")

    return None


async def generate_story_llm(prompt):
    model_name = 'models/gemini-2.5-flash'
    result= await _connect_llm(model_name, prompt)
    return result

async def generate_image(prompt):
    model_name = 'gemini-2.5-flash-image'
    result= await _connect_llm(model_name, prompt)
    return result



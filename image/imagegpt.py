import json
import os

import openai

openai.api_key = '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'

response = openai.Image.create(
    prompt="程序员",
    n=1,
    size="1024x1024",
)
image_url = response['data'][0]['url']

print(image_url)

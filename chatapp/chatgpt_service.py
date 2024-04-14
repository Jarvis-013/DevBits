# chatapp/chatgpt_service.py

import openai

openai.api_key = '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'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

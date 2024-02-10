

import openai

def generate_openai_recommendations(api_key, financial_context):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": financial_context}, {"role": "user", "content": "What are some personalized investment recommendations?"}]
    )
    return response.choices[0].message["content"]

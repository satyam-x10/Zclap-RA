# gemma2-9b-it
# llama-3.3-70b-versatile
# deepseek-r1-distill-llama-70b
# qwen-qwq-32b
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


import os
from groq import Groq


def chat_with_groq(user_input: str,model) -> str:
    
    api_key = "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"
    client = Groq(api_key=api_key)
# gemma2-9b-it , llama-3.3-70b-versatile ,whisper-large-v3 ,distil-whisper-large-v3-en
    completion =  client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": user_input}
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""

    print(f"Response from Groq: {response}")

    return response

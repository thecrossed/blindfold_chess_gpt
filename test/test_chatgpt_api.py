from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from the .env file (if present)
load_dotenv()


client = OpenAI()

def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content


text = f"""
d1
"""
prompt = f"""
simplify the text into one chess move notation that stockfish can read. Remember remove the "-" string between the positions.

For example, if I say "move my knight from g1 to f3, the answer is g1f3"

If I say Nf3, you need to figure out the starting square of this piece and combine it into the format such as g1f3. 

If the starting square is ambigous or unclear, you need to ask me what is the starting position of this piece.
```{text}```
"""
response = get_completion(prompt)
print(response)
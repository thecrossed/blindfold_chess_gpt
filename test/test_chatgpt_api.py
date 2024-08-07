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
h5
"""
prompt = f"""
Simplify the text into one chess move notation that stockfish can read, as starting square ending square.

Remember remove the "-" string between the positions.

For example, if I say "move my knight from g1 to f3, the answer format is g1f3"

If the instruction only contains the end position, such as Nf3, in the case above, you need to ask the player to clarify the starting position.

For example, you could say, do you mean the knight at g1 to f3?

The instruction is
```{text}```
"""
response = get_completion(prompt)
print(response)
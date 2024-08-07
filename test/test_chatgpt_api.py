#from openai import OpenAI
import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file (if present)
# load_dotenv()

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')


#client = OpenAI()



def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]



print('What is your move?')
first_move = input()

text = first_move
prompt = f"""
Simplify the text into one chess move notation that stockfish can read, as starting square ending square.

Remember remove the "-" string between the positions.

For example, if I say "move my knight from g1 to f3, the answer format is g1f3"

If the instruction only contains the end position, such as Nf3, in the case above, you need to ask the player to clarify the starting position.

For example, you could say, do you mean the knight at g1 to f3?

The instruction is
```{text}```
"""
response1 = get_completion(prompt)
print(response1)

print("clearify the starting position")
clearification = input()

text =  "The start position is " + clearification + ". " +  "And the end position is " +first_move
print(text)
response2 = get_completion(prompt)
print(response2)

#from openai import OpenAI
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

OPENAI_API_KEY  = os.getenv('OPENAI_API_KEY')

client = OpenAI()

prompt = """knight to f3"""

message_history = [{"role": "user", 
                    "content": """
                Instruction:
                I will give you a piece of text and simplify it as a chess notation as starting square plus ending square
                For example, if I say "I move my knight from g1 to h3", and you should give me the answer in the quote marks "g1h3".
                Rule 1:
                Remember remove anything but the notation e.g. "g1h3" in the example above.
                Rule 2:
                If my text does not clarify either starting position or the end position, you need to ask me for clarification.

                The text is below {text}
                """.format(text = prompt)}
                ]

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=message_history
)

message_history.append({"role": "user", "content": prompt})


reply_content = completion.choices[0].message.content

message_history.append({"role": "assistant", "content": reply_content})


#print(reply_content)

#print("-----")

#print(message_history)

prompt = """e4"""

message_history.append({"role": "user", "content": prompt})


completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=message_history
)

reply_content = completion.choices[0].message.content

print(reply_content)

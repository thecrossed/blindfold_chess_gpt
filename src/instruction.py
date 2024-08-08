#from openai import OpenAI
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

OPENAI_API_KEY  = os.getenv('OPENAI_API_KEY')

client = OpenAI()

def user_input():
    user_input_text = input("Please input your move\n")
    return user_input_text 

def completion_create(client = OpenAI(), model = "gpt-4o-mini", messages = []):
    client = client
    completion = client.chat.completions.create(
    model= model,
    messages = messages
    )
    return completion

def reply_create(completion):
    reply_content = completion.choices[0].message.content
    return reply_content

def message_create(role , content):
    message = {"role": role, "content": content}

    return message

def message_history_append(message_history, message):
    message_history = message_history
    message_history.append(message)
    return message_history

def message_history_init(prompt):
    message_history = [{"role": "user", 
                    "content": """
                Instruction:
                I will give you a piece of text and simplify it as a chess notation as starting square plus ending square
                For example, if I say "I move my knight from g1 to h3", and you should give me the answer in the quote marks "g1h3".
                Rule 1:
                Remember remove anything but the notation e.g. "g1h3" in the example above.
                Rule 2:
                If my text does not clarify either starting position or the end position, you need to ask me for clarification.
                Rule 3:
                If my text contain wrong chess notation, you need to ask me to correct it.

                The text is below {text}
                """.format(text = prompt)}
                ]
    return message_history

promt = user_input()
message_history = message_history_init(promt)
completion = completion_create(messages = message_history)
reply = reply_create(completion)
print(reply)
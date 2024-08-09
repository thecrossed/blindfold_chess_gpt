#from openai import OpenAI
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

OPENAI_API_KEY  = os.getenv('OPENAI_API_KEY')

client = OpenAI()

def user_input(text = "Please input your move\n"):
    user_input_text = input(text)
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


def stockfish_move(prompt):
    message_history = [{"role": "user", 
                    "content": """
                                the text is a chess move innstruction, turn it into something sounds  more natural to a human"

                                The text is below {text}
                                """.format(text = prompt)}
                ]
    return message_history


stockfish_move = stockfish_move("The move from computer is Piece.WHITE_PAWN from d2 to d4.")
completion = completion_create(messages=stockfish_move)
reply = reply_create(completion)
print(reply)
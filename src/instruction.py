#from openai import OpenAI
import os
from openai import OpenAI
import audio as a
import time

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

OPENAI_API_KEY  = os.getenv('OPENAI_API_KEY')

client = OpenAI()

init_message =  {"role": "user", 
                    "content": """
                Instruction:
                I will give you a piece of text and simplify it as a chess notation as starting square plus ending square
                For example, if I say "I move my knight from g1 to h3", and you should give me the answer inside the quote marks "g1h3".
                remember, remove the " marks in the final output.
                Rule 1:
                Remember remove anything but the notation e.g. g1h3 in the example above.
                Rule 2:
                If my text does not clarify either starting position or the end position, you need to ask me for clarification.
                Rule 3:
                If my text contain wrong chess notation, you need to ask me to correct it.
                """}

def user_input(text = "Please input your move\n"):
    user_input_text = input(text)
    return user_input_text 

def completion_create(client = OpenAI(), model = "gpt-4o-mini", messages = [init_message]):
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
    message_history.append(message)
    return message_history

msg_history = []

#move_input = user_input()        
#print(move_input)   

#message = message_create('user', move_input)

message_history = message_history_append(msg_history, init_message)

def move_instruction(input):
    move_for_stockfish = ""
    move_input = input
    while len(move_for_stockfish) != 4:
        correct_text = ""
        #print(move_input) 
        message = message_create('user', move_for_stockfish + move_input)
        history = message_history_append(message_history, message)
        creation = completion_create(messages= history)
        move_for_stockfish = reply_create(creation)
        a.text_to_audio(move_for_stockfish, "/Users/jasminezhu/blindfold_chess_gpt/resource/reply.m4a")
        a.play_audio("/Users/jasminezhu/blindfold_chess_gpt/resource/reply.m4a")
        time.sleep(3)
        print(move_for_stockfish)
        a.record("/Users/jasminezhu/blindfold_chess_gpt/resource/my_move_correct.m4a")
        correct_text = a.audio_to_text("/Users/jasminezhu/blindfold_chess_gpt/resource/my_move_correct.m4a")
        move_input = correct_text
    return  move_for_stockfish
        #print(len(move_for_stockfish))










import feedback as  fd
import instruction  as ins
import game as g
import audio as a
import  time
import stockfish_engine as s 

def main():
    # start game
    # import game module

    # ask for move audio
    a.text_to_audio("What is your move?","../resource/what_is_your_move.m4a")
    a.play_audio("resource/what_is_your_move.m4a")
    
    # record the instruction
    time.sleep(2)
    a.record("/Users/jasminezhu/blindfold_chess_gpt/resource/my_move.m4a")
    # turn the audio move into text
    instruction_text = a.audio_to_text("/Users/jasminezhu/blindfold_chess_gpt/resource/my_move.m4a")
    # translatte instruction to stockfish format
    move_for_sf = ins.move_instruction(instruction_text)
    print("Great, The move for stockfish is "  + move_for_sf)
    # stockfish return its move
    s.set_position(str(move_for_sf))
    position = s.get_fen_position()
    print("position is " + position)
    best_move, piece = s.make_best_move(position)
    print(best_move)
    print(piece)
    # trasnlate the stockfish move to human language
    stockfish_reply = s.move_instruction(best_move, piece)
    print(stockfish_reply)

    stockfish_move = fd.stockfish_move(stockfish_reply)
    completion = fd.completion_create(messages=stockfish_move)
    reply = fd.reply_create(completion)

    print(reply)
    # turn the feedback into audio
    a.text_to_audio(reply,"/Users/jasminezhu/blindfold_chess_gpt/resource/stockfish_reply.m4a")
    # play audio
    time.sleep(2)
    a.play_audio("/Users/jasminezhu/blindfold_chess_gpt/resource/stockfish_reply.m4a")
    # do it  over and over
    pass

if __name__ == "__main__":
    main()
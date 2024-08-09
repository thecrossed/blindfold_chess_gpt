from stockfish import Stockfish
import chess

# "/usr/local/Cellar/stockfish/16/bin/stockfish"
# https://chess.stackexchange.com/questions/40038/cant-properly-use-python-stockfish-package-in-mac
stockfish = Stockfish(path="/usr/local/Cellar/stockfish/16/bin/stockfish")

# starting position FEN
start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
stockfish.set_fen_position(start_fen)

# set elo rating of stockfish
stockfish.set_elo_rating(1500)

# set depth of stockfish
stockfish.set_depth(15)

get_move = stockfish.get_best_move()

#print(get_move)

def make_best_move(fen):
    stockfish.set_fen_position(fen)
    best_move = stockfish.get_best_move()
    piece = stockfish.get_what_is_on_square(best_move[:2])
    return best_move, piece


best_move, piece = make_best_move(start_fen)

def move_instruction(best_move, piece):
    text = "The move from computer is {piece} from {start} to {end}.".format(start = best_move[:2],
                                                                             end = best_move[2:],
                                                                             piece = str(piece))
    return text

print(move_instruction(best_move, piece))


# get the piece on certain positions
e1_sqaure_piece = stockfish.get_what_is_on_square("e1") # returns Stockfish.Piece.WHITE_KING
#print(e1_sqaure_piece)

# set position
#stockfish.set_position(["e2e4", "e7e6"])
e6_sqaure_piece = stockfish.get_what_is_on_square("e6") # returns Stockfish.Piece.WHITE_KING
#print(e6_sqaure_piece)

# illegal move
# Cannot make move: e2e5
# stockfish.set_position(["e2e5"])
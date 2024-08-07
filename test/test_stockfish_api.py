from stockfish import Stockfish
import chess

# "/usr/local/Cellar/stockfish/16/bin/stockfish"
# https://chess.stackexchange.com/questions/40038/cant-properly-use-python-stockfish-package-in-mac
stockfish = Stockfish(path="/usr/local/Cellar/stockfish/16/bin/stockfish")

get_move = stockfish.get_best_move()

print(get_move)

# set elo rating of stockfish
stockfish.set_elo_rating(1500)

# set depth of stockfish
stockfish.set_depth(15)

# get the piece on certain positions
e1_sqaure_piece = stockfish.get_what_is_on_square("e1") # returns Stockfish.Piece.WHITE_KING
print(e1_sqaure_piece)

# set position
stockfish.set_position(["e2e4", "e7e6"])
e6_sqaure_piece = stockfish.get_what_is_on_square("e6") # returns Stockfish.Piece.WHITE_KING
print(e6_sqaure_piece)
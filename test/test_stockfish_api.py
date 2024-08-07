from stockfish import Stockfish
import chess

# "/usr/local/Cellar/stockfish/16/bin/stockfish"
# https://chess.stackexchange.com/questions/40038/cant-properly-use-python-stockfish-package-in-mac
stockfish = Stockfish(path="/usr/local/Cellar/stockfish/16/bin/stockfish")

first_move = stockfish.get_best_move()

print(first_move)
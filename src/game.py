from stockfish_engine import Stockfish
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
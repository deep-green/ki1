import chess
import chess.pgn
import chess.uci

board = chess.Board()
pgn = open("Kasparov.pgn")
first_game = chess.pgn.read_game(pgn)
moves = first_game.main_line()
node = first_game
while not node.is_end():
    next_node = node.variations[0]
    print(board.fen())
    board.push_san(node.board().san(next_node.move))
    print(board.uci(next_node.move,chess960=None))
    #print(node.board().san(next_node.move))
    node = next_node

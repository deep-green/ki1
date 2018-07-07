import chess.pgn
import chess.uci
from src import parseFEN
from TensorflowSkripte import Moves

pathwithoutend = ""

def writeToFile(fen, move):
    fen = str(fen)
    parsedfen = parseFEN.parse(fen)
    if (parseFEN.inverted):
        move = parseFEN.invertMove(move)
    allmoves = Moves.getMoves()
    parsedmove = []
    for m in allmoves:
        if (move == m):
            parsedmove.append(1)
        else:
            parsedmove.append(0)
    fenwrite = ""
    for f in parsedfen:
        fenwrite += str(f)+","
    movewrite = ""
    for p in parsedmove:
        movewrite += str(p)+","

    with open(pathwithoutend + ".txt", "a") as myfile:
        myfile.write(fenwrite + "|" + movewrite + "\n")

board = chess.Board()
pgn = open(pathwithoutend + ".pgn")
first_game = chess.pgn.read_game(pgn)
moves = first_game.main_line()
node = first_game
while not node.is_end():
    next_node = node.variations[0]
    fen = board.fen()
    board.push_san(node.board().san(next_node.move))
    move = board.uci(next_node.move,chess960=None)
    node = next_node
    writeToFile(fen, move)


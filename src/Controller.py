import json
import sys
import imp
sys.path.insert(0,'..')
sys.path.insert(0,'../TensorflowSkripte')
sys.path.append("../TensorflowSkripte")
imp.find_module('NNController')
import NNController 
import parseFEN
import chess


game_id = -1



def init(receive):
    jsonstr = json.dumps(receive)
    jsonobj = json.loads(jsonstr)
    global game_id
    game_id = jsonobj["ID_game"]
    fen = jsonobj["FEN"]
    parsedfen = parseFEN.parse(fen)
    moves = jsonobj["turns"]
    if (parseFEN.inverted):
        moves2 = []
        for m in moves:
            moves2.append(parseFEN.invertMove(m))
        moves = moves2
    retMove = NNController.calc(parsedfen ,moves)
    if (parseFEN.inverted):
        retMove = parseFEN.invertMove(retMove)

    board = chess.Board(fen)
    chessmove = chess.Move.from_uci(retMove)
    board.push(chessmove)

    ret = {"FEN": board.fen(),
           "ID_game": game_id}
    #ret = {"Move": retMove,
    #       "ID_game": game_id}
    return ret


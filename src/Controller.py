import json
import sys
import imp
sys.path.insert(0,'..')
sys.path.insert(0,'../TensorflowSkripte')
sys.path.append("../TensorflowSkripte")
imp.find_module('NNController')
import NNController 
import parseFEN


game_id = -1

testdata = {
  "FEN": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
  "ID_game": "2",
  "color": "false",
  "turns": [
    "e2e4",
    "c2c4"
  ]
}

def init(receive):
    jsonstr = json.dumps(receive)
    jsonobj = json.loads(jsonstr)
    global game_id
    game_id = jsonobj["ID_game"]
    retMove = NNController.calc(parseFEN.parse(jsonobj["FEN"]),jsonobj["turns"])
    ret = {"Move": retMove,
           "ID_game": game_id}
    return ret

init(testdata)

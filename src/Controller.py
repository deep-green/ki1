import json
import TensorflowSkripte.NNController as NNController
import parseFEN


game_id = -1

def init(receive):
    jsonstr = json.dumps(receive)
    jsonobj = json.loads(jsonstr)
    global game_id
    game_id = jsonobj["ID_game"]
    retMove = NNController.calc(parseFEN.parse(jsonobj["FEN"]),jsonobj["turns"])
    ret = {"Move": retMove,
           "ID_game": game_id}
    return ret

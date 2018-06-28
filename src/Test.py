import json
import sys
import imp
sys.path.insert(0,'..')
import Controller
import parseFEN
testdata = {
  "FEN": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
  "ID_game": "2",
  "color": "false",
  "turns": [
    "e2e4",
    "c2c4"
  ]
}
Controller.init(testdata)

import sys
sys.path.insert(0,'./')
import ChessNeuralNetwork as ChessNeuralNetwork
def calc(parsedFEN, possibleMoves):
    move = ChessNeuralNetwork.Neural_Networke(parsedFEN,possibleMoves)
    return move

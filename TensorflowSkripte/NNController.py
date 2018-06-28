import sys
sys.path.insert(0,'./')
import ChessNeuralNetwork as ChessNeuralNetwork
def calc(parsedFEN, possibleMoves):
    #print("NNController: ", parsedFEN)
    #print("NNController: ", possibleMoves)
    #ChessNeuralNetwork.initi()
    move = ChessNeuralNetwork.Neural_Networke(parsedFEN,possibleMoves)
    print(move)
    return move

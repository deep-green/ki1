import tensorflow as tf
import parseFEN
import Moves
# Parameters
learning_rate = 0.1
num_steps = 500
batch_size = 128
display_step = 100

# Network Parameters
n_hidden_1 = 500 # 1st layer number of neurons
n_hidden_2 = 500 # 2nd layer number of neurons
n_hidden_3 = 500
num_input = 64 # Chess-Tiles
num_classes = 4032 # Moves in Chess

# tf Graph input
X = tf.placeholder("float", [None, num_input])
Y = tf.placeholder("float", [None, num_classes])

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([num_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3])),
    'out': tf.Variable(tf.random_normal([n_hidden_3, num_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'b3': tf.Variable(tf.random_normal([n_hidden_3])),
    'out': tf.Variable(tf.random_normal([num_classes]))
}


# Create model
def neural_net(x):
    # Hidden fully connected layer with 500 neurons
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    # Hidden fully connected layer with 500 neurons
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    # Hidden fully connected layer with 500 neurons
    layer_3 = tf.add(tf.matmul(layer_2, weights['h3']), biases['b3'])
    # Output fully connected layer with a neuron for each class
    out_layer = tf.matmul(layer_3, weights['out']) + biases['out']
    return out_layer
arr = []
for x in range(64):
    arr.append(x)
arrr = [arr]
prr= []
for y in range(4032):
    prr.append(0)
prrr = [prr]

#FEN
#FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
#listvar = parseFEN.parse(FEN)
#inputlist = [listvar]

# Construct model
logits = neural_net(X)
ses = None 
def initi():    
    global ses
    ses = tf.Session()
    writer = tf.summary.FileWriter("output",ses.graph)
    ses.run(tf.global_variables_initializer())
    writer.close
    
def Neural_Networke(parsedFEN, possibleMoves):
    inputlist = [parsedFEN]
    test = []
    moves = possibleMoves  
    test = ses.run(logits, feed_dict={X: inputlist, Y: prrr})
    tesst = test[0]
    tesst = tesst.tolist()
    maxval = max(tesst)
    minval = min(tesst)
    for x in range(0,len(tesst)):
        y = (tesst[x]-minval)/(maxval-minval)
        tesst[x] = y
    maxval = max(tesst)
    minval = min(tesst)    
    turns = Moves.getMoves()
    for x in tesst:
        ind = tesst.index(maxval)
        #print(str(tesst[ind]) + ": " + turns[ind])
        if(turns[ind] in moves):
            print(str(tesst[ind]) + ": " + turns[ind])
            return turns[ind]
        tesst[ind] = -1
        maxval = max(tesst)
    

    

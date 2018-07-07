import tensorflow as tf
import parseFEN
import Moves
# Parameters
learning_rate = 0.1
num_steps = 500
batch_size = 512#128
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
    tf.nn.relu(layer_1)
    # Hidden fully connected layer with 500 neurons
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    tf.nn.relu(layer_2)
    # Hidden fully connected layer with 500 neurons
    layer_3 = tf.add(tf.matmul(layer_2, weights['h3']), biases['b3'])
    tf.nn.relu(layer_3)
    # Output fully connected layer with a neuron for each class
    out_layer = tf.matmul(layer_3, weights['out']) + biases['out']
    tf.nn.relu(out_layer)
    return out_layer
arr = []
for x in range(64):
    arr.append(x)
arrr = [arr]
prr= []
for y in range(4032):
    prr.append(0)
prrr = [prr]


#Init Saver
saver = tf.train.Saver()

# Construct model
logits = neural_net(X)
ses = None 
def initi():    
    global ses
    ses = tf.Session()
    writer = tf.summary.FileWriter("output",ses.graph)
    #ses.run(tf.global_variables_initializer())
    #save_path = saver.save(ses, "./tmp/model.ckpt")
    print("Model saved in path: %s" % save_path)
    writer.close
    
def Neural_Networke(parsedFEN, possibleMoves):
    ses = tf.Session()
    #ses.run(tf.global_variables_initializer())
    saver.restore(ses, "./tmp2/model.ckpt")
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
    #save_path = saver.save(ses, "/tmp/model.ckpt")
    print("Model saved in path2: %s" % save_path)
    

def readpgn():
    li = []
    liinput = []
    lioutput = []
    f = open('A02.txt', 'r')
    for line in f:
        #Input
        strinput = line.split("|")[0]
        strinput = strinput.split(",")
        del strinput[64:]
        for x in range(0, len(strinput)):
            strinput[x] = float(strinput[x])
        #Output
        stroutput = line.split("|")[1]
        stroutput = stroutput.split(",")
        del stroutput[4032:]
        for x in range(0, len(stroutput)):
            stroutput[x] = float(stroutput[x])
        liinput.append(strinput)
        lioutput.append(stroutput)
    li.append(liinput)
    li.append(lioutput)
    f.close()
    return li
    
def restore():
    ses = tf.Session()
    saver.restore(ses, "./tmp/model.ckpt")

def train_neural_network(x):
    inoutlist = readpgn()
    ses = tf.Session()
    inlist = inoutlist[0]
    outlist = inoutlist[1]
    prediction = neural_net(x)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=Y) )
    optimizer = tf.train.AdamOptimizer().minimize(cost)
    hm_epochs = 100
    ses.run(tf.global_variables_initializer())
    for epoch in range(hm_epochs):
        epoch_loss = 0
        for _ in range(int(len(inlist)/batch_size)):
             epoch_x = inlist[(_*batch_size):(batch_size*_+batch_size)]
             epoch_y = outlist[(_*batch_size):(batch_size*_+batch_size)]
             _, c = ses.run([optimizer, cost], feed_dict={X: epoch_x, Y: epoch_y})
             epoch_loss += c
        print('Epoch', epoch, 'completed out of',hm_epochs,'loss:',epoch_loss)
        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        save_path = saver.save(ses, "./tmp/model.ckpt")
        print("Model saved in path2: %s" % save_path)
        #print('Accuracy:',accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))
    save_path = saver.save(ses, "./tmp/model.ckpt")
    print("Model saved in path2: %s" % save_path)


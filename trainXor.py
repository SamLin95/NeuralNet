from NeuralNet import buildNeuralNet

xOrData = ([([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0]), ([0, 0], [0])], [([0, 1], [1]), ([1, 0], [1]), ([1,1], [0]), ([0, 0], [0])])
accurList = []
def trainXorData(hiddenLayer):
	return buildNeuralNet(examples=xOrData, hiddenLayerList=hiddenLayer, maxItr=10000)

trainXorData([])

for perceptronNum in range(0, 50):
	nnet,accur=trainXorData([perceptronNum])

print "result for (0, 1)" + nnet.feedForward([0, 1])[-1]
print "result for (1, 1)" + nnet.feedForward([1, 1])[-1]
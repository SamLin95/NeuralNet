from Testing import *

for layerNum in range(0, 45, 5):
	out = []
	for iteration in range(0, 6):
		print "running iteration %d for neuron number of %d: "%(iteration, layerNum)
		outNN, accur = testCarData(hiddenLayers=[layerNum])
		out.append(accur)
	print 'test over for neuron Number %d'%(layerNum,)
	print "average: %f"%(average(out))
	print "stDeviation: %f"%(stDeviation(out))
	print "max: %f \n"%(max(out))
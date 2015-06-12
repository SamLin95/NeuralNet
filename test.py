
"""this is the script for question 5"""

from Testing import *

print "start testing PenData....."
outPut = []
for i in range(5):
	print "start iteration %s......"%(i,)
	outNNet, accuracy = testPenData()
	outPut.append(accuracy)

print 'test over ......'
print "average: %f"%(average(outPut))
print "stDeviation: %f"%(stDeviation(outPut))
print "max: %f"%(max(outPut))

print "start testing CarData....."
outPut = []
for i in range(5):
	print "start iteration %s......"%(i,)
	outNNet, accuracy = testCarData()
	outPut.append(accuracy)

print 'test over ......'
print "average: %f"%(average(outPut))
print "stDeviation: %f"%(stDeviation(outPut))
print "max: %f"%(max(outPut))

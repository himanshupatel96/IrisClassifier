import numpy as np
from numpy import *
import csv
import operator
from random import shuffle

# dataSet = genfromtxt('Iris.csv', delimiter=',', skip_header=1)

def Classifier(inX, data, labels, k):
	dSize = data.shape[0]
	diffMat = tile(inX, (dSize,1)) - data
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndices = distances.argsort()
	classCount = {}

	for i in range(0,k):
		vote = labels[sortedDistIndices[i]]
		classCount[vote] = classCount.get(vote,0) + 1
	sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]


rawData = []
labels = []
dataSet = []

with open("Iris.csv", "rb") as f:
	reader = csv.reader(f,delimiter="\t")
	for row in enumerate(reader):
		rawData.append((row[1][0]).split(","))

rawDataSize = size(rawData)/size(rawData[0])
rawData = rawData[1:rawDataSize]
rawDataSize = size(rawData)/size(rawData[0])
shuffle(rawData)
rowSize = size(rawData[0])
for i in range(1,rawDataSize):
	temprow = []
	for j in range(1,rowSize-1):
		temprow.append(float(rawData[i][j]))
	dataSet.append(temprow)
	labels.append(rawData[i][rowSize-1])

dataSize = size(dataSet)/size(dataSet[0])

limit = int((dataSize)*0.85)

trgData = np.array(dataSet[0:limit])
testdata = np.array(dataSet[limit:dataSize])
testLabels = labels[limit:dataSize]
labels = labels[0:limit]

i = 0
cnt = 0
total = dataSize-limit
for row in testdata:
	testValue = Classifier(row,trgData,labels,15)
	if testValue == testLabels[i]:
		cnt+=1
	i+=1
accuracy = (cnt*100.0)/total
print accuracy
print cnt
print total
def classify0(int x,dataSet,labels,k):
	dataSetSize=dataSet.shape[0]
	diffMat=tile(intX,(dataSetSize,1))
	sqDiffMat=diffMat**2
	sqDistances=sqDiffMat.sum(axis=1)
	distances=sqDistances**0.5
	sortedDistIndicies=distances.argsort()
	classCount={}
	for i in range(k):
		voteIlabel=labels[sortedDistIndicies[i]]
		classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
	sortedClassCount=sorted(classCount.iteritems(),
		key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]
def classify0(int x,dataSet,labels,k):
        """这是一个基于kNN算法的分类器
      --------------------------
      args:
      	int x :       目标特征的坐标              eg. [0,0]
      	dataSet : 样本特征坐标集              eg. array[[1.,1.1],[1.,1.4],[1.,0],[1.,0.2]]
      	labels :   与样本对应的特征属类  eg. ['A','A','B','B']
      --------------------------"""
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

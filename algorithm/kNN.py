##-*-coding:utf-8-*-
from numpy import *
import operator

def createDataSet():
	#这个函数用于输出一个样本坐标矩阵和一个样本属类列表
	group=array([[1.,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels=['A','A','B','B']
	return group,labels


def classify0(inX,dataSet,labels,k):
        """这是一个基于kNN算法的分类器
      --------------------------
      args:
      	 inX :       目标特征的坐标              eg. [0,0]
      	dataSet : 样本特征坐标集              eg. array[[1.,1.1],[1.,1.4],[1.,0],[1.,0.2]]
      	labels :   与样本对应的特征属类  eg. ['A','A','B','B']
      --------------------------"""
	dataSetSize=dataSet.shape[0]
	diffMat=tile(inX,(dataSetSize,1))
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

# group,labels=createDataSet()
# print classify0([0,0],group,labels,1)

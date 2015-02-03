import ast
import pickle
import math
import sys
import os
import os.path


def calPofDgivenC(thisline,label):
	PofDLabel = 0.0
	for letter in thisline:
		if letter != '\n':
			if letter not in featuredict:
				PofDLabel += (math.log(1)-math.log(labelcount[label]+len(featuredict)+1))
			elif label not in featuredict[letter]:
				PofDLabel += (math.log(1)-math.log(labelcount[label]+len(featuredict)+1))
			else:
				PofDLabel += featuredict[letter][label]
	return PofDLabel


def classifyz(file,thisline):
	sortlabel = {}
	for label in labeldict:
		sortlabel[label] = calPofDgivenC(thisline,label) + labeldict[label]
	sortedlabel = sorted(sortlabel.items(),key=lambda e:e[1],reverse=True)
	resultoutdict[file]=sortedlabel[0][0]
	#resultFile.write(sortedlabel[0][0]+'\n')

def CalPredict():
	Predict_CORRECT={}
	Predict_SPAM = {}
	Belong_to_SPAM = {}
	for label in labeldict:
		Predict_CORRECT[label]=0
		Predict_SPAM[label]=0
		Belong_to_SPAM[label]=0

	for i in range(0,len(sortedoutput)):
		for label in labeldict:
			if sortedoutput[i][1] == label:
				Predict_SPAM[label]+=1
				if sortedoutput[i][0].split('.')[0] == label:
					Predict_CORRECT[label]+=1
			if sortedoutput[i][0].split('.')[0] == label:
				Belong_to_SPAM[label] +=1
	for label in labeldict:
		if (Predict_SPAM[label] != 0) & (Belong_to_SPAM[label] != 0) & (Predict_CORRECT[label] != 0):
			print(str(label)+' Precision: '+str(Predict_CORRECT[label]/Predict_SPAM[label]))
			print(str(label)+' Recall: '+str(Predict_CORRECT[label]/Belong_to_SPAM[label]))
			print(str(label)+' F-score: '+str(2*((Predict_CORRECT[label]/Predict_SPAM[label]))*(Predict_CORRECT[label]/Belong_to_SPAM[label])/
												((Predict_CORRECT[label]/Predict_SPAM[label])+(Predict_CORRECT[label]/Belong_to_SPAM[label]))))
	return




if __name__ == "__main__":
	testDir = sys.argv[2]
	#testDir = 'SPAM_dev/'
	#testDir = 'SPAM_training/'
	modelfilePath = sys.argv[1]
	modellist = pickle.load( open( modelfilePath, "rb" ) )
	classifymode = sys.argv[1].split('.')[0]
	output = (str(classifymode)+'.out')
	# testformat = 'testformat.txt'
	# testformatFile = open(testformat,'w')
	resultFile = open(output,'w')

	
	labeldict = modellist[0]
	labelcount = modellist[1]
	featuredict = modellist[2]


	# for file in os.listdir(testDir):
	# 	# filedir = testDir+file
	# 	# inputfile = open(filedir,'r', errors = 'ignore')
	# 	# for line in inputfile:
	# 	# 	if line != '\n':
	# 	# 		testformatFile.write(line.rstrip()+' ')
	# 	# testformatFile.write('\n')
	# 	# inputfile.close()
	# # testformatFile.close()
	# # testformatFile = open(testformat,'r')

	# testformatFile = open(testformat,'r')
	# for line in testformatFile:
	# 	if line != "\n":
	# 		thisline = line.split()
	# 		classifyz(thisline)
	# resultFile.close()




	resultoutdict = {}
	for file in os.listdir(testDir):
		filedir = testDir+file
		testformatstr =''
		inputfile = open(filedir,'r', errors = 'ignore')
		for line in inputfile:
			if line != '\n':
				testformatstr+=(line.rstrip().lower()+' ')
		inputfile.close()
		thisline = testformatstr.split()
		if thisline != '\n':
			resultoutdict[file]=0
			classifyz(file,thisline)

	sortedoutput = sorted(resultoutdict.items(), key=lambda d: d[0])
	#resultFile.write(str(sortedoutput))
	# for element in sortedoutput:
	# 	resultFile.write(str(sortedoutput[element])+'\n')
	for i in range(0,len(sortedoutput)):
		resultFile.write(sortedoutput[i][1]+'\n')
		
	#CalPredict()
	resultFile.close()
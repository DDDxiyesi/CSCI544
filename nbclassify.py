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


def classifyz(thisline):
	sortlabel = {}
	for label in labeldict:
		sortlabel[label] = calPofDgivenC(thisline,label) + labeldict[label]
	sortedlabel = sorted(sortlabel.items(),key=lambda e:e[1],reverse=True)
	resultFile.write(sortedlabel[0][0]+'\n')
	#print(sortedlabel[0][0])




if __name__ == "__main__":
	testDir = sys.argv[2]
	#testDir = 'SPAM_dev/'
	#testDir = 'SPAM_training/'
	modelfilePath = sys.argv[1]
	modellist = pickle.load( open( modelfilePath, "rb" ) )
	output = 'output.txt'
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
			resultFile.write(file+' ')
			classifyz(thisline)

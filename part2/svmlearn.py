import sys
import math
import pickle

def createDict():
	featureNo = 0
	for line in spamtrainingfile:
		if line != '\n':	
			string = line
			label = string.partition(' ')[0]	#find label
			if label not in classdic and label != '\n':
				labelcount[label] = 0
				classdic[label] = 1
			elif label != '\n':
				classdic[label] +=1
			thisline = string.split()			#get the line
			labelcount[label] += len(thisline)-1
			for i in range(1,len(thisline)):	#from 2nd word to end of line
				word = thisline[i]				#the No.i word
				if word not in featuredic:		#the word not in dic
					featuredic[word] = {}
					featureNo +=1
					featureNodic[word] = featureNo
					for label1 in classdic:
						featuredic[word][label1]=0
					featuredic[word][label] = 1
				else:
					if label not in featuredic[word]:	
						featuredic[word][label] = 1
					else:
						featuredic[word][label] += 1

def converttosvm():
	for line in spamtrainingfile:
		if line != '\n':
			thislinedict = {}
			label = line.partition(' ')[0]
			if label == 'SPAM':
				svmfile.write('1 ')
			elif label == 'HAM':
				svmfile.write('-1 ')
			thisline = line.split()
			for feature in thisline[1:]:
				thislinedict[feature] = featureNodic[feature]
			sortedline = sorted(thislinedict.items(),key=lambda e:e[1],reverse=False)
			for i in range(0,len(sortedline)):
				#print(sortedline[i][1])
				svmfile.write(str(sortedline[i][1])+':'+str(featuredic[sortedline[i][0]][label]))
				if i < len(sortedline)-1:
					svmfile.write(' ')
			svmfile.write('\n')

def writetobyte():
	modellist = classdic,labelcount,featuredic, featureNodic
	# for label in classdic:
	# 	featuredic[labelnum][label] = classdic[label]
	# for label in labelcount:
	# 	featuredic['LABEL##'][label] = labelcount[label]
	pickle.dump(modellist,open(modelfilepicklePath, "wb"))
	return			

if __name__ == "__main__":
	# Initial
	#spamtrainingfilePath = 'svm_training.txt'
	#modelfilepicklePath = sys.argv[2]
	#svmformatfile = 'svmformat.txt'
	modelfilepicklePath = 'model.nb'
	spamtrainingfilePath = sys.argv[1]
	#svmformatfile = sys.argv[2]
	spamtrainingfile = open(spamtrainingfilePath,'r')
	#svmfile = open(svmformatfile,'w')
	classdic = {}
	labelcount = {}
	featuredic = {}
	featureNodic = {}
	createDict()
	spamtrainingfile.close()	
	labelsum = 0
	for label in classdic:
		labelsum += classdic[label]
	for label in classdic:
		classdic[label] = classdic[label]/labelsum
	for feature in featuredic:
		for label in featuredic[feature]:
			if label in labelcount:
				featuredic[feature][label] = (featuredic[feature][label]+1)/(labelcount[label]+len(featuredic)+1)
	spamtrainingfile = open(spamtrainingfilePath,'r')
	#converttosvm()
	writetobyte()
	spamtrainingfile.close()
	#svmfile.close()
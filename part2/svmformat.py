import sys
import math
import pickle

def converttosvm():
	for line in spamtrainingfile:
		if line != '\n':
			thislinedict = {}
			label = line.partition(' ')[0]
			if label == 'SPAM' or "POS":
				svmfile.write('1 ')
			elif label == 'HAM' or 'NEG':
				svmfile.write('-1 ')
			thisline = line.split()
			for feature in thisline[1:]:
				if feature not in featuredic:
					break
				thislinedict[feature] = featureNodic[feature]
			sortedline = sorted(thislinedict.items(),key=lambda e:e[1],reverse=False)
			for i in range(0,len(sortedline)):
				#print(sortedline[i][1])
				svmfile.write(str(sortedline[i][1])+':'+str(featuredic[sortedline[i][0]][label]))
				if i < len(sortedline)-1:
					svmfile.write(' ')
			svmfile.write('\n')

if __name__ == "__main__":
	modelfilePath = 'model.nb'
	modellist = pickle.load( open( modelfilePath, "rb" ) )
	spamformatfilePath = sys.argv[1]
	spamtrainingfile = open(spamformatfilePath,'r')
	svmformatfilePath = sys.argv[2]
	svmfile = open(svmformatfilePath,'w')
	labeldict = modellist[0]
	labelcount = modellist[1]
	featuredic = modellist[2]
	featureNodic = modellist[3]
	converttosvm()
	spamtrainingfile.close()
	svmfile.close()
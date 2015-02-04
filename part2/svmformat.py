import sys
import math
import pickle

def converttosvm():
	thislinedict = {}
	thislinecount = {}
	for line in spamtrainingfile:
		if line != '\n':
			line = 	"".join(l for l in line if l not in delset)
			thislinedict.clear()
			thislinecount.clear()
			label = line.partition(' ')[0]
			if label == 'SPAM' or label == 'POS' :
				svmfile.write('+1 ')
			elif label == 'HAM' or label == 'NEG':
				svmfile.write('-1 ')
			else:
				svmfile.write('0 ')
			thisline = line.split()
			for word in thisline[1:]:
				feature = word.lower()
				if feature in featuredic:
					thislinedict[feature] = featureNodic[feature]
					if feature not in thislinecount:
						thislinecount[feature] = 1
					else:
						thislinecount[feature] += 1
			sortedline = sorted(thislinedict.items(),key=lambda e:e[1],reverse=False)
			for i in range(0,len(sortedline)):
				#print(thislinecount[sortedline[i][0]])
				l = float(thislinecount[sortedline[i][0]])/float((len(thisline)-1))
				svmfile.write(str(sortedline[i][1])+':'+str(l))
				if i < len(sortedline)-1:
					svmfile.write(' ')
				#print(sortedline[i][0])
				#print(sortedline[i][1])
				# if 'SPAM' in labeldict:
				# 	theSpamLabel = 'SPAM'
				# elif 'POS' in labeldict:
				# 	theSpamLabel = 'POS'
				# if theSpamLabel not in featuredic[sortedline[i][0]]:
				# 	featuredic[sortedline[i][0]][theSpamLabel] = 1/(labelcount[theSpamLabel]+len(featuredic)+1)
				# svmfile.write(str(sortedline[i][1])+':'+str(featuredic[sortedline[i][0]].get(theSpamLabel)))
				# if i < len(sortedline)-1:
				# 	svmfile.write(' ')
			svmfile.write('\n')


if __name__ == "__main__":
	delset = ('~','!','@','^','*','(',')','_','+','`','-',
		'=','{','}','[',']',':',';',',','"','.','#')
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
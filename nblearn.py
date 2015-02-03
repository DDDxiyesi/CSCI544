import sys
import math
import pickle

def write2txt():
		modelfilePath = 'model.txt'
		modelfile = open(modelfilePath,'w')
		# for label in classdic:
		# for feature in featuredic:
		# 	if label not in featuredic[feature]:
		# 		featuredic[feature][label] = 0
		# modelfilePath = 'model2.txt'
		# modelfile2 = open(modelfilePath,'w')
		# modelfile2.write(str(classdic)+'\n')
		# modelfile2.write(str(labelcount)+'\n')
		# for feature in featuredic:
		# 	modelfile2.write(str(feature)+' ')
		# 	modelfile2.write(str(featuredic[feature]))
		# 	modelfile2.write('\n')
		
		modelfile.write(str(classdic)+'\n')
		modelfile.write(str(labelcount)+'\n')
		for feature in featuredic:
			modelfile.write(str(feature)+' ')
			modelfile.write(str(featuredic[feature]))
			modelfile.write('\n')
		return
	
def writetobyte():
	modellist = classdic,labelcount,featuredic
	# for label in classdic:
	# 	featuredic[labelnum][label] = classdic[label]
	# for label in labelcount:
	# 	featuredic['LABEL##'][label] = labelcount[label]
	pickle.dump(modellist,open(modelfilepicklePath, "wb"))
	return

if __name__ == "__main__":
	# Initial
	spamtrainingfilePath = sys.argv[1]
	modelfilepicklePath = sys.argv[2]
	spamtrainingfile = open(spamtrainingfilePath,'r')
	classdic = {}
	labelcount = {}
	featuredic = {}
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
			for i in range(1,len(thisline)):	#from 2nd letter to end of line
				word = thisline[i]				#the No.i word
				if word not in featuredic:		#the word not in dic
					featuredic[word] = {}
					for label1 in classdic:
						featuredic[word][label1]=0
					featuredic[word][label] = 1
				else:
					if label not in featuredic[word]:	
						featuredic[word][label] = 1
					else:
						featuredic[word][label] += 1
	#count = 0
	spamtrainingfile.close()
	labelsum = 0
	for label in classdic:
		labelsum += classdic[label]
		#print(labelsum)
	for label in classdic:
		classdic[label] = math.log(classdic[label])-math.log(labelsum)
	for feature in featuredic:
		for label in featuredic[feature]:
			if label in labelcount:
				featuredic[feature][label] = math.log(featuredic[feature][label]+1)-math.log(labelcount[label]+len(featuredic)+1)


	#write2txt()
	writetobyte()

	#print(len(featuredic))
	#print(len(featuredic))
	# 	for label in featuredic[feature]:
	# 		count+=featuredic[feature][label]
	# print(count)
	


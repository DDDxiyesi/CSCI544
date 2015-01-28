import sys
if __name__ == "__main__":
	# Initial
	spamtrainingfilePath = '/home/yang/Desktop/csci544-hw1/spam_training.txt'
	modelfilePath = 'model.txt'
	spamtrainingfile = open(spamtrainingfilePath,'r')
	modelfile = open(modelfilePath,'w')
	classdic = {}
	featuredic = {}
	for line in spamtrainingfile:
		if line != '\n':	
			string = line
			label = string.partition(' ')[0]	#find label
			if label not in classdic and label != '\n':
				classdic[label] = 1
			elif label != '\n':
				classdic[label] +=1
			thisline = string.split()			#get the line
			for i in range(1,len(thisline)):	#from 2nd letter to end of line
				word = thisline[i]				#the No.i word
				if word not in featuredic:		#the word not in dic
					featuredic[word] = {}
					featuredic[word][label] = 1
				else:
					if label not in featuredic[word]:	
						featuredic[word][label] = 1
					else:
						featuredic[word][label] += 1
	modelfile.write(str(classdic)+'\n')
	for feature in featuredic:
		modelfile.write(str(feature)+' ')
		modelfile.write(str(featuredic[feature]))
		modelfile.write('\n')
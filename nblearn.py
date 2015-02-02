import sys
import math
if __name__ == "__main__":
	# Initial
	spamtrainingfilePath = '/home/yang/Desktop/csci544-hw1/spam_training.txt'
	modelfilePath = 'model.txt'
	spamtrainingfile = open(spamtrainingfilePath,'r')
	modelfile = open(modelfilePath,'w')
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
			print(thisline)
			labelcount[label] += len(thisline)-1
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
	#count = 0
	spamtrainingfile.close()

	labelsum = 0
	modelfilePath = 'model2.txt'
	modelfile2 = open(modelfilePath,'w')
	modelfile2.write(str(classdic)+'\n')
	modelfile2.write(str(labelcount)+'\n')
	for feature in featuredic:
		modelfile2.write(str(feature)+' ')
		modelfile2.write(str(featuredic[feature]))
		modelfile2.write('\n')
	for label in classdic:
		labelsum += classdic[label]
	print(labelsum)
	for label in classdic:
		classdic[label] = math.log(classdic[label])-math.log(labelsum)
	for feature in featuredic:
		for label in featuredic[feature]:
			if label in labelcount:
				#featuredic[feature][label] = math.log(featuredic[feature][label]+1)-math.log(labelcount[label]+len(featuredic))
				featuredic[feature][label] = (featuredic[feature][label]+1)/(labelcount[label]+len(featuredic))
				featuredic[feature][label] = math.log(featuredic[feature][label])
	modelfile.write(str(classdic)+'\n')
	modelfile.write(str(labelcount)+'\n')
	

	for feature in featuredic:
		modelfile.write(str(feature)+' ')
		modelfile.write(str(featuredic[feature]))
		modelfile.write('\n')
	print(len(featuredic))
	#print(len(featuredic))
	# 	for label in featuredic[feature]:
	# 		count+=featuredic[feature][label]
	# print(count)
	


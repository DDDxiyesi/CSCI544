import sys
import os
import os.path
import fnmatch


if __name__ == "__main__":
	#rootdir = '/home/yang/Desktop/csci544-hw1/'
	spamtrainingdir = sys.argv[1]
	spamtrainingfilePath = sys.argv[2]
	spamtrainingfile = open(spamtrainingfilePath,'w')
	filedict = []
	for file in os.listdir(spamtrainingdir):
		filedict.append(file)
	filesort = sorted(filedict)
	for file in filesort:
		filedir = spamtrainingdir+file
		inputfile = open(filedir,'r', errors = 'ignore')
		spamtrainingfile.write(file.split('.')[0]+' ')
		for line in inputfile:
			if line != '\n':
				spamtrainingfile.write(line.rstrip().lower()+' ')
		spamtrainingfile.write('\n')
		inputfile.close()
		# if fnmatch.fnmatch(file, 'HAM.*'):
		# 	filedir = spamtrainingdir+file
		# 	inputfile = open(filedir,'r', errors = 'ignore')
		# 	spamtrainingfile.write('HAM ')
		# 	for line in inputfile:
		# 		if line != '\n':
		# 			spamtrainingfile.write(line.rstrip()+' ')
		# 	spamtrainingfile.write('\n')
		# 	inputfile.close()
		# elif fnmatch.fnmatch(file, 'SPAM.*'):
		# 	filedir = spamtrainingdir+file
		# 	inputfile = open(filedir,'r', errors = 'ignore')
		# 	spamtrainingfile.write('SPAM ')
		# 	for line in inputfile:
		# 		if line != '\n':
		# 			spamtrainingfile.write(line.rstrip()+' ')
		# 	spamtrainingfile.write('\n')
		# 	inputfile.close()
	spamtrainingfile.close()
	# spamtrainingfile = spamtrainingfile = open(rootdir+'spam_training.txt','r')
	# s = spamtrainingfile.read()
	# print(s)
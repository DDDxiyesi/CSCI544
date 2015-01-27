import sys

import  os
import  os.path
import fnmatch

#coding=utf-8

if __name__ == "__main__":
	rootdir = '/home/yang/Desktop/csci544-hw1/'
	spamtrainingdir = rootdir+'SPAM_training/'
	spamtrainingfile = open(rootdir+'spam_training.txt','w')
	for file in os.listdir(spamtrainingdir):
		if fnmatch.fnmatch(file, 'HAM.*'):
			filedir = spamtrainingdir+file
			inputfile = open(filedir,'r', errors = 'ignore')
			spamtrainingfile.write('HAM ')
			for line in inputfile:
				spamtrainingfile.write(line.rstrip()+' ')
			spamtrainingfile.write('\n')
			inputfile.close()
		elif fnmatch.fnmatch(file, 'SPAM.*'):
			filedir = spamtrainingdir+file
			inputfile = open(filedir,'r', errors = 'ignore')
			spamtrainingfile.write('SPAM ')
			for line in inputfile:
				spamtrainingfile.write(line.rstrip()+' ')
			spamtrainingfile.write('\n')
			inputfile.close()
	spamtrainingfile.close()
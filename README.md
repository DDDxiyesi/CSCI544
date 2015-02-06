The files and code in top root consist a classifier based on Naive Bayes.
The file in part2 directory are models and outputs of SVM and MegaM.
Here are the instructions to run the code of NB-classifier:
	1. Pull all the files in a folder.
	2. If you want to make a new model, copy your training data in a folder. Else skip to step 4.
	3. Open terminal run python3 nbformat.py THE_FOLDER_OF_TRAINING_DATA 			  		THE_TRAINING_FILE_NAME_AFTER_FORMATTING to get a training file(like spam_training.txt).
	4. Run python3 nblearn.py THE_TRAINING_FILE_NAME_AFTER_FORMATTING MODEL_FILE to create a 		model file(like spam.nb, sentiment.nb).
	5. Run python3 nbclassify.py MODEL_FILE TEST_DATA_FOLDER to get an output.txt, and each line 		in it is a label.
	6. If you want to evaluate the classifier, the function in nbclassify.py called "CalPredict" 		can help you. It's in line 118.

I used dictionary to store characters of features to speed up the program in part1.
I used add-one smoothing to avoid 0 in probability which can lead to a bad result.
I regarded all unknown words as one feature. So the vocabulary increased by 1. And when doing classify, the unknown word has probability of log(1/N+V+1).
And I stored the probability in log base to avoid underflow.
Also, I removed some symbols like `,#,^,*,(,),etc in spam model but restored them in sentiment model because I found without puctuations, spam model could have a higher accuarcy without considering puntuations while sentiment couldn't.
I also tried only consider the feature with length greater than 1. which turned out better in sentiment but worse in spam.

In SVM of part2, I stored the features one by one in dict to format them in increasing order and choose the tf-idf value of the word as its character.
In MegaM of part2, I used non-bernoulli implicit format to imply binary and multiclass. For each feature, I set the initial value as 1.0. I created the model and ran test with binary which had a better result.

Q1 What are the precision, recall and F-score on the development data for your classifier in part I for each of the two datasets.
A1 For SPAM_dev dataset, the precision of SPAM is 0.9646739130434783
			 the recall of SPAM is 0.977961432506887
			 the F-score of SPAM is 0.9712722298221614
			 the precision of HAM is 0.9919597989949749
			 the recall of HAM is 0.987
			 the F-score of HAM is 0.9894736842105264
   For SENTIMENT_dev I chose about 2500 data as dev data and decreased the training set by that number.                  the NEG precision is 0.7604832977967306
			 the NEG recall is 0.8485329103885805
			 the NEG F-score is 0.8020989505247376
			 the POS precision is 0.8297682709447415
			 the Pos recall is 0.7342271293375394
    			 the POS F-score is 0.7790794979079497

Q2 What are the precision, recall and F-score for your classifier in part II for each of the two datasets.
A2 In SVM: For SPAM_dev dataset, the SPAM precision is 0.9671232876712329
		   	 the SPAM recall is 0.9724517906336089
			 the SPAM F-score is 0.9697802197802199
			 the HAM precision is  0.9899799599198397
			 the HAM recall is 0.988
			 the HAM F-score is 0.988988988988989
  	   For SENTIMENT_dev, the POS precision is 0.8725901089689857
		         the POS recall is 0.8209779179810726
		         the POS F-score is 0.8459975619666803
		         the NEG precision is 0.8300898203592815
		         the NEG recall is 0.8794607454401269
		         the NEG F-score is 0.8540623796688487
   In MegaM: 


Q3 What happens exactly to precision, recall and F-score in each of the two tasks (on the development data) when only 10% of the training data is used to train the classifiers in part I and part II? Why do you think that is?
A3 





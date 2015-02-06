02/05/2015
Yang Liu

I used dictionary to store characters of features to speed up the program in part1. (In class, this has been mentioned by Prof. Sagae.)
I used add-one smoothing to avoid 0 in probability which can lead to a bad result. (Also mentioned in class.)
I regarded all unknown words as one feature. So the vocabulary increased by 1. And when doing classify, the unknown word has probability of log(1/N+V+1). (Also metioned in class.)
And I stored the probability in log base to avoid underflow. (Mentioned in class, too.)
Also, I removed some symbols like `,#,^,*,(,),etc in spam model but restored them in sentiment model because I found without puctuations, spam model could have a higher accuarcy without considering puntuations while sentiment couldn't.
I also tried only consider the feature with length greater than 1. which turned out better in sentiment but worse in spam.
And I tried to remove the digits, but turned out no differnce...

In SVM of part2, I stored the features one by one in dict to format them in increasing order and choose the tf-idf value of the word as its character since it has a better result than frequency of the word in one document. The tf-idf was mentioned in class.

In MegaM of part2, I used non-bernoulli implicit format to imply binary and multiclass. For each feature, I set the initial value as 1.0. I created the model and ran test with binary which had a better result. (A student also said binary has a better result on piazza.)

I chose about adjacent 2500 data form SENTIMENT_training as dev data and delete the same data in training set.
Q1 What are the precision, recall and F-score on the development data for your classifier in part I for each of the two datasets.
A1 For SPAM_dev dataset, the precision of SPAM is 0.9646739130434783
			 the recall of SPAM is 0.977961432506887
			 the F-score of SPAM is 0.9712722298221614
			 the precision of HAM is 0.9919597989949749
			 the recall of HAM is 0.987
			 the F-score of HAM is 0.9894736842105264
   For SENTIMENT_dev, the NEG precision is 0.7604832977967306
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
   In MegaM: For SPAM_dev dataset, the SPAM precision is 0.9781420765027322
				   the SPAM recall is 0.9862258953168044
				   the SPAM F-score is 0.9821673525377228
				   the HAM precision is 0.9949849548645938
				   the HAM recall is 0.992
				   the HAM F-score is 0.9934902353530296
	     For SENTIMENT_dev dataset, the POS precision is 0.8598277212216131
				        the POS recall is 0.8659305993690851
				        the POS F-score is 0.8628683693516698
				        the NEG precision is 0.8642172523961661
				        the NEG recall is 0.8580491673275178
				        the NEG F-score is 0.8611221647433346

Q3 What happens exactly to precision, recall and F-score in each of the two tasks (on the development data) when only 10% of the training data is used to train the classifiers in part I and part II? Why do you think that is?
A3 I delete 90% files in training set.
   For part 1, in SPAM classification, SPAM precision is 0.6766917293233082
				 SPAM recall is 0.9917355371900827
				 SPAM F-score is 0.8044692737430168
				 HAM precision is 0.9963898916967509
				 HAM recall is 0.828
				 HAM F-score is 0.904423812124522
   In SENTIMENT classification, POS precision is 0.817157712305026
			  POS recall is 0.7436908517350158
			  POS F-score is 0.7786952931461603
			  NEG precision is 0.7636363636363637
			  NEG recall is 0.8326724821570183
			  NEG F-score is 0.7966616084977238
   We can see that in SPAM classification the accuracy decrease about 7%. However, In SENTIMENT, it only decreased about 1%.
   I think SPAM decreased because the training set is small, when the training set decrease 90% the accuracy wil decrease. But it still has high accuracy. I think it's because in spam documents some features that occur lots of times that classifier more likely to label the doc as spam so spam recall is very high or the styles of training and dev set are similar which lead to a high accuracy even without big training set.
   I think the reason that SENTIMENT decreased little is that it still has enough data to train and sentiment has stronger relationship with context than SPAM does. So even the bag-of-word decreased, the accuracy only decreased a little.
   For part 2, in SVM:
	in SPAM classification, SPAM Precision: 0.9541284403669725
			        SPAM Recall: 0.859504132231405
			        SPAM F-score: 0.9043478260869566
                         	HAM Precision: 0.9507722007722008
		                HAM Recall: 0.985
			        HAM F-score: 0.9675834970530454
	in SENTIMENT classification, POS Precision: 0.8475298126064736
				     POS Recall: 0.7847003154574133
				     POS F-score: 0.8149058149058149
				     NEG Precision: 0.7985239852398524
				     NEG Recall: 0.8580491673275178
		                     NEG F-score: 0.8272171253822629
   The accuarcy of 2 classification has a decrease of nearly 5%. The decrease is not so much as part 1. I think it's mainly because SVM is good at binary classification-it cares about the feature weight more than the times it occurs. And tf-idf is a weight value for features even without big training set.
  In Megam: For SPAM classification: SPAM Precision: 0.943342776203966
			  	     SPAM Recall: 0.9173553719008265
			 	     SPAM F-score: 0.9301675977653631
		          	     HAM Precision: 0.9702970297029703
			  	     HAM Recall: 0.98
			             HAM F-score: 0.9751243781094527
	    For SENTIMENT classification: NEG Precision: 0.8313057583130575
					  NEG Recall: 0.8128469468675654
					  NEG F-score: 0.8219727345629512
					  POS Precision: 0.8179012345679012
					  POS Recall: 0.8359621451104101
					  POS F-score: 0.826833073322933
   The accuracy of both decreased about 3%-4%. The decrease is lower than SVM. I think it because I created the model with very big iterations and use binary classification. So the important words can
have very big weight. And maybe the similar of training set and dev set is another reason. With the similarity the words in training set may also appear in dev set with a similar meaning so that it's easy to classify.
   In conlusion, the bigger training set may not be better because the model may be over-fit, and when training, it's better to use training data with different style. And SENTIMENT is more dificlut in text classification than SPAM~

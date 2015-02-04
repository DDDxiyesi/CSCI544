The files and code in top root consist a classifier based on Naive Bayes.
The file in part2 directory are models and outputs of svm and megam.
Here are the instructions to run the code of NB-classifier:
	1. Pull all the files in a folder.
	2. If you want to make a new model, copy your training data in a folder. Else skip to step 4.
	3. Open terminal run python3 nbformat.py THE_FOLDER_OF_TRAINING_DATA THE_TRAINING_FILE_NAME_AFTER_FORMATTING to get a training file(like spam_training.txt).
	4. Run python3 nblearn.py THE_TRAINING_FILE_NAME_AFTER_FORMATTING MODEL_FILE to create a model file(like spam.nb, sentiment.nb).
	5. Run python3 nbclassify.py MODEL_FILE TEST_DATA_FOLDER to get an output.txt, and each line in it is a label.
	6. If you want to evaluate the classifier, the function in nbclassify.py called "CalPredict" can help you. It's in line 118.
I used dictionary to store characters of features to speed up the program. 
And remove some symbols like `,#,^,*,(,),etc which are irrelevant in my opinion.

In SVM of part2, I stored the features one by one in dict to format them in increasing order and choose the frequency of the word in the line as its character.
In Megam of part2, I used non-bernoulli implicit format to imply multiclass.


These files and code consist a classifier based on Naive Bayes.
Here are the instructions to run the code:
	1. Pull all the files in a folder.
	2. If you want to make a new model, copy your training data in a folder. Else skip to step 4.
	3. Open terminal run python3 nbformat.py THE_FOLDER_OF_TRAINING_DATA THE_TRAINING_FILE_NAME_AFTER_FORMATTING to get a training file(like spam_training.txt).
	4. Run python3 nblearn.py THE_TRAINING_FILE_NAME_AFTER_FORMATTING MODEL_FILE to create a model file(like spam.nb, sentiment.nb).
	5. Run python3 nbclassify.py MODEL_FILE TEST_DATA_FOLDER to get an output.txt, and each line in it is a label.
	6. If you want to evaluate the classifier, the function in nbclassify.py called "CalPredict" can help you. It's in line 118.

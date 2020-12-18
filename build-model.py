 ################## importing the necessary modules
from spam_classifier import SpamClassifier, process_message

import numpy as np
import pandas as pd
import pickle
import os

############### lets read the data of spam and ham examples mails
## the spam.csv is taken from kaggle.com

mails = pd.read_csv('spamham.csv', encoding = 'latin-1')
# mails.head()

###################### processing the data

mails.rename(columns = {'v1': 'labels', 'v2': 'message'}, inplace = True)
# mails.head()

mails['label'] = mails['labels'].map({'ham': 0, 'spam': 1})
# mails.head()

mails.drop(['labels'], axis = 1, inplace = True)
# mails.head()

totalMails = 4825 + 747
trainIndex, testIndex = list(), list()
for i in range(mails.shape[0]):
    if np.random.uniform(0, 1) < 0.75:
        trainIndex += [i]
    else:
        testIndex += [i]
trainData = mails.loc[trainIndex]
testData = mails.loc[testIndex]


trainData.reset_index(inplace = True)
trainData.drop(['index'], axis = 1, inplace = True)
# trainData.head()


testData.reset_index(inplace = True)
testData.drop(['index'], axis = 1, inplace = True)
# testData.head()


spam_words = ' '.join(list(mails[mails['label'] == 1]['message']))


ham_words = ' '.join(list(mails[mails['label'] == 0]['message']))


    #####################################################

sc_tf_idf = SpamClassifier(trainData, 'tf-idf')
sc_tf_idf.train()
preds_tf_idf = sc_tf_idf.predict(testData['message'])

# this code is comented out because the another classifier have lower accuracy
# sc_bow = SpamClassifier(trainData, 'bow')
# sc_bow.train()
# preds_bow = sc_bow.predict(testData['message'])

# pm = process_message('I cant pick the phone right now. Pls send a message')
# res = sc_tf_idf.classify(pm)
# print(res)


model_name = "spam_ham_clf.pkl"
clf_pkl = open(model_name,'wb')
pickle.dump(sc_tf_idf,clf_pkl)
clf_pkl.close()

# from sklearn.externals import joblib
# joblib.dump(sc_tf_idf,"spam_ham_clf.pkl")
print('\n successfully created model')
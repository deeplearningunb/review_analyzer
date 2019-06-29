import numpy as np
import matplotlib as plt
import pandas as pd

dataset = pd.read_csv('classifier/movies_merged.csv', sep='|')
dataset = dataset.dropna()
dataset = dataset.applymap(str.lower)
x = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer

nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB())])
nb.fit(x_train, y_train)

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
y_pred = nb.predict(x_test)

print(accuracy_score(y_pred, y_test))
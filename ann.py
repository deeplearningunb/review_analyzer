import numpy as np
import matplotlib as plt
import pandas as pd

dataset = pd.read_csv('classifier/movies_merged.csv', sep='|')
dataset = dataset.dropna()
dataset = dataset.applymap(str.lower)
x = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values

# from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler(with_mean=False)
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()
# input layer
classifier.add(Dense(units = 32, kernel_initializer = 'uniform', activation = 'relu', input_dim = 35440))
# first
classifier.add(Dense(units = 32, kernel_initializer = 'uniform', activation = 'sigmoid'))
# second
classifier.add(Dense(units = 32, kernel_initializer = 'uniform', activation = 'sigmoid'))
#third
classifier.add(Dense(units = 32, kernel_initializer = 'uniform', activation = 'sigmoid'))
# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'relu'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# classifier.fit(x_train, y_train, batch_size = 10, epochs = 100)

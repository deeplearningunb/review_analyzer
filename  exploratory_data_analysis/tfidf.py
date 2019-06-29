from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd 

df = pd.read_csv("movies_merged.csv", sep='|')
df = df.dropna()
df = df.applymap(str.lower)
fresh = df.loc[df['Review'] == "fresh"]
rotten = df.loc[df['Review'] == 'rotten']
print(fresh)

vectorizer = TfidfVectorizer()
fresh_ = vectorizer.fit_transform(fresh.iloc[:,0])
print(vectorizer.get_feature_names())
print(fresh_.shape)

vectorizer = TfidfVectorizer()
rotten_ = vectorizer.fit_transform(rotten.iloc[:,0])
print(vectorizer.get_feature_names())
print(rotten_.shape)

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer        
import pandas as pd 
import sys


class MovieTfidf:

    def open_process(self, filename):
        df = pd.read_csv(filename, sep='|')
        df = df.dropna()
        df = df.applymap(str.lower)
        fresh = df.loc[df['Review'] == "fresh"]
        rotten = df.loc[df['Review'] == 'rotten']
        self.tfidf(fresh, rotten)

    def tfidf(self, fresh, rotten):
        data = fresh.iloc[:,0]

        cv = CountVectorizer()
        data = cv.fit_transform(data)

        tfidf_transformer = TfidfTransformer()
        tfidf_matrix = tfidf_transformer.fit_transform(data)
        word2tfidf = dict(zip(cv.get_feature_names(), tfidf_transformer.idf_))
        print("=========Fresh=========")
        for word, score in word2tfidf.items():
            print(word, score)

        data = rotten.iloc[:,0]

        cv = CountVectorizer()
        data = cv.fit_transform(data)

        tfidf_transformer = TfidfTransformer()
        tfidf_matrix = tfidf_transformer.fit_transform(data)
        word2tfidf = dict(zip(cv.get_feature_names(), tfidf_transformer.idf_))
        print("\n\n\n")
        print("=========Rotten=========")
        for word, score in word2tfidf.items():
            print(word, score)


if __name__ == "__main__":
    filename = sys.argv[1]
    movie_tfidf = MovieTfidf()
    movie_tfidf.open_process(filename)

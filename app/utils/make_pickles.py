from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np
import spacy
from spacy.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
import en_core_web_md
import pickle
from os import path


class make_pickles_isaac():
    def __init__(self):
        """ coppied from notebook at app/ml/Build_week_IsaacGrove.ipynb
        """
        self.PICKLE_PATH = path.join(path.dirname(__file__), '..', 'pickles',
                                     '')

        leafly = pd.read_csv(
            'https://raw.githubusercontent.com/Build-Week-Med-Cabinet-6/DS/mark-dev/data/cannabis.csv'
        )

        # Set up spacy tokenizer
        nlp = en_core_web_md.load()
        tokenizer = Tokenizer(nlp.vocab)

        # clean some missing info
        leafly.replace('None', np.NaN, inplace=True)
        leafly = leafly.dropna()

        # Make tokens out of descriptions
        tokens = []
        for desc in tokenizer.pipe(leafly['Description'], batch_size=500):
            desc_tokens = [token.text for token in desc]
            tokens.append(desc_tokens)
        leafly['tokens'] = tokens
        leafly['tokens'].head()

        def tokenize(document):

            doc = nlp(document)

            return [
                token.lemma_.strip() for token in doc
                if (token.is_stop != True) and (token.is_punct != True)
            ]

        # Instantiate vectorizer object
        tfidf = TfidfVectorizer(ngram_range=(1, 2),
                                max_df=.97,
                                min_df=3,
                                tokenizer=tokenize)

        # Create a vocabulary and get word counts per listing
        dtm = tfidf.fit_transform(leafly['Description'])

        # Get feature names to use a dataframe column headers
        dtm = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())
        # Fit on dtm
        nn = NearestNeighbors(n_neighbors=20, algorithm='kd_tree')
        nn.fit(dtm)
        self.model = nn
        self.transform = tfidf

    def save_pickles(self):
        with open(self.PICKLE_PATH + "nn_isaac.pickle", 'wb') as fp0:
            pickle.dump(self.model, fp0)
        with open(self.PICKLE_PATH + "tfidf_isaac.pickle", 'wb') as fp1:
            pickle.dump(self.transform, fp1)
        return

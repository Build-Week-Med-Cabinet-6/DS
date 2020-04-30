from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np
import spacy
from spacy.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from spacy.lang.en import English

# not working on production server dropping the
# implementation and comming back to it
#import en_core_web_md

import pickle
from os import path


class make_pickles_isaac():
    def __init__(self):
        """ coppied from notebook at app/ml/Build_week_IsaacGrove.ipynb
        """
        self.PICKLE_PATH = path.join(path.dirname(__file__), '..', 'pickles',
                                     '')

        # for now i'm loading data from a static link, will try to pull live data
        # in future iters
        leafly = pd.read_csv(
            'https://raw.githubusercontent.com/Build-Week-Med-Cabinet-6/DS/mark-dev/data/cannabis.csv'
        )

        # Set up spacy tokenizer
        nlp = English()
        tokenizer = Tokenizer(nlp.vocab)

        # work around for pickle
        self.nlp = nlp

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

        # Instantiate vectorizer object
        tfidf = TfidfVectorizer(ngram_range=(1, 2),
                                max_df=.7,
                                min_df=.001,
                                tokenizer=self.tokenize)

        # Create a vocabulary and get word counts per listing
        dtm = tfidf.fit_transform(leafly['Description'])

        # Get feature names to use a dataframe column headers
        dtm = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())
        # Fit on dtm
        nn = NearestNeighbors(n_neighbors=20, algorithm='kd_tree')
        nn.fit(dtm)
        self.model = nn
        self.transform = tfidf
        return

    def save_pickles(self):
        """A method to save pickles locally to the server from this script
        """
        with open(self.PICKLE_PATH + "nn_isaac.pickle", 'wb') as fp0:
            pickle.dump(self.model, fp0)
        with open(self.PICKLE_PATH + "tfidf_isaac.pickle", 'wb') as fp1:
            pickle.dump(self.transform, fp1)
        return

    def tokenize(self, document):
        """Local method to the model from above, taken and put as a class model
        so that pickle won't break.
        """
        nlp = English()
        doc = nlp(document)

        return [
            token.lemma_.strip() for token in doc
            if (token.is_stop != True) and (token.is_punct != True)
        ]


class make_pickles_mark():
    def __init__(self):
        """A model for taking effects and flavors and returning database entries
        for the predicted strains that are similar to those strains.
        """
        self.PICKLE_PATH = path.join(path.dirname(__file__), '..', 'pickles',
                                     '')
        # set up the spacy tokenizer
        nlp = English()
        tokenizer = Tokenizer(nlp.vocab)
        # read data from remote
        # TODO implement local read from db
        df = pd.read_csv(
            "https://raw.githubusercontent.com/Build-Week-Med-Cabinet-6/DS/mark-dev/data/cannabis.csv"
        )
        # clean the data
        df.replace('None', np.NaN, inplace=True)
        df = df.dropna()

        # comine effects and flavors
        df['Combined'] = df['Effects'] + ',' + df['Flavor']

        #make a tfidf and transfor the training data
        dtm_combined_tf = TfidfVectorizer(stop_words='english')
        dtm_combined = dtm_combined_tf.fit_transform(
            df['Combined'].values.astype('U'))
        dtm_combined = pd.DataFrame(
            dtm_combined.todense(),
            columns=dtm_combined_tf.get_feature_names())

        #knn model to make predictions
        nn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
        nn.fit(dtm_combined)

        # save to class atributes to pickle
        self.model = nn
        self.transform = dtm_combined_tf

        return

    def save_pickles(self):
        """A method to save pickles locally to the server from this script
        """
        with open(self.PICKLE_PATH + "nn_mark.pickle", 'wb') as fp0:
            pickle.dump(self.model, fp0)
        with open(self.PICKLE_PATH + "tfidf_mark.pickle", 'wb') as fp1:
            pickle.dump(self.transform, fp1)
        return

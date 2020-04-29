from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from spacy.tokenizer import Tokenizer

import pickle


class modelone():
    def __init__(self, model_pickle: str, dtm_transformer: str) -> type(None):

        # load pickles into ram and assign as attributes
        self.model = pickle.load(open(model_pickle, 'rb'))
        self.dtm_transformer = pickle.load(open(dtm_transformer, 'rb'))

        return

    def transform_predict(self, user_text):
        # transform the text the user sent
        t = self.dtm_transformer.transform(user_text)
        # use knn to make results
        results = self.model.kneighbors(t.todense())
        # should be list of tuples
        self.results = results

        return

    def getResults(self) -> type(None):
        # just returning the id's of the results of the prediction
        return self.results[1]


# ignore pickle had a fit
def tokenize(document):

    doc = nlp(document)

    return [
        token.lemma_.strip() for token in doc
        if (token.is_stop != True) and (token.is_punct != True)
    ]


# part of the seed code left here for prosperity and to ref back to
# Instantiate the tokenizer
#nlp = English()
#tokenizer = Tokenizer(nlp.vocab)
#df = pd.read_csv(
#    "https://raw.githubusercontent.com/Build-Week-Med-Cabinet-6/DS/mark-dev/data/cannabis.csv"
#)
#df.head()
# drop nan or missing values
#df = df.dropna()
#df = df.drop(df.index[149])
#df = df.reset_index(drop=True)
# Combine the Effects and Flavors in one column
#df['Combined'] = df['Effects'] + ',' + df['Flavor']

# Instantiate vecorizer object - call tokenize
#dtm_combined_tf = TfidfVectorizer(stop_words='english')
# dtm_combined  (vocabulary) and get word counts
# effects and flavors combined
#dtm_combined = dtm_combined_tf.fit_transform(df['Combined'].values.astype('U'))
#dtm_combined = pd.DataFrame(dtm_combined.todense(),
#                            columns=dtm_combined_tf.get_feature_names())
#dtm_combined.head()

# Fit on TF-IDF Vectors
#nn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
#nn.fit(dtm_combined)
# Practice passing a strain to the model with this string
#ideal_strain = [
#    'Creative,Energetic,Tingly,Euphoric,Relaxed,Earthy,Sweet,Citrus'
#]
# Query for similar strains using the test case
#new = dtm_combined_tf.transform(ideal_strain)
#results = nn.kneighbors(new.todense())
# Results are returned in a tuple of arrays
#results

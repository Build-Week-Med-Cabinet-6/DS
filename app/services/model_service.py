# since both models use the same thing i can just import
# the parent classes to unpickle them
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import en_core_web_md
import pickle


class modelone():
    """A class that loades a pickled model, makes prediction on input,
    and returns the model predictions in a web injestable form for web_routes
    """
    def __init__(self, model_pickle: str, dtm_transformer: str) -> type(None):
        """Loads the Pickled model and transformer then save's them as class atributes
        Arguments:
        -----------
        model_pickle {str} : the file path to the model that is used to make predictions

        dtm_transformer {str} : the file path to the transformer compaonest that
        processes input text
        Returns:
        -------
        None
        """
        # load pickles into ram and assign as attributes
        self.model = pickle.load(open(model_pickle, 'rb'))
        self.dtm_transformer = pickle.load(open(dtm_transformer, 'rb'))

        return

    def transform_predict(self, user_text: str) -> type(None):
        """Transform the input text and make predictions based on the trained model
        Arugments:
        -------------
        user_text {str} : the string that is used to make the prediction
        Returns:
        ----------
        None
        """
        # transform the text the user sent
        t = self.dtm_transformer.transform(user_text)
        # use knn to make results
        results = self.model.kneighbors(t.todense())
        # should be list of tuples
        self.results = results

        return

    def getResults(self) -> type(None):
        """Returns the results target variable from the prediction
        Arguments:
        ----------
        None
        Returns:
        -----------
        None
        """
        # just returning the id's of the results of the prediction
        return self.results[1]


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

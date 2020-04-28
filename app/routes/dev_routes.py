# !! 
# -------------------

# !!
import os
import pandas as pd
import pickle
from sklearn.neighbors import NearestNeighbors


# the path to the pickle files are working so long as in the routes 
# folder. Thats where it lived while troubleshooting
this_dir, this_filename = os.path.split(__file__)  # Get path of data.pkl

dtm_path = os.path.join(this_dir, 'dtm_combined.pkl')
dtm = pickle.load(open(dtm_path, 'rb'))

tf_path = os.path.join(this_dir, 'dtm_combined_tf.pkl')
tf = pickle.load(open(tf_path, 'rb'))

# the csv I was using as a base
URL = "https://raw.githubusercontent.com/Build-Week-Med-Cabinet-6/DS/mark-dev/data/cannabis.csv"

df = pd.read_csv(URL)
df = df.dropna()
#drop index 149 its a duplicate
df = df.drop(df.index[149])
df = df.reset_index(drop=True)
# Combine the Effects and Flavors in one column
df['Combined'] = df['Effects'] + ',' + df['Flavor']

@web_routes.route("/products/query_test/", methods=['POST'])
def predict(user_input):
    
    if 'effects' in request.args:
        effects = request.args['effects']

    if 'flavors' in request.args:
        flavors = request.args['flavors']


    if 'user_input' in request.args:
        user_input = request.args['user_input']

    ideal_strain = [user_input]
    
    # print("Function Firing")
    # import pdb; pdb.set_trace()

    # instantiate and fit 
    nn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
    nn.fit(dtm)

    #apply tfidf vectorization
    new = tf.transform(ideal_strain)
    
    results = nn.kneighbors(new.todense())

    #output results here, rec strains criteria and description
    rec_str = [strains['Strain'][results[1][0][i]] for i in range(5)]
    rec_crit = [strains['Combined'][results[1][0][i]] for i in range(5)]
    rec_str_desc = [strains['Description'][results[1][0][i]] for i in range(5)]
    
    rec1 = rec_str[0] + ' * ' + rec_crit[0] + ' * ' + rec_str_desc[0]
    rec2 = rec_str[1] + ' * ' + rec_crit[1] + ' * ' + rec_str_desc[1]
    rec3 = rec_str[2] + ' * ' + rec_crit[2] + ' * ' + rec_str_desc[2]
    rec4 = rec_str[3] + ' * ' + rec_crit[3] + ' * ' + rec_str_desc[3]
    rec5 = rec_str[4] + ' * ' + rec_crit[4] + ' * ' + rec_str_desc[4]

    return rec1, rec2, rec3, rec4, rec5

#from app_dash import cache


import pandas as pd
from sklearn import datasets

TIMEOUT = 60

#@cache.memoize(timeout=TIMEOUT)
def query_data():
    # This could be an expensive data querying step
    iris_raw = datasets.load_iris()
    iris = pd.DataFrame(iris_raw["data"], columns=iris_raw["feature_names"])
    return iris.to_json(date_format='iso', orient='split')

def dataframe():    
    return pd.read_json(query_data(), orient='split')

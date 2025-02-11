import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

#______________________________________________________________________________
#
# region ColumnTransformer
#______________________________________________________________________________
class ColumnTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, column_name, callable_job, bins):
        self.column_name = column_name
        self.job_to_be_done = callable_job
        self.bins = bins
    
    def fit(self, X, y=None):
        return self
    
    def get_feature_names_out(self, input_features=None):
        return np.array([self.column_name])

    def do_the_job(self, value) :
        return self.job_to_be_done(value)

    def transform(self, X_initial):
        X = pd.DataFrame(X_initial)
        
        if self.column_name not in X.columns:
            raise ValueError(f"La colonne '{self.column_name}' est absente des données")

        X[self.column_name] = X[self.column_name].apply(lambda val: self.do_the_job(val))

        return X
    
#______________________________________________________________________________
#
# region state_job
#______________________________________________________________________________
def state_job(self, value) :
    labels = str(value)

    return self.job_to_be_done(value)
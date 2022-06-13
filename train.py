"""Train model"""
import pandas as pd
import swifter
import numpy as np
from config import Config
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import mlflow
import mlflow.sklearn
from urllib.parse import urlparse

import pickle

config = Config()

df = pd.read_parquet(config.TRAIN_VECTORIZED)

X_train, X_test, y_train, y_test = train_test_split(np.stack(df.texts), df.label)

max_depth = 6
random_state = 14

with mlflow.start_run():

    clf = RandomForestClassifier(max_depth=max_depth, random_state=random_state)
    clf.fit(X_train, y_train)
    
    
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("random_state", random_state)

    tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
    print(tracking_url_type_store)

    # Model registry does not work with file store
    if tracking_url_type_store != "file":

        # Register the model
        # There are other ways to use the Model Registry, which depends on the use case,
        # please refer to the doc for more information:
        # https://mlflow.org/docs/latest/model-registry.html#api-workflow
        mlflow.sklearn.log_model(clf, "model", registered_model_name="random forest classifier")
    else:
        mlflow.sklearn.log_model(clf, "model")



with open("clf.pkl", "wb") as f:
    pickle.dump(clf, f)

pd.DataFrame({"texts": X_test.tolist(), "labels": y_test}).to_parquet(config.TRAIN_VALID)
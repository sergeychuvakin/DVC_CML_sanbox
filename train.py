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

max_depth = 7
random_state = 10
# run_id = mlflow.create_experiment("auna")
experiment = mlflow.get_experiment_by_name("auna")

with mlflow.start_run(experiment_id=experiment.experiment_id, run_name= f"run_{'ouf'}"):

    clf = RandomForestClassifier(max_depth=max_depth, random_state=random_state)
    clf.fit(X_train, y_train)
    
    
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("random_state", random_state)

    tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
    print(tracking_url_type_store)

    # mlflow.sklearn.log_model(
    #     sk_model=clf,
    #     artifact_path="sklearn-model",
    #     registered_model_name="sk-learn-random-forest-reg-model"
    # )
    mlflow.sklearn.log_model(clf, "model")



with open("clf.pkl", "wb") as f:
    pickle.dump(clf, f)

pd.DataFrame({"texts": X_test.tolist(), "labels": y_test}).to_parquet(config.TRAIN_VALID)
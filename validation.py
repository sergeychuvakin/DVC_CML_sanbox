"""Validation"""
import pandas as pd
import swifter
from sklearn.metrics import f1_score
from config import Config
import numpy as np
import json
import pickle

import mlflow
import mlflow.sklearn

config = Config()

df = pd.read_parquet(config.TRAIN_VALID)
with open("clf.pkl", "rb") as f:
    clf = pickle.load(f)

experiment = mlflow.get_experiment_by_name("auna")

with mlflow.start_run(experiment_id=experiment.experiment_id, run_name= f"run_{'ouf'}"):

    y_pred = clf.predict(np.stack(df.texts))

    f1_macro = f1_score(df.labels, y_pred, average="macro")
    f1_micro = f1_score(df.labels, y_pred, average="micro")
    f1_weighted = f1_score(df.labels, y_pred, average="weighted")

    mlflow.log_metric("f1_macro", f1_macro)
    mlflow.log_metric("f1_micro", f1_micro)
    mlflow.log_metric("f1_weighted", f1_weighted)


with open("metrics.json", "w") as f:
    json.dump(
        {
            "f1_score (macro)": f1_macro,
            "f1_score (micro)": f1_micro,
            "f1_score (weighted)": f1_weighted,
        },
        f,
    )

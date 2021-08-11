"""Validation"""
import pandas as pd
import swifter
from sklearn.metrics import f1_score
from config import Config
import numpy as np

import pickle

config = Config()

df = pd.read_parquet(config.TRAIN_VALID)
with open("clf.pkl", "rb") as f:
    clf = pickle.load(f)

y_pred = clf.predict(np.stack(df.texts))

with open("metrics.txt", "w") as f:
    f.write(f"f1_score (macro): {f1_score(df.labels, y_pred, average='macro')}")
    f.write("\n")
    f.write(f"f1_score (micro): {f1_score(df.labels, y_pred, average='micro')}")
    f.write("\n")
    f.write(f"f1_score (weighted): {f1_score(df.labels, y_pred, average='weighted')}")
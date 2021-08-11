"""Train model"""
import pandas as pd
import swifter
import numpy as np
from config import Config
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import pickle

config = Config()

df = pd.read_parquet(config.TRAIN_VECTORIZED)

X_train, X_test, y_train, y_test = train_test_split(np.stack(df.texts), df.label)

clf = RandomForestClassifier(max_depth=10, random_state=0)
clf.fit(X_train, y_train)

with open("clf.pkl", "wb") as f:
    pickle.dump(clf, f)

pd.DataFrame({"texts": X_test.tolist(), "labels": y_test}).to_parquet(config.TRAIN_VALID)
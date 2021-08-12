"""Get Raw Data""" 
from sklearn.datasets import fetch_20newsgroups
import pandas as pd
from config import Config

config = Config()

data = fetch_20newsgroups(subset='train')
df = pd.DataFrame({"text": data.data, "label": data.target}).sample(2000).reset_index(drop=True)
df.to_csv(config.TRAIN_RAW)
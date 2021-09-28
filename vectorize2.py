"""vectorize"""
import pandas as pd
import swifter
from config import Config
from sklearn.feature_extraction.text import TfidfVectorizer


config = Config()
vectorizer = TfidfVectorizer(max_features=3000)

df = pd.read_csv(config.TRAIN_PROCESSED_2)
vectorizer.fit(df.text)

df.loc[:, "vecs"] = (
    df
     .text
     .swifter
     .progress_bar(True)
     .apply(lambda x: vectorizer
            .transform([x])
            .todense()
            .tolist()[0])
                    )

df[["vecs", "label"]].rename(columns={"vecs": "texts"}).to_parquet(config.TRAIN_VECTORIZED_2)
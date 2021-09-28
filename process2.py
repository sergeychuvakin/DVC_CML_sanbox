"""Preprocessing"""
import pandas as pd
from config import Config
import spacy 
import swifter
import stopwords
from nltk.tokenize import TreebankWordTokenizer
import string


config = Config()
df = pd.read_csv(config.TRAIN_RAW_2)


nlp = spacy.load("en_core_web_sm")
stops = stopwords.get_stopwords("english")
tokenizer = TreebankWordTokenizer()
punctuations = string.punctuation

def preprocess_raw_text(sentence):
    """
    Method to designed to make basic text preprocessing before label prediction
    Args:
        sentence: str - text to preprocess

    """
    mytokens = nlp(sentence)
    mytokens = [word.lemma_.lower().strip() for word in mytokens]
    mytokens = [
        word
        for word in mytokens
        if word not in stops and word not in punctuations
    ]
    mytokens = " ".join(mytokens)
    return mytokens

df = df.iloc[:1000,].reset_index(drop=True)
df.loc[:, "text"] = df.text.swifter.progress_bar(True).apply(preprocess_raw_text)
df.to_csv(config.TRAIN_PROCESSED_2)
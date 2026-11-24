import re, time, warnings
from collections import Counter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from IPython.display import HTML, display

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer
from nltk.stem import PorterStemmer

CAT_NAMES  = {1: "News & Politics", 2: "CS & Data Science", 3: "Lit, Music & TV",
              4: "Health & Fitness", 5: "Food, Home & Pets"}

df = pd.read_csv("Team 5 - Corpus.csv")
corpus = pd.DataFrame(df[['text', 'category_1', 'category_2', 'sentiment']])

corpus.insert(0, "doc_id", range(1, len(corpus) + 1))
corpus.to_csv("demo_corpus.csv", index=False)          # same format as your Google Sheet export
print(f"Saved {len(corpus)} documents to demo_corpus.csv")

df["category_2"] = df["category_2"].astype(str)    # "none" or "1"–"5"
df["category"]   = df["category_1"].map(CAT_NAMES) # readable name of the main category
df["type"]       = np.where(df["category_2"] == "none", "Single", "Mixed")
df["n_words"]    = df["text"].str.split().str.len()

# Check the number of documents
print("Number of documents:", len(df))

# Display the first few documents
df.head(8)



def show_tokens(tokens, color="steelblue"):
    chips = "".join(f'<span style="background-color:{color};color:white;padding:3px 9px;margin:3px;'
                    f'border-radius:12px;display:inline-block;font-family:monospace;font-size:13px">{t}</span>'
                    for t in tokens)
    display(HTML(chips))

nltk.download('punkt_tab')

raw = df.loc[0, "text"]
print("RAW   :", raw, "\n")
print("SENTS :")
for s in sent_tokenize(raw):
    print("   •", s)
print("\nWORDS :")
show_tokens(word_tokenize(raw))

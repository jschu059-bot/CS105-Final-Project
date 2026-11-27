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

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity

CAT_NAMES  = {1: "News & Politics", 2: "CS & Data Science", 3: "Lit, Music & TV",
              4: "Health & Fitness", 5: "Food, Home & Pets"}

df = pd.read_excel("Team 5.xlsx", sheet_name="Corpus")
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


STOP_WORDS = ENGLISH_STOP_WORDS
stemmer = PorterStemmer()

def preprocess(text, stem=False):
    if pd.isna(text):
        return []

    tokens = re.findall(r"[a-z]+", str(text).lower())
    tokens = [t for t in tokens if t not in STOP_WORDS and len(t) > 1]

    if stem:
        tokens = [stemmer.stem(t) for t in tokens]

    return tokens

df["tokens"] = df["text"].apply(preprocess)
df["clean"]  = df["tokens"].str.join(" ")        # cleaned text, ready for vectorizers

example = df.loc[60, "text"]
print("Original :", example)
show_tokens(preprocess(example))
show_tokens(preprocess(example, stem=True), color="blue")


# How much does each step shrink the vocabulary?
all_text = " ".join(df["text"].dropna().astype(str))

steps = {
    "raw split()":         set(all_text.split()),
    "lowercase + letters": set(re.findall(r"[a-z]+", all_text.lower())),
    "– stop words":        {t for toks in df.tokens for t in toks},
    "+ stemming":          {t for txt in df.text for t in preprocess(txt, stem=True)},
}

sizes = pd.Series({k: len(v) for k, v in steps.items()})

ax = sizes.plot.bar(color=["paleturquoise", "turquoise", "teal", "darkslategray"], rot=0, width=0.65, figsize=(8, 4))
for i, v in enumerate(sizes):
    ax.text(i, v + 8, v, ha="center", fontweight="bold")

ax.set_title("Unique words (= features) after each preprocessing step")
ax.set_ylabel("vocabulary size")
plt.show()

freq = Counter(t for toks in df.tokens for t in toks)
top = pd.Series(dict(freq.most_common(15)))

ax = top[::-1].plot.barh(color="navy", figsize=(8, 5))
ax.set_title("15 most frequent words (after cleaning)"); ax.set_xlabel("count")
for i, v in enumerate(top[::-1]):
    ax.text(v + 0.1, i, v, va="center", fontsize=9)
plt.show()

bow_vectorizer = CountVectorizer()
x_bow = bow_vectorizer.fit_transform(df["clean"])
bow_df = pd.DataFrame(x_bow.toarray(), columns = bow_vectorizer.get_feature_names_out())
print("Bow Matrix Shape: ",x_bow.shape)
display(bow_df.head())

tfidf_vectorizer = TfidfVectorizer();
x_tfidf = tfidf_vectorizer.fit_transform(df["clean"])

tfidf_df = pd.DataFrame(x_tfidf.toarray(),columns=tfidf_vectorizer.get_feature_names_out())
print("TF-IDF Matrix Shape:", x_tfidf.shape)
display(tfidf_df.head())
binary_vectorizer = CountVectorizer(binary=True)
x_binary = binary_vectorizer.fit_transform(df["clean"])
print("Binary Matrix Shape:", x_binary.shape)




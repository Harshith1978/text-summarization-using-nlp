"""
summarizer.py

Simple Extractive Text Summarizer using TF-IDF sentence scoring.
Run:
    python summarizer.py
"""

import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Download tokenizer (first run only)
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")


def summarize(text, num_sentences=3):
    sentences = sent_tokenize(text)

    if len(sentences) <= num_sentences:
        return text

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(sentences)

    # Importance score = sum of TF-IDF weights
    scores = np.asarray(tfidf.sum(axis=1)).ravel()

    top_idx = np.argsort(scores)[-num_sentences:]
    top_idx = sorted(top_idx)

    summary = " ".join(sentences[i] for i in top_idx)
    return summary


if __name__ == "__main__":
    print("=" * 60)
    print("Text Summarization Using NLP")
    print("=" * 60)

    choice = input(
        "\n1. Enter your own text\n2. Use sample_input.txt\n\nChoose (1/2): "
    ).strip()

    if choice == "2":
        try:
            with open("sample_input.txt", "r", encoding="utf-8") as f:
                document = f.read()
        except FileNotFoundError:
            print("sample_input.txt not found.")
            raise SystemExit
    else:
        print("\nPaste your text below (press Enter twice when finished):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        document = "\n".join(lines)

    print("\nOriginal Text\n")
    print(document)

    print("\n" + "=" * 60)
    print("Generated Summary\n")
    print(summarize(document, num_sentences=3))
    print("=" * 60)

 📝 Text Summarization Using Natural Language Processing

A supervised extractive text summarization system built using **Python**, **Scikit-learn**, and **Natural Language Processing (NLP)**. The project automatically identifies the most important sentences in a document and generates concise, meaningful summaries using **TF-IDF feature extraction** and a **Logistic Regression** classifier.

---

## 📌 Project Overview

Text summarization is an important task in Natural Language Processing that aims to reduce lengthy documents into shorter versions while preserving the key information.

This project implements a **Supervised Extractive Text Summarization** approach, where a machine learning model is trained to classify sentences based on their importance. The generated summary consists of the highest-ranked sentences from the original document.

---

## 🚀 Features

- Automatic text preprocessing
- Sentence tokenization
- TF-IDF feature extraction
- Sentence importance scoring
- Logistic Regression classifier
- Extractive summary generation
- Lightweight and efficient implementation
- Easy to understand and extend

---

## 🛠 Technologies Used

- Python
- Natural Language Processing (NLP)
- Scikit-learn
- Pandas
- NumPy
- TF-IDF Vectorization
- Logistic Regression
- Jupyter Notebook

---

## 📂 Project Structure

```
Text-Summarization-Using-NLP/
│
├── Text_Summarization_Extractive.ipynb
├── Text_Summarization_Supervised.ipynb
├── requirements.txt
├── sample_input.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YourUsername/text-summarization-using-nlp.git
```

Move into the project directory

```bash
cd text-summarization-using-nlp
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook

```bash
jupyter notebook
```

Open either notebook and run all the cells.

---

## 📖 How It Works

1. Load the input document.
2. Split the document into individual sentences.
3. Preprocess the text.
4. Extract sentence features using TF-IDF.
5. Train a Logistic Regression classifier.
6. Score each sentence based on importance.
7. Select the highest-ranked sentences.
8. Generate the final extractive summary.

---

## 📊 Machine Learning Pipeline

```
Input Document
       │
       ▼
Sentence Tokenization
       │
       ▼
Text Preprocessing
       │
       ▼
TF-IDF Feature Extraction
       │
       ▼
Logistic Regression Classifier
       │
       ▼
Sentence Ranking
       │
       ▼
Generated Summary
```

---

## 📈 Applications

- News Summarization
- Research Paper Summarization
- Document Summarization
- Legal Document Analysis
- Educational Content Summarization
- Article Summarization

---

## 🔮 Future Improvements

- TextRank-based summarization
- BERT embeddings
- Transformer-based summarization
- T5 and PEGASUS models
- ROUGE score evaluation
- Interactive web interface using Streamlit or Flask

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Harshith Reddy**

---

⭐ If you found this project useful, consider giving it a star!

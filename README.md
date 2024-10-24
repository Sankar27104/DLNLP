# Deep learning with Natural Language Processing
This repository showcases a variety of Natural Language Processing (NLP) techniques, implemented using Python libraries such as NLTK, Scikit-learn, Keras, and Gensim. Each section explores different text preprocessing and vectorization techniques along with deep learning implementations.
## Table of Contents
1. Text Preprocessing with NLTK
2. Word Count Vectors with Scikit-learn
3. Word Frequency Vectors with Scikit-learn (TF-IDF)
4. Hash Encoding with Scikit-learn
5. Text Splitting with Keras
6. One-Hot Encoding with Keras
7. Hash Encoding with Keras
8. Tokenizer API in Keras
9. Sentiment Analysis
10. Word2Vec Embedding with Gensim
## 1. Text Preprocessing with NLTK
This module demonstrates fundamental preprocessing techniques like:
+ Tokenization: Breaking text into words.
+ Stemming: Reducing words to their root form.
+ Lemmatization: More advanced word reduction based on vocabulary.
+ Stop Word Removal: Removing common words like "the", "is", etc., using NLTK.
Code is provided for each preprocessing step to clean and prepare raw text for further analysis.

## 2. Word Count Vectors with Scikit-learn
This section converts text into word count vectors using CountVectorizer from Scikit-learn. Word count vectors represent text data as a matrix, where each cell contains the frequency of a specific word.

## 3. Word Frequency Vectors with Scikit-learn (TF-IDF)
Using TfidfVectorizer, this module converts text into Term Frequency-Inverse Document Frequency (TF-IDF) vectors. TF-IDF emphasizes important words while diminishing the influence of frequent, less meaningful words.

## 4. Hash Encoding with Scikit-learn
This implementation uses HashingVectorizer to transform text into fixed-length hash-encoded vectors. This method is useful for large datasets and avoids the need to store a vocabulary in memory.

## 5. Text Splitting with Keras
In this section, we use Keras’s text_to_word_sequence to split text into sequences of words. This utility is useful in deep learning models that require text inputs to be tokenized into sequences.

## 6. One-Hot Encoding with Keras
This module implements one_hot encoding with Keras, converting words into one-hot encoded vectors that are useful for embedding layers in neural networks.

## 7. Hash Encoding with Keras
In this part, the hashing_trick method from Keras is used to convert text into hash-encoded representations. It’s a fast and memory-efficient way to map words to integers.

## 8. Tokenizer API in Keras
This section demonstrates the use of Keras's Tokenizer API, which splits text into tokens and converts them into integer sequences. Tokenizer also supports padding and truncating sequences for deep learning models.

## 9. Sentiment Analysis
A real-world sentiment analysis experiment on datasets (e.g., Twitter tweets, movie reviews). The experiment uses various models to classify text as either positive or negative.

## 10. Word2Vec Embedding with Gensim
This module implements Word2Vec using Gensim, which creates word embeddings based on the context of words in a corpus. These embeddings capture semantic similarities between words and are widely used in deep learning NLP tasks.


## Installation
To run the scripts, follow these steps:
1. Clone the repository:
   ```git clone https://github.com/your-repo-link/dlnlp.git```
2. Install the required dependencies:
   ```pip install -r requirements.txt```

## How to Use
Each topic has its own script. To run an experiment, navigate to the respective script and execute it with Python.

For example:
```python text_preprocessing_nltk.py```


Feel free to update this README as the project evolves!

Let me know if you need any adjustments!

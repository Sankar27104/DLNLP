# Using keras deep-learning library and split words with (text_to_word_sequence) 
#Keras is an open-source library written in Python. It provides a user-friendly modular interface for
#designing, building, training, and deploying various types of Artificial neural networks, particularly in deep learning networks.
#Keras was developed in a focus on enabling rapid experimentation and prototyping of learning.
import tensorflow as tf
print(tf.__version__)
from tensorflow.keras.preprocessing.text import text_to_word_sequence
text = 'The quick brown fox jumps over the lazy dog'
result = text_to_word_sequence(text)
print(result)
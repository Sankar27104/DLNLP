import tensorflow as tf
print(tf.__version__)
from tensorflow.keras.preprocessing.text import text_to_word_sequence

text = 'The quick brown fox jumps over the lazy dog'
result = text_to_word_sequence(text)
print(result)

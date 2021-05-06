from keras_preprocessing.text import text_to_word_sequence
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.text import one_hot

text = "Hei, dette er noe testtext"

tronder_file = open("TextInput/rawText.txt", "r", encoding="utf-8")
tronder_text = tronder_file.read()
tronder_file.close()

one_hot_result = one_hot(tronder_text, len(tronder_text))
ttws_result = text_to_word_sequence(tronder_text)

print(ttws_result)
print(one_hot_result)
print(len(ttws_result))
print(len(one_hot_result))
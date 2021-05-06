from keras_preprocessing.text import text_to_word_sequence

text = "Hei, dette er noe testtext"

tronder_file = open("TextInput/rawText.txt", "r", encoding="utf-8")
tronder_text = tronder_file.read()
tronder_file.close()

result = text_to_word_sequence(tronder_text)
print(result)
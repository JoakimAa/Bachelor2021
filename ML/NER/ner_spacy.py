import spacy

text_file = open("TextInput/rawText.txt", "r", encoding="utf-8")
text = text_file.read()
text_file.close()

print("-----------BEFORE JOIN--------------")
print(text)

text = str.join(" ", text.splitlines())

print("-----------AFTER JOIN--------------")
print(text)

nlp = spacy.load("nb_core_news_sm")

print("-----------SPACY OUTPUT--------------")
doc = nlp(text)

for entity in doc.ents:
    print(entity.text, entity.label)

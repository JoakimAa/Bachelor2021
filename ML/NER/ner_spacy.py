import spacy

text_file = open("TextInput/rawText_neptun.txt", "r", encoding="utf-8")
text = text_file.read()
text_file.close()

print("-----------BEFORE JOIN--------------")
print(text)

#text = str.join(" ", text.splitlines())

#print("-----------AFTER JOIN--------------")
#print(text)

nlp = spacy.load("pl_core_news_md")

print("-----------SPACY OUTPUT--------------")
doc = nlp(text)

for entity in doc.ents:
    print(entity.text, entity.label)

import spacy
from spacy.lang.nb.examples import sentences
from spacy import displacy

text_file = open("TextInput/rawText_neptun.txt", "r", encoding="utf-8")

nlp = spacy.load("nb_core_news_sm")

text_file = open("TextInput/rawText_tronder.txt", "r", encoding="UTF-8", )

text = text_file.read()
text_file.close()

print("-----------BEFORE JOIN--------------")
print(text)

# text = str.join(" ", text.splitlines())

# print("-----------AFTER JOIN--------------")
# print(text)


nlp = spacy.load("pl_core_news_md")

print("-----------SPACY OUTPUT--------------")
doc = nlp(text)
# displacy.serve(doc)
for ent in doc.ents:
    # print(ent.text, ent.label_)
    if (ent.label_ == "MISC"):
        print(ent.text)

#displacy.serve(doc, style='dep')
for doc in doc.ents:
    for ent in doc:
        # print(token.ent_type_)
        if ent.label_ == "MISC":
            subj = [w for w in ent.head if w.dep_ == "flat:name"]
            if subj:
                print(subj[0], "-->", ent.text)
            # We have a prepositional object with a preposition
        elif ent.dep_ == "noun" and ent.head.dep_ == "flat:name":
            print(ent.head.head, "-->", ent.text)
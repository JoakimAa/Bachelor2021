import spacy


def run_spacy(img_text):
    nlp = spacy.load("nb_core_news_sm")
    doc = nlp(img_text)
    price = get_price(doc)
    date = get_date(doc)

    return price, date


def get_price(doc):
    price_found = False
    price = 0
    for ent in doc.ents:
        if ent.label == "MONEY" and int(ent.text) > price:
            price = int(ent.text)
            price_found = True
    if price_found:
        return price
    return -1


def get_date(doc):
    date_found = False
    date = ""
    for ent in doc.ents:
        if ent.label == "DATE":
            date = ent.text
            date_found = True
    if date_found:
        return date
    return "Date not found"




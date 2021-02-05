try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

img = Image.open('img/testimg1.jpg')

#Henter data om bildets rotasjon og skirfttype (orientation and script detection)
print("------------------OSD data------------------\n")
print(pytesseract.image_to_osd(img, lang="nor"))

# Skriver ut output i streng-format
print("------------------Output in string format------------------\n")
print(pytesseract.image_to_string(img, lang="nor"))

#Lagrer output i pdf-format
pdf = pytesseract.image_to_pdf_or_hocr(img, extension='pdf', lang="nor")
with open('pdf_output.pdf', 'w+b') as f:
    f.write(pdf)

#Lagrer output i xml-format
xml = pytesseract.image_to_alto_xml(img,lang="nor")
xml_string = xml.decode("utf-8")
with open("xml_output.xml", "w") as f:
    f.write(xml_string)

#Lagrer output i hocr-format
hocr = pytesseract.image_to_pdf_or_hocr(img, extension='hocr',lang="nor")
hocr_string = hocr.decode('utf-8')
with open("hocr_output.xml", "w") as f:
    f.write(hocr_string)


from xml.etree import ElementTree as et

doc = et.parse("bookstore.xml")

for child in doc.getroot():
    print(child.tag, child.attrib)

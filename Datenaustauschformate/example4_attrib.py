from xml.etree import ElementTree as et

doc = et.parse("bookstore.xml")

for element in doc.findall("book"):
    print(element.attrib)
    print(element.attrib["category"])

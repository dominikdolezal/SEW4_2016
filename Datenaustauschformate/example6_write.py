from xml.etree import ElementTree as et

doc = et.parse("bookstore.xml")

for element in doc.findall("book"):
    if "stock" not in element.attrib:
        element.attrib["stock"] = "10"

doc.write("bookstore2.xml")

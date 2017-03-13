from xml.etree import ElementTree as et

doc = et.parse("bookstore.xml")
print(doc.find("book/title").text)

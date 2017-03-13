from xml.etree import ElementTree as et

doc = et.parse("bookstore.xml")

for element in doc.findall("book"):
    print(element.find("author").text + " " +
          element.find("year").text +
          ", €" + element.find("price").text)

from xml.etree import ElementTree as et

doc = et.parse("bookstore.xml")
print(et.tostring(doc.getroot()).decode('utf-8'))

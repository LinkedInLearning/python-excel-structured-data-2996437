import xml.etree.ElementTree as ET
import os

tree = ET.parse(os.getcwd()+"/daten/convertcsv.xml")
xml_data = tree.getroot()
print(xml_data)
print(xml_data.tag)
print(xml_data.attrib)
print(xml_data.text)
print("*" * 50)
print(type(xml_data))
print("*" * 50)
for child in xml_data:
    print(child, child.tag, child.attrib)
    for el in child:
        print(el.tag, el.attrib, el.text)
        
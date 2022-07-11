import xml.etree.ElementTree as ET

tree = ET.parse('static.xml')
root = tree.getroot()

for child in root.iter('ACTOR'):
    print(child.tag, child.text)

import xml.etree.ElementTree as ET

tree = ET.parse('static.xml')
root = tree.getroot()
print(ET.tostring(root))

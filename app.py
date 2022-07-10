import xml.etree.ElementTree as ET

tree = ET.parse('static.xml')
root = tree.getroot()
# print(ET.tostring(root))
for actor in root.findall('ACTOR'):
    print(tree.findall('ACTOR'))
    print(actor)
    print('\n')
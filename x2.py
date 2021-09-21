import xml.etree.ElementTree as ET

mytree = ET.parse("xml_sample.xml")
myroot = mytree.getroot()

# updating price attribute for all food nodes
for prices in myroot.iter('price'):
    prices.text = str(float(prices.text.strip('$')) + 10)
    prices.set('newprices', 'yes')

for x in myroot.findall('food'):
    ET.SubElement(x, "tasty")

for temp in myroot.iter("tasty"):
    temp.text = str("Yes")

# popping the element
print(myroot[1][0].attrib.pop('name'))

mytree.write('modified.xml')
"""
Nombre del programa:
Descripción:
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 17/12/22
"""
import xml.etree.ElementTree as ET
import random

"""
tree = ET.parse('victories.xml')
root = tree.getroot()

for element in root.iter('victory'):
    print(element.attrib.keys())
    print(element.attrib.get('choice'))
    print(element.attrib)

for element in root.findall('victory'):
    choices = element.get('choice')
    com_choices = element.get('against')
    print(choices, com_choices)

print("------------------------------")

for element in root.findall('victory'):
    choices = element.get('choice')
    com_choices = element.get('against')
    if choices == "Scissors":
        print(com_choices)

print("------------------------------")

for element in root.findall('victory'):
    element.get('choice')

for element in root.findall(".[@choice]"):
    print(element)

print(root.findall(".[@choice]"))
"""


def get_against_text(choice, xml_file):
  tree = ET.parse(xml_file)
  root = tree.getroot()
  against_text = []
  random_action = ''
  for victory in root.findall('victory'):
    if victory.get('choice') == choice:
      against_text.append(victory.get('against'))
      print(victory.get('against'))
  random_action = random.choice(against_text)
  return against_text


against_text = get_against_text('Scissors', 'victories.xml')
print(against_text)



from utilities import *
import pandas as pd




def elem_to_dictionary(elem):
    d=dict(tag=elem.tag)
    if elem.text:
        d['text']=elem.text
    if elem.attrib:
        d['attributes']=elem.attrib
    children=elem.getchildren()
    if children:
        d['children']=map(elem_to_dictionary, children)
    if elem.tail:
        d['tail']=elem.tail
    return d

                      
def to_json(elem):

    if hasattr(elem, 'getroot'):
        elem=elem.getroot()
    return simplejson.dumps(elem_to_dictionary(elem), indent=4 * ' ')


def depth(node):
    d = 0
    while node is not None:
        d += 1
        node = node.getparent()
    return d

def get_max_depth():
    levels = []

    for element in tree.getiterator():
        #print("Level: " + str(depth(element)))
        levels.append(depth(element))

    max_depth = max(levels)
    return max_depth

def to_xml_tree():
    for element in tree.getiterator():


        if element.text.strip() == "":
            print("Parent: " + str(element.tag))

        else:
            print("\tChild: " + str(element.tag) + " - " + repr(element.text.strip()))


    print("-" * 20)
    print("Max depth is: " + str(get_max_depth()))



def main():

    print(to_json(tree))
    to_xml_tree()




if __name__ == "__main__":
    main()
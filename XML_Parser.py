from utilities import *
import pandas as pd


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

def elem_to_pesterfish(elem):
    """
    turns an elementtree-compatible object into a pesterfish dictionary
    (not json).
    
    """
    d=dict(tag=elem.tag)
    if elem.text:
        d['text']=elem.text
    if elem.attrib:
        d['attributes']=elem.attrib
    children=elem.getchildren()
    if children:
        d['children']=map(elem_to_pesterfish, children)
    if elem.tail:
        d['tail']=elem.tail
    return d

                  
def to_pesterfish(elem):
    """
    turns an elementtree-compatible element or tree
    into a pesterfish json string.
    
    """
    if hasattr(elem, 'getroot'):
        elem=elem.getroot()
    return simplejson.dumps(elem_to_pesterfish(elem))


def main():

    print(to_pesterfish(tree))

    for element in tree.getiterator():

   
        if element.text.strip() == "":
            print("Parent: " + str(element.tag))
    
        else:
            print("\tChild: " + str(element.tag) + " - " + repr(element.text.strip()))


    print("-" * 20)
    print("Max depth is: " + str(get_max_depth()))

'''
    NESTED_DEPTH_CHILD = 0


    print("Root tag: " + str(root.tag))
    print("Root attrib: " + str(root.attrib))
    print("Root text: " + repr(root.text))

    for child in root:
        #print("Child tag: " + str(child.tag))
        #print("Child attrib: " + str(child.attrib))
        #print("Child text: " + repr(child.text))

        listOfChildTags = [x.tag for x in root.findall(child.tag+"/*")]


        NESTED_DEPTH_CHILD += 1

    print(listOfChildTags[0:])


    getUniqueSet = {}

    for elem in listOfChildTags:
        getUniqueSet.insert(elem)

    print(getUniqueSet)
'''
'''
    print("\t\t\tNested Depth: " + str(NESTED_DEPTH_CHILD))

    if NESTED_DEPTH_CHILD == 1:

        for child in root:
            for sub_child in child:
                print("Subchild tag: " + str(sub_child.tag))
                #print("Subchild attrib: " + str(sub_child.attrib))
                #print("Subchild text: " + repr(sub_child.text))
                NESTED_DEPTH_SUB_CHILD += 1

'''

if __name__ == "__main__":
    main()
# Imports
import sys
sys.dont_write_bytecode=True

from lxml import etree as ET
            
import simplejson

# Utilities


def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)


class _Const():
    @constant
    def XML_FILE():
    # Edit static final variable here
        return 'test.xml'
    @constant
    def TAG_TO_FIND():
        # Edit the tag for which you want to find children of
        return 'breakfast_menu' #e.g. headlines


#Global Constant var
CONST = _Const()
tags = []

tree = ET.parse(CONST.XML_FILE)
root = tree.getroot()
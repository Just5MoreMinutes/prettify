##################################################
#                    IMPORTS                     #
##################################################
from typing import NewType

from err import NOCOLOREXCEPTION

##################################################
#                      MAIN                      #
##################################################
#--------- TYPING ---------#
color = NewType('color', str) # -> color type, clarifying certain types for easier understanding

#--------- FUNCTIONS ---------#
#: rgb
def rgb(r,g,b,bg=False) -> str:
    """
    Converts RGB to escape sequence
    """
    return '\033[{};2;{};{};{}m'.format(48 if bg else 38,r,g,b)

#: hex
def hex(code,bg=False) -> str:
    """
    Converts HEX to escape sequence
    """
    tmp = tuple(int(code.strip('#')[i:i+2],16) for i in (0,2,4))
    return '\033[{};2;{};{};{}m'.format(48 if bg else 38,tmp[0],tmp[1],tmp[2])

#: auto converter
def converter(inpt, *tdict) -> str:
    if inpt in tdict.keys():
        tmp = inpt
        pass

    if inpt[0] == '#':
        tmp = hex(inpt)
    elif inpt[0] == '\\':
        tmp = inpt
    else: raise NOCOLOREXCEPTION
    return tmp

#--------- CLASSES ---------#
#: styled printer
class StyledPrinter:
    def __init__(self, inpt, _color) -> None:
        self.inpt = inpt
        self._color = _color

    def color_assign(self, inpt, _color) -> color:
        ...

#: prettify main class
class prettify:

    col_list = { }
    pal_list = { }
    elm_list = { }
    reset    = reset = '\033[0m'

    def addColor(self, name, col):
        #: prettify.addColor('light_green', 'rgb(93, 222, 117)')
        #: prettify.addColor('light_green', '#5dde75')
        self.col_list[name] = converter(col)
    
    def createPalette(self, name, items):
        """
        Add up to 5 items to a palette
        """
        #: prettify.createPalette('palette_name', ['light_green', 'other_color', 'more_color'])
        #:                          background      extras          primary       secondary     tercary
        pal_items = []
        for i in items: pal_items.append(converter(i))
        self.pal_list[name] = pal_items

    def paletteSettings(self, pal):
        """
        Make your palette apply to only certain items.
        """
        ...

    def returnList(self, _list) -> dict:
        if _list == 'col':
            return self.col_list
        if _list == 'pal':
            return self.pal_list
        if _list == 'elm':
            return self.elm_list

prettify = prettify()
StyledPrinter = StyledPrinter()
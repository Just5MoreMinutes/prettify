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

    col_list = { 'red': '\033[38;2;252;0;0m',
                 'blue': '\033[38;2;0;0;255m',
                 'green': '\033[38;2;0;255;0m',
                 'yellow':  '\033[38;2;255;255;0m',
                 'purple': '\033[38;2;160;32;240m',
                 'orange': '\033[38;2;255;165;0m', 
                 'light_red': '\033[38;2;255;204;203m',
                 'light_blue': '\033[38;2;173;216;230m',
                 'light_green': '\033[38;2;144;238;144m' }
    pal_list = { }
    elm_list = { 'bold': '\033[1m',
                 'underline': '\033[4m',
                 'warning': '\033[48;2;255;0;0m \033[1m',
                 'notice': '\033[48;2;255;255;0m',
                 'italic': '\033[3m',
                 
                 'end_bold': '\033[22m',
                 'end_underline': '\033[24m',
                 'end_warning': '\033[49m \033[22m',
                 'end_notice': '\033[49m',
                 'end_italic': '\033[23m' }
    reset    = '\033[0m'

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
StyledPrinter = StyledPrinter('','')
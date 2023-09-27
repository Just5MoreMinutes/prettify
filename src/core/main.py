"""
prettify.py is a library to make styling your command-line
output easier. It allows you to change colors, fonts, 
font-sizes and much more all in one line. Besides that
prettify has a variety of other features that allow you to
add and create your own palettes and presets to use in your
program. prettify.py is designed to be as lightweight as 
possible while also adding lots of features to your program.
prettify.py does not rely on external libraries.

VERSION: 0.0.1 (alpha)
"""
##################################################
#                    IMPORTS                     #
##################################################
from prettify import rgb, hex, converter
from err import NOCOLOREXCEPTION

##################################################
#                      MAIN                      #
##################################################
def pprint(str_inpt:str, *further:list) -> str:
    ...
##################################################
#                    IMPORTS                     #
##################################################
from presets import preset_list
from prettify import (prettify, rgb, hex)
from err import (NOCOLOREXCEPTION, EXITSEQUENCE, 
                 NOELEMENTEXCEPTION)

##################################################
#                      MAIN                      #
##################################################
class parser:
    completed = []
    """
    The parser is supposed to take apart an input-string and
    convert the tags to their corresponding escape sequences.
    This done by separating the string into smaller pieces and 
    then replacing the tags one by one before dissolving the
    list created at the start and creating a new string from 
    said list.

    Below is a list of in-line tags (elements in [] are palceholers and 
    are to be replaced in the program):
    - <bold> / <b>: make a text-element bold
    - <underline> / <u>: underline a text-element
    - <italic> / <i>: make text-element italic
    - <[color]>: set a custom font-color
    - <bg:[color]>: set a custom background color for a text-element
    - <[font]>: set a custom font for a text-element

    Beside the in-line tags above, there is a list of full-line tags.
    These tags have to be placed at the start of a line and affect the 
    entire line. 
    Below is a list of all full-line tags:
    - <palette:[palette-name]>: apply a custom palette to the text
    - <sticky:[top/bottom]>: make text stick to the top or bottom
    - <line-wipe> / <lw>: this line gets wiped from the screen as soon as 
    a new one appears. This means that the line will basically be replaced
    by the next one
    - <style:[styling arguments]>: see "styleParser"
    Further features of the library cannot be handled by the main parser (this
    one) and will therefore be the secondary parser's tasks. See 
    "secondary_parser".
    """
    def splitter(self, inpt) -> None:
        #: sample string: "<light_green>Hello, <underline>world</underline></light_green>!"
        __start = 0
        while __start < len(inpt):
            tag_open = inpt.find('<', __start)
            if tag_open == -1:
                self.completed.append(inpt[__start:])
                break
            
            tag_close = inpt.find('>', tag_open)
            if tag_close == -1:
                break

            if tag_open > __start: 
                self.completed.append(inpt[__start:tag_open])

            tag = inpt[tag_open:tag_close + 1]
            self.completed.append(tag)

            __start = tag_close + 1

    def interpret(self) -> str:
        for i in self.completed:
            if i.startswith('<\\'):
                self.completed[self.completed.index(i)] = prettify.reset
                pass
            if i[1:-1] in prettify.returnList('col') and i.startswith('<'):
                self.completed[self.completed.index(i)] = prettify.returnList('col')[i]
            else: 
                if '<' in i and '>' in i: raise (NOCOLOREXCEPTION, EXITSEQUENCE)
                if '<' not in i or '>' not in i: pass
            if i[1:-1] in prettify.returnList('elm') and i.startswith('<'):
                self.completed[self.completed.index(i)] = prettify.returnList('elm')[i]
            else:
                if '<' in i and '>' in i: raise (NOCOLOREXCEPTION, NOELEMENTEXCEPTION, EXITSEQUENCE)
                if '<' not in i or '>' not in i: pass
            if i[1:-1] in prettify.returnList('pal') and i.startswith('<'):
                secondary_parser.paletteHandler(i)

parser = parser()
                
class secondary_parser:
    """
    The secondary parser is supposed to handle tasks which
    are simply too large for the parser class. This includes 
    the palette handling, styling lists, and things like 
    in-string mutes. While the main parser is tasked with
    identifying and replacing the tags, the secondary parser
    has to first understand and implement the more complex
    elements, before handing them to the main parser to be
    implemented. 
    A list of features the secondary parser handles:
    PALETTES:
        prettify.paletteSettings()
        prettify.usePalette()
        prettify.switchPaletteOn()
    STYLING:
        pprint(list)
        pprint(dict)
        pprint(tuple)
    TAGS:
        str = "Hello <mute until=func()>World<\mute>!"
    In the rare case that the <style> tag requires more than
    just regular element replacement, the secondary parser
    will once again be used to implement more complex
    functionality.
    """
    def paletteHandler(pal) -> str:
        """
        NOTE ON PALETTES:
        The palette format as seen in the sample.txt file has to be
        used at all times. At index 0, is the primary color, at 1, 
        is the secondary color, at 2, there is the tercary color. 
        At the optional last index (4) would be the color that is to be
        used for background colors.
        While there are 3 different primary colors (0,1,2) that can be
        used, it is highly encouraged to set 'tercary' to None in
        prettify.paletteSettings().
        prettify.usePalette(<paletteName>) has to be used in order
        to engage the palette. It will be used until a new palette 
        has been engaged, or until the program has ended.
        """
        ...

secondary_parser = secondary_parser()
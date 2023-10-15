##################################################
#                    IMPORTS                     #
##################################################
from presets import preset_list
from prettify import (prettify, rgb, hex,
                      converter)
from err import (NOCOLOREXCEPTION, EXITSEQUENCE, 
                 NOELEMENTEXCEPTION, UNKNOWNCOLOREXCEPTION)

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
    def textSplitter(self, inpt) -> None:
        """
        The splitter is used to split the input text into smaller
        snippets, which can later be used to replace the tags with their
        corresponding escape sequences.
        """
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

    def findAllCorresponding(self) -> str:
        """
        The interpret function is used to correctly identify the tag
        type and hands it down to the correct handler which will then
        take care of replacing the tag with a corresponding escape
        sequence.
        """
        reset = prettify.reset
        for i in self.completed:
            #: close-tag
            if i.startswith('</'):
                self.completed[self.completed.index(i)] = reset # -> NOTE: keep it at that for NOW
                pass
            #: color-tags
            if i[1:-1] in prettify.returnList('col') and i.startswith('<'):
                self.completed[self.completed.index(i)] = prettify.returnList('col')[i[1:-1]] # -> replaces current index with col dict value
            else: 
                if '<' not in i or '>' not in i: pass
            #: other elements
            if i[1:-1] in prettify.returnList('elm') and i.startswith('<'):
                self.completed[self.completed.index(i)] = prettify.returnList('elm')[i[1:-1]] # -> replaces current index with elm dict value
            else:
                # if '<' in i and '>' in i: raise NOELEMENTEXCEPTION
                if '<' not in i or '>' not in i: pass
            #: <palette> tag
            if i[1:-1] in prettify.returnList('pal') and i.startswith('<'):
                secondary_parser.inLinePaletteHandler(i)

    def convertAllColors(self) -> str:
        """
        Converts all colors remaining in the 'completed' list and
        resets the colors accordingly.
        """
        _rgb = []
        for i in self.completed:
            if i.startswith('<'):
                if i[1] == '#':
                    self.completed[self.completed.index(i)] = hex(i[1:-1])
            if i.startswith('rgb('):
                _rgb = i[4:-1].split(',')
                self.completed[self.completed.index(i)] = rgb(int(_rgb[0]),int(_rgb[1]),int(_rgb[2]))
    
    def convertAllElements(self) -> str:
        """
        Converts all elements remaining in the 'completed' list and
        resets them accordingly.
        """
        ...

    def provideCompleted(self) -> completed: return self.completed
    def printCompleted(self) -> str: print(self.completed)

parser = parser()
                
class secondary_parser:
    completed = []
    inline    = []
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
    def inLinePaletteHandler(self, pal, txt) -> str:
        """
        NOTE ON PALETTES:
        The palette format as seen in the sample.txt file has to be
        used at all times. At index 0, is the primary color, at 1, 
        is the secondary color, at 2, there is the tertiary color. 
        At the optional last index (4) would be the color that is to be
        used for background colors.
        While there are 3 different primary colors (0,1,2) that can be
        used, it is highly encouraged to set 'tertiary' to None in
        prettify.paletteSettings().
        prettify.usePalette(<paletteName>) has to be used in order
        to engage the palette. It will be used until a new palette 
        has been engaged, or until the program has ended.

        Explaining parameters: \n
        - pal: gets the palette's name (str)
        - txt: gets the full text-element including the in-line palette element (list)
        """
        _pal_list = prettify.returnList('pal') # -> dict
        _col_list = prettify.returnList('col')
        _pal = _pal_list[pal] # -> get items (dict key: pal parameter; dict value: specific color palette)

        #: <palette> tag
        for i in _pal:
            if i not in _col_list: raise (NOCOLOREXCEPTION, UNKNOWNCOLOREXCEPTION)
            else: 
                if i.startswith('#'):
                    _pal[_pal.index(i)] = hex(i)
                else:
                    _pal[_pal.index(i)] = _col_list[_col_list.index(i)]

        pal_tmp = []
        pal_start = int
        pal_end   = int
        txt_len   = len(txt) - 1
        cur_index = -1 # -> starts at -1 so the first list item is at index 0 not 1
        #: while loop to find all palette tags and remember their index if a tag was found
        while cur_index < txt_len:
            for i in txt:
                if i == f'<palette={str}>':
                    pal_start = txt.index(i)
                if i == '</palette>':
                    pal_end = txt.index(i)
                cur_index += 1

        #: iterate through 'txt' again and append all items between opening and closing tag to pal_tmp
        for i in txt:
            if txt.index(i) >= pal_start and txt.index(i) <= pal_end:
                pal_tmp.append(i)
        del (txt_len, cur_index) # -> IMPORTANT: pal_start and pal_end MUST remain set because the styled text will be inserted back into txt

        pal_edit = {} # -> includes all items in pal_tmp but with type identificators
        #: find tags between <palette> tags
        for i in pal_tmp:
            if i[0] and i[-1] == '>':
                pal_edit[i] = 'type:palette'
            else:
                pal_edit[i] = 'type:text'

class styleHandler:
    """
    The style handler is the the handler used to replace tags with
    corresponding escape sequences. This is done using the rgb, hex and
    converter function from the prettify.py file. 
    """
    def inLinePaletteConversion(self, pal_edit:dict, _pal:list) -> list:
        _keys = pal_edit.keys()
        #: NOTE: here comes code to replace the tags INBETWEEN the <palette> tags
        #        this code will be implemented as soon as there is a way to detect,
        #        replace and handle the tags adequately. This is ONLY used for in-line
        #        palettes.
        completed = parser.provideCompleted()

styleHandler     = styleHandler()     
secondary_parser = secondary_parser()
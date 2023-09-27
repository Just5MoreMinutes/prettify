# prettify.py
prettify.py is a simple library to make styling command-line outputs easier. 

***NOTE***: Many of the features mentioned here are yet to be implemented, I just decided to write this README to procrastinate working on the project

Styling outputs with prettify.py works somewhat similar to using tags in HTML. You first provide an opening tag (`<tag-name>`), followed by some text, and then a closing tag (`<\tag-name>`).
In the README file, you will find a quick guide on how to use the library, and a list of all tags and how to use them appropriately.

ALSOOOO, prettify.py does not use any external libraries and is completely standalone. The only external module that has been imported is `typing.NewType` as a quality of (my) life measure

## Samples
Below you will find a handful of sample code-snippets that demonstrate the program.

First, here is a simple print-statement with prettify.py. prettify.py introduces the `pprinter` functions, which you will use in order to use the library's features:

#### Sample #1
The sample below makes the word "World" red. Now, as prettify.py is able to convert both **RGB** and **HEX** codes into escape sequences, you are free to use them whenever you like.
```python
pprinter("Hello, <#fc0303>World<\#fc0303>!")
```

#### Sample #2
If you aren't a fan of copying the **RGB** or **HEX** codes all the time, you can add your own, custom, color using `prettify.addColor(<color-name>, <rgb/hex-code>)`:
```python
prettify.addColor('light_red', '#e6374e')
pprinter("Hello, <light_red>World<\light_red>")
```

#### Sample #3
You can also add and use color-palettes. These will automatically detect and style certain elements. For a more detailed explanation, please take a look at the full documentation once it's published.
In the example below, the text will be colored in `#4A5759`, the tags `<highlight>`, `<notice>` and `<warning>` will be colored in `#B0C4B1`, the color `#F7E1D7` will not be used, and lastly, the color `delft_blue` (a custom color) will be used for all `<background>` or `<bg>` elements.
```python
prettify.addPalette('main', ['#4A5759', '#B0C4B1', '#F7E1D7', 'delft_blue'])
prettify.paletteSettings(primary='default', secondary=['highlight', 'notice', 'warning'], tercary=None)
prettify.usePalette('main')

pprinter("Hello, <highlight>World</highlight>!")
```

## Tags
Below you can find a list of all tags:
#### General tags:
`<[color]>`: Sets a text-element to a custom color <br>
`<bg:[color]`>: Sets background color to a custom color <br>
`<bold>`: Makes text bold <br>
`<italic>`: Makes text italic (not supported by all machines) <br>
`<underline>`: Makes text underlined <br>
`<notice>`: Provides custom styling that makes text element more prominent. NOTE: `<notice>` should not be used mid statement! Only at the alone, at the start or end! <br>
`<warning>`: The same as `<notice>` just more flashy <br>
`<highlight>`: Combines multiple tags for a very flashy text element <br>
`<[font]>`: Changes the font of the text to <br>
`<palette:[palette-name]>`: For changing palettes mid-print. This will not disengage a palette engaged using `prettify.usePalette()`! <br>
`<sticky:[top/bottom]>`: Make text element to one end of the window <br>
`<linewipe>` or `<lw>`: The current line will automatically be wiped (disappears) from the screen <br>
`<mute until=[func]>`: Mute a certain text-element until a certain function has been executed

... and more to come
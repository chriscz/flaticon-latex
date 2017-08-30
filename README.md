Introduction
------------
Script that takes a Flaticon font package, extracts the names of all glyphs from
the CSS file included by Flaticon and generates a LaTeX source file with commands 
for each glyph.

Example
-------
See the `snippet.tex` file for how this was produced.

![Presentation Overview](/screenshot.png?raw=true)

Quick Intro
-----------
1. create and download a font package from [Flaticon](http://www.flaticon.com/).
2. unzip the font directory into your latex project, say to the `font/` directory
3. cd into your project directory
4. execute:
    python process-fonts.py -b fonts/ > flaticon.tex 
5. you may need to edit the source file to change the location
   of the flaticon font file.
6. you should be using XeTeX or LuaTeX as your LaTeX compiler.
7. enjoy!

Name Mappings
-------------
1. All `-`'s are removed from names
2. All digits are mapped as follows:
```
   1 -> q
   2 -> w
   3 -> e
   4 -> r
   5 -> t
   6 -> y
   7 -> u
   8 -> i
   9 -> o
   0 -> p
```
3. this uses the top row of a qwerty keyboard, which
   makes translation from digits to letters fairly obvious.
4. for example, if the glyph name is `big-cat44` then the name 
   would be translated to `bigcatrr`.


Example
-------
A small example can be found under the `example/` directory.
It contains some useful font definitions.

   
AWK Script
----------
This project also contains the original translation AWK script.
The script is not maintained, and may be removed in the future.
   
   
   
   
   
   
   
   
   

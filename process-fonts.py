# Processes a CSS file included in a flaticon (http://flaticon.com) 
# archive, extracts the indexes and names of all ttf symbols and 
# generates latex commands corresponding to each
from __future__ import print_function
import re
import os
import sys
import argparse
from StringIO import StringIO

PREAMBLE_COMMENT =\
'''
%%
% FLATICON EXTRACTOR OUTPUT
%
% To use this in a latex project, use \input{output.latex} where
% output.latex contains this file.
%
%%
'''

name_translation = {
        '-': '',
        '0': 'p',
        '1': 'q',
        '2': 'w',
        '3': 'e',
        '4': 'r',
        '5': 't',
        '6': 'y',
        '7': 'u',
        '8': 'i',
        '9': 'o',
}

def error(fmat, *args, **kwargs):
    print("[ERROR] {}".format(fmat.format(*args, **kwargs)), file=sys.stderr)
    sys.exit(1)

def translate(string, dict):
    s = list(string)
    for i, c in enumerate(s):
        if c in dict:
            s[i] = dict[c]
    return ''.join(s)

def main(base, cssfile, prefix, family, fontfile_name):
    name_pattern = re.compile(r'^\}?\.flaticon-([^:]*):before')
    content_pattern = re.compile(r'^\s*content: "\\([^"]*)";')                                                       
    latexfontline = r'\def\{prefix}{name}{{\{family}\symbol{{"{ident}}}}}'

    font_name = None
    
    # print the preamble
    print(PREAMBLE_COMMENT)
#    print("\AtBeginDocument{\@ifpackageloaded{babel}{}{\RequirePackage{fontspec}}}")
    print("\\newfontfamily\\{family}[Path={base}]{{{fontfile_name}}}\n\n".format( 
            family=family,
            base=base,
            fontfile_name=fontfile_name))

    with open(cssfile, 'r') as f:
        for line in f:
            if name_pattern.match(line):
                font_name = name_pattern.match(line).group(1)
                font_name = translate(font_name, name_translation)
            elif font_name and content_pattern.match(line):
                ident = content_pattern.match(line).group(1)
                ident = ident.upper()
                print(latexfontline.format(prefix=prefix, 
                                           name=font_name,
                                           family=family,
                                           ident=ident))     
                font_name = None
        print("\n%% END OF FLATICON FONTS\n") 
            
            

if __name__ == '__main__':
    pass

    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-b','--base', help='The directory containing extracted flaticon fonts', required=True)
    parser.add_argument('-p','--prefix', help='The prefix to use for linux font commands', default='fl')
    parser.add_argument('-c','--css', help='The CSS file, relative to `--base`, in the flaticon directory', default='flaticon.css')
    parser.add_argument('-f','--family', help='Font family name to use', default='Flaticon')
    parser.add_argument('-g','--ttf-file', help='The font file to use', default='flaticon.ttf')
    args = vars(parser.parse_args())

    prefix = args['prefix']
    basedir = args['base']
    css_name = args['css']
    family = args['family']
    ttf_name = args['ttf_file']

    css = os.path.join(basedir, css_name)
    ttf = os.path.join(basedir, ttf_name)
    
    if not os.path.exists(css):
        error("font CSS file `{}` does not exist in directory {}", css_name, basedir)

    if not os.path.exists(ttf):
        error("font TTF file `{}` does not exist in directory {}", ttf_name, basedir)

    if not os.path.exists(basedir):
        error("base `{}` does not exist.", basedir)
    elif not os.path.isdir(basedir):
        error("base `{}` not a directory.", basedir)

    main(basedir, css, prefix, family, ttf_name)

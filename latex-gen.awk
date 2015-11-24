# Process a CSS file downloaded from freepik and spit out a latex file to define all the fonts
#

BEGIN {
    DIR="fonts/"
    FONT="flaticon.ttf"
    FAMILY="Flaticon"
    PREFIX="fl"

    printf("%% Flaticon font extractor\n")
    printf("\\newfontfamily\\%s[Path=%s]{%s}\n\n", FAMILY, DIR, FONT)
}

{
    if (match($0,"(^|\\})\\.flaticon-(.*?):before", grp)) {
        didmatch=1  
        name=grp[2]
        gsub("-", "", name)
        gsub("0", "p", name)
        gsub("1", "q", name)
        gsub("2", "w", name)
        gsub("3", "e", name)
        gsub("4", "r", name)
        gsub("5", "t", name)
        gsub("6", "y", name)
        gsub("7", "u", name)
        gsub("8", "i", name)
        gsub("9", "o", name)
    } else if (didmatch && match($0,"content:[::blank::]*...(.*?).;", ident)) {
        printf("\\def\\%s%s{\\%s\\symbol{\"%s}}\n", PREFIX, name, FAMILY, toupper(ident[1]));
        didmatch=0
    }
    

}

END {
    printf("\n%% END OF FLATICON FONTS\n")
}



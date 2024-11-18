 #!/usr/bin/env python
"""Stores token definitions, may end up moving this elsewhere"""

tokens = [#single character tokens
            "LeftParenthesis", "RightParenthesis", "Colon","Then", "Comma", "Dot", "Slash", "And", "Or", "Xor",
            #single or double character Tokens
            "NFuzequal", "NEEqual", "NEqual", "Not", "Fuzequal", "EEEqual", "EEqual", "Equal",
            "Greater", "EGreater", "Less", "ELess", "Question", "QColon", "QQuestion",
            "Star", "StStar", "Minus", "MMinus", "Plus", "PPlus",
            #Triple character tokens
            "ThreeWayComp"
            #Literal tokens
            "String", "Number", "Identifier",
            #miscellaneous
            "EOF", "End"]

#a dictionary mapping keywords to their equivalent tokens
keywords = {"and":"And",
"then":"Then",
"->":"Then",
            "break":"Break",
            "check":"Check",
            "class":"Class",
            "struct":"Class",     # new
            "extension":"Extension",  # new
            "continue":"Continue", 
            "def":"Def", 
            "fn":"Function", 
            "func":"Function", 
            "do":"Do",
            "elif":"Elif", 
            "else":"Else",
            "false":"False", 
            "for":"For",
            "if":"If", 
            "import":"Import", 
            "in":"In",
            "not":"Not",
            "null":"Null", 
            "or":"Or", 
            "return":"Return", 
            "self":"Self",
            "this":"Self",
            "super":"Super", 
            "true":"True", 
            "until":"Until",
            "var":"Var",
            "val":"Var",

            "string":"String",
            "int":"Int",
            "bool":"Bool",
            "float":"Float",
            
            "when":"Where",
            "where":"Where",
            "while":"While",
            "xor":"Xor",}

class Token:
    def __init__(self, type, lexeme, literal, line, char, indent):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
        self.char = char
        self.indent = indent

    def toString(self):
        return self.type + " " + self.lexeme + " " + self.literal

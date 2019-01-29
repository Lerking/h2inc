"""Contains class PARSER"""
from itertools import count

#Element type definitions. Used in the parse process.
ELEMENT_TYPE_PREPROCESS = 1
ELEMENT_TYPE_REGULAR = 2

TOKENS = ['TOKEN_CSTART','TOKEN_CMID','TOKEN_CEND','TOKEN_RPAREN',
        'TOKEN_LPAREN','TOKEN_ENDLINE','TOKEN_RETVAL','TOKEN_PREPROCESS',
        'TOKEN_ID','TOKEN_PLUS','TOKEN_MINUS','TOKEN_DIV','TOKEN_MULT',
        'TOKEN_ASSIGN','TOKEN_EQUAL','TOKEN_LBRACE','TOKEN_RBRACE',
        'TOKEN_COMMA','TOKEN_SEMICOLON','TOKEN_LANGLE','TOKEN_RANGLE','TOKEN_POINTER']

RESERVED = {'auto'  : 'AUTO','break' : 'BREAK','case' : 'CASE','char' : 'CHAR',
        'const' : 'CONST','continue' : 'CONTINUE','default' : 'DEFAULT','do' : 'DO',
        'int' : 'INT','long' : 'LONG','register' : 'REGISTER','return' : 'RETURN',
        'short' : 'SHORT','signed' : 'SIGNED','sizeof' : 'SIZEOF','static' : 'STATIC',
        'struct' : 'STRUCT','switch' : 'SWITCH','typedef' : 'TYPEDEF','union' : 'UNION',
        'unsigned' : 'UNSIGNED','void' : 'VOID','volatile' : 'VOLATILE','while' : 'WHILE',
        'double' : 'DOUBLE','else' : 'ELSE','enum' : 'ENUM','extern' : 'EXTERN',
        'float' : 'FLOAT','for' : 'FOR','goto' : 'GOTO','if' : 'IF'}

PREPROCESSOR_DIRECTIVES = {'#include' : 'TOKEN_PREPROCESS','#define' : 'TOKEN_PREPROCESS','#undef' : 'TOKEN_PREPROCESS',
        '#if' : 'TOKEN_PREPROCESS','#ifdef' : 'TOKEN_PREPROCESS','#ifndef' : 'TOKEN_PREPROCESS','#error' : 'TOKEN_PREPROCESS',
        '__FILE__' : 'TOKEN_PREPROCESS','__LINE__' : 'TOKEN_PREPROCESS','__DATE__' : 'TOKEN_PREPROCESS',
        '__TIME__' : 'TOKEN_PREPROCESS','__TIMESTAMP__' : 'TOKEN_PREPROCESS','pragma' : 'TOKEN_PREPROCESS',
        '#' : 'TOKEN_PREPROCESS','##' : 'TOKEN_PREPROCESS','#endif' : 'TOKEN_PREPROCESS'}

REGULAR = {'/*' : 'TOKEN_CSTART','*/' : 'TOKEN_CEND', '*' : 'TOKEN_CMID', '=' : 'TOKEN_ASSIGN','==' : 'TOKEN_EQUAL',
        '{' : 'TOKEN_LBRACE','}' : 'TOKEN_RBRACE','\+' : 'TOKEN_PLUS','-' : 'TOKEN_MINUS',
        '\*' : 'TOKEN_MULT','/' : 'TOKEN_DIV','\(' : 'TOKEN_LPAREN','\)' : 'TOKEN_RPAREN',
        ',' : 'TOKEN_COMMA',';' : 'TOKEN_SEMICOLON','\<' : 'TOKEN_LANGLE','\>' : 'TOKEN_RANGLE'}

NASM_PREPROCESS_DIRECTIVES = {'#include' : '%include','#define' : '%define','#undef' : '%undef',
        '#if' : '%if','#ifdef' : '%ifdef','#ifndef' : '%ifndef','#endif' : '%endif',
        '#error' : '%error','__FILE__' : '__FILE__','__LINE__' : '__LINE__',
        '__DATE__' : '__DATE__','__TIME__' : '__TIME__','__TIMESTAMP__' : '__TIMESTAMP__',
        'pragma' : 'pragma','#' : '#','##' : '##'}

NASM_ENUM = "EQU"

NASM_REGULAR = {'/*' : ';', '*' : ';', '*/' : ''}

TOKENS += RESERVED.values()

COMMENT_SINGLE_LINE = 0
COMMENT_MULTI_LINE = 1

class PARSEOBJECT:
    _passes = count(0)
    
    def __init__(self):
        self.parseline = []
        self.parsefile = []
        self.passes = 0
    
    def parse_reset(self):
        self.parseline = []
        self.parsefile = []
        self._passes = count(0)
        self.inside_comment = False
        self.inside_typedef = False
        self.typedef_enum = False
        self.enum_begin = False

    def inc_passes(self):
        self.passes = next(self._passes)

    def parseheader(self, fl):
        tempfile = []
        self.parse_reset()
        for l in fl:
            analyzed_line = self.analyzer(l)
            tempfile.append(analyzed_line)
        self.inc_passes()
        self.parsefile = self.parsetokens(tempfile)
        return self.parsefile

    def parseinclude(self, data):
        tempstr = str(data)
        if tempstr.startswith('<'):
            tempstr = tempstr.replace('<', '"')
            tempstr = tempstr.replace('.h>', '.inc"')
        if tempstr.endswith('.h'):
            tempstr = '"'+tempstr
            tempstr = tempstr.replace('.h', '.inc"')
        return tempstr

    def tokenizer(self, w):
        token = ""
        if w in PREPROCESSOR_DIRECTIVES:
            token = PREPROCESSOR_DIRECTIVES.get(w)
            return token
        if w in REGULAR:
            token = REGULAR.get(w)
            return token
        return False

    def analyzer(self, ln):
        analysed = []
        word = [w for w in ln.split()]
        for w in word:
            t = self.tokenizer(w)
            if t == False:
                analysed.append(w)
                continue
            else:
                analysed.append(t)
                analysed.append(w)
        return analysed

    def parsetokens(self, fl):
        templine = []
        tempfile = []
        enum_cnt = 0

        for l in fl:
            templine = []
            tempstr = ""
            if len(l) == 0:
                templine.append("\n")
                continue
            if l[0] == "TOKEN_CSTART" or l[0] == "TOKEN_CMID" or l[0] == "TOKEN_CEND":
                self.inside_comment = True
                tempfile.append(self.parse_comment(l))
                continue
            if l[0] == "TYPEDEF" or l[0] == "typedef":
                self.parse_typedef(l)
                if self.typedef_enum == False:
                    templine.append("; ")
                    for e in l:
                        templine.append(e)
                    tempfile.append(templine)
                continue
            if l[0] == "TOKEN_PREPROCESS":
                tempfile.append(self.parse_preprocess(l))
                continue
            if self.inside_typedef == True:
                if self.typedef_enum == True:
                    if l[0] == "TOKEN_LBRACE" and len(l) == 2:
                        self.enum_begin = True
                        continue
                    if len(l) == 1:
                        if l[0].endswith(","):
                            tempstr = l[0]
                            templine.append(tempstr[:-1]+"\t")
                            templine.append("EQU\t")
                            templine.append(str(enum_cnt)+"\n")
                            tempfile.append(templine)
                            enum_cnt += 1
                            continue
                        else:
                            templine.append(l[0]+"\t")
                            templine.append("EQU\t")
                            templine.append(str(enum_cnt)+"\n")
                            tempfile.append(templine)
                            enum_cnt += 1
                            continue
                    if len(l) == 3:
                        if l[0].endswith(","):
                            tempstr = l[0]
                            enum_cnt = l[2]
                            templine.append(tempstr[:-1]+"\t")
                            templine.append("EQU"+"\t")
                            templine.append(enum_cnt+"\n")
                            tempfile.append(templine)
                            continue
                    if l[0] == "TOKEN_RBRACE" and len(l) == 3:
                        self.enum_begin = False
                        self.typedef_enum = False
                        self.inside_typedef = False
                        enum_cnt = 0
                        continue
        return tempfile

    def parse_typedef(self, l):
        templine = []
        for w in l:
            if w == "TYPEDEF" or w == "typedef":
                self.inside_typedef = True
                continue
            if w == "ENUM" or w == "enum":
                self.typedef_enum = True
                continue
            

    def parse_comment(self, l):
        templine = []
        for w in l:
            if w in TOKENS:
                continue
            if w in NASM_REGULAR:
                templine.append(NASM_REGULAR.get(w))
                continue
            templine.append(w)
        return templine

    def parse_preprocess(self, l):
        newline = []
        for w in l:
            if w in TOKENS:
                continue
            if w in PREPROCESSOR_DIRECTIVES:
                newline.append(NASM_PREPROCESS_DIRECTIVES.get(w))
                continue
            if w.startswith("<"):
                newline.append(self.parseinclude(w))
                continue
            if w in NASM_REGULAR:
                newline.append(NASM_REGULAR.get(w))
                continue
            newline.append(w)
        return newline
                

class PARSER(PARSEOBJECT):
    _ids = count(0)
    _passes = count(0)

    def __init__(self):
        self.id = next(self._ids)
        self.tupline = []
        self.tupfile = []
        self.passes = next(self._passes)
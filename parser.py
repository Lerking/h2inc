'''
Contains class PARSER
'''
from itertools import count
import os
from tokenizer import TOKENIZER

#Element type definitions. Used in the parse process.
ELEMENT_TYPE_PREPROCESS = 1
ELEMENT_TYPE_REGULAR = 2

TOKENS = ['TOKEN_CSTART','TOKEN_CMID','TOKEN_CEND','TOKEN_RPAREN',
        'TOKEN_LPAREN','TOKEN_ENDLINE','TOKEN_RETVAL','TOKEN_TYPEDEF',
        'TOKEN_IF','TOKEN_PLUS','TOKEN_MINUS','TOKEN_DIV','TOKEN_MULT',
        'TOKEN_ASSIGN','TOKEN_EQUAL','TOKEN_LBRACE','TOKEN_RBRACE',
        'TOKEN_COMMA','TOKEN_SEMICOLON','TOKEN_LANGLE','TOKEN_RANGLE',
        'TOKEN_POINTER', 'TOKEN_STRUCT','TOKEN_ENUM','TOKEN_MACRO',
        'TOKEN_FUNCTION','TOKEN_TYPEDEF_ENUM','TOKEN_TYPEDEF_STRUCT',
        'TOKEN_TYPEDEF_STRUCT_STRUCT']

RESERVED = {'auto'  : 'AUTO','break' : 'BREAK','case' : 'CASE','char' : 'CHAR',
        'const' : 'CONST','continue' : 'CONTINUE','default' : 'DEFAULT','do' : 'DO',
        'int' : 'INT','long' : 'LONG','register' : 'REGISTER','return' : 'RETURN',
        'short' : 'SHORT','signed' : 'SIGNED','sizeof' : 'SIZEOF','static' : 'STATIC',
        'struct' : 'STRUCT','switch' : 'SWITCH','typedef' : 'TYPEDEF','union' : 'UNION',
        'unsigned' : 'UNSIGNED','void' : 'VOID','volatile' : 'VOLATILE','while' : 'WHILE',
        'double' : 'DOUBLE','else' : 'ELSE','enum' : 'ENUM','extern' : 'EXTERN',
        'float' : 'FLOAT','for' : 'FOR','goto' : 'GOTO','if' : 'IF'}

PREPROCESSOR_DIRECTIVES = {'#include' : 'TOKEN_INCLUDE','#define' : 'TOKEN_DEFINE','#undef' : 'TOKEN_UNDEFINE',
        '#if' : 'TOKEN_IF','#ifdef' : 'TOKEN_IFDEF','#ifndef' : 'TOKEN_IFNDEF','#error' : 'TOKEN_ERROR',
        '__FILE__' : 'TOKEN_BASE_FILE','__LINE__' : 'TOKEN_BASE_LINE','__DATE__' : 'TOKEN_BASE_DATE',
        '__TIME__' : 'TOKEN_BASE_TIME','__TIMESTAMP__' : 'TOKEN_BASE_TIMESTAMP','pragma' : 'TOKEN_PRAGMA',
        '#' : 'TOKEN_HASH','##' : 'TOKEN_DOUBLEHASH','#endif' : 'TOKEN_ENDIF'}

REGULAR = {'/*' : 'TOKEN_CSTART','/**' : 'TOKEN_CSTART','*/' : 'TOKEN_CEND', '*' : 'TOKEN_CMID', '=' : 'TOKEN_ASSIGN',
        '==' : 'TOKEN_EQUAL','{' : 'TOKEN_LBRACE','}' : 'TOKEN_RBRACE','};' : 'TOKEN_ENDBRACE','+' : 'TOKEN_PLUS','-' : 'TOKEN_MINUS',
        '*' : 'TOKEN_MULT','/' : 'TOKEN_DIV','(' : 'TOKEN_LPAREN',')' : 'TOKEN_RPAREN',',' : 'TOKEN_COMMA',
        ';' : 'TOKEN_SEMICOLON','<' : 'TOKEN_LANGLE','>' : 'TOKEN_RANGLE','TYPEDEF' : 'TOKEN_TYPEDEF',
        'typedef' : 'TOKEN_TYPEDEF','enum' : 'TOKEN_ENUM','ENUM' : 'TOKEN_ENUM','struct' : 'TOKEN_STRUCT',
        'STRUCT' : 'TOKEN_STRUCT','char' : 'TOKEN_CHAR','CHAR' : 'TOKEN_CHAR','const' : 'TOKEN_CONST',
        'CONST' : 'TOKEN_CONST','int' : 'TOKEN_INT','INT' : 'TOKEN_INT','long' : 'TOKEN_LONG','LONG' : 'TOKEN_LONG',
        'short' : 'TOKEN_SHORT','SHORT' : 'TOKEN_SHORT','signed' : 'TOKEN_SIGNED','SIGNED' : 'TOKEN_SIGNED',
        'unsigned' : 'TOKEN_UNSIGNED','UNSIGNED' : 'TOKEN_UNSIGNED','void' : 'TOKEN_VOID','VOID' : 'TOKEN_VOID',
        'volatile' : 'TOKEN_VOLATILE','VOLATILE' : 'TOKEN_VOLATILE','double' : 'TOKEN_DOUBLE','DOUBLE' : 'TOKEN_DOUBLE',
        'float' : 'TOKEN_FLOAT','FLOAT' : 'TOKEN_FLOAT', '!defined' : 'TOKEN_NOT_DEFINED', '!DEFINED' : 'TOKEN_NOT_DEFINED',
        'boolean' : 'TOKEN_BOOLEAN', 'BOOLEAN' : 'TOKEN_BOOLEAN', '(*' : 'TOKEN_FUNCTION_POINTER'}

NASM_PREPROCESS_DIRECTIVES = {'#include' : '%include','#define' : '%define','#undef' : '%undef',
        '#if' : '%if','#ifdef' : '%ifdef','#ifndef' : '%ifndef','#endif' : '%endif',
        '#error' : '%error','__FILE__' : '__FILE__','__LINE__' : '__LINE__',
        '__DATE__' : '__DATE__','__TIME__' : '__TIME__','__TIMESTAMP__' : '__TIMESTAMP__',
        'pragma' : 'pragma','#' : '#','##' : '##'}

NASM_ENUM = "EQU"

NASM_REGULAR = {'/*' : ';', '*' : ';', '*/' : ''}

#REGULAR += RESERVED.values()

PARSER_TOKENS = ['PARSE_MULTILINE_COMMENT', 'PARSE_SINGLELINE_COMMENT', 'PARSE_TYPEDEF_ENUM', 'PARSE_TYPEDEF_STRUCT',
                'PARSE_TYPEDEF_STRUCT_STRUCT', 'PARSE_STRUCT', 'PARSE_TAG_NAME', 'PARSE_STRUCT_MEMBER', 'PARSE_ENDSTRUCT',
                'PARSE_ALIAS', 'PARSE_FUNCTION_POINTER', 'PARSE_FUNCTION', 'PARSE_IFNDEF']

COMMENT_SINGLE_LINE = 0
COMMENT_MULTI_LINE = 1

inside_member = False
inside_braces = False
inside_typedef_struct_struct = False
inside_typedef_struct = False
inside_typedef_enum = False
inside_typedef = False
inside_struct = False
inside_include = False
inside_string = False
inside_comment = False
inside_if = False
inside_ifndef = False
substitute = False

class PARSEOBJECT:
    _passes = count(0)
    
    def __init__(self):
        self.tokenize = TOKENIZER()
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
        self.typedef_struct = False
        self.struct_begin = False
        self.enum_begin = False
        self.struct = False
        self.struct_end = False

    def inc_passes(self):
        self.passes = next(self._passes)

    def parseheader(self, fl, fn):
        tempfile = []
        tempfile1 = []
        outfile = ''
        self.parse_reset()
        for l in fl:
            analyzed_line = self.analyzer(l)
            tempfile.append(analyzed_line)
        self.inc_passes()
        for l in tempfile:
            analyzed_line = self.token_analyzer(l)
            tempfile1.append(analyzed_line)
        for l in tempfile1:
            for w in l:
                outfile += w+" "
            outfile += "\n"
        outputfile = os.path.splitext(fn)[0]+'.tokenized'
        self.write_file(outputfile,outfile)
        self.inc_passes()
        tempfile = []
        for l in tempfile1:
            analyzed_line = self.parser_analyzer(l)
            tempfile.append(analyzed_line)
        for l in tempfile:
            for w in l:
                outfile += w+" "
            outfile += "\n"
        outputfile = os.path.splitext(fn)[0]+'.parsenized'
        self.write_file(outputfile,outfile)
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
        global inside_comment
        global inside_string
        global inside_include
        global inside_struct
        token = ""
        if w in PREPROCESSOR_DIRECTIVES:
            token = PREPROCESSOR_DIRECTIVES.get(w)
            return token
        if w in REGULAR:
            token = REGULAR.get(w)
            return token
        if w.startswith('/*'):
            inside_comment = True
            token = 'TOKEN_CSTART'
            return token
        if inside_comment == True:
            if w.endswith('*/'):
                inside_comment = False
                token = 'TOKEN_CEND'
                return token
        if w.startswith('"'):
            inside_string = True
            return False
        if w.endswith('"'):
            inside_string = False
            return False
        if w.isupper():
            if inside_string == True:
                return False
            else:
                token = 'TOKEN_MACRO'
                return token
        if w.islower():
            if inside_string == True or inside_include == True or inside_struct == True:
                return False
            else:
                if w.startswith('(*'):
                    token = 'TOKEN_FUNCTION_POINTER'
                    return token
                else:
                    token = 'TOKEN_FUNCTION'
                    return token
        return False

    def analyzer(self, ln):
        global inside_include
        global inside_typedef
        global inside_typedef_enum
        global inside_typedef_struct
        global inside_typedef_struct_struct
        global inside_braces
        global inside_struct
        global inside_member
        analysed = []
        word = [w for w in ln.split()]
        for w in word:
            t = self.tokenizer(w)
            if t == 'TOKEN_INCLUDE':
                inside_include = True
            if t == 'TOKEN_TYPEDEF':
                inside_typedef = True
            if t == 'TOKEN_ENUM' and inside_typedef == True:
                inside_typedef_enum = True
                inside_typedef = False
                analysed.pop(0)
                analysed.insert(0,'TOKEN_TYPEDEF_ENUM')
                analysed.append(w)
                continue
            if t == 'TOKEN_STRUCT':
                if inside_typedef == True:
                    if ln.endswith(';\n'):
                        inside_typedef_struct = True
                        inside_typedef = False
                        analysed.pop(0)
                        analysed.insert(0,'TOKEN_TYPEDEF_STRUCT')
                        analysed.append(w)
                        continue
                    else:
                        inside_typedef_struct_struct = True
                        inside_typedef_struct = False
                        inside_typedef = False
                        analysed.pop(0)
                        analysed.insert(0,'TOKEN_TYPEDEF_STRUCT_STRUCT')
                        analysed.append(w)
                        inside_typedef_struct_struct = False #### THIS needs to be further refined!
                        continue
                else:
                    inside_struct = True
                    analysed.append(t)
                    analysed.append(w)
                    continue
            if t == 'TOKEN_LBRACE':
                inside_braces = True
                analysed.append(w)
                continue
            if t == 'TOKEN_RBRACE' and inside_struct == True:
                inside_braces = False
                inside_struct = False
                analysed.append(t)
                analysed.append(w)
                continue
            if inside_braces == True and inside_struct == True:
                if inside_member == True:
                    inside_member = False
                    analysed.append(w)
                    continue
                else:
                    t = 'TOKEN_MEMBER'
                    inside_member = True
                    analysed.append(t)
                    analysed.append(w)
                    continue
            if t == False:
                analysed.append(w)
                continue
            else:
                analysed.append(t)
                analysed.append(w)
        inside_include = False
        inside_struct = False
        return analysed

    def token_analyzer(self, ln):
        global inside_comment
        analyzed = []
        for w in ln:
            if w == 'TOKEN_CSTART':
                inside_comment = True
                analyzed.append(w)
                continue
            if inside_comment == True:
                if w == 'TOKEN_MULT':
                    analyzed.append('TOKEN_CMID')
                    continue
                else:
                    if w == 'TOKEN_CEND':
                        analyzed.append(w)
                        inside_comment = False
                        continue
                    else:
                        if w.startswith('TOKEN'):
                            continue
            analyzed.append(w)
        return analyzed

    def parser_analyzer(self, ln):
        global inside_comment
        global inside_if
        global inside_ifndef
        global substitute
        analyzed = []
        subst = []
        for w in ln:
            if w == 'TOKEN_CSTART':
                inside_comment = True
                if ln[-1] != 'TOKEN_CEND':
                    analyzed.append('PARSE_MULTILINE_COMMENT')
                    continue
                else:
                    analyzed.append('PARSE_SINGLELINE_COMMENT')
                    continue
            if w == 'TOKEN_CMID':
                analyzed.append('PARSE_MULTILINE_COMMENT')
                continue
            if w == 'TOKEN_CEND':
                inside_comment = False
                continue
            if inside_comment == False:
                if w == '*/':
                    continue
            if w == 'TOKEN_IF':
                inside_if = True
                analyzed.append('PARSE_IF')
                continue
            if inside_if == True:
                if w == 'TOKEN_NOT_DEFINED':
                    substitute = True
                    inside_if = False
                    inside_ifndef = True
                    subst.append('PARSE_IFNDEF')
                    continue
                else:
                    analyzed.append(w)
                    continue
            if substitute == True:
                subst.append(w)
                continue
            else:
                analyzed.append(w)
                continue
        return analyzed

    def parsetokens(self, fl):
        templine = []
        tempfile = []
        enum_cnt = 0

        for l in fl:
            templine = []
            tempstr = ""
            if l == []:
                templine.append("")
                tempfile.append(templine)
                continue
            if "TOKEN_CSTART" in l:
                self.inside_comment = True
                tempfile.append(self.parse_comment(l))
                continue
            if "TOKEN_CMID" in l:
                self.inside_comment = True
                tempfile.append(self.parse_comment(l))
                continue
            if "TOKEN_CEND" in l:
                self.inside_comment = True
                tempfile.append(self.parse_comment(l))
                continue
            if "TYPEDEF" in l:
                self.parse_typedef(l)
                if self.typedef_enum == False and self.typedef_struct == False:
                    templine.append("; ")
                    for e in l:
                        templine.append(e)
                    tempfile.append(templine)
                if self.typedef_struct == True:
                    templine.append('struc')
                    templine.append(l[-1][:-1])
                    tempfile.append(templine)
                    templine = []
                    templine.append('endstruc')
                    tempfile.append(templine)
                continue
            if "typedef" in l:
                self.parse_typedef(l)
                if self.typedef_enum == False and self.typedef_struct == False:
                    templine.append("; ")
                    for e in l:
                        templine.append(e)
                    tempfile.append(templine)
                if self.typedef_struct == True:
                    templine.append('struc')
                    templine.append(l[-1][:-1])
                    tempfile.append(templine)
                    templine = []
                    templine.append('endstruc')
                    tempfile.append(templine)
                continue
            if "struct" in l:
                self.parse_struct(l)

            if "TOKEN_PREPROCESS" in l:
                tempfile.append(self.parse_preprocess(l))
                continue
            if self.inside_typedef == True:
                if self.typedef_enum == True:
                    if l[0] == "TOKEN_LBRACE" and len(l) == 2:
                        self.enum_begin = True
                        enum_cnt = 0
                        continue
                    if len(l) == 1:
                        if l[0].endswith(","):
                            tempstr = l[0]
                            templine.append(tempstr[:-1]+"\t")
                            templine.append("EQU\t")
                            templine.append(str(enum_cnt))
                            tempfile.append(templine)
                            enum_cnt += 1
                            continue
                        else:
                            templine.append(l[0]+"\t")
                            templine.append("EQU\t")
                            templine.append(str(enum_cnt))
                            tempfile.append(templine)
                            continue
                    if len(l) == 3:
                        if l[0].endswith(","):
                            tempstr = l[0]
                            enum_cnt = l[2]
                            templine.append(tempstr[:-1]+"\t")
                            templine.append("EQU"+"\t")
                            templine.append(enum_cnt)
                            tempfile.append(templine)
                            continue
                    if l[0] == "TOKEN_RBRACE" and len(l) == 3:
                        self.enum_begin = False
                        self.typedef_enum = False
                        self.inside_typedef = False
                        enum_cnt = 0
                        continue
        return tempfile

    def parse_struct(self, l):
        templine = []
        for w in l:
            if w == "struct":
                self.struct = True
                templine.append('struc')
                continue
            if w != "":
                templine.append(w)
                continue
            if w == "{" and self.struct == True:
                self.struct_begin = True
                continue
        return templine

    def parse_typedef(self, l):
        templine = []
        for w in l:
            if w == "TYPEDEF" or w == "typedef":
                self.inside_typedef = True
                continue
            if w == "ENUM" or w == "enum":
                self.typedef_enum = True
                self.typedef_struct = False
                continue
            if w == "STRUCT" or w == "struct":
                self.typedef_struct = True
                self.typedef_enum = False
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
                
    def write_file(self, fn, data):
        if not os.path.exists(os.path.dirname(fn)):
            try:  
                os.makedirs(os.path.dirname(fn))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        newfile = open(fn, "w")
        newfile.write(data)
        newfile.close()

class PARSER(PARSEOBJECT):
    _ids = count(0)
    _passes = count(0)

    def __init__(self):
        self.id = next(self._ids)
        self.tupline = []
        self.tupfile = []
        self.passes = next(self._passes)
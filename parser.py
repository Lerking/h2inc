from itertools import count

TOKENS = ['CSTART','CMID','CEND','RPAREN','LPAREN','ENDLINE','RETVAL','PREPROCESS',
        'ID','PLUS','MINUS','DIV','MULT','ASSIGN','EQUAL','LBRACE','RBRACE',
        'COMMA','SEMICOLON','LANGLE','RANGLE','POINTER']

RESERVED = {'auto'  : 'AUTO','break' : 'BREAK','case' : 'CASE','char' : 'CHAR',
        'const' : 'CONST','continue' : 'CONTINUE','default' : 'DEFAULT','do' : 'DO',
        'int' : 'INT','long' : 'LONG','register' : 'REGISTER','return' : 'RETURN',
        'short' : 'SHORT','signed' : 'SIGNED','sizeof' : 'SIZEOF','static' : 'STATIC',
        'struct' : 'STRUCT','switch' : 'SWITCH','typedef' : 'TYPEDEF','union' : 'UNION',
        'unsigned' : 'UNSIGNED','void' : 'VOID','volatile' : 'VOLATILE','while' : 'WHILE',
        'double' : 'DOUBLE','else' : 'ELSE','enum' : 'ENUM','extern' : 'EXTERN',
        'float' : 'FLOAT','for' : 'FOR','goto' : 'GOTO','if' : 'IF'}

PREPROCESSOR_DIRECTIVES = {'#include' : 'PREPROCESS','#define' : 'PREPROCESS','#undef' : 'PREPROCESS',
        '#if' : 'PREPROCESS','#ifdef' : 'PREPROCESS','#ifndef' : 'PREPROCESS','#error' : 'PREPROCESS',
        '__FILE__' : 'PREPROCESS','__LINE__' : 'PREPROCESS','__DATE__' : 'PREPROCESS',
        '__TIME__' : 'PREPROCESS','__TIMESTAMP__' : 'PREPROCESS','pragma' : 'PREPROCESS',
        '#' : 'PREPROCESS','##' : 'PREPROCESS'}

REGULAR = {'/*' : 'CSTART','*/' : 'CEND','=' : 'ASSIGN','==' : 'EQUAL',
        '{' : 'LBRACE','}' : 'RBRACE','\+' : 'PLUS','-' : 'MINUS',
        '\*' : 'MULT','/' : 'DIV','\(' : 'LPAREN','\)' : 'RPAREN',
        ',' : 'COMMA',';' : 'SEMICOLON','\<' : 'LANGLE','\>' : 'RANGLE'}

NASM_PREPROCESS_DIRECTIVES = {'#include' : '$include','#define' : '$define','#undef' : '$undef',
        '#if' : '$if','#ifdef' : '$ifdef','#ifndef' : '$ifndef',
        '#error' : '$error','__FILE__' : '__FILE__','__LINE__' : '__LINE__',
        '__DATE__' : '__DATE__','__TIME__' : '__TIME__','__TIMESTAMP__' : '__TIMESTAMP__',
        'pragma' : 'pragma','#' : '#','##' : '##'}
    
TOKENS += RESERVED.values()

#Element type definitions. Used in the parse process.
ELEMENT_TYPE_UNKNOWN = -1
ELEMENT_TYPE_DEFINE = 1
ELEMENT_TYPE_INCLUDE = 2
ELEMENT_TYPE_UNDEF = 3
ELEMENT_TYPE_IFDEF = 4
ELEMENT_TYPE_IFNDEF = 5
ELEMENT_TYPE_IF = 6
ELEMENT_TYPE_ELSE = 7
ELEMENT_TYPE_ELIF = 8
ELEMENT_TYPE_ENDIF = 9
ELEMENT_TYPE_ERROR = 10
ELEMENT_TYPE_PRAGMA = 11
ELEMENT_TYPE_COMMENT_START = 20
ELEMENT_TYPE_COMMENT_MULTILINE = 21
ELEMENT_TYPE_COMMENT_END = 22

#Keyword : Element type dictionary, for read C-header line.
hdr_keywords = {'/*': ELEMENT_TYPE_COMMENT_START,
                '*': ELEMENT_TYPE_COMMENT_MULTILINE,
                '*/': ELEMENT_TYPE_COMMENT_END,
                '#define': ELEMENT_TYPE_DEFINE,
                '#include': ELEMENT_TYPE_INCLUDE,
                '#undef': ELEMENT_TYPE_UNDEF,
                '#ifdef': ELEMENT_TYPE_IFDEF,
                '#ifndef': ELEMENT_TYPE_IFNDEF,
                '#if': ELEMENT_TYPE_IF,
                '#else': ELEMENT_TYPE_ELSE,
                '#elif': ELEMENT_TYPE_ELIF,
                '#endif': ELEMENT_TYPE_ENDIF,
                '#error': ELEMENT_TYPE_ERROR,
                '#pragma': ELEMENT_TYPE_PRAGMA}        

#Element type : keyword, for assembly include output file.
inc_keywords = {ELEMENT_TYPE_COMMENT_START: ';',
                ELEMENT_TYPE_COMMENT_MULTILINE: ';',
                ELEMENT_TYPE_COMMENT_END: '',
                ELEMENT_TYPE_DEFINE: '%define',
                ELEMENT_TYPE_INCLUDE: '%include',
                ELEMENT_TYPE_UNDEF: '%undef',
                ELEMENT_TYPE_IFDEF: '%ifdef',
                ELEMENT_TYPE_IFNDEF: '%ifndef',
                ELEMENT_TYPE_IF: '%if',
                ELEMENT_TYPE_ELSE: '%else',
                ELEMENT_TYPE_ELIF: '%elif',
                ELEMENT_TYPE_ENDIF: '%endif',
                ELEMENT_TYPE_ERROR: '%error',
                ELEMENT_TYPE_PRAGMA: '%pragma'}

class PARSEOBJECT:
    def __init__(self):
        self.tupline = []
        self.tupfile = []
        self.passes = 0
    
    def parseinclude(self, data):
        tempstr = str(data)
        if tempstr.startswith('<'):
            tempstr = tempstr.replace('<', '"')
            tempstr = tempstr.replace('.h>', '.inc"')
        if tempstr.endswith('.h'):
            tempstr = '"'+tempstr
            tempstr = tempstr.replace('.h', '.inc"')
        return tempstr

    def lexer_get_token(k):
        prep = keywords.preprocessor_directives
        reg = keywords.regular
        token = ""

        if w in prep:
            token = prep(w)
        if w in reg:
            token = reg(w)

        return token

    def analyzer(self, ln):
        word = [w for w in ln.split()]
        for w in word:
            if w in hdr_keywords:
                v = hdr_keywords[w]
                self.tupline.append(v)
            else:
                self.tupline.append(w)
        return self.tupline

        for l in self.tupfile:
            if len(l) == 0:
                continue
            if l[0] == ELEMENT_TYPE_INCLUDE:
                templine.append('%include'+' '+str(self.parseinclude(l[1])))

class PARSER(PARSEOBJECT):
    _ids = count(0)

    def __init__(self):
        self.id = next(self._ids)
        self.tupline = []
        self.tupfile = []
        self.passes = 0
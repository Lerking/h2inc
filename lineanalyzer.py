'''
Contains class LINEANALYSER
'''
from contextlib import ContextDecorator
from itertools import count

PREPROCESSOR_DIRECTIVES = ['#include','#define','#undef','#if','#ifdef','#ifndef','#error','#endif']

class ANALYZEOBJECT:
    _passes = count(0)
    _analyzed = []

    def __init__(self):
        self.passes = 0
        self.analyzeline = []
        self.analyzed = []
        self.comment = False
        self.typedef = False
        self.members = False

    def analyze(self,l):
        if self.typedef == True:
            rv = self.analyze_typedef(l)
            if rv != False:
                return rv
        if l == '' or l == '\n':
            return l
        rv = self.analyze_comment(l)
        if rv != False:
            return rv
        rv = self.analyze_preproc(l)
        if rv != False:
            return rv
        rv = self.analyze_typedef(l)
        if rv != False:
            return rv
        return l
    
    def analyze_comment(self,l):
        s = l.split()
        w = [w for w in s]
        if w[0] == '/*' or w[0] == '/**':
            self.comment = True
            if w[-1] == '*/' or w[-1] == '**/':
                self.comment = False
            return l
        if w[0] == '*/' or w[0] == '**/':
            self.comment = False
            return l
        if self.comment == True:
            if w[0] == '*':
                return l
        return False
    
    def analyze_preproc(self,l):
        s = l.split()
        w = [w for w in s]
        if w[0] in PREPROCESSOR_DIRECTIVES:
            return l
        return False

    def analyze_typedef(self,l):
        ts = ''
        ts += l
        s = l.split()
        w = [w for w in s]
        if w[0] == 'typedef':
            if w[1] == 'struct':
                if w[-1].endswith(';'):
                    self.typedef = False
                    return ts
                else:
                    self.typedef = True
                    return 'next'
            if w[1] == 'enum':
                if w[-1].endswith(';'):
                    self.typedef = False
                    return ts
                else:
                    self.typedef = True
                    return 'next'
        return False

    def analyze_struct(self,l):
        ts = ''
        ts += l
        s = l.split()
        w = [w for w in s]
        if w[0] == 'struct':
            if w[-1].endswith(';'):
                self.struct = False
                return ts
            else:
                self.struct = True
                return 'next'
        if self.struct == True:
            if w[0] == '{':
                if w[-1].endswith(';'):
                    self.members = False
                    return ts
                else:
                    self.members = True
                    return 'next'
        return False

class ANALYZER(ANALYZEOBJECT):
    _ids = count(0)
    _passes = count(0)

    def __init__(self):
        self.id = next(self._ids)
        self.tupline = []
        self.tupfile = []
        self.passes = next(self._passes)
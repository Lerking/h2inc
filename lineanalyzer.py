'''
Contains class LINEANALYSER
'''
from contextlib import ContextDecorator
from itertools import count

class ANALYZEOBJECT:
    _passes = count(0)
    _analyzed = []

    def __init__(self):
        self.passes = 0
        self.analyzeline = []
        self.analyzed = []
        self.comment = False

    def analyze(self,l):
        if l.startswith('/*') or l.startswith('/**'):
            self.comment = True
            if l.endswith('*/') or l.endswith('**/'):
                self.comment = False
            return l
        if self.comment == True:
            if l.startswith('*') or l.startswith('**'):
                return l
            if l.startswith(' *'):
                return l
    
class ANALYZER(ANALYZEOBJECT):
    _ids = count(0)
    _passes = count(0)

    def __init__(self):
        self.id = next(self._ids)
        self.tupline = []
        self.tupfile = []
        self.passes = next(self._passes)
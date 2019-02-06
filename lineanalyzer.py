'''
Contains class LINEANALYSER
'''
from contextlib import ContextDecorator
from itertools import count

class ANALYZEOBJECT:
    _passes = count(0)
    _analyzed = []

    def __exit__(self, *exc):
        return False

    def __init__(self):
        self.passes = 0
        self.analyzeline = []
        self.analyzed = []

    
class ANALYZER(ANALYZEOBJECT):
    _ids = count(0)
    _passes = count(0)

    def __init__(self):
        self.id = next(self._ids)
        self.tupline = []
        self.tupfile = []
        self.passes = next(self._passes)
'''
Contains class TOKENIZER
'''
from contextlib import ContextDecorator
from itertools import count

class TOKENIZEOBJECT:
    _passes = count(0)
    _analyzed = []

    def __exit__(self, *exc):
        return False

    def __init__(self):
        self.passes = 0
        self.analyzeline = []
        self.analyzed = []

    class typedef_struct(ContextDecorator):
        def __enter__(self):
            TOKENIZER._analyzed.append('TOKEN_TYPEDEF_STRUCT')
            return self

        def __exit__(self, *exc):
            return False
        
    class typedef_enum(ContextDecorator):
        def __enter__(self):
            TOKENIZER._analyzed.append('TOKEN_TYPEDEF_ENUM')
            return self

        def __exit__(self, *exc):
            return False

    class enum(ContextDecorator):
        def __enter__(self):
            TOKENIZER._analyzed.append('TOKEN_ENUM')
            return self

        def __exit__(self, *exc):
            return False

    class tagname(ContextDecorator):
        def __enter__(self):
            TOKENIZER._analyzed.append('TOKEN_TAG_NAME')
            return self

        def __exit__(self, *exc):
            return False

    class alias(ContextDecorator):
        def __enter__(self):
            TOKENIZER._analyzed.append('TOKEN_ALIAS')
            return self

        def __exit__(self, *exc):
            return False
            
    @typedef_struct()
    def TD_struct(self, tsl):
        '''
        Takes a Typedef Struct 'list' and appends all items (i) in that list to _analyzed.
        '''
        for i in tsl:
            self._analyzed.append(i)
        return

    @typedef_enum()
    def TD_enum(self, e):
        '''
        Takes a Typedef enum member and appends it to _analyzed.
        '''
        self._analyzed.append(e)
        return

    @tagname()
    def TD_tagname(self, tn):
        '''
        Takes a Typedef tagname and appends it to _analyzed.
        '''
        self._analyzed.append(tn)
        return
    
class TOKENIZER(TOKENIZEOBJECT):
    _ids = count(0)
    _passes = count(0)

    def __init__(self):
        self.id = next(self._ids)
        self.tupline = []
        self.tupfile = []
        self.passes = next(self._passes)
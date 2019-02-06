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

    class Decorators(ContextDecorator):
        @classmethod
        def typedef_struct(ContextDecorator):
            TOKENIZER._analyzed.append('TOKEN_TYPEDEF_STRUCT')
            return

        @classmethod
        def typedef_enum(ContextDecorator):
            TOKENIZER._analyzed.append('TOKEN_TYPEDEF_ENUM')
            return

        @classmethod
        def enum(ContextDecorator):
            TOKENIZER._analyzed.append('TOKEN_ENUM')
            return

        @classmethod
        def tagname(ContextDecorator):
            TOKENIZER._analyzed.append('TOKEN_TAG_NAME')
            return

        @classmethod
        def alias(ContextDecorator):
            TOKENIZER._analyzed.append('TOKEN_ALIAS')
            return
            
    @Decorators.typedef_struct
    def TD_struct(self, tsl):
        '''
        Takes a Typedef Struct 'list' and appends all items (i) in that list to _analyzed.
        '''
        for i in tsl:
            self._analyzed.append(i)
        return

    @Decorators.tagname
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
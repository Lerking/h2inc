from metaclasses import InstanceCounterMeta
from rply import LexerGenerator

class comment(object, metaclass=InstanceCounterMeta):
    def __init__(self,com):
        self.id = next(self.__class__._ids)
        self.comment_lexer = LexerGenerator()
        self.comment_lexer.add("CSTART", r"(/*)")
        
        self.comment_lexer.add("CEND", r"(*/)")
        self.comment_lexer.ignore(r'\s+')
        
    
    def parse_comment(self):
        com = self.comment
        if com.startswith('/*'):
            self.block_comment = True
    

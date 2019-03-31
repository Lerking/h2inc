from metaclasses import InstanceCounterMeta

class comment(object, metaclass=InstanceCounterMeta):
    def __init__(self,com):
        self.id = next(self.__class__._ids)
        self.comment = com
        self.block_comment = False
        self.line_comment = False
    
    def parse_comment(self):
        com = self.comment
        if com.startswith('/*'):
            self.block_comment = True
    

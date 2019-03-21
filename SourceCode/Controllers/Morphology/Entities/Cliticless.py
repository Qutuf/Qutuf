'''
Created on ٢٨‏/٠٤‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from ....Models.Lexicon.RootAndPatterns.Root import *;
from ....Controllers.Morphology.Entities.Morpheme import *;


class Cliticless(Morpheme):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyiR_I35Ed-gg8GOK1TmhA
    """
    '''
    classdocs
    '''
            
        
    def __init__(self):
        '''
        Constructor
        '''
           
    pass
    
    def SetAttributeFromBinaryPOS(self, binaryPOS):
        self.BinaryPOS = binaryPOS;
        raise Exception('Not Implemented');
    pass
    

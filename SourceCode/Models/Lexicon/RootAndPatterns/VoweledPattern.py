
'''
Created on ٢٨‏/٠٤‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from ...Lexicon.RootAndPatterns.Root import *;
from ...Tagging.POSTags.CliticlessPOS import *;



class VoweledPattern(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qz4WPI35Ed-gg8GOK1TmhA
    """
    '''
    classdocs
    '''
    
    ID = 0;
    
    VoweledForm = '';
    
    CanonicForm = '';
    
    POS = CliticlessPOS();
    
    def __init__(self, id = 0, voweledForm = '', canonicForm = '', mainClass = 0, gender = 0, count = 0, inflectionState = 0):
        '''
        Constructor
        '''
        
        self.ID = id;        
        self.VoweledForm = voweledForm;        
        self.CanonicForm = canonicForm;        
        self.MainClass = mainClass;               
        self.Gender = gender;        
        self.Count = count;        
        self.InflectionState = inflectionState;     
        
        self.POS = CliticlessPOS();
        pass
    
    def SetAttributeFromBinaryPOS(self, binaryPOS):
        self.BinaryPOS = binaryPOS;
        raise Exception('Not Implemented');
        pass
    

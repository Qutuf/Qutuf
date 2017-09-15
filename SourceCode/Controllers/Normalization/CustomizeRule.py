'''
Created on ٢٣‏/٠٣‏/٢٠١٠

@author: Mad Blue
'''

from Lexicon.NormalizationRulesDict import *

class CustomizeRule(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qz4V1I35Ed-gg8GOK1TmhA
    """
    '''
    classdocs
    '''
    customize=dict()    

    def __init__(self):
        '''
        Constructor
        '''
        self.customize = FirstNormDict;
        for key, value in SecondNormDict.items():
            self.customize.addRule(self,key,value);        
        pass
        
    def addRule(self,key,value):        
        self.customize[key]=value;
        pass
    
    def reomveRule(self,key):
        self.customize.pop(key);
        pass

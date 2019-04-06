
'''
Created on ١١‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from ..TextEntities import *
from ...Models.Normalization.NormalizationRulesDict import *

class Normalizer(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qz4V5o35Ed-gg8GOK1TmhA
    """
    '''
    Text Normalizer
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        
    def Normalize(self, sentences, updateBy):
        # Normalize Sentences >> Words
        for i in range(len(sentences)):
            for j in range(len(sentences[i].Words)):
                sentences[i].Words[j].FirstNormalizationForm = sentences[i].Words[j].OriginalString;
                for key, value in FirstNormDict.items():
                    sentences[i].Words[j].FirstNormalizationForm = sentences[i].Words[j].FirstNormalizationForm.replace(key, value);
                    if(updateBy == 1):
                        sentences[i].Words[j].String = sentences[i].Words[j].FirstNormalizationForm;

        for i in range(len(sentences)):
            for j in range(len(sentences[i].Words)):
                sentences[i].Words[j].SecondNormalizationForm = sentences[i].Words[j].FirstNormalizationForm ;
                for key, value in SecondNormDict.items():
                    sentences[i].Words[j].SecondNormalizationForm = sentences[i].Words[j].SecondNormalizationForm.replace(key, value);
                    if(updateBy == 2):
                        sentences[i].Words[j].String = sentences[i].Words[j].SecondNormalizationForm;
                               
    pass
            
    def NormalizeCustomized(self, sentences):
        if (CustomizedDict.item()!=[]):
            for i in range(len(sentences)):
                for j in range(len(sentences[i].Words)):                    
                    for key, value in CustomizedDict.items():
                        sentences[i].Words[j].String = sentences[i].Words[j].OriginalString.replace(key, value);
    pass

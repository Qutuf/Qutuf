
'''
Created on ٢٨‏/٠٦‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from ....Controllers.General.ArabicStringUtility import *;
from ....Controllers.Tokenization.TokenType import TokenType;
from ....Controllers.Morphology.Entities.SurfaceFormMorphemes import *;

class CompoundParsing(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0LRgY35Ed-gg8GOK1TmhA
    """
    '''
    Parsing Compound words
    '''


    def __init__(self):
        '''
        Constructor
        '''
    pass

    def Parsing(self, textEncapsulator, specialWords):
        compoundNounsDict = specialWords.CompoundNouns;
        
        for sentence in textEncapsulator.Sentences[:]:
            index = 0;
            while index < len(sentence.Words)-2:
                if(not (sentence.Words[index].TokenType.Id == TokenType.Constants.Id.ArabicText and \
                   sentence.Words[index+1].TokenType.Id == TokenType.Constants.Id.WhiteSpace and \
                   sentence.Words[index+2].TokenType.Id == TokenType.Constants.Id.ArabicText)):
                    index += 1;
                    continue;
                
                unvoweldForm = ' '.join([sentence.Words[index].SecondNormalizationForm , sentence.Words[index+2].SecondNormalizationForm]) ;
                firstNormalizationForm = ' '.join([sentence.Words[index].FirstNormalizationForm , sentence.Words[index+2].FirstNormalizationForm]) ;
                
                if unvoweldForm in compoundNounsDict.keys():
                    compound = compoundNounsDict[unvoweldForm];
                    if(not ArabicStringUtility.IsCompatible(ArabicStringUtility, firstNormalizationForm, compound.VoweledForm)):
                        index += 1;
                        continue;
                    originalString = ' '.join([sentence.Words[index].OriginalString,  sentence.Words[index+2].OriginalString]) ;
                    
                    #Compound:
                    sentence.Words[index].OriginalString = originalString;
                    sentence.Words[index].FirstNormalizationForm = compound.VoweledForm;
                    sentence.Words[index].SecondNormalizationForm = compound.UnvoweledForm;
                    sentence.Words[index].String = compound.UnvoweledForm;
                    sentence.Words[index].MorphologicalParsingCompleted = True;
                    sentence.Words[index].SurfaceFormMorphemes = [];
                    sentence.Words[index].SurfaceFormMorphemes.append(SurfaceFormMorphemes([], compound.ReturnAsUnderivedCliticless(), []));
                
                    #remove space
                    sentence.Words.remove(sentence.Words[index+1]);
                    #remove second Part
                    sentence.Words.remove(sentence.Words[index+1]);
                    
                index += 1;
                    
        
    pass

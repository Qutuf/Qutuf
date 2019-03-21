
'''
Created on ١١‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from ...Tagging.RuleBasedExpertSystemTagger import RuleBasedExpertSystemTagger;
from ...Morphology.Entities.SurfaceFormMorphemes import SurfaceFormMorphemes; 
from ...TextEntities import *

from ....Models.General.TransducersXmlLoader import *

class OverdueTagger(RuleBasedExpertSystemTagger):
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0BgHY35Ed-gg8GOK1TmhA
    """
    '''
    Assign Word Classes:
    1) Use Lexicon to assign tags (Word Classes).
    2) Resolve ambiguities.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def SortAndUseThresholds(self, textEncapsulator, overdureTaggingThreshold = None, overdureTaggingTopReservants = None):
                         
        for sentence in textEncapsulator.Sentences:
            for word in sentence.Words:
                word.SurfaceFormMorphemes = \
                    sorted(word.SurfaceFormMorphemes, key=SurfaceFormMorphemes.GetCertainty, reverse=True);
                
        if(overdureTaggingThreshold == None and overdureTaggingTopReservants == None):
            return;
        for sentence in textEncapsulator.Sentences:
            for word in sentence.Words:
                newSurfaceFormMorphemes = [];
                print('len(word.SurfaceFormMorphemes) = ', len(word.SurfaceFormMorphemes));
                for surfaceFormMorphemes in word.SurfaceFormMorphemes:
                    if(overdureTaggingTopReservants != None and \
                       len(newSurfaceFormMorphemes) >= overdureTaggingTopReservants and \
                       newSurfaceFormMorphemes[len(newSurfaceFormMorphemes)-1].GetCertainty() != surfaceFormMorphemes.GetCertainty()):
                        break;
                    if(overdureTaggingThreshold == None or \
                       surfaceFormMorphemes.GetCertainty() >= overdureTaggingThreshold):
                        print('surfaceFormMorphemes.GetCertainty() = ', surfaceFormMorphemes.GetCertainty());
                        newSurfaceFormMorphemes.append(surfaceFormMorphemes);
                    else:
                        break;
                word.SurfaceFormMorphemes = newSurfaceFormMorphemes;
                print('len(word.SurfaceFormMorphemes) = ', len(word.SurfaceFormMorphemes));
    pass
    

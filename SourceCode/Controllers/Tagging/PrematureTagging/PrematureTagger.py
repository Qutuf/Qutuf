
'''
Created on ١١‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from Controllers.Tagging.RuleBasedExpertSystemTagger import *;

from TextEntities import *
from Models.General.TransducersXmlLoader import *

class PrematureTagger(RuleBasedExpertSystemTagger):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyYgsY35Ed-gg8GOK1TmhA
    """
    '''
    1) Tagging the stop words
    2) Apply fast tagging rules; those how have 100% certainty
    '''

    def __init__(self):
        '''
        Constructor
        '''
    pass
    
    def ApplyTaggingRules(self, textEncapsulator, rulesStatesGraphs):
        
        for si in range(len(textEncapsulator.Sentences)):
            for wi in range(len(textEncapsulator.Sentences[si].Words)):
                textEncapsulator.Sentences[si].Words[wi].PrematureTags = [];
        
        RuleBasedExpertSystemTagger.ApplyTaggingRules(self, textEncapsulator, rulesStatesGraphs);
    pass

    def TagStopWords(self, textEncapsulator):
        '''
        أضف وسماً مبدئياً للكلمات المستبعدة
        Add Premature tag to the Stop Words.
        '''
        
        for i in range(len(textEncapsulator.Sentences)):
            for j in range(len(textEncapsulator.Sentences[i].Words)):
                #Add code here... Like:
                if False:
                    textEncapsulator.Sentences[i].Words[j].PrematureTags['Neglected'] = 1;
            pass
    pass
    
    
    def InferPrematureTags(self, textEncapsulator):
        for i in range(len(textEncapsulator.Sentences)):
            for j in range(len(textEncapsulator.Sentences[i].Words)):
                tempTags  = dict();
                preTags = textEncapsulator.Sentences[i].Words[j].PrematureTags;
                for k in range(len(preTags)):
                    name = preTags[k][0];
                    if preTags[k][0] not in tempTags.keys():
                        tempTags[name] = preTags[k][1];
                    else:
                        if tempTags[name] >= 0 and preTags[k][1] >= 0:
                            tempTags[name] = tempTags[name] + preTags[k][1] * (1 - tempTags[name]);
                        elif tempTags[name] <= 0 and preTags[k][1] <= 0:
                            tempTags[name] = tempTags[name] + preTags[k][1] * (1 + tempTags[name]);
                        elif tempTags[name] == -1* preTags[k][1]:
                            tempTags[name] = 0;
                        else:
#                        #Equivalent to:
#                        elif tempTags[name] >= 0 and preTags[k][1] <= 0 \
#                        or tempTags[name] <= 0 and preTags[k][1] >= 0:
                            tempTags[name] = (tempTags[name] + preTags[k][1]) / (1 - min(abs(tempTags[name]), abs(preTags[k][1])));
                
                #Re-Fill the PrematureTags:              
                textEncapsulator.Sentences[i].Words[j].PrematureTags = {};
                for key, value in tempTags.items():
                    textEncapsulator.Sentences[i].Words[j].PrematureTags[key] = value;
                if(textEncapsulator.Sentences[i].Words[j].PrematureTags != {}):
                    for key in ['Noun', 'Verb', 'Particle']:
                        if(key not in textEncapsulator.Sentences[i].Words[j].PrematureTags.keys()):
                            textEncapsulator.Sentences[i].Words[j].PrematureTags[key] = 0;
    pass

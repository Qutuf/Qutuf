
'''
Created on ٠٢‏/٠٤‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Controllers.Tokenization.TokenType import TokenType;
from Transducers.StatesGraph import *;
from Transducers.State import *;


class AffixParser(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyiSsI35Ed-gg8GOK1TmhA
    """
    '''
    Morphological Affix Parser.
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def ParsePrefix(self, sentences, statesGraphs):
               
        
        for i in range(len(sentences)):
            j = 0;
            while j <len(sentences[i].Words):
                while(j < len(sentences[i].Words) and (
                    sentences[i].Words[j].TokenType.Id != TokenType.Constants.Id.ArabicText\
                    or sentences[i].Words[j].MorphologicalParsingCompleted == True)):
                    j += 1;
                if(j == len(sentences[i].Words)):
                    break;
                for k2 in range(len(statesGraphs)):
                    #Create new different instance of StatesGraph since there are temporary variables inside it.
                    statesGraph = StatesGraph(statesGraphs[k2].Start, statesGraphs[k2].States);
                    state = statesGraph.Start;
                    
                    l = 0;
                    while l < len(sentences[i].Words[j].String):
                        [nextState, numberToConsume] = statesGraph.Match(state, sentences[i], j, l);
                        
                        if type(nextState) is State: #There is a match:
                            l += numberToConsume;
                            
                            
                            if nextState.IsEnd == True:
                                #Apply Actions:
                                for currentWordIndex, actions in statesGraph.ActionsToApply.items():
                                    actions.ApplyToWord(sentences[i], currentWordIndex);
                                
                                #Clear is used to forbid applying the same actions more than once if there are many ends.
                                statesGraph.ActionsToApply.clear();
                            state = nextState;
                        else:
                            break;
                j += 1;        
    pass

   
    def ParseSuffix(self, sentences, statesGraphs):
              
        
        for i in range(len(sentences)):
            j = 0;
            while j <len(sentences[i].Words):
                while(j < len(sentences[i].Words) and (
                    sentences[i].Words[j].TokenType.Id != TokenType.Constants.Id.ArabicText\
                    or sentences[i].Words[j].MorphologicalParsingCompleted == True)):
                    j += 1;
                if(j == len(sentences[i].Words)):
                    break;
                for k2 in range(len(statesGraphs)):
                    #Create new different instance of StatesGraph since there are temporary variables inside it.
                    statesGraph = StatesGraph(statesGraphs[k2].Start, statesGraphs[k2].States);
                    state = statesGraph.Start;
                    
                    l = len(sentences[i].Words[j].String)-1;
                    while l >= 0:
#                        print('-- test match'+str(l));
                        [nextState, numberToConsume] = statesGraph.Match(state, sentences[i], j, l, False);
                        
                        if type(nextState) is State: #There is a match:
#                            print('-- is state'+str(l));
                            l -= numberToConsume;
                            
                            
                            if nextState.IsEnd == True:
                                #Apply Actions:
                                for currentWordIndex, actions in statesGraph.ActionsToApply.items():
#                                    print('-- apply actions one index: '+str(currentWordIndex));
                                    actions.ApplyToWord(sentences[i], currentWordIndex);
#                                    print('--'+str(currentWordIndex));
                                        
                                #Clear is used to forbid applying the same actions more than once if there are many ends.
                                statesGraph.ActionsToApply.clear();
                            state = nextState;
                        else:
#                            print('-- not state'+str(l));
                            break;
                j += 1;

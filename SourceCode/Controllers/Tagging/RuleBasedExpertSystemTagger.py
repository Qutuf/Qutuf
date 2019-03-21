'''
Created on ١٨‏/٠٧‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from ..TextEntities import *
from ...Models.General.TransducersXmlLoader import *

class RuleBasedExpertSystemTagger(object):
    '''
    Rule Based Expert System Tagger
    '''


    def __init__(self):
        '''
        Constructor
        '''
    pass



    def ApplyTaggingRules(self, textEncapsulator, rulesStatesGraphs):
        #write code here... To assign tags to Sections>>Paragraphs>>Sentences>>Words
        
        
        for i in range(len(textEncapsulator.Sentences)):    
#            print('i = ', i); 
            MatchedStatesGraphs = [];
            j = 0;
            while j < len(textEncapsulator.Sentences[i].Words):
                while(j < len(textEncapsulator.Sentences[i].Words) and textEncapsulator.Sentences[i].Words[j].TokenType.Id != 0):
                    j += 1;
                if(j == len(textEncapsulator.Sentences[i].Words)):
                    break;
                k1Limit = len(MatchedStatesGraphs);
                k1 = 0;
                #Try to follow matched Graphs:
                while k1 < k1Limit:
                    graph = MatchedStatesGraphs[k1][0];
                    state = MatchedStatesGraphs[k1][1];
                    [nextState, numberToConsume] = graph.Match(state, textEncapsulator.Sentences[i], j);   
                    if type(nextState) is State: #There is a match:
                        if numberToConsume != 1:
                            raise Exception('OverdueTagger is not implemented to deal with [numberToConsume] other than 1');
                        #Do not change MatchedStatesGraphs[k1][1] to 'state' 
                        #that would not change the value of MatchedStatesGraphs[k1][1]!
                        MatchedStatesGraphs[k1][1] = nextState;
                        if nextState.IsEnd == True:
                            #Apply Actions:
                            for currentWordIndex, actions in graph.ActionsToApply.items():
                                actions.ApplyToWord(textEncapsulator.Sentences[i], currentWordIndex);
                                    
                            #Clear is used to forbid applying the same actions more than once if there are many ends.
                            graph.ActionsToApply.clear();                            
                                   
                    else:
                        MatchedStatesGraphs.remove(MatchedStatesGraphs[k1]);
                        k1Limit -= 1;
                        k1 -= 1;
                        
                    k1 += 1;
                    

                #Try starting new Graphs:
                for k2 in range(len(rulesStatesGraphs)):
                    start = rulesStatesGraphs[k2].Start;
                    
                    #Create new different instance of StatesGraph since there are temporary variables inside it.
                    statesGraph = StatesGraph(start, rulesStatesGraphs[k2].States);
                    
                    [nextState, numberToConsume] = statesGraph.Match(start, textEncapsulator.Sentences[i], j);
                    
                    if type(nextState) is State: #There is a match:
                        MatchedStatesGraphs.append([statesGraph, nextState]);
                        
                        if nextState.IsEnd == True:
                            #Apply Actions:
                            for currentWordIndex, actions in statesGraph.ActionsToApply.items():
                                actions.ApplyToWord(textEncapsulator.Sentences[i], currentWordIndex);
#                        break;
                        
                j += 1;
    pass
    

'''
Created on ١٩‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Transducers.StatesGraph import StatesGraph;
from Transducers.State import State;
from Transducers.TransitionCondition import TransitionCondition;
from Transducers.TransitionAction import TransitionAction;
from Transducers.Transition import Transition;
from Transducers.TransitionActions import TransitionActions;


class TransducersXmlLoader(object):
    """
    # PyUML: Do not remove this line! # XMI_ID:_qzkznY35Ed-gg8GOK1TmhA
    """
    '''
    Load Premature Tagging Graph from Xml File into Memory.
    '''
    
    __xmlFileName = ''
    StatesGraphs = [];

    def __init__(self, xmlFileName):
        '''
        Constructor
        '''
        from xml.dom import minidom;
        self.__xmlFileName = xmlFileName;
        xmldoc = minidom.parse(xmlFileName);
        
        self.StatesGraphs = [];
        for xmlrule in xmldoc.getElementsByTagName('Rule'):
            #Create graph...  
            statesGraph = StatesGraph();
            self.StatesGraphs.append(statesGraph);
            for xmlstate in xmlrule.childNodes: 
                if xmlstate.nodeType != 1:
                    continue;
                id = xmlstate.attributes['id'].value;
                state = None;
                if id not in statesGraph.States.keys():            
                    state = State(id);
                else:
                    state = statesGraph.States[id];
                statesGraph.States[state.Id] = state;
                if 'isStart' in xmlstate.attributes.keys() and xmlstate.attributes['isStart'].value == 'True':
                    state.IsStart = True;
                    if statesGraph.Start != None:
                        raise Exception('A Graph State can only have one start');
                    statesGraph.Start = state;                        
                if 'isEnd' in xmlstate.attributes.keys() and xmlstate.attributes['isEnd'].value == 'True':
                    state.IsEnd = True;
                    for xmlEndActions in xmlstate.childNodes: 
                        if xmlEndActions.nodeType != 1:
                            continue;
                        #Do some parsing if needed in the future.  
                    
                for xmlStateChildNodes in xmlstate.childNodes: 
                    if xmlStateChildNodes.nodeType != 1:
                        continue;
                    if xmlStateChildNodes.nodeName == "Transition":
                        nextStateId = xmlStateChildNodes.attributes['next_state_id'].value;
                        if nextStateId not in statesGraph.States.keys():
                            nextState = State(nextStateId);
                            statesGraph.States[nextStateId] = nextState;
                        else:
                            nextState = statesGraph.States[nextStateId];
                            
                        conditionsList = [];
                        actionsList = [];
                        consume = int(xmlStateChildNodes.attributes['consume'].value);
#                        if statesGraph.States[nextStateId] not in state.NextStates.keys():
#                            state.NextStates[statesGraph.States[nextStateId]] = [];
#                        state.NextStates[statesGraph.States[nextStateId]].append([conditionsList, actionsList]);
                        transitionActions = None;
                        for xmlConditionsActions in xmlStateChildNodes.childNodes: 
                            if xmlConditionsActions.nodeType != 1:
                                continue;
                            if xmlConditionsActions.nodeName == 'Conditions':
                                for xmlCondition in xmlConditionsActions.childNodes:
                                    if xmlCondition.nodeType != 1:
                                        continue;
                                    transitionCondition  = TransitionCondition(xmlCondition.attributes['type'].value\
                                                                , xmlCondition.attributes['attribute_name'].value\
                                                                , xmlCondition.attributes['value'].value);
                                    conditionsList.append(transitionCondition);
                            
                            if xmlConditionsActions.nodeName == 'Actions':
                                if(transitionActions!=None):
                                    raise Exception('Multiple entries for Actions is not allowed!!!');
                                
                                for xmlAction in xmlConditionsActions.childNodes:
                                    if xmlAction.nodeType != 1:
                                        continue;
                                    transitionAction = TransitionAction(xmlAction.attributes['attribute_name'].value, \
                                                         xmlAction.attributes['type'].value, \
                                                         xmlAction.attributes['value'].value, \
                                                         int(xmlAction.attributes['on_relative_index'].value));
                                    actionsList.append(transitionAction);
                                    
                                transitionActions = TransitionActions(actionsList, []);
                        if(transitionActions == None):        
                            transitionActions = TransitionActions([], []);
                        state.Transitions.append(Transition(conditionsList, transitionActions, nextState, consume));


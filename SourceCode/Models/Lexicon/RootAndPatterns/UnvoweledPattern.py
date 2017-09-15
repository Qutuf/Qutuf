
'''
Created on ٢٩‏/٠٤‏/٢٠١٠

@Created by: Muhammad Altabba
'''

class UnvoweledPattern(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qz4WCI35Ed-gg8GOK1TmhA
    """
    '''
    Unvoweled Pattern
    '''
    String = '';
    Rules = [];
    IDs = [];

    def __init__(self, string, rules, ids):
        '''
        Constructor
        '''
        self.String = string;
        self.Rules = rules;
        self.IDs = ids;
        pass
    
    def GetRootsStringsAndRules(self, string):
        if (string == None):
            string = self.String;
            
        rootStrings = [];
        rootRules = [];
        for j in range(len(self.Rules)):
            rootRule = '';
            rootString = '';
            for k in range(len(self.Rules[j])):
                rootRule += self.Rules[j][k];
                if self.Rules[j][k].isdigit():
                    rootString += string[int(self.Rules[j][k]) - 1];
                else:
                    rootString += self.Rules[j][k];
            rootStrings.append(rootString);
            rootRules.append(rootRule);
                    
        return [rootStrings, rootRules];

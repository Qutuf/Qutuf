
'''
Created on ١٠‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from Controllers.Morphology.Entities.SurfaceFormMorphemes import *;
from Controllers.Morphology.Entities.GreedyMorphemes import *;
from Controllers.Tokenization.TokenType import *;
from Controllers.General.ArabicStringUtility import *;
from Models.Lexicon.LettersConstants import *;
from Controllers.Morphology.Entities.Particle import *;
from Controllers.Morphology.Entities.DerivedCliticless import *;

class Word(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyYhVY35Ed-gg8GOK1TmhA
    """
    '''
    Text Word
    '''
    
    OriginalString = '';
    #Original String:
    
    FirstNormalizationForm = '';
    #String after making normalization without loosing information: example removing hyphen (-)
        
    SecondNormalizationForm = '';
    #String after making normalization that make information lost: example removing التشكيل (vowelization)

    String = '';
    #String in manipulation.
    
    TokenType = TokenType();
    #Token Type:
    
    MorphologicalParsingCompleted = False;
    #To be set to True if the word is completely finished Morphological Parsing.
    #For example if it is detected as a compound word and parsed completely at the stage of Compound Parsing.
    
    
    PrematureTags = {};
    #Possible Premature Tags assigned by Premature Tagger. It takes it values from PrematureTagsSet.
    #self.PrematureTags[index] = ['TagName', Certainty]
    
#    أصبح موجود ضمن Morpheme
#    Tags = [];
#    #Possible Tags assigned by Overdue Tagger: It takes it values from TagSet.
#    #self.Tags[index] = ['TagName', Certainty]
#    
    
    GreedyMorphemes = GreedyMorphemes([],None,[]);   
    
    SurfaceFormMorphemes = [];
    #Possible sequences of the analyzed word:
    #This an array of instances of Morphology.Entities.SurfaceFormMorphemes
    
       
    def GetAffixationPosibilities(self):
        '''
        Return a list of all possibilities of word segmentation. 
            (That is all possible forms of the word with clitics)
        Number of possibilities = 1 + (Number of Proclitics + 1) * (Number of Enclitics + 1) 
        For example: أوبعلمائكم
            [[], 'أوبعلمائكم', []]  
            [[], 'أوبعلمائك', ['م']], 
            [[], 'أوبعلمائ', ['ك', 'م']], 
            [['أ'], 'وبعلمائكم', []], 
            [['أ'], 'وبعلمائك', ['م']], 
            [['أ'], 'وبعلمائ', ['ك', 'م']], 
            [['أ', 'و'], 'بعلمائكم', []], 
            [['أ', 'و'], 'بعلمائك', ['م']], 
            [['أ', 'و'], 'بعلمائ', ['ك', 'م']],
            [['أ', 'و', 'ب'], 'علمائكم', []], 
            [['أ', 'و', 'ب'], 'علمائك', ['م']], 
            [['أ', 'و', 'ب'], 'علمائ', ['ك', 'م']]

        '''
#        
#        procliticsLen = 0;
#        for k in range(len(self.GreedyMorphemes.Proclitics)):
#            procliticsLen += len(GreedyMorphemes.Proclitics[k][0]);
#        encliticsLen = 0;
#        for k in range(len(GreedyMorphemes.Enclitics)):
#            encliticsLen += len(GreedyMorphemes.Enclitics[k][0]);          
        
        tempList = [];
        tempList.append([[('','c')], self.String, [('','c')]]);
        tempP = [('','c')];
        procliticsCutIndex = 0;
        for i in range(-1,len(self.GreedyMorphemes.Proclitics)):
            tempS = [('','c')];
            if i > -1:            
                tempP = list(tempP);
                tempP.append([x for x in self.GreedyMorphemes.Proclitics[i]]);
                procliticsCutIndex += len(self.GreedyMorphemes.Proclitics[i][0]);
                tempList.append([tempP,self.String[procliticsCutIndex:], tempS]);
            encliticsCutIndex = 0;
            for j in range(len(self.GreedyMorphemes.Enclitics)):
                li = [[x for x in self.GreedyMorphemes.Enclitics[j]]];
                li.extend(tempS);                                
                tempS = li;
                encliticsCutIndex += len(self.GreedyMorphemes.Enclitics[j][0]);
                tempList.append([tempP,self.String[procliticsCutIndex:len(self.String)-(encliticsCutIndex)], tempS]);
        return tempList;
    pass
    
    def __init__(self, string):
        '''
        Constructor
        '''
        self.OriginalString = string
        self.String = string

        self.FirstNormalizationForm = '';
        self.SecondNormalizationForm = '';
        self.TokenType = TokenType();
        self.PrematureTags = {};
        self.Tags = [];
        self.SurfaceFormMorphemes = [];
        self.GreedyMorphemes = GreedyMorphemes([],None,[]);
        self.MorphologicalParsingCompleted = False;
    pass
    
    def __str__(self):
        str = 'Word:';
        str += '\tOriginal:' + self.OriginalString;
        str += '\tFirst Norm. Form:' + self.FirstNormalizationForm;
        str += '\tSecond Norm. Form:' + self.SecondNormalizationForm;
        str += '\tString:' + self.String;
        str += '\tToken Type:' + self.TokenType.__str__();
        str += '\tPre. Tags:' + self.PrematureTags.__str__();
        str += '\tGreedy Morphemes: ' + self.GreedyMorphemes.__str__();
        str += '\tTags:' + self.Tags.__str__();
        str += '\tPos. Morphemes:' + self.SurfaceFormMorphemes.__str__();
        str += '\n';
        return str;
    pass
    
    def ClipString(self, formNumber, lettersCountFromStart, lettersCountFromEnd):
        string = '';
        if formNumber == 0:
            string = self.OriginalString;
        elif formNumber == 1:
            string = self.FirstNormalizationForm;
        elif formNumber == 2:
            string = self.SecondNormalizationForm;
        elif formNumber == None:
            string = self.String;
        
        return ArabicStringUtility.ClipString(ArabicStringUtility, string, lettersCountFromStart, lettersCountFromEnd);   
    
    pass

    def GetDiacratic(self, procliticString, searchFromRight = False):
        
        return ArabicStringUtility.GetDiacratic(ArabicStringUtility, self.FirstNormalizationForm, procliticString, 0, searchFromRight);        
        
    pass
    
    def GetTopPrematureTagsKeys(self, word):
        
        topKeys = [];
        max = -1;
        if (word.PrematureTags != {}):
            for key in ['Noun', 'Verb', 'Particle']:
                if (max == word.PrematureTags[key]):
                    topKeys.append(key)
                elif (max < word.PrematureTags[key]):
                    max = word.PrematureTags[key]
                    topKeys = []
                    topKeys.append(key)
        
        return topKeys
    pass

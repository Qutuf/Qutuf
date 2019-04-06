'''
Created on ١٠‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from .Word import *

class Sentence(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyYg4Y35Ed-gg8GOK1TmhA
    """
    '''
    Text Sentence
    '''
    OriginalString = "";
    
    # List of instances of the Word class:
    Words = [];

    def __init__(self, string):
        '''
        Constructor
        '''
        self.OriginalString = string;
        self.Words = [];
        
    def Tokenize(self):        
        i = 0;
        while i < len(self.OriginalString):
            nextIndex = len(self.OriginalString);
            dotIndex = self.OriginalString.find(' ', i);
            if nextIndex > dotIndex and dotIndex != -1:
                nextIndex = dotIndex;
            word = Word(self.OriginalString[i:nextIndex])
            word.TokenType = TokenType();
            self.Words.append(word);
            i += nextIndex - i + 1
        pass
        
    def __str__(self):
        str = 'Sentence:';
        str += '\tOriginal String:' + self.OriginalString;
        str += '\n\tWords:';
        str += '\n';
        for i in range(len(self.Words)):
            str += self.Words[i].__str__();
        return str;


'''
Created on ١٠‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from Models.Tokenization.TokenizerConstants import TokenTypeDict;


class TokenType(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_hUBlbo34Ed-gg8GOK1TmhA
    """
    '''
    Token Type
    '''
    Id = 0
    Name = ""

    def __init__(self, id = 0):
        '''
        Constructor
        '''
        self.Id = id
        self.Name = TokenTypeDict[id]
    pass
    
    def __str__(self):   
        str1 = '(Id = ' + str(self.Id);
        str1 += ', Name = ' + self.Name+')';
        return str1;
    pass



    class Constants:
        class Id:
            ArabicText = 0;
            Numbers = 1;
            WhiteSpace = 2;
            Punctuation = 3;
            OtherText = 4;
            
    

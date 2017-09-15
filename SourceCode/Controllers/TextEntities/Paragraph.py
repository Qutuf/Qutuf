'''
Created on ١٠‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''

class Paragraph(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyYgx435Ed-gg8GOK1TmhA
    """
    '''
    Text Paragraph
    '''
    OriginalString = "";
    
    Sentences = [];
    #List of instances of the Section class:

    def __init__(self, string):
        '''
        Constructor
        '''
        self.OriginalString = string;

'''
Created on ١٠‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from TextEntities import Paragraph
from TextEntities import Sentence
from TextEntities import Word

class Section(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyYg1I35Ed-gg8GOK1TmhA
    """
    '''
    Text Section
    '''
    OriginalString = "";
    
    Paragraphs = []
    #List of instances of the Sentence class:

    def __init__(self, string):
        '''
        Constructor
        '''
        self.OriginalString = string;
        #write code to fill Sections>>Paragraphs>>Sentences>>Words

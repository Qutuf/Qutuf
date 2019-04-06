
'''
Created on ٢٧‏/٠٥‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from ....Models.Tagging.POSTags.POS import POS;



class Morpheme(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyiSU435Ed-gg8GOK1TmhA
    """
    '''
    Morpheme
    '''   
    
    OriginalString = '';
    
    
    UnvoweledForm = '';
    
    
    VoweledForm = '';
    #الكلمة مشكّلة.
    #لا يتم التشكيل إلا بعد استدعاء التابع FillDiacritizedForm

    POS = POS();
    
#    __Certainty = 0;
#    #مقدار الثقة لتشكّل هذا الجزء بهذا التصريف


    def __init__(self):
        '''
        Constructor
        '''
#        self.__Certainty = 0;
    pass

    def FillDiacritizedForm(self):
        raise Exception('Unimplemented Abstract method! at Class Morpheme');
    pass

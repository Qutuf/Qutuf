'''
Created on ١١‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''


class GreedyMorphemes(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyiSM435Ed-gg8GOK1TmhA
    """
    '''
    Word Morphemes
    '''
                
    Proclitics = [];
    #لواصق بادئة
    #مصفوفة من صنف Proclitic.
    
#    ProcliticsClasses = [];
    
    
    
    Enclitics = [];
    #لواصق ختامية
    #مصفوفة من صنف Enclitic.         
    
#    EncliticsClasses = [];
    
#    SurfaceForm = '';
#    #الشكل المدخل قبل المعالجة   
     
    CliticlessWords = [];
    #الشكل المعزول غن اللواصق
    #مصفوفة من الصنف DerivedWord أو UnderivedWord.
    
#    StringWithDiacritics = '';
#    #الكلمة مُشكّلة  
    
    CertaintyOrProbability = None;
    # مقدار الثقة أو الاحتمال لتوارد هذه الكلمة مع هذا النسق من اللواصق
    
    def GetStringWithDiacritics(self):
        '''
        الحصول على الكلمة مُشكّلة 
        '''
        
        raise Exception('Not Implemented!');
    
        pass
    
    

    def __init__(self, proclitics, cliticlessWords, enclitics):
        '''
        Constructor
        '''
        self.Proclitics = proclitics;
        self.CliticlessWords = cliticlessWords;
        self.Enclitics = enclitics;
        pass
    
    
    def __str__(self):
        str = '';
        str += '\t\tProclitics:' + self.Proclitics.__str__();
        str += '\t\tEnclitics:' + self.Enclitics.__str__();
#        str += '\t\tPrefixes:' + self.Prefixes.__str__();
#        str += '\t\tSuffixes:' + self.Suffixes.__str__();
#        str += '\t\tCliticlessForm:' + self.CliticlessForm;
#        str += '\t\tStem:' + self.Stem;
#        if(self.Root != None and self.Root.String != None):
#            str += '\t\tRoot:' + self.Root.String;
#        if(self.UnoweledPattern.String != None):
#            str += '\t\tPattern:'+self.UnoweledPattern.String;
#        if(self.VoweledPattern != None):
#            str += '\t\tPattern:'+self.VoweledPattern.VoweledForm;
        return str;
        pass
        

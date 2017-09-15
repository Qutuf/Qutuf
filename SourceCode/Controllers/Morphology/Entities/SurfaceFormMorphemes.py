
'''
Created on ١٥‏/٠٦‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from Controllers.Morphology.Entities.Cliticless import Cliticless;
from Controllers.Morphology.Entities.DerivedCliticless import DerivedCliticless;
from Controllers.Morphology.Entities.Particle import *;


class SurfaceFormMorphemes(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyiSdY35Ed-gg8GOK1TmhA
    """
    '''
    Morphemes of Word in the Surface Form.
    '''
    
    VoweledForm = '';
    
    Proclitics = [];
    #لواصق بادئة
    #مصفوفة من Particle
    #Particle.State = ParticleConstants.State.Proclitic
     
    Enclitics = []; 
    #لواصق ختامية
    #مصفوفة من Particle
    #Particle.State = ParticleConstants.State.Enclitic
    
    Cliticless = Cliticless();
    #إما من الصنف
    #DerivedCliticless أو UnderivedCliticless


    __Certainty = 0;
    # مقدار الثقة لتوارد هذه الكلمة مع هذا النسق من اللواصق
    
    def GetCertainty(self):
        return self.__Certainty;
    pass
    
    def AddCertainty(self, value):
        if(self.__Certainty >= 0 and value >= 0):
            self.__Certainty = self.__Certainty + value - self.__Certainty * value;
        elif(self.__Certainty <= 0 and value <= 0):
            self.__Certainty = self.__Certainty + value + self.__Certainty * value;
        else:
            self.__Certainty = (self.__Certainty + value) / (1 - min(abs(self.__Certainty), abs(value)));            
    pass
    
    
    def __init__(self, proclitics, cliticless, enclitics, fillVoweledForm = True):
        '''
        Constructor
        '''
        self.Proclitics = proclitics;
        self.Cliticless = cliticless;
        if(type(self.Cliticless) is DerivedCliticless):
            self.Cliticless.UpdateInternalEnclitic();
            if(self.Cliticless.InternalEnclitic != None):
                enclitics = [x for x in enclitics];
                enclitics.insert(0, self.Cliticless.InternalEnclitic);
        self.Enclitics = enclitics;        
        
        self.__Certainty = 0;
        if(fillVoweledForm == True):
            self.FillVoweledForm();
        else:
            self.VoweledForm = '';
    pass
    
    def FillVoweledForm(self, forceFilling = True):
        '''
        الحصول على الكلمة مُشكّلة 
        '''
        if(self.VoweledForm != '' and forceFilling == False):
            return;
        
        proclitics = ''.join([p.VoweledForm for p in self.Proclitics]);
        procliticsString = ''.join(proclitics);
        
        enclitics = [p.VoweledForm for p in self.Enclitics];
        if(type(self.Cliticless) is DerivedCliticless and len(enclitics) > 0 \
           and self.Cliticless.InternalEnclitic != None):
            enclitics.remove(enclitics[0]);        
        encliticsString = ''.join(enclitics);
        
        self.VoweledForm = ''.join([procliticsString, self.Cliticless.VoweledForm, encliticsString]);
    
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

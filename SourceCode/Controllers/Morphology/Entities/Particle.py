from Morphology.Entities.Morpheme import Morpheme


'''
Created on ٢٩‏/٠٥‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Controllers.Morphology.Entities.Morpheme import *;
from Controllers.Morphology.Entities.Particle import *;
from Models.Lexicon.SpecialWords.StandAloneParticle import *;


class ParticleConstants:
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyiSYI35Ed-gg8GOK1TmhA
    """
    class State:
        #غير معالجة
        Unprocessed = 0;
        #لاصقة بادئة
        Proclitic = 1;
        #لاصقة نهائية
        Enclitic = 2;
        #منفصلة
        StandAlone = 4
        #جميع الاحتمالات
        all_Cases = 7;



class Particle(Morpheme):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyiSYY35Ed-gg8GOK1TmhA
    """
    '''
    Particle
    '''
    
    State = 0;
    '''
    لاصقة بادئة = 1
    لاصقة نهائية = 2
    منفصلة = 4
    stand alone, proclitic, enclitic
    '''
        

    def __init__(self, unvoweledForm, voweledForm, state, pos = None):
        '''
        Constructor
        '''
        self.UnvoweledForm = unvoweledForm;
        self.VoweledForm = voweledForm;
        self.State = state;
        
        if(pos == None):
            self.POS = ParticlePOS();
            self.POS.MainClass = POSConstants.MainClass.Particle;
        else:
            self.POS = pos;
        
    pass

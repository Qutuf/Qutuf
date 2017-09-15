
'''
Created on ٢٩‏/٠٥‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Models.Tagging.POSTags.ParticlePOS import *;
from Controllers.Morphology.Entities.Particle import *;


class StandAloneParticle(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_hULWSI34Ed-gg8GOK1TmhA
    """
    '''
    Particle
    '''
    
    
    VoweledForm = '';
        
    
    UnvoweledForm = '';
    
    
    PrefixeClasses = ''; 
       
    
    SuffixeClasses = '';
    
    POS = ParticlePOS();

    def __init__(self):
        '''
        Constructor
        '''
        
        self.POS = ParticlePOS();
        self.POS.MainClass = POSConstants.MainClass.Particle;
        self.VoweledForm = '';
        self.UnvoweledForm = '';
        self.PrefixeClasses = '';
        self.SuffixeClasses = '';
    pass
        
    def AssignFromAlKalilDB(self, unvoweledForm, voweledForm, prefixeClasses, suffixeClasses, type):
    #سابقاً كان يتم تعبئته من الملف
    #toolwords.xml
    #ولاحقاً أصبح من
    #standaloneparticles.xml
        
        self.VoweledForm = voweledForm;
        self.UnvoweledForm = unvoweledForm;
        self.PrefixeClasses = prefixeClasses;
        self.SuffixeClasses = suffixeClasses;
        
        if(type == 'حرف جر'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.Preposition;  
        elif(type == 'حرف جزم'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.Apocopative;  
        elif(type == 'حرف نصب'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.Accusative;
        elif(type == 'حرف ناسخ'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.Annuler;
        elif(type == 'حرف عطف'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.Conjunction;
        elif(type == 'حرف نداء'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.Vocative;
        elif(type == 'حرف استثناء'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.Exceptive;
        elif(type == 'حرف استفهام'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.Interrogative;
        elif(type == 'حرف استقبال'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.Futurity;
        elif(type == 'حرف شرط'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.Conditional;
        elif(type == 'حرف تحقيق'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.RealizationORAlmost; 
        elif(type == 'حرف نصب فرعي'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.PartialAccusative;            
        elif(type == 'حرف تعليل'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.Causative;            
        elif(type == 'حرف نفي'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.Negative;
        elif(type == 'حرف قسم'):
            self.POS.SubClass = ParticlePOSConstants.SubClass.Jurative;
        
#        elif(type == 'حرف استئناف'):
#            #غير موجودة في الخليل وضعتها من أجل المستقبل
#            self.POS.SubClass = ParticlePOSConstants.SubClass.Resumption;
#            
        else:
            raise Exception('This type [' + type + '] is not known for a Particle!');
        
    pass
                        
      
    def ReturnAsParticle(self):
        
        pos = self.POS.Clone();
        particle = Particle(self.UnvoweledForm, self.VoweledForm, ParticleConstants.State.StandAlone, pos);
                
        return particle;
    pass  
            

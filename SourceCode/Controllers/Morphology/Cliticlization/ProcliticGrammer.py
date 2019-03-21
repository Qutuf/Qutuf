
'''
Created on ٢٦‏/٠٦‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from ...Morphology.Cliticlization.CliticGrammer import *;
from ...Morphology.Entities.Particle import *;
from ....Models.Tagging.POSTags.CliticlessPOS import CliticlessPOSConstants;
from ....Models.Tagging.POSTags.VerbalPOS import VerbalPOSConstants;
from ....Models.Tagging.POSTags.NominalPOS import NominalPOSConstants;
from ....Models.Tagging.POSTags.ParticlePOS import ParticlePOSConstants;
from ....Models.Tagging.POSTags.POS import POSConstants;

class ProcliticGrammer(CliticGrammer):
    """
     # PyUML: Do not remove this line! # XMI_ID:_hULWqI34Ed-gg8GOK1TmhA
    """
    '''
    Grammer of a Particle
    '''
    CliticSubClass = None;
    NextMainClass = None;
    NextCaseAndMood = None;
    NextNounSubClass = None;
    NextVerbAspect = None;
    NextDefiniteness = None;
    ComesAsLast = None;

    def __init__(self, particleSubClass, \
                 nextMainClass = POSConstants.MainClass.all_Cases, \
                 nextCaseAndMood = CliticlessPOSConstants.CaseAndMood.all_Cases, \
                 nextNounSubClass = NominalPOSConstants.SubClass.all_Cases, \
                 nextVerbAspect = VerbalPOSConstants.Aspect.all_Cases, \
                 nextDefiniteness = NominalPOSConstants.Definiteness.all_Cases, \
                 comesAsLast = False):
        '''
        Constructor
        '''
        self.CliticSubClass = particleSubClass;
        self.NextMainClass = nextMainClass;
        self.NextCaseAndMood = nextCaseAndMood;
        self.NextNounSubClass = nextNounSubClass;
        self.NextVerbAspect = nextVerbAspect;
        self.NextDefiniteness = nextDefiniteness;
        self.ComesAsLast = comesAsLast;
    pass

    def IsCompatible(self, cliticlessWord):
        
        if(cliticlessWord.POS.MainClass & self.NextMainClass != 0):            
            
            #إذا كانت فعل أو اسم علينا فحص توافق الحالة الإعرابية
            if(cliticlessWord.POS.MainClass == 0 or \
               cliticlessWord.POS.MainClass & self.NextMainClass & (POSConstants.MainClass.Verb + POSConstants.MainClass.Noun) != 0):
                
                if(cliticlessWord.POS.MainClass != 0):
                    cliticlessWord.POS.MainClass = cliticlessWord.POS.MainClass & self.NextMainClass;
                else:
                    cliticlessWord.POS.MainClass = self.NextMainClass;
                if(cliticlessWord.POS.CaseAndMood == 0 or \
                    cliticlessWord.POS.CaseAndMood & self.NextCaseAndMood != 0):
                    if(cliticlessWord.POS.CaseAndMood != 0):
                        cliticlessWord.POS.CaseAndMood = cliticlessWord.POS.CaseAndMood & self.NextCaseAndMood;
                    else:
                        cliticlessWord.POS.CaseAndMood = self.NextCaseAndMood;
                else:
                    return False;
        
            #إذا كان فعل علينا فحص توافق الصيغة
            if(cliticlessWord.POS.MainClass & POSConstants.MainClass.Verb != 0):
                if(cliticlessWord.POS.Aspect == 0 or\
                   cliticlessWord.POS.Aspect & self.NextVerbAspect != 0):                                
                    if(cliticlessWord.POS.Aspect != 0):
                        cliticlessWord.POS.Aspect = cliticlessWord.POS.Aspect & self.NextVerbAspect;
                    else:
                        cliticlessWord.POS.Aspect = self.NextVerbAspect;
                else:
                    return False;
                
            #إذا كان اسم أو حرف فعلينا فحص توافق الصنف الفرعي
            elif(cliticlessWord.POS.MainClass & POSConstants.MainClass.Noun != 0
                 or cliticlessWord.POS.MainClass & POSConstants.MainClass.Particle != 0):
                if(cliticlessWord.POS.SubClass == 0 or\
                   cliticlessWord.POS.SubClass & self.NextNounSubClass != 0):  
                    if(cliticlessWord.POS.SubClass != 0):         
                        cliticlessWord.POS.SubClass = cliticlessWord.POS.SubClass & self.NextNounSubClass;
                    else: 
                        cliticlessWord.POS.SubClass = self.NextNounSubClass;
                else: 
                    return False;
                        
            
                #إذا كان اسم فعلينا فحص التعريف
                if(cliticlessWord.POS.MainClass & self.NextMainClass & POSConstants.MainClass.Noun != 0):
                    if(cliticlessWord.POS.Definiteness == 0 or\
                       cliticlessWord.POS.Definiteness & self.NextDefiniteness != 0):                                
                        if(cliticlessWord.POS.Definiteness != 0):
                            cliticlessWord.POS.Definiteness = cliticlessWord.POS.Definiteness & self.NextDefiniteness;
                        else:
                            cliticlessWord.POS.Definiteness = self.NextDefiniteness;
                    else:
                        return False;
        else:
            return False;
        
        return True;
    pass

    def IsConsistentWith(self, listOfGrammars):
        for item in listOfGrammars[:]:
            otherGrammar = item.Grammar;
            if(otherGrammar.ComesAsLast == True and self.CliticSubClass != ParticlePOSConstants.SubClass.Appendix):
                return False;
            if(otherGrammar == self \
               or self.NextCaseAndMood & otherGrammar.NextCaseAndMood == 0\
               or self.NextMainClass & otherGrammar.NextMainClass == 0\
               or self.NextNounSubClass & otherGrammar.NextNounSubClass == 0):
                return False;
        return True;
    pass

    def CreateClitic(self, clticString, clticWithDiacritics, cliticState):
        particle = Particle(clticString, clticWithDiacritics, cliticState);
        particle.POS.SubClass = self.CliticSubClass;
        
        return particle;
    pass


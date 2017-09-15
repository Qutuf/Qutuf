
'''
Created on ٢٦‏/٠٦‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Controllers.Morphology.Entities.Particle import *;
from Controllers.Morphology.Entities.UnderivedCliticless import UnderivedCliticless;
from Controllers.Morphology.Cliticlization.CliticGrammer import CliticGrammer;


from Models.Tagging.POSTags.CliticlessPOS import CliticlessPOSConstants;
from Models.Tagging.POSTags.VerbalPOS import VerbalPOSConstants;
from Models.Tagging.POSTags.NominalPOS import NominalPOSConstants, NominalPOS;
from Models.Tagging.POSTags.ParticlePOS import ParticlePOSConstants;
from Models.Tagging.POSTags.POS import POSConstants;



class EncliticGrammer(CliticGrammer):
    """
     # PyUML: Do not remove this line! # XMI_ID:_hULWio34Ed-gg8GOK1TmhA
    """
    '''
    Grammer of a Particle
    '''

    PronounSubClass = None;
    CliticGender = None;
    CliticNumber = None;
    CliticPerson = None;
    
    WordCaseAndMood = None;
    WordGender = None;
    WordNumber = None;
    WordPerson = None;
    VerbAspect = None;
    VerbActiveness = None;
    VerbTransitivity = None;
    NounDefiniteness = None;

    def __init__(self, pronounSubClass = 0, \
                gender = CliticlessPOSConstants.Gender.all_Cases, \
                number = CliticlessPOSConstants.Number.all_Cases, \
                person = CliticlessPOSConstants.Person.all_Cases, \
                
                WordCaseAndMood = CliticlessPOSConstants.CaseAndMood.all_Cases, \
                WordGender = CliticlessPOSConstants.Gender.all_Cases, \
                WordNumber = CliticlessPOSConstants.Number.all_Cases, \
                WordPerson = CliticlessPOSConstants.Person.all_Cases, \
                VerbAspect = VerbalPOSConstants.Aspect.all_Cases, \
                VerbActiveness = VerbalPOSConstants.Activeness.Active, \
                VerbTransitivity = VerbalPOSConstants.Transitive.all_Cases, \
                NounDefiniteness = NominalPOSConstants.Definiteness.all_Cases):
        '''
        Constructor
        '''
        self.PronounSubClass = pronounSubClass;
        self.CliticGender = gender;
        self.CliticNumber = number;
        self.CliticPerson = person;
        
        self.WordCaseAndMood = WordCaseAndMood;
        self.WordGender = WordGender;
        self.WordNumber = WordNumber;
        self.WordPerson = WordPerson;
        self.VerbAspect = VerbAspect;
        self.VerbActiveness = VerbActiveness;
        self.VerbTransitivity = VerbTransitivity;
        
        self.NounDefiniteness = NounDefiniteness;
    pass

    def IsCompatible(self, cliticlessWord):

        #إذا كانت اسم أو فعل فعلينا فحص توافق الخواص
        if(cliticlessWord.POS.MainClass & POSConstants.MainClass.Noun != 0 \
           or cliticlessWord.POS.MainClass & POSConstants.MainClass.Verb != 0):
                            
        
            if(self.WordCaseAndMood & cliticlessWord.POS.CaseAndMood == 0):
                return False;
            if(self.WordGender & cliticlessWord.POS.Gender == 0):
                return False;
            if(self.WordNumber & cliticlessWord.POS.Number == 0):
                return False;
        
            #إذا كانت اسم علينا فحص توافق الخواص
            if(cliticlessWord.POS.MainClass & POSConstants.MainClass.Noun != 0):
                
                #التوافق في التعريف
                if(cliticlessWord.POS.Definiteness == 0 or \
                    cliticlessWord.POS.Definiteness & self.NounDefiniteness != 0):
                    
                    if(cliticlessWord.POS.Definiteness != 0):
                        cliticlessWord.POS.Definiteness = cliticlessWord.POS.Definiteness & self.NounDefiniteness;
                    else:
                        cliticlessWord.POS.Definiteness = self.NounDefiniteness;
                else:
                    return False;
                
                #التوافق في الأسناد
                #وهو فقط في حالة الأسماء
                if(cliticlessWord.POS.Person == 0 or \
                    cliticlessWord.POS.Person & self.CliticPerson != 0):
                    
                    if(cliticlessWord.POS.Person != 0):
                        cliticlessWord.POS.Person = cliticlessWord.POS.Person & self.CliticPerson;
                    else:
                        cliticlessWord.POS.Person = self.CliticPerson;
                else:
                    return False;
        
            if(cliticlessWord.POS.MainClass & POSConstants.MainClass.Verb != 0):
                
                if(cliticlessWord.POS.Transitive == 0 or \
                   self.VerbTransitivity & cliticlessWord.POS.Transitive != 0):
                    if(cliticlessWord.POS.Transitive != 0):
                        cliticlessWord.POS.Transitive = self.VerbTransitivity & cliticlessWord.POS.Transitive;
                    else:
                        cliticlessWord.POS.Transitive = self.VerbTransitivity;
                else:
                    return False;
                                
                if(cliticlessWord.POS.Aspect == 0 or \
                   self.VerbAspect & cliticlessWord.POS.Aspect != 0):
                    if(cliticlessWord.POS.Aspect != 0):
                        cliticlessWord.POS.Aspect = self.VerbAspect & cliticlessWord.POS.Aspect;
                    else:
                        cliticlessWord.POS.Aspect = self.VerbAspect;
                else:
                    return False;
                
                                    
                if(cliticlessWord.POS.Activeness == 0 or \
                   self.VerbActiveness & cliticlessWord.POS.Activeness != 0):
                    if(cliticlessWord.POS.Activeness != 0):
                        cliticlessWord.POS.Activeness = self.VerbActiveness & cliticlessWord.POS.Activeness;
                    else:
                        #يجب أن لا يكون فعل أمر لأن الأمر لا يبنى للمجهول
                        if(cliticlessWord.POS.Aspect & VerbalPOSConstants.Aspect.Imperative == 0):
                            cliticlessWord.POS.Activeness = self.VerbActiveness;
                else:
                    return False;
                
        
        
        return True;
    pass

    def IsConsistentWith(self, listOfGrammars):
#        for item in listOfGrammars[:]:
#            otherGrammar = item.Grammar;
#            if(otherGrammar.ComesAsLast == True and self.PronounSubClass != ParticlePOSConstants.SubClass.Appendix):
#                return False;
#            if(otherGrammar == self \
#               or self.NextCaseAndMood & otherGrammar.NextCaseAndMood == 0\
#               or self.MainClass & otherGrammar.MainClass == 0\
#               or self.NextNounSubClass & otherGrammar.NextNounSubClass == 0):
#                return False;
        return True;
    pass

    def CreateClitic(self, clticString, clticWithDiacritics, cliticState):
        pos = NominalPOS();
        pos.SubClass = self.PronounSubClass;
        pos.Definiteness = NominalPOSConstants.Definiteness.Definite_by_Itself;
        pos.Gender = self.CliticGender ;
        pos.Number = self.CliticNumber;
        pos.Person = self.CliticPerson;
        
        #جميع ما في قاعدة بيانات الأوزان هي ضمائر رفع وجميع ما في اللواصق اللاحقة هي ضمائر نصب
        pos.CaseAndMood = CliticlessPOSConstants.CaseAndMood.AccusativeOrSubjunctive;
        
        particle = UnderivedCliticless(clticString, clticWithDiacritics);
        particle.POS = pos;
        
        return particle;
    pass



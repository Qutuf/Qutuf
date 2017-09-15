
'''
Created on ٢٨‏/٠٥‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from Controllers.Morphology.Entities.Cliticless import Cliticless;
from Controllers.Morphology.Entities.Particle import Particle, ParticleConstants;

from Models.Lexicon.RootAndPatterns.UnvoweledPattern import UnvoweledPattern;
from Models.Lexicon.RootAndPatterns.VoweledPattern import VoweledPattern;
from Models.Lexicon.RootAndPatterns.Root import Root;
from Models.Lexicon.LettersConstants import DiacriticsConstants, HamzaConstants;

from Models.Tagging.POSTags.CliticlessPOS import CliticlessPOSConstants;
from Models.Tagging.POSTags.VerbalPOS import VerbalPOSConstants;
from Models.Tagging.POSTags.NominalPOS import NominalPOSConstants, NominalPOS;
from Models.Tagging.POSTags.ParticlePOS import ParticlePOSConstants;
from Models.Tagging.POSTags.POS import POSConstants;

class DerivedCliticless(Cliticless):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyiSBY35Ed-gg8GOK1TmhA
    """
    '''
    classdocs
    '''
    
    
    Root = Root(None, None);   
    #الجذر
    
    UnvoweledPattern = UnvoweledPattern(None, None, None);
    #وزن الجذع الغير مشكول
    
    VoweledPattern = VoweledPattern();
    #وزن الجذع المشكول
    
    
#
#    Prefixes = [];
#    #بوادئ
#
#    Suffixes = [];
#    #نهايات
#    
    
    __StemString = '';
    #الجذع
    
    InternalEnclitic = None;
    
    
    def __init__(self, string, root, unvoweledPattern, voweledPattern):
        '''
        Constructor
        '''
        self.OriginalString = string;
        self.Root = root;
        
        self.UnvoweledForm = string;
        self.UnvoweledPattern = unvoweledPattern;
        
        self.VoweledPattern = voweledPattern
        self.FillDiacritizedForm();
        
        self.POS = self.VoweledPattern.POS.Clone();
        
        self.InternalEnclitic = None;
        
    pass
        
    def UpdateInternalEnclitic(self):
        
        [internalEnclitics, internalEncliticsCutLength] = self.GetInternalEnclitic();
        if(internalEnclitics != None):
            self.InternalEnclitic = internalEnclitics;
            
        
        self.__StemString = self.UnvoweledForm[0:len(self.UnvoweledForm) - internalEncliticsCutLength]; 
        
    pass
      

    def GetStemString(self):
        
        return self.__StemString;
    pass

  
    def FillDiacritizedForm(self):
        voweledForm = '';
        wordIndexCounter = 0;
        for i in range(len(self.VoweledPattern.VoweledForm)):
            if(self.VoweledPattern.VoweledForm[i] in ['ف','ع','ل']):
                voweledForm += self.UnvoweledForm[wordIndexCounter];
            else:
                voweledForm += self.VoweledPattern.VoweledForm[i];
            if(self.VoweledPattern.VoweledForm[i] not in DiacriticsConstants.AllDiacritics\
               or (wordIndexCounter != len(self.UnvoweledForm) and self.VoweledPattern.VoweledForm[i] == self.UnvoweledForm[wordIndexCounter])):
                wordIndexCounter += 1;
                
        self.VoweledForm = voweledForm;
    pass

    def IsHamzaCompatibleWithVoweldForm(self):
        start = -1;
        while(True):
            hamzaFound = False;
            for hamza in HamzaConstants.AllHamzas:
                hamzaIndex = self.VoweledForm.find(hamza, start+1);
                if(hamzaIndex == -1):                    
                    continue;
                else:
                    hamzaFound = True;
                    if(self.__IsHamzaCompatibleWithVoweldForm(hamzaIndex)):
                        start = hamzaIndex;
                        break;
                    else:
                        return False;
            if(hamzaFound == False):
                break;
        return True;
    pass
    
    def __IsHamzaCompatibleWithVoweldForm(self, hamzaIndex):
        if(hamzaIndex == len(self.VoweledForm)-1):
            #############################################            
            return True;
        
        hamza = self.VoweledForm[hamzaIndex];
        DiacriticOfHamza = self.VoweledForm[hamzaIndex + 1];
        if(hamzaIndex == 0):
            if(DiacriticOfHamza in [DiacriticsConstants.Fatha, DiacriticsConstants.Damma]\
               and hamza  == HamzaConstants.OnAlif):
                return True;
            elif(DiacriticOfHamza in [DiacriticsConstants.Kasra]\
               and hamza == HamzaConstants.UnderAlif):
                return True;
            else:
                return False;
        else:
            if(DiacriticOfHamza not in DiacriticsConstants.AllDiacritics):
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#                print('Warning: hamza is not well diacritized! VoweledForm = ['+self.VoweledForm+']'\
#                      + ', The Sukoon will be considered [ْ]' );
                DiacriticOfHamza = DiacriticsConstants.Sukoon;
            DiacriticBefore = self.VoweledForm[hamzaIndex - 1];
            
            #############################################
            #يجب معالجة القواعد الشاذة لكتابة الهمسة هنا!!!!
            #############################################
            
            if(DiacriticOfHamza == DiacriticsConstants.Sukoon):
                DiacriticOfHamza = DiacriticBefore;
            elif(DiacriticBefore == DiacriticsConstants.Kasra):
                DiacriticOfHamza = DiacriticBefore;
            elif(DiacriticBefore == DiacriticsConstants.Damma and DiacriticOfHamza == DiacriticsConstants.Fatha):
                DiacriticOfHamza = DiacriticBefore;
            
            if(DiacriticOfHamza in [DiacriticsConstants.Damma, DiacriticsConstants.DoubleDamma]):
                if(hamza == HamzaConstants.OnWaw):
                    return True;
                else:
                    return False;
            elif(DiacriticOfHamza in [DiacriticsConstants.Kasra, DiacriticsConstants.DoubleKasra]):
                if(hamza == HamzaConstants.OnYa):
                    return True;
                else:
                    return False;
            elif(DiacriticOfHamza in [DiacriticsConstants.Fatha, DiacriticsConstants.DoubleFatha]):
                if(hamza == HamzaConstants.OnAlif):
                    return True;
                else:
                    return False;
                
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#        print('Warning: This Code is not supposed to be reached!');
        return False;
            
    pass


    def GetInternalEnclitic(self):

        if(type(self) is list):
            x = 0;
        if(self.POS.MainClass & POSConstants.MainClass.Verb == 0):
            return [None, 0];
        if(self.POS.Number & CliticlessPOSConstants.Number.Singular != 0 and \
           self.POS.Person & VerbalPOSConstants.Person.Third_Person  != 0 ):
            
                #قد يكون ضمير مستتر وقد لا يكون
#                unvoweled = 'هو';
#                voweled = 'هُوَ';
            return [None, 0];
        

        unvoweled = '';
        voweled = '';
        
        isHidden = False;
        
        #المتحول التالي يستخدم لفصل الضمير المظاهر عن الكلمة
        #ولكن العملية تحتاج إلى معالجة أكثر تعقيداً
        #لذلك إلى أن تتم المعالجة بالشكل الأمثل
        #قمت بإسناد القيمة 0 لهذا المتحول في نهاية هذا التابع
        cutLength = 0;
        
#            "مسند إلى المتكلم أنا"
        if(self.POS.Number == VerbalPOSConstants.Number.Singular and \
            self.POS.Gender == VerbalPOSConstants.Gender.all_Cases and \
            self.POS.Person == VerbalPOSConstants.Person.First_Person):
            if(self.POS.Aspect == VerbalPOSConstants.Aspect.Perfective):
                unvoweled = 'ت';
                voweled = 'تُ';
            else:
                #ضمير مستتر
                isHidden = True;
                unvoweled = 'أنا';
                voweled = 'أَنَاْ';            
            
#            "مسند إلى المتكلمين (نحن)"
        if(self.POS.Number == VerbalPOSConstants.Number.Plural and \
            self.POS.Gender == VerbalPOSConstants.Gender.all_Cases and \
            self.POS.Person == VerbalPOSConstants.Person.First_Person):
            if(self.POS.Aspect == VerbalPOSConstants.Aspect.Perfective):
                #ضمير ظاهر
                unvoweled = 'نا';
                voweled = 'نَاْ';
                cutLength = 2;
            else:
                #ضمير مستتر
                isHidden = True;
                unvoweled = 'نحن';
                voweled = 'نحن';
        
#            "مسند إلى المخاطَب أنت"
        if(self.POS.Number == VerbalPOSConstants.Number.Singular and \
            self.POS.Gender == VerbalPOSConstants.Gender.Masculine and \
            self.POS.Person == VerbalPOSConstants.Person.Second_Person):
            if(self.POS.Aspect == VerbalPOSConstants.Aspect.Perfective):
                #ضمير ظاهر
                unvoweled = 'ت';
                voweled = 'تَ';
                cutLength = 1;
            else:
                #ضمير مستتر
                isHidden = True;
                unvoweled = 'أنت';
                voweled = 'أَنْتَ';

#            "مسند إلى المخاطبة (أنتِ)"
        if(self.POS.Number == VerbalPOSConstants.Number.Singular and \
            self.POS.Gender == VerbalPOSConstants.Gender.Feminine and \
            self.POS.Person == VerbalPOSConstants.Person.Second_Person):
            if(self.POS.Aspect == VerbalPOSConstants.Aspect.Perfective):
                #ضمير ظاهر
                unvoweled = 'ت';
                voweled = 'تِ';
                cutLength = 1;
            else:
                unvoweled = 'ي';
                voweled = 'ي';
                if(self.POS.Aspect == VerbalPOSConstants.Aspect.Imperfective and \
                   self.POS.CaseAndMood == VerbalPOSConstants.CaseAndMood.NominativeOrIndicative):
                    cutLength = 2;                    
                else:                    
                    cutLength = 1;

            
#            "مسند إلى المخاطَبَين (أنتما)"
        if(self.POS.Number == VerbalPOSConstants.Number.Dual and \
            self.POS.Gender == VerbalPOSConstants.Gender.Masculine and \
            self.POS.Person == VerbalPOSConstants.Person.Second_Person):
            #ضمير ظاهر
            unvoweled = 'ا';
            voweled = 'اْ';
            if(self.POS.Aspect == VerbalPOSConstants.Aspect.Perfective):
                cutLength = 3;
            elif((self.POS.Aspect == VerbalPOSConstants.Aspect.Imperfective and \
               self.POS.CaseAndMood == VerbalPOSConstants.CaseAndMood.NominativeOrIndicative) \
               or (self.POS.Aspect == VerbalPOSConstants.Aspect.Imperfective and \
               self.POS.Asserted == VerbalPOSConstants.Asserted.Asserted)):
                cutLength = 2;
            else:
                cutLength = 1;

#            "مسند إلى المخاطبين (أنتم)"
        if(self.POS.Number == VerbalPOSConstants.Number.Plural and \
            self.POS.Gender == VerbalPOSConstants.Gender.Masculine and \
            self.POS.Person == VerbalPOSConstants.Person.Second_Person):
            if(self.POS.Aspect == VerbalPOSConstants.Aspect.Perfective):
                #ضمير مستتر
                isHidden = True;
                unvoweled = 'أنتم';
                voweled = 'أَنْتُمْ';
                cutLength = 2;
            else:
                #ضمير ظاهر
                unvoweled = 'و';
                voweled = 'وْ';
                if(self.POS.Aspect == VerbalPOSConstants.Aspect.Imperfective and \
                   self.POS.Asserted == VerbalPOSConstants.Asserted.Asserted):                    
                    cutLength = 1;
                else:
                    cutLength = 2;
        
#            "مسند إلى المخاطَبات (أنتن)"
        if(self.POS.Number == VerbalPOSConstants.Number.Plural and \
            self.POS.Gender == VerbalPOSConstants.Gender.Feminine and \
            self.POS.Person == VerbalPOSConstants.Person.Second_Person):
            #ضمير ظاهر
            unvoweled = 'ن';
            voweled = 'نَ';
            if(self.POS.Aspect == VerbalPOSConstants.Aspect.Perfective):
                cutLength = 2;
            elif(self.POS.Aspect == VerbalPOSConstants.Aspect.Imperfective and \
               self.POS.Asserted == VerbalPOSConstants.Asserted.Asserted):
                cutLength = 3;                    
            else:                    
                cutLength = 1;
#                
##            "مسند إلى الغائب (هو)"
#        if(self.POS.Number == VerbalPOSConstants.Number.Singular and \
#            self.POS.Gender == VerbalPOSConstants.Gender.Masculine and \
#            self.POS.Person == VerbalPOSConstants.Person.Third_Person):
#            unvoweled = '';
#            voweled = '';
#
##            "مسند إلى الغائبة (هي)"
#        if(self.POS.Number == VerbalPOSConstants.Number.Singular and \
#            self.POS.Gender == VerbalPOSConstants.Gender.Feminine and \
#            self.POS.Person == VerbalPOSConstants.Person.Third_Person):
#            unvoweled = '';
#            voweled = '';

#            "مسند إلى الغائبَين (هما)"
        if(self.POS.Number == VerbalPOSConstants.Number.Dual and \
            self.POS.Gender == VerbalPOSConstants.Gender.Masculine and \
            self.POS.Person == VerbalPOSConstants.Person.Third_Person):
            #ضمير ظاهر
            unvoweled = 'ا';
            voweled = 'اْ';
            if((self.POS.Aspect == VerbalPOSConstants.Aspect.Imperfective and \
               self.POS.CaseAndMood == VerbalPOSConstants.CaseAndMood.NominativeOrIndicative) \
               or (self.POS.Aspect == VerbalPOSConstants.Aspect.Imperfective and \
               self.POS.Asserted == VerbalPOSConstants.Asserted.Asserted)):
                cutLength = 2;
            else:
                cutLength = 1;

#            "مسند إلى الغائبتين (هما)"
        if(self.POS.Number == VerbalPOSConstants.Number.Dual and \
            self.POS.Gender == VerbalPOSConstants.Gender.Feminine and \
            self.POS.Person == VerbalPOSConstants.Person.Third_Person):
            #ضمير ظاهر
            unvoweled = 'ا';
            voweled = 'اْ';
            if(self.POS.Aspect == VerbalPOSConstants.Aspect.Perfective):
                cutLength = 2;
            elif((self.POS.Aspect == VerbalPOSConstants.Aspect.Imperfective and \
               self.POS.CaseAndMood == VerbalPOSConstants.CaseAndMood.NominativeOrIndicative) \
               or (self.POS.Aspect == VerbalPOSConstants.Aspect.Imperfective and \
               self.POS.Asserted == VerbalPOSConstants.Asserted.Asserted)):
                cutLength = 2;
            else:
                cutLength = 1;
        
#            "مسند إلى الغائبين (هم)"
        if(self.POS.Number == VerbalPOSConstants.Number.Plural and \
            self.POS.Gender == VerbalPOSConstants.Gender.Masculine and \
            self.POS.Person == VerbalPOSConstants.Person.Third_Person):
            unvoweled = 'و';
            voweled = 'وْ';
            if(self.POS.Aspect == VerbalPOSConstants.Aspect.Imperfective and \
               self.POS.Asserted == VerbalPOSConstants.Asserted.Asserted):
                cutLength = 1;
            else:
                cutLength = 2;
                
#            "مسند إلى الغائبات (هن)"
        if(self.POS.Number == VerbalPOSConstants.Number.Singular and \
            self.POS.Gender == VerbalPOSConstants.Gender.Feminine and \
            self.POS.Person == VerbalPOSConstants.Person.Third_Person):
            unvoweled = 'ن';
            voweled = 'نَ';
            if(self.POS.Aspect == VerbalPOSConstants.Aspect.Imperfective and \
               self.POS.Asserted == VerbalPOSConstants.Asserted.Asserted):
                cutLength = 1;
            else:
                cutLength = 2;
        
        pos = NominalPOS();
        
        if(isHidden == False):
            pos.Substantivness = NominalPOSConstants.Substantivness.Substantive;
        else:
            pos.Substantivness = NominalPOSConstants.Substantivness.Hidden;
        pos.Number = self.POS.Number;
        pos.Gender = self.POS.Gender;    
        pos.CaseAndMood = CliticlessPOSConstants.CaseAndMood.NominativeOrIndicative;  
        pos.SubClass = NominalPOSConstants.SubClass.Nominative_Pronoun; 
        pos.Definiteness = NominalPOSConstants.Definiteness.Definite_by_Itself; 
                   
        
        particle  = Particle(unvoweled, voweled, ParticleConstants.State.Enclitic, pos);
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
        #المتحول التالي يستخدم لفصل الضمير المظاهر عن الكلمة
        #ولكن العملية تحتاج إلى معالجة أكثر تعقيداً
        #لذلك إلى أن تتم المعالجة بالشكل الأمثل
        #قمت بإسناد القيمة 0 لهذا المتحول في نهاية هذا التابع
        cutLength = 0;
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        return [particle, cutLength];
    pass

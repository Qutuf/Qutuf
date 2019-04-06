
'''
Created on ٠٢‏/٠٧‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from ...Morphology.Cliticlization.CliticsGrammers import CliticsGrammers;

from ...Morphology.Cliticlization.EncliticGrammer import EncliticGrammer;
from ....Models.Lexicon.LettersConstants import DiacriticsConstants;
from ....Models.Tagging.POSTags.ParticlePOS import ParticlePOSConstants;
from ....Models.Tagging.POSTags.POS import POSConstants;
from ....Models.Tagging.POSTags.CliticlessPOS import CliticlessPOSConstants;
from ....Models.Tagging.POSTags.VerbalPOS import VerbalPOSConstants;
from ....Models.Tagging.POSTags.NominalPOS import NominalPOSConstants;

class EncliticsGrammers(CliticsGrammers):
    '''
    classdocs
    '''
    
    GrammersDict = {};

    def __init__(self):
        '''
        Constructor
        '''
        
#        Nominative_Pronoun
#        Accusative_or_Genitive_Pronoun
        
        
#        pronounSubClass = 0, \
#        gender = CliticlessPOSConstants.Gender.all_Cases, \
#        number = CliticlessPOSConstants.Number.all_Cases, \
#        person = CliticlessPOSConstants.Person.all_Cases, \
#                    
#        CliticlessPOSConstants.CaseAndMood.all_Cases, \
#        CliticlessPOSConstants.Gender.all_Cases, \
#        CliticlessPOSConstants.Number.all_Cases, \
#        CliticlessPOSConstants.Person.all_Cases, \
#        VerbalPOSConstants.Aspect.all_Cases, \
#        VerbalPOSConstants.Activeness.all_Cases
#        NominalPOSConstants.Definiteness.all_Cases):
  
        '''
        جميع الضمائر الموجودة هنا هي ضمائر نصب لأن ضمائر الرفع موجودة ضمن الأوزان:
        القواعد المستخدمة:
        ضمائر النصب لا تأتي مع الأفعال الازمة
        ضمائر المخاطب لا تأتي مع فعل الأمر
        مع المبني للمجهول تأتي جميع الضمائر (في الخليل لا يأتي مع المبني للمجهول ضمائر) لا أدري لماذا
        
        ضمائر النصب لا تأتي مع المعرّف بأل أو النكرة, فهي تأتي مع الأسماء في محل جر بالإضافة والاسم قبلها معرّف بالإضافة
        '''
  
                
        #كَ
        Masculine_Singular_Second_Person = EncliticGrammer(NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun, \
                NominalPOSConstants.Gender.Masculine, \
                NominalPOSConstants.Number.Singular, \
                NominalPOSConstants.Person.Second_Person, \
                CliticlessPOSConstants.CaseAndMood.all_Cases, \
                CliticlessPOSConstants.Gender.all_Cases, \
                CliticlessPOSConstants.Number.all_Cases, \
                CliticlessPOSConstants.Person.all_Cases, \
                VerbalPOSConstants.Aspect.all_Cases - VerbalPOSConstants.Aspect.Imperative, \
                VerbalPOSConstants.Activeness.all_Cases, \
                VerbalPOSConstants.Transitive.all_Cases - VerbalPOSConstants.Transitive.Intransitive, \
                NominalPOSConstants.Definiteness.Definite_by_Another);
        
        
        #كِ
        Feminine_Singular_Second_Person = EncliticGrammer(NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun, \
                NominalPOSConstants.Gender.Feminine, \
                NominalPOSConstants.Number.Singular, \
                NominalPOSConstants.Person.Second_Person, \
                CliticlessPOSConstants.CaseAndMood.all_Cases, \
                CliticlessPOSConstants.Gender.all_Cases, \
                CliticlessPOSConstants.Number.all_Cases, \
                CliticlessPOSConstants.Person.all_Cases, \
                VerbalPOSConstants.Aspect.all_Cases - VerbalPOSConstants.Aspect.Imperative, \
                VerbalPOSConstants.Activeness.all_Cases, \
                VerbalPOSConstants.Transitive.all_Cases - VerbalPOSConstants.Transitive.Intransitive, \
                NominalPOSConstants.Definiteness.Definite_by_Another);
        #كما
        all_Cases_Dual_Second_Person = EncliticGrammer(NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun, \
                NominalPOSConstants.Gender.all_Cases, \
                NominalPOSConstants.Number.Dual, \
                NominalPOSConstants.Person.Second_Person, \
                CliticlessPOSConstants.CaseAndMood.all_Cases, \
                CliticlessPOSConstants.Gender.all_Cases, \
                CliticlessPOSConstants.Number.all_Cases, \
                CliticlessPOSConstants.Person.all_Cases, \
                VerbalPOSConstants.Aspect.all_Cases - VerbalPOSConstants.Aspect.Imperative, \
                VerbalPOSConstants.Activeness.all_Cases, \
                VerbalPOSConstants.Transitive.all_Cases - VerbalPOSConstants.Transitive.Intransitive, \
                NominalPOSConstants.Definiteness.Definite_by_Another);
        #كم
        Masculine_Plural_Second_Person = EncliticGrammer(NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun, \
                NominalPOSConstants.Gender.Masculine, \
                NominalPOSConstants.Number.Plural, \
                NominalPOSConstants.Person.Second_Person, \
                CliticlessPOSConstants.CaseAndMood.all_Cases, \
                CliticlessPOSConstants.Gender.all_Cases, \
                CliticlessPOSConstants.Number.all_Cases, \
                CliticlessPOSConstants.Person.all_Cases, \
                VerbalPOSConstants.Aspect.all_Cases - VerbalPOSConstants.Aspect.Imperative, \
                VerbalPOSConstants.Activeness.all_Cases, \
                VerbalPOSConstants.Transitive.all_Cases - VerbalPOSConstants.Transitive.Intransitive, \
                NominalPOSConstants.Definiteness.Definite_by_Another);
        #كن
        Feminine_Plural_Second_Person = EncliticGrammer(NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun, \
                NominalPOSConstants.Gender.Feminine, \
                NominalPOSConstants.Number.Plural, \
                NominalPOSConstants.Person.Second_Person, \
                CliticlessPOSConstants.CaseAndMood.all_Cases, \
                CliticlessPOSConstants.Gender.all_Cases, \
                CliticlessPOSConstants.Number.all_Cases, \
                CliticlessPOSConstants.Person.all_Cases, \
                VerbalPOSConstants.Aspect.all_Cases - VerbalPOSConstants.Aspect.Imperative, \
                VerbalPOSConstants.Activeness.all_Cases, \
                VerbalPOSConstants.Transitive.all_Cases - VerbalPOSConstants.Transitive.Intransitive, \
                NominalPOSConstants.Definiteness.Definite_by_Another);
        
        #ه
        Masculine_Singular_Third_Person = EncliticGrammer(NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun, \
                NominalPOSConstants.Gender.Masculine, \
                NominalPOSConstants.Number.Singular, \
                NominalPOSConstants.Person.Third_Person, \
                CliticlessPOSConstants.CaseAndMood.all_Cases, \
                CliticlessPOSConstants.Gender.all_Cases, \
                CliticlessPOSConstants.Number.all_Cases, \
                CliticlessPOSConstants.Person.all_Cases, \
                VerbalPOSConstants.Aspect.all_Cases, \
                VerbalPOSConstants.Activeness.all_Cases, \
                VerbalPOSConstants.Transitive.all_Cases - VerbalPOSConstants.Transitive.Intransitive, \
                NominalPOSConstants.Definiteness.Definite_by_Another);
        
        #ها
        Feminine_Singular_Third_Person = EncliticGrammer(NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun, \
                NominalPOSConstants.Gender.Feminine, \
                NominalPOSConstants.Number.Singular, \
                NominalPOSConstants.Person.Third_Person, \
                CliticlessPOSConstants.CaseAndMood.all_Cases, \
                CliticlessPOSConstants.Gender.all_Cases, \
                CliticlessPOSConstants.Number.all_Cases, \
                CliticlessPOSConstants.Person.all_Cases, \
                VerbalPOSConstants.Aspect.all_Cases, \
                VerbalPOSConstants.Activeness.all_Cases, \
                VerbalPOSConstants.Transitive.all_Cases - VerbalPOSConstants.Transitive.Intransitive, \
                NominalPOSConstants.Definiteness.Definite_by_Another);
        #هما
        all_Cases_Dual_Third_Person = EncliticGrammer(NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun, \
                NominalPOSConstants.Gender.all_Cases, \
                NominalPOSConstants.Number.Dual, \
                NominalPOSConstants.Person.Third_Person, \
                CliticlessPOSConstants.CaseAndMood.all_Cases, \
                CliticlessPOSConstants.Gender.all_Cases, \
                CliticlessPOSConstants.Number.all_Cases, \
                CliticlessPOSConstants.Person.all_Cases, \
                VerbalPOSConstants.Aspect.all_Cases, \
                VerbalPOSConstants.Activeness.all_Cases, \
                VerbalPOSConstants.Transitive.all_Cases - VerbalPOSConstants.Transitive.Intransitive, \
                NominalPOSConstants.Definiteness.Definite_by_Another);
        #هم
        Masculine_Plural_Third_Person = EncliticGrammer(NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun, \
                NominalPOSConstants.Gender.Masculine, \
                NominalPOSConstants.Number.Plural, \
                NominalPOSConstants.Person.Third_Person, \
                CliticlessPOSConstants.CaseAndMood.all_Cases, \
                CliticlessPOSConstants.Gender.all_Cases, \
                CliticlessPOSConstants.Number.all_Cases, \
                CliticlessPOSConstants.Person.all_Cases, \
                VerbalPOSConstants.Aspect.all_Cases, \
                VerbalPOSConstants.Activeness.all_Cases, \
                VerbalPOSConstants.Transitive.all_Cases - VerbalPOSConstants.Transitive.Intransitive, \
                NominalPOSConstants.Definiteness.Definite_by_Another);
        #هن
        Feminine_Plural_Third_Person = EncliticGrammer(NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun, \
                NominalPOSConstants.Gender.Feminine, \
                NominalPOSConstants.Number.Plural, \
                NominalPOSConstants.Person.Third_Person, \
                CliticlessPOSConstants.CaseAndMood.all_Cases, \
                CliticlessPOSConstants.Gender.all_Cases, \
                CliticlessPOSConstants.Number.all_Cases, \
                CliticlessPOSConstants.Person.all_Cases, \
                VerbalPOSConstants.Aspect.all_Cases, \
                VerbalPOSConstants.Activeness.all_Cases, \
                VerbalPOSConstants.Transitive.all_Cases - VerbalPOSConstants.Transitive.Intransitive, \
                NominalPOSConstants.Definiteness.Definite_by_Another);
              
        
        #ني - ي
        all_Cases_Singular_First_Person = EncliticGrammer(NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun, \
                NominalPOSConstants.Gender.all_Cases, \
                NominalPOSConstants.Number.Singular, \
                NominalPOSConstants.Person.First_Person, \
                CliticlessPOSConstants.CaseAndMood.all_Cases, \
                CliticlessPOSConstants.Gender.all_Cases, \
                CliticlessPOSConstants.Number.all_Cases, \
                CliticlessPOSConstants.Person.all_Cases, \
                VerbalPOSConstants.Aspect.all_Cases, \
                VerbalPOSConstants.Activeness.all_Cases, \
                VerbalPOSConstants.Transitive.all_Cases - VerbalPOSConstants.Transitive.Intransitive, \
                NominalPOSConstants.Definiteness.Definite_by_Another);
        #نا
        all_Cases_DualPlural_First_Person = EncliticGrammer(NominalPOSConstants.SubClass.Nominative_Pronoun, \
                NominalPOSConstants.Gender.all_Cases, \
                NominalPOSConstants.Number.Dual & NominalPOSConstants.Number.Plural, \
                NominalPOSConstants.Person.First_Person, \
                CliticlessPOSConstants.CaseAndMood.all_Cases, \
                CliticlessPOSConstants.Gender.all_Cases, \
                CliticlessPOSConstants.Number.all_Cases, \
                CliticlessPOSConstants.Person.all_Cases, \
                VerbalPOSConstants.Aspect.all_Cases, \
                VerbalPOSConstants.Activeness.all_Cases, \
                VerbalPOSConstants.Transitive.all_Cases - VerbalPOSConstants.Transitive.Intransitive, \
                NominalPOSConstants.Definiteness.Definite_by_Another);
                
                


        #حرف زائد
        appendix = EncliticGrammer(ParticlePOSConstants.SubClass.Appendix);
        
        #ربما ينتح حرف الواو في اللواحق عن إشباع الضم
        self.GrammersDict = {};
        
        self.GrammersDict['و'] = {};
        self.GrammersDict['و'][DiacriticsConstants.Sukoon] \
                = [appendix];
        
        self.GrammersDict['ي'] = {};
        self.GrammersDict['ي'][DiacriticsConstants.Sukoon] \
                = [all_Cases_Singular_First_Person];
        
        
        self.GrammersDict['ني'] = {};
        self.GrammersDict['ني'][DiacriticsConstants.Kasra, DiacriticsConstants.Sukoon] \
                = [all_Cases_Singular_First_Person];
        
        self.GrammersDict['نا'] = {};
        self.GrammersDict['نا'][DiacriticsConstants.Fatha, DiacriticsConstants.Sukoon] \
                = [all_Cases_DualPlural_First_Person];
                

        self.GrammersDict['ك'] = {};
        self.GrammersDict['ك'][DiacriticsConstants.Fatha] \
                = [Masculine_Singular_Second_Person];
        self.GrammersDict['ك'][DiacriticsConstants.Kasra] \
                = [Feminine_Singular_Second_Person];
                
        self.GrammersDict['كما'] = {};
        self.GrammersDict['كما'][DiacriticsConstants.Damma, DiacriticsConstants.Fatha, DiacriticsConstants.Sukoon] \
                = [all_Cases_Dual_Second_Person];
                
        self.GrammersDict['كم'] = {};
        self.GrammersDict['كم'][DiacriticsConstants.Damma, DiacriticsConstants.Sukoon] \
                = [Masculine_Plural_Second_Person];
                
        self.GrammersDict['كن'] = {};
        self.GrammersDict['كن'][DiacriticsConstants.Damma, DiacriticsConstants.Shadda] \
                = [Feminine_Plural_Second_Person];
                
        self.GrammersDict['ه'] = {};
        self.GrammersDict['ه'][DiacriticsConstants.Damma] \
                = [Masculine_Singular_Third_Person];
                
        self.GrammersDict['ها'] = {};
        self.GrammersDict['ها'][DiacriticsConstants.Fatha, DiacriticsConstants.Sukoon] \
                = [Feminine_Singular_Third_Person];
                
        self.GrammersDict['هما'] = {};
        self.GrammersDict['هما'][DiacriticsConstants.Damma, DiacriticsConstants.Fatha, DiacriticsConstants.Sukoon] \
                = [all_Cases_Dual_Third_Person];
                
        self.GrammersDict['هم'] = {};
        self.GrammersDict['هم'][DiacriticsConstants.Damma, DiacriticsConstants.Sukoon] \
                = [Masculine_Plural_Third_Person];
                
        self.GrammersDict['هن'] = {};
        self.GrammersDict['هن'][DiacriticsConstants.Damma, DiacriticsConstants.Shadda] \
                = [Feminine_Plural_Third_Person];
        
    
    
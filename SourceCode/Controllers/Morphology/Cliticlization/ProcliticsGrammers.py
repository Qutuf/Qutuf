
'''
Created on ٠٢‏/٠٧‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Controllers.Morphology.Cliticlization.CliticsGrammers import CliticsGrammers;

from Controllers.Morphology.Cliticlization.ProcliticGrammer import ProcliticGrammer;
from Models.Lexicon.LettersConstants import DiacriticsConstants;
from Models.Tagging.POSTags.ParticlePOS import ParticlePOSConstants;
from Models.Tagging.POSTags.POS import POSConstants;
from Models.Tagging.POSTags.CliticlessPOS import CliticlessPOSConstants;
from Models.Tagging.POSTags.VerbalPOS import VerbalPOSConstants;
from Models.Tagging.POSTags.NominalPOS import NominalPOSConstants;


class ProcliticsGrammers(CliticsGrammers):
    """
     # PyUML: Do not remove this line! # XMI_ID:_hUUgWo34Ed-gg8GOK1TmhA
    """
    '''
    classdocs
    '''

    GrammersDict = {};

    def __init__(self):
        '''
        Constructor
        '''
#         ProcliticGrammer parameters:
#         Particle SubClass
#         nextMainClass = POSConstants.MainClass.all_Cases, \
#         nextCaseAndMood = CliticlessPOSConstants.CaseAndMood.all_Cases, \
#         nextNounSubClass = NominalPOSConstants.SubClass.all_Cases, \
#         nextVerbAspect = VerbalPOSConstants.Aspect.all_Cases, \
#         nextDefiniteness = NominalPOSConstants.Definiteness.all_Cases, \
#         comesAsLast = False):

        #العطف
        conjunction = ProcliticGrammer(ParticlePOSConstants.SubClass.Conjunction);
        #الاستئناف
        resumption = ProcliticGrammer(ParticlePOSConstants.SubClass.Resumption);
        #الاستفهام
        interrogative = ProcliticGrammer(ParticlePOSConstants.SubClass.Interrogative, \
                                        POSConstants.MainClass.all_Cases, \
                                        CliticlessPOSConstants.CaseAndMood.all_Cases, \
                                        NominalPOSConstants.SubClass.all_Cases, \
                                        VerbalPOSConstants.Aspect.Perfective + VerbalPOSConstants.Aspect.Imperfective\
                                        );
        
        #جر
        preposition = ProcliticGrammer(ParticlePOSConstants.SubClass.Preposition, \
                                        POSConstants.MainClass.Noun, \
                                        CliticlessPOSConstants.CaseAndMood.GenitiveOrJussive, \
                                        NominalPOSConstants.SubClass.all_Cases);
        
        #قسم - القسم يدخل فقط على الاسم الظاهر - الاسم الظاهر هو كل اسم عدا الضمير
        jurative = ProcliticGrammer(ParticlePOSConstants.SubClass.Jurative, \
                                        POSConstants.MainClass.Noun, \
                                        CliticlessPOSConstants.CaseAndMood.GenitiveOrJussive, \
                                        NominalPOSConstants.SubClass.all_Cases - NominalPOSConstants.SubClass.Nominative_Pronoun - NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun , \
                                        VerbalPOSConstants.Aspect.all_Cases, \
                                        NominalPOSConstants.Definiteness.all_Cases, 
                                        True);
        #نصب الفعل المضارع
        accusative = ProcliticGrammer(ParticlePOSConstants.SubClass.Accusative, \
                                        POSConstants.MainClass.Verb, \
                                        CliticlessPOSConstants.CaseAndMood.AccusativeOrSubjunctive, \
                                        NominalPOSConstants.SubClass.all_Cases, \
                                        VerbalPOSConstants.Aspect.Imperfective);
        #لام الأمر
        imperative = ProcliticGrammer(ParticlePOSConstants.SubClass.Imperative, \
                                        POSConstants.MainClass.Verb, \
                                        CliticlessPOSConstants.CaseAndMood.GenitiveOrJussive, \
                                        NominalPOSConstants.SubClass.all_Cases, \
                                        VerbalPOSConstants.Aspect.Imperfective);
        #لام الإبتداء وتأتي للتوكيد
        emphasisStarter = ProcliticGrammer(ParticlePOSConstants.SubClass.EmphasisStarter, \
                                        POSConstants.MainClass.Noun + POSConstants.MainClass.Verb, \
                                        CliticlessPOSConstants.CaseAndMood.all_Cases, \
                                        NominalPOSConstants.SubClass.all_Cases, \
                                        VerbalPOSConstants.Aspect.Imperfective+VerbalPOSConstants.Aspect.Perfective);
        #سين المستقبل القريب
        forthcomingFuturity = ProcliticGrammer(ParticlePOSConstants.SubClass.ForthcomingFuturity, \
                                        POSConstants.MainClass.Verb, \
                                        CliticlessPOSConstants.CaseAndMood.NominativeOrIndicative, \
                                        NominalPOSConstants.SubClass.all_Cases, \
                                        VerbalPOSConstants.Aspect.Imperfective);
        #ال التعريف
        definite = ProcliticGrammer(ParticlePOSConstants.SubClass.Appendix, \
                                        POSConstants.MainClass.Noun, \
                                        CliticlessPOSConstants.CaseAndMood.all_Cases, \
                                        NominalPOSConstants.SubClass.all_Cases, \
                                        VerbalPOSConstants.Aspect.all_Cases,\
                                        NominalPOSConstants.Definiteness.Definite_by_Itself,\
                                        True);
        #حرف زائد - كالواو في بعض الأحيان
        appendix = ProcliticGrammer(ParticlePOSConstants.SubClass.Appendix);
        
        self.GrammersDict = {};
        self.GrammersDict['ب'] = {};
        self.GrammersDict['ب'][DiacriticsConstants.Kasra] = [preposition, jurative];
        
        
        self.GrammersDict['ك'] = {};
        self.GrammersDict['ك'][DiacriticsConstants.Fatha] = [preposition];
        
        self.GrammersDict['ل'] = {};
        self.GrammersDict['ل'][DiacriticsConstants.Kasra] = [preposition, imperative];
        self.GrammersDict['ل'][DiacriticsConstants.Fatha] = [emphasisStarter, accusative];
        
        self.GrammersDict['س'] = {};
        self.GrammersDict['س'][DiacriticsConstants.Fatha] = [forthcomingFuturity];
        
        
        self.GrammersDict['و'] = {};
        self.GrammersDict['و'][DiacriticsConstants.Fatha] = [conjunction, preposition, jurative, appendix];
        
        self.GrammersDict['ف'] = {};
        self.GrammersDict['ف'][DiacriticsConstants.Fatha] = [conjunction, resumption];
        
        self.GrammersDict['أ'] = {};
        self.GrammersDict['أ'][DiacriticsConstants.Fatha] = [interrogative];
        
        self.GrammersDict['ال'] = {};
        self.GrammersDict['ال'][DiacriticsConstants.Fatha, DiacriticsConstants.Sukoon] = [definite];
        

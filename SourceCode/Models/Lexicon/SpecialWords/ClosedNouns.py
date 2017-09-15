
'''
Created on ١٥‏/٠٦‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from Models.Tagging.POSTags.CliticlessPOS import CliticlessPOS,\
    CliticlessPOSConstants;
from Models.Tagging.POSTags.POS import POSConstants;
from Models.Tagging.POSTags.NominalPOS import NominalPOSConstants, NominalPOS;
from Controllers.Morphology.Entities.UnderivedCliticless import UnderivedCliticless;

class ClosedNoun(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_hUBlgI34Ed-gg8GOK1TmhA
    """
    '''
    Enclosed Nouns
    '''
    
    
    VoweledForm = '';
        
    
    UnvoweledForm = '';
    
    
    PrefixeClasses = ''; 
       
    
    SuffixeClasses = '';
    
    
    POS = NominalPOS();


    def __init__(self, unvoweled, voweled):
        '''
        Constructor
        '''
        self.VoweledForm = voweled;
        self.UnvoweledForm = unvoweled;
        
        self.POS = NominalPOS();
        self.POS.MainClass = POSConstants.MainClass.Noun;
    pass
    


    def AssignFromAlKalilDB(self, prefixeClasses, suffixeClasses,\
        type, definiteness, gender, case, number):
    #سابقاً كان يتم تعبئته من الملف
    #toolwords.xml
    #ولاحقاً أصبح من
    #closednouns.xml
        
        self.PrefixeClasses = prefixeClasses;
        self.SuffixeClasses = suffixeClasses;
        
        if(type == 'اسم شرط'):
            self.POS.SubClass = NominalPOSConstants.SubClass.Conditional_Noun;            
        elif(type == 'ظرف'):
            self.POS.SubClass = NominalPOSConstants.SubClass.Adverb_of_Time;  
            self.POS.SubClass += NominalPOSConstants.SubClass.Adverb_of_Place;            
        elif(type == 'ظرف مكان'):
            self.POS.SubClass = NominalPOSConstants.SubClass.Adverb_of_Place;
        elif(type == 'ظرف زمان'):
            self.POS.SubClass = NominalPOSConstants.SubClass.Adverb_of_Time;         
        elif(type == 'ضمير منفصل'):
            self.POS.SubClass = NominalPOSConstants.SubClass.Nominative_Pronoun;           
        elif(type == 'ضمير نصب'):
            self.POS.SubClass = NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun;           
        elif(type == 'اسم إشارة'):
            self.POS.SubClass = NominalPOSConstants.SubClass.Demonstrative_Noun;           
        elif(type == 'اسم موصول خاص'):
            self.POS.SubClass = NominalPOSConstants.SubClass.Special_Relative_Noun;        
        elif(type == 'اسم موصول مشترك'):
            self.POS.SubClass = NominalPOSConstants.SubClass.Common_Relative_Noun;          
        elif(type == 'كناية'):
            self.POS.SubClass = NominalPOSConstants.SubClass.Allusive;    
        elif(type == 'اسم جامد'):
            self.POS.SubClass = NominalPOSConstants.SubClass.Indeclinable_Noun;
        else:
            print('Warning: This type ['+type+'] is not processed for this Enclosed Noun ['+unvoweledform+']!'); 
        
        
#        definiteness, gender, case, number
        if (definiteness == 'م'):
            self.POS.Definiteness = NominalPOSConstants.Definiteness.Definite_by_Itself;  
        elif (definiteness == 'ن'):
            self.POS.Definiteness = NominalPOSConstants.Definiteness.Indefinite;  
        elif (definiteness == 'ك'):
            self.POS.Definiteness = NominalPOSConstants.Definiteness.all_Cases;  
        else:
            raise Exception('This value for definiteness [' + definiteness + '] is not known!');
        

        if (gender == 'ذ'):
            self.POS.Gender = CliticlessPOSConstants.Gender.Masculine;
        elif (gender == 'ث'):
            self.POS.Gender = CliticlessPOSConstants.Gender.Feminine;
        elif (gender == 'ك'):
            self.POS.Gender = CliticlessPOSConstants.Gender.all_Cases;
        elif (gender == ''):
            self.POS.Gender = CliticlessPOSConstants.Gender.Unprocessed;  
        else:
            raise Exception('This value for gender [' + gender + '] is not known!');
        
        if (case == 'ر'):
            self.POS.CaseAndMood = CliticlessPOSConstants.CaseAndMood.NominativeOrIndicative;  
        elif (case == 'ن'):
            self.POS.CaseAndMood = CliticlessPOSConstants.CaseAndMood.AccusativeOrSubjunctive;  
        elif (case == 'ج'):
            self.POS.CaseAndMood = CliticlessPOSConstants.CaseAndMood.GenitiveOrJussive;  
        elif (case == 'نج'):
            self.POS.CaseAndMood = CliticlessPOSConstants.CaseAndMood.GenitiveOrJussive + \
                CliticlessPOSConstants.CaseAndMood.AccusativeOrSubjunctive;  
        elif (case == 'ك'):
            self.POS.CaseAndMood = CliticlessPOSConstants.CaseAndMood.all_Cases;  
        elif (case == ''):
            self.POS.CaseAndMood = CliticlessPOSConstants.CaseAndMood.Unprocessed; 
        else:
            raise Exception('This value for case [' + case + '] is not known!');
        
        

        if (number == '1'):
            self.POS.Number = CliticlessPOSConstants.Number.Singular;
        elif (number == '2'):
            self.POS.Number = CliticlessPOSConstants.Number.Dual;
        elif (number == '3'):
            self.POS.Number = CliticlessPOSConstants.Number.Plural;
        elif (number == 'ك'):
            self.POS.Number = CliticlessPOSConstants.Number.all_Cases;
        elif (number == ''):
            self.POS.Number = CliticlessPOSConstants.Number.Unprocessed;  
        else:
            raise Exception('This value for number [' + number + '] is not known!');
    pass

    def ReturnAsUnderivedCliticless(self):
        underivedCliticless = UnderivedCliticless(self.UnvoweledForm, self.VoweledForm);
        underivedCliticless.POS = self.POS.Clone();
        
        return underivedCliticless;
    pass

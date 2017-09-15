from Lexicon.RootAndPatterns.VoweledPattern import VoweledPattern


'''
Created on ٢٨‏/٠٤‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Models.Lexicon.RootAndPatterns.Root import *;
from Models.Lexicon.RootAndPatterns.VoweledPattern import *;
from Models.Tagging.POSTags.VerbalPOS import *;


class VoweledVerbalPattern(VoweledPattern):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qz4WZ435Ed-gg8GOK1TmhA
    """
    '''
    classdocs
    '''
    
    
    def __init__(self, id, voweledForm, canonicForm):
        '''
        Constructor
        '''
        self.ID = id;
        self.VoweledForm = voweledForm;
        self.CanonicForm = canonicForm;
        
        self.POS = VerbalPOS();
        self.POS.MainClass = VerbalPOSConstants.MainClass.Verb;
        
        
        pass

    def AssignFromAlKhalilDB(self, type, cas, ncg, aug, trans):
        if type == "مم":
#            "فعل ماض مبني للمعلوم"
            self.POS.Aspect = VerbalPOSConstants.Aspect.Perfective;
            self.POS.Activeness  = VerbalPOSConstants.Activeness.Active;
        elif type == "مج":
#            "فعل ماض مبني للمجهول"
            self.POS.Aspect = VerbalPOSConstants.Aspect.Perfective;
            self.POS.Activeness  = VerbalPOSConstants.Activeness.Passive;
        elif type == "ضم":
#            "فعل مضارع مبني للمعلوم"
            self.POS.Aspect = VerbalPOSConstants.Aspect.Imperfective;
            self.POS.Activeness  = VerbalPOSConstants.Activeness.Active;
            self.POS.Asserted = VerbalPOSConstants.Asserted.Unasserted;
        elif type == "ضءم":
#            "فعل مضارع مؤكد مبني للمعلوم"
            self.POS.Aspect = VerbalPOSConstants.Aspect.Imperfective;
            self.POS.Activeness  = VerbalPOSConstants.Activeness.Active;
            self.POS.Asserted = VerbalPOSConstants.Asserted.Asserted;
        elif type == "ضج":
#            "فعل مضارع مبني للمجهول"
            self.POS.Aspect = VerbalPOSConstants.Aspect.Imperfective;
            self.POS.Activeness  = VerbalPOSConstants.Activeness.Passive;
            self.POS.Asserted = VerbalPOSConstants.Asserted.Unasserted;
        elif type == "ضءج":
#            "فعل مضارع مؤكد مبني للمجهول"
            self.POS.Aspect = VerbalPOSConstants.Aspect.Imperfective;
            self.POS.Activeness  = VerbalPOSConstants.Activeness.Passive;
            self.POS.Asserted = VerbalPOSConstants.Asserted.Asserted;
        elif type == "أ":
#            "فعل أمر"
            self.POS.Aspect = VerbalPOSConstants.Aspect.Imperative;
            self.POS.Asserted = VerbalPOSConstants.Asserted.Unasserted;
        elif type == "أء":
#            "فعل أمر مؤكد"
            self.POS.Aspect = VerbalPOSConstants.Aspect.Imperative;
            self.POS.Asserted = VerbalPOSConstants.Asserted.Asserted;            
    
        elif type == "#":
#            حميع الحالات
            self.POS.Aspect = VerbalPOSConstants.Aspect.all_Cases;
            self.POS.Activeness  = VerbalPOSConstants.Activeness.all_Cases;
            self.POS.Asserted = VerbalPOSConstants.Asserted.all_Cases;
        else:
            raise Exception('This [type] for Verbal Pattern is unknown!, ['+str(type)+']');
        
        
        if cas == "ر":
#           "مرفوع"
            self.POS.CaseAndMood = VerbalPOSConstants.CaseAndMood.NominativeOrIndicative; 
        elif cas == "ن":
#            "منصوب"
            self.POS.CaseAndMood = VerbalPOSConstants.CaseAndMood.AccusativeOrSubjunctive;  
        elif cas == "ج":
#            "مجزوم" 
            self.POS.CaseAndMood = VerbalPOSConstants.CaseAndMood.GenitiveOrJussive;  
        elif cas == "":  
#            حميع الحالات       
            if(self.POS.Aspect == VerbalPOSConstants.Aspect.Imperative or \
               self.POS.Aspect == VerbalPOSConstants.Aspect.Perfective):
                self.POS.CaseAndMood = VerbalPOSConstants.CaseAndMood.Inapplicable; 
            else:
                self.POS.CaseAndMood = VerbalPOSConstants.CaseAndMood.Unprocessed; 
#        elif cas == "#":  
##            حميع الحالات       
#            self.POS.CaseAndMood = VerbalPOSConstants.CaseAndMood.all_Cases; 
        else:
            raise Exception('This [cas] for Verbal Pattern is unknown!, ['+cas+']');


            
        if ncg.isnumeric() or (ncg[0] == '-' and ncg[1:].isnumeric()):
            ncg = int(ncg);
        if ncg == 1:
#            "مسند إلى المتكلم أنا"
            self.POS.Number = VerbalPOSConstants.Number.Singular;
            self.POS.Gender = VerbalPOSConstants.Gender.all_Cases;
            self.POS.Person = VerbalPOSConstants.Person.First_Person;
        elif ncg == 2:
#            "مسند إلى المتكلمين (نحن)"
            self.POS.Number = VerbalPOSConstants.Number.Plural;
            self.POS.Gender = VerbalPOSConstants.Gender.all_Cases;
            self.POS.Person = VerbalPOSConstants.Person.First_Person;
        elif ncg == 3:
#            "مسند إلى المخاطَب أنت"
            self.POS.Number = VerbalPOSConstants.Number.Singular;
            self.POS.Gender = VerbalPOSConstants.Gender.Masculine;
            self.POS.Person = VerbalPOSConstants.Person.Second_Person;
        elif ncg == 4:
#            "مسند إلى المخاطبة (أنتِ)"
            self.POS.Number = VerbalPOSConstants.Number.Singular;
            self.POS.Gender = VerbalPOSConstants.Gender.Feminine;
            self.POS.Person = VerbalPOSConstants.Person.Second_Person;
        elif ncg == 5:
#            "مسند إلى المخاطَبَين (أنتما)"
            self.POS.Number = VerbalPOSConstants.Number.Dual;
            self.POS.Gender = VerbalPOSConstants.Gender.Masculine;
            self.POS.Person = VerbalPOSConstants.Person.Second_Person;
        elif ncg == 6:
#            "مسند إلى المخاطبين (أنتم)"
            self.POS.Number = VerbalPOSConstants.Number.Plural;
            self.POS.Gender = VerbalPOSConstants.Gender.Masculine;
            self.POS.Person = VerbalPOSConstants.Person.Second_Person;
        elif ncg == 7:
#            "مسند إلى المخاطَبات (أنتن)"
            self.POS.Number = VerbalPOSConstants.Number.Plural;
            self.POS.Gender = VerbalPOSConstants.Gender.Feminine;
            self.POS.Person = VerbalPOSConstants.Person.Second_Person;
        elif ncg == 8:
#            "مسند إلى الغائب (هو)"
            self.POS.Number = VerbalPOSConstants.Number.Singular;
            self.POS.Gender = VerbalPOSConstants.Gender.Masculine;
            self.POS.Person = VerbalPOSConstants.Person.Third_Person;
        elif ncg == 9:
#            "مسند إلى الغائبة (هي)"
            self.POS.Number = VerbalPOSConstants.Number.Singular;
            self.POS.Gender = VerbalPOSConstants.Gender.Feminine;
            self.POS.Person = VerbalPOSConstants.Person.Third_Person;
        elif ncg == 10:
#            "مسند إلى الغائبَين (هما)"
            self.POS.Number = VerbalPOSConstants.Number.Dual;
            self.POS.Gender = VerbalPOSConstants.Gender.Masculine;
            self.POS.Person = VerbalPOSConstants.Person.Third_Person;
        elif ncg == 11:
#            "مسند إلى الغائبتين (هما)"
            self.POS.Number = VerbalPOSConstants.Number.Dual;
            self.POS.Gender = VerbalPOSConstants.Gender.Feminine;
            self.POS.Person = VerbalPOSConstants.Person.Third_Person;
        elif ncg == 12:
#            "مسند إلى الغائبين (هم)"
            self.POS.Number = VerbalPOSConstants.Number.Plural;
            self.POS.Gender = VerbalPOSConstants.Gender.Masculine;
            self.POS.Person = VerbalPOSConstants.Person.Third_Person;
        elif ncg == 13:
#            "مسند إلى الغائبات (هن)"
            self.POS.Number = VerbalPOSConstants.Number.Singular;
            self.POS.Gender = VerbalPOSConstants.Gender.Feminine;
            self.POS.Person = VerbalPOSConstants.Person.Third_Person;
        elif ncg == "#":
            self.POS.Number = VerbalPOSConstants.Number.all_Cases;
            self.POS.Gender = VerbalPOSConstants.Gender.all_Cases;
            self.POS.Person = VerbalPOSConstants.CaseAndMood.all_Cases;
        else:
            raise Exception('This [ncg] for Verbal Pattern is unknown!, ['+str(ncg)+']');
                        
        
#        المجرّد والمزيد (aug):
        if (aug == "جر"):
#        "جر" => "مجرد"
            self.POS.IsAugmented = False;
        elif (aug == "زي"):
#        "زي" => "مزيد"
            self.POS.IsAugmented = True;
        elif (aug == "#"):
            self.POS.IsAugmented = None;
        else:
            raise Exception('This [aug] for Verbal Pattern is unknown!, ['+str(aug)+']');
            

#        اللزوم والتعدي (trans):
        if (trans == "ل"):
#            "ل" => "لازم"
            self.POS.Transitive = VerbalPOSConstants.Transitive.Intransitive;
        elif (trans == "م"):
#            "م" => "متعد"
            self.POS.Transitive = 0;            
            self.POS.Transitive += VerbalPOSConstants.Transitive.Transitive_for_1;
            self.POS.Transitive += VerbalPOSConstants.Transitive.Transitive_for_2;
            self.POS.Transitive += VerbalPOSConstants.Transitive.Transitive_for_3;
        elif (trans == "ك"):
#            "ك" => "لازم ومتعد"
            self.POS.Transitive = VerbalPOSConstants.Transitive.all_Cases;   
        else:
            raise Exception('This [trans] for Verbal Pattern is unknown!, ['+str(trans)+']');

        self.POS.Perfectness = VerbalPOSConstants.Perfectness.Unprocessed;
        pass
    

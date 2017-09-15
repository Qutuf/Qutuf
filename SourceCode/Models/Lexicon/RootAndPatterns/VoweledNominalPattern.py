
'''
Created on ٢٨‏/٠٤‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Models.Lexicon.RootAndPatterns.Root import *;
from Models.Lexicon.RootAndPatterns.VoweledPattern import VoweledPattern;
from Models.Tagging.POSTags.NominalPOS import NominalPOSConstants, NominalPOS;

class VoweledNominalPattern:
    """
     # PyUML: Do not remove this line! # XMI_ID:_qz4WI435Ed-gg8GOK1TmhA
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
        
        self.POS = NominalPOS();
        self.POS.MainClass = NominalPOSConstants.MainClass.Noun;
        
        pass
        
    def AssignFromAlKhalilDB(self, type, cas, ncg):
        if type == "":
#            "غير معالج"
            self.POS.SubClass = NominalPOSConstants.SubClass.Unprocessed;
        elif type == "فا":
#            "اسم فاعل"
            self.POS.SubClass = NominalPOSConstants.SubClass.Active_Participle;
        elif type == "مف" :
#             "اسم مفعول"
            self.POS.SubClass = NominalPOSConstants.SubClass.Passive_Participle;
        elif type == "مفا":
#            "مبالغة اسم الفاعل"
            self.POS.SubClass = NominalPOSConstants.SubClass.Exaggeration_Active_Participle;
        elif type == "آ":
#            "اسم آلة"
            self.POS.SubClass = NominalPOSConstants.SubClass.Instrumental_Noun;
        elif type == "زمك":
#            "اسم زمان ومكان"
            self.POS.SubClass = NominalPOSConstants.SubClass.Noun_of_Place;
            self.POS.SubClass += NominalPOSConstants.SubClass.Noun_of_Time;
        elif type == "فض" :
#            "اسم تفضيل"
            self.POS.SubClass = NominalPOSConstants.SubClass.Elative_Noun;
        elif type == "وش":
#            "صفة مشبهة"
            self.POS.SubClass = NominalPOSConstants.SubClass.Assimilate_Adjective;
        elif type == "صأ":
#            "مصدر أصلي"
            self.POS.SubClass = NominalPOSConstants.SubClass.Gerund;
        elif type == "صم":
#            "مصدر ميمي"
            self.POS.SubClass = NominalPOSConstants.SubClass.Meem_Gerund;
        elif type == "صه":
#            "مصدر هيئة"
            self.POS.SubClass = NominalPOSConstants.SubClass.Quality_Gerund;
        elif type == "صر":
#            "مصدر مرة"
            self.POS.SubClass = NominalPOSConstants.SubClass.Nomen_Vicis;
        elif type == "جا":
#            "اسم جامد"
            self.POS.SubClass = NominalPOSConstants.SubClass.Indeclinable_Noun;
        elif type == "#":
            self.POS.SubClass = NominalPOSConstants.SubClass.all_Cases; 
#            حميع الحالات
        else:
            raise Exception('This [type] for Nominal Pattern id: ('+str(self.ID)+') is unknown!, ['+type+']');
        
        if cas == "":
#            غير معالج
            self.POS.Definiteness = NominalPOSConstants.Definiteness.Unprocessed; 
        elif cas == "إض":
#            معرّف Definite 
            self.POS.Definiteness = NominalPOSConstants.Definiteness.Definite_by_Itself + \
                                    NominalPOSConstants.Definiteness.Definite_by_Another; 
        elif cas == "نك":
#            نكرة Indefinite 
            self.POS.Definiteness = NominalPOSConstants.Definiteness.Indefinite; 
        elif cas == "#":
#            حميع الحالات
            self.POS.Definiteness = NominalPOSConstants.Definiteness.all_Cases; 
        else:
            raise Exception('This [cas] for Nominal Pattern is unknown!, ['+cas+']');
                        
            
        if ncg.isnumeric() or (ncg[0] == '-' and ncg[1:].isnumeric()):
            ncg = int(ncg);
        if ncg == 0:
#            0 => "مفرد مذكر"
            self.POS.Number = NominalPOSConstants.Number.Singular;
            self.POS.Gender = NominalPOSConstants.Gender.Masculine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.all_Cases;
        elif ncg == -1:
#            -1 => "مفرد مؤنث"
            self.POS.Number = NominalPOSConstants.Number.Singular;
            self.POS.Gender = NominalPOSConstants.Gender.Feminine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.all_Cases;
        elif ncg == -2:
#            -2 => "جمع مذكر"
            self.POS.Number = NominalPOSConstants.Number.Plural;
            self.POS.Gender = NominalPOSConstants.Gender.Masculine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.all_Cases;
        elif ncg == -3:
#            -3 => "جمع مؤنث"
            self.POS.Number = NominalPOSConstants.Number.Plural;
            self.POS.Gender = NominalPOSConstants.Gender.Feminine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.all_Cases;
        elif ncg == 1:
#            1 => "مفرد مذكر مرفوع"
            self.POS.Number = NominalPOSConstants.Number.Singular;
            self.POS.Gender = NominalPOSConstants.Gender.Masculine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.NominativeOrIndicative;
        elif ncg == 2:
#            2 => "مفرد مؤنث مرفوع"
            self.POS.Number = NominalPOSConstants.Number.Singular;
            self.POS.Gender = NominalPOSConstants.Gender.Feminine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.NominativeOrIndicative;
        elif ncg == 3:
#            3 => "مثنى مذكر مرفوع"
            self.POS.Number = NominalPOSConstants.Number.Dual;
            self.POS.Gender = NominalPOSConstants.Gender.Masculine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.NominativeOrIndicative;
        elif ncg == 4:
#            4 => "مثنى مؤنث مرفوع"
            self.POS.Number = NominalPOSConstants.Number.Dual;
            self.POS.Gender = NominalPOSConstants.Gender.Feminine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.NominativeOrIndicative;
        elif ncg == 5:
#            5 => "جمع مذكر مرفوع"
            self.POS.Number = NominalPOSConstants.Number.Plural;
            self.POS.Gender = NominalPOSConstants.Gender.Masculine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.NominativeOrIndicative;
        elif ncg == 6:
#            6 => "جمع مؤنث مرفوع"
            self.POS.Number = NominalPOSConstants.Number.Plural;
            self.POS.Gender = NominalPOSConstants.Gender.Feminine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.NominativeOrIndicative;
        elif ncg == 7:
#            7 => "مفرد مذكر منصوب"
            self.POS.Number = NominalPOSConstants.Number.Singular;
            self.POS.Gender = NominalPOSConstants.Gender.Masculine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.AccusativeOrSubjunctive;
        elif ncg == 8:
#            8 => "مفرد مؤنث منصوب"
            self.POS.Number = NominalPOSConstants.Number.Singular;
            self.POS.Gender = NominalPOSConstants.Gender.Feminine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.AccusativeOrSubjunctive;
        elif ncg == 9:
#            9 => "مثنى مذكر منصوب"
            self.POS.Number = NominalPOSConstants.Number.Dual;
            self.POS.Gender = NominalPOSConstants.Gender.Masculine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.AccusativeOrSubjunctive;
        elif ncg == 10:
#            10 => "مثنى مؤنث منصوب"
            self.POS.Number = NominalPOSConstants.Number.Dual;
            self.POS.Gender = NominalPOSConstants.Gender.Feminine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.AccusativeOrSubjunctive;
        elif ncg == 11:
#            11 => "جمع مذكر منصوب"
            self.POS.Number = NominalPOSConstants.Number.Plural;
            self.POS.Gender = NominalPOSConstants.Gender.Masculine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.AccusativeOrSubjunctive;
        elif ncg == 12:
#            12 => "جمع مؤنث منصوب"
            self.POS.Number = NominalPOSConstants.Number.Plural;
            self.POS.Gender = NominalPOSConstants.Gender.Feminine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.AccusativeOrSubjunctive;
        elif ncg == 13:
#            13 => "مفرد مذكر مجرور"
            self.POS.Number = NominalPOSConstants.Number.Singular;
            self.POS.Gender = NominalPOSConstants.Gender.Masculine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.GenitiveOrJussive;
        elif ncg == 14:
#            14 => "مفرد مؤنث مجرور"
            self.POS.Number = NominalPOSConstants.Number.Singular;
            self.POS.Gender = NominalPOSConstants.Gender.Feminine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.GenitiveOrJussive;
        elif ncg == 15:
#            15 => "مثنى مذكر مجرور"
            self.POS.Number = NominalPOSConstants.Number.Dual;
            self.POS.Gender = NominalPOSConstants.Gender.Masculine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.GenitiveOrJussive;
        elif ncg == 16:
#            16 => "مثنى مؤنث مجرور"
            self.POS.Number = NominalPOSConstants.Number.Dual;
            self.POS.Gender = NominalPOSConstants.Gender.Feminine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.GenitiveOrJussive;
        elif ncg == 17:
#            17 => "جمع مذكر مجرور"
            self.POS.Number = NominalPOSConstants.Number.Plural;
            self.POS.Gender = NominalPOSConstants.Gender.Masculine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.GenitiveOrJussive;
        elif ncg == 18:
#            18 => "جمع مؤنث مجرور"
            self.POS.Number = NominalPOSConstants.Number.Plural;
            self.POS.Gender = NominalPOSConstants.Gender.Feminine;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.GenitiveOrJussive;
        elif ncg == "#":
            self.POS.Number = NominalPOSConstants.Number.all_Cases;
            self.POS.Gender = NominalPOSConstants.Gender.all_Cases;
            self.POS.CaseAndMood = NominalPOSConstants.CaseAndMood.all_Cases;
        else:
            raise Exception('This [ncg] for Nominal Pattern is unknown!, ['+str(ncg)+']');
                        
        
        self.POS.Substantivness = NominalPOSConstants.Substantivness.Substantive;
        
        pass
    

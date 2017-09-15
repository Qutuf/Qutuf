from Tagging.POSTags.CliticlessPOS import CliticlessPOSConstants
from Tagging.POSTags.CliticlessPOS import CliticlessPOS


'''
Created on ٢٩‏/٠٥‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Models.Tagging.POSTags.CliticlessPOS import *;
from Models.Tagging.POSTags.POS import *;

class NominalPOSConstants(CliticlessPOSConstants):
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0BgY435Ed-gg8GOK1TmhA
    """
    class SubClass:
        
        #غير معالج = 0
        Unprocessed = 0;
        #اسم فاعل = 1 
        Active_Participle = 1;
        #اسم مفعول = 2 
        Passive_Participle = 2;
        #مبالغة اسم الفاعل = 4 
        Exaggeration_Active_Participle  = 4;
        #اسم آلة = 8 
        Instrumental_Noun = 8;
        #اسم مكان = 16 
        Noun_of_Place = 16;
        #اسم زمان = 16 
        Noun_of_Time = 32;
        #اسم تفضيل = 32 
        Elative_Noun = 64;
        #صفة مشبهة = 64 
        Assimilate_Adjective = 128;
        #مصدر أصلي = 128 
        Gerund = 256;
        #مصدر ميمي = 256 
        Meem_Gerund = 512;
        #مصدر هيئة = 512 
        Quality_Gerund = 1024;
        #مصدر مرة = 1024 
        Nomen_Vicis = 2048;
        #اسم جامد, اسم جنس  = 2048 
        Indeclinable_Noun = 4096;
        #اسم علم = 4096 
        Proper_Noun = 8192;
        
        #اسم شرط = 8192 
        Conditional_Noun = 16384;
        #ظرف = 16384 
        Adverb_of_Time = 32768;
        #ظرف = 16384 
        Adverb_of_Place = 65536;
        #ضمير رفع = 32768 
        Nominative_Pronoun = 131072;
        #ضمير نصب وجر = 65536 
        Accusative_or_Genitive_Pronoun = 262144;
        #اسم إشارة = 131072 
        Demonstrative_Noun = 524288;
        #اسم موصول خاص = 262144 
        Special_Relative_Noun = 1048576;
        #اسم موصول مشترك = 524288 
        Common_Relative_Noun = 2097152;
        #كناية = 524288 
        Allusive = 4194304;
        
        #جميع الحالات = 8191
        all_Cases = 8388607;
        
        #عدد البتات اللازمة: 12
        Number_of_bits = 23;

    class Definiteness:
        #Definiteness التعريف والتنكير:
        #غير معالج = 0 
        Unprocessed = 0;
        #معرّف بنفسه = 1 
        Definite_by_Itself = 1;
        #معرّف بالإضافة = 1 
        Definite_by_Another = 2;
        #نكرة = 2 
        Indefinite = 4;
        #حميع الحالات = 3
        all_Cases = 7;
        
        #عدد البتات اللازمة: 2
        Number_of_bits = 3;

    class Substantivness:
        #غير معالجة
        Unprocessed = 0;
        #مضمرة - محذوفة - مقدّرة
        Hidden = 1;
        #ظاهرة
        Substantive = 2;
        #جميع الاحتمالات
        all_Cases = 3;


class NominalPOS(CliticlessPOS):
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0BgZI35Ed-gg8GOK1TmhA
    """
    '''
    Nominal POS
    '''
    
    SubClass = 0;
    '''
    القيم الممكنة
        غير معالج = 0
        اسم فاعل = 1 Active_Participle
        اسم مفعول = 2 Passive_Participle
        مبالغة اسم الفاعل = 4 Exaggeration_Active_Participle
        اسم آلة = 8 Instrumental_Noun
        اسم زمان أو مكان = 16 Noun_of_Time_and_Place 
        اسم تفضيل = 32 Elative_Noun
        صفة مشبهة = 64 Assimilate_Adjective
        مصدر أصلي = 128 Gerund
        مصدر ميمي = 256 Meem_Gerund
        مصدر هيئة = 512 Quality_Gerund
        مصدر مرة = 1024 Nomen_Vicis
        اسم جامد = 2048 Indeclinable_Noun
        
        
        جميع الحالات = 4095
    
    عدد البتات اللازمة: 12 أي فقط ثلاثة أرباع ما يلزم لمحرف واحد من نوع 
    UTF-8
    
    يمكن تعبئتها من الخليل
    '''
    
    Definiteness = 0;
    '''
    غير معالج = 0 
    معرّف  = 1 Definite 
    نكرة = 2 Indefinite 
    حميع الحالات = 3
    
    عدد البتات اللازمة: 2
    
    يمكن تعبئتها من الخليل
    '''
    
    '''
    الإظهار - الإضمار
    '''
    Substantivness = 0;
    
    def __init__(self):
        '''
        Constructor
        '''
        self.MainClass = POSConstants.MainClass.Noun;
        self.Substantivness = NominalPOSConstants.Substantivness.Substantive; 
    pass

    def WriteSubClassArabicText(self, stringStream):
        stringList = [];
        if(self.SubClass == NominalPOSConstants.SubClass.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.SubClass & NominalPOSConstants.SubClass.Active_Participle != 0):
                stringList.append('اسم فاعل');
            if(self.SubClass & NominalPOSConstants.SubClass.Passive_Participle != 0):
                stringList.append('اسم مفعول');
            if(self.SubClass & NominalPOSConstants.SubClass.Exaggeration_Active_Participle != 0):
                stringList.append('مبالغة اسم الفاعل');
            if(self.SubClass & NominalPOSConstants.SubClass.Instrumental_Noun != 0):
                stringList.append('اسم آلة');
            if(self.SubClass & NominalPOSConstants.SubClass.Noun_of_Place != 0):
                stringList.append('اسم مكان');
            if(self.SubClass & NominalPOSConstants.SubClass.Noun_of_Time != 0):
                stringList.append('اسم زمان');
            if(self.SubClass & NominalPOSConstants.SubClass.Elative_Noun != 0):
                stringList.append('اسم تفضيل');
            if(self.SubClass & NominalPOSConstants.SubClass.Assimilate_Adjective != 0):
                stringList.append('صفة مشبهة');
            if(self.SubClass & NominalPOSConstants.SubClass.Gerund != 0):
                stringList.append('مصدر أصلي');
            if(self.SubClass & NominalPOSConstants.SubClass.Meem_Gerund != 0):
                stringList.append('مصدر ميمي');
            if(self.SubClass & NominalPOSConstants.SubClass.Quality_Gerund != 0):
                stringList.append('مصدر هيئة');
            if(self.SubClass & NominalPOSConstants.SubClass.Nomen_Vicis != 0):
                stringList.append('مصدر مرة');
            if(self.SubClass & NominalPOSConstants.SubClass.Indeclinable_Noun != 0):
                stringList.append('اسم جامد');
            if(self.SubClass & NominalPOSConstants.SubClass.Proper_Noun != 0):
                stringList.append('اسم علم');
            if(self.SubClass & NominalPOSConstants.SubClass.Conditional_Noun != 0):
                stringList.append('اسم شرط');
                
            if(self.SubClass & NominalPOSConstants.SubClass.Adverb_of_Time != 0 \
               and self.SubClass & NominalPOSConstants.SubClass.Adverb_of_Place != 0):
                stringList.append('ظرف');
            else:
                if(self.SubClass & NominalPOSConstants.SubClass.Adverb_of_Time != 0):
                    stringList.append('ظرف زمان');
                elif(self.SubClass & NominalPOSConstants.SubClass.Adverb_of_Place != 0):
                    stringList.append('ظرف مكان');
            if(self.SubClass & NominalPOSConstants.SubClass.Nominative_Pronoun != 0):
                stringList.append('ضمير رفع');
            if(self.SubClass & NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun != 0):
                stringList.append('ضمير نصب');
            if(self.SubClass & NominalPOSConstants.SubClass.Demonstrative_Noun != 0):
                stringList.append('اسم إشارة');
            if(self.SubClass & NominalPOSConstants.SubClass.Special_Relative_Noun != 0):
                stringList.append('اسم موصول خاص');
            if(self.SubClass & NominalPOSConstants.SubClass.Common_Relative_Noun != 0):
                stringList.append('اسم موصول مشترك');
            if(self.SubClass & NominalPOSConstants.SubClass.Allusive != 0):
                stringList.append('كناية');
                
        stringStream.write(' أو '.join(stringList));
    pass

    def WriteSubClassTag(self, stringStream):
        stringList = [];
        if(self.SubClass == NominalPOSConstants.SubClass.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.SubClass & NominalPOSConstants.SubClass.Active_Participle != 0):
                stringList.append('u');#اسم فاعل
            if(self.SubClass & NominalPOSConstants.SubClass.Passive_Participle != 0):
                stringList.append('k');#اسم مفعول
            if(self.SubClass & NominalPOSConstants.SubClass.Exaggeration_Active_Participle != 0):
                stringList.append('w');#مبالغة اسم الفاعل
            if(self.SubClass & NominalPOSConstants.SubClass.Instrumental_Noun != 0):
                stringList.append('z');#اسم آلة
            if(self.SubClass & NominalPOSConstants.SubClass.Noun_of_Place != 0):
                stringList.append('l');#اسم مكان
            if(self.SubClass & NominalPOSConstants.SubClass.Noun_of_Time != 0):
                stringList.append('t');#اسم زمان
            if(self.SubClass & NominalPOSConstants.SubClass.Elative_Noun != 0):
                stringList.append('^');#صيغة تفضيل
            if(self.SubClass & NominalPOSConstants.SubClass.Assimilate_Adjective != 0):
                stringList.append('j');#صفة مشبهة
            if(self.SubClass & NominalPOSConstants.SubClass.Gerund != 0):
                stringList.append('g');#مصدر أصلي
            if(self.SubClass & NominalPOSConstants.SubClass.Meem_Gerund != 0):
                stringList.append('m');#مصدر ميمي
            if(self.SubClass & NominalPOSConstants.SubClass.Quality_Gerund != 0):
                stringList.append('s');#مصدر هيئة
            if(self.SubClass & NominalPOSConstants.SubClass.Nomen_Vicis != 0):
                stringList.append('o');#مصدر مرة
            if(self.SubClass & NominalPOSConstants.SubClass.Indeclinable_Noun != 0):
                stringList.append('q');#اسم جامد, اسم جنس
            if(self.SubClass & NominalPOSConstants.SubClass.Proper_Noun != 0):
                stringList.append('n');#اسم علم
            if(self.SubClass & NominalPOSConstants.SubClass.Conditional_Noun != 0):
                stringList.append('h');#اسم شرط
            if(self.SubClass & NominalPOSConstants.SubClass.Adverb_of_Time != 0):
                stringList.append('v');#ظرف زمان
            if(self.SubClass & NominalPOSConstants.SubClass.Adverb_of_Place != 0):
                stringList.append('%');#ظرف مكان
            if(self.SubClass & NominalPOSConstants.SubClass.Nominative_Pronoun != 0):
                stringList.append('p');#ضمير رفع
            if(self.SubClass & NominalPOSConstants.SubClass.Accusative_or_Genitive_Pronoun != 0):
                stringList.append('@');#ضمير نصب
            if(self.SubClass & NominalPOSConstants.SubClass.Demonstrative_Noun != 0):
                stringList.append('d');#اسم إشارة
            if(self.SubClass & NominalPOSConstants.SubClass.Special_Relative_Noun != 0):
                stringList.append('r');#اسم موصول خاص
            if(self.SubClass & NominalPOSConstants.SubClass.Common_Relative_Noun != 0):
                stringList.append('c');#اسم موصول مشترك
            if(self.SubClass & NominalPOSConstants.SubClass.Allusive != 0):
                stringList.append('a');#كناية
                
        stringStream.write(''.join(stringList));
    pass

    def WriteDefinitenessArabicText(self, stringStream):
        stringList = [];
        if(self.Definiteness == NominalPOSConstants.Definiteness.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Definiteness & NominalPOSConstants.Definiteness.Definite_by_Itself != 0):
                stringList.append('معرفة');
            if(self.Definiteness & NominalPOSConstants.Definiteness.Definite_by_Another != 0):
                stringList.append('معرَّف بالإضافة');
            if(self.Definiteness & NominalPOSConstants.Definiteness.Indefinite != 0):
                stringList.append('نكرة');
                
        stringStream.write(' أو '.join(stringList));
    pass

    def WriteDefinitenessTag(self, stringStream):
        stringList = [];
        if(self.Definiteness == NominalPOSConstants.Definiteness.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Definiteness & NominalPOSConstants.Definiteness.Definite_by_Itself != 0):
                stringList.append('d');
            if(self.Definiteness & NominalPOSConstants.Definiteness.Definite_by_Another != 0):
                stringList.append('a');
            if(self.Definiteness & NominalPOSConstants.Definiteness.Indefinite != 0):
                stringList.append('i');
                
        stringStream.write(''.join(stringList));
    pass
    def WriteSubstantivnessText(self, stringStream):
        stringList = [];
        if(self.Substantivness == NominalPOSConstants.Substantivness.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Substantivness & NominalPOSConstants.Substantivness.Hidden != 0):
                stringList.append('مضمر/مقدّر');
            if(self.Substantivness & NominalPOSConstants.Substantivness.Substantive != 0):
                stringList.append('ظاهر');
        
                
        stringStream.write(' أو '.join(stringList));
    pass

    def WriteArabicText(self, stringStream):
        CliticlessPOS.WriteArabicText(self, stringStream);
        stringStream.write(', ');
        self.WriteSubClassArabicText(stringStream);
        stringStream.write(', ');
        self.WriteDefinitenessArabicText(stringStream);
        stringStream.write(', ');
        self.WriteSubstantivnessText(stringStream);
    pass
    
    
    def WriteTag(self, stringStream):
        CliticlessPOS.WriteTag(self, stringStream);
        stringStream.write(',');
        self.WriteSubClassTag(stringStream);
        stringStream.write(',');
        self.WriteDefinitenessTag(stringStream);
    pass
    
    
    def Clone(self):
        pos = NominalPOS();
        pos.BinaryTag = self.BinaryTag;
        pos.MainClass = self.MainClass;
        
        pos.Gender = self.Gender;
        pos.Number = self.Number;
        pos.CaseAndMood = self.CaseAndMood;
        
        pos.SubClass = self.SubClass
        pos.Definiteness = self.Definiteness
        
        return pos;
    pass


#import io;
#output = io.StringIO()
#
#pos = NominalPOS();
#pos.SubClass = NominalPOSConstants.SubClass.Elative_Noun;
#pos.Definiteness = NominalPOSConstants.Definiteness.Definite;
#pos.WriteArabicText(output);
#print(output.getvalue())

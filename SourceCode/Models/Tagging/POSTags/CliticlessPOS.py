from Tagging.POSTags.POS import POSConstants
from Tagging.POSTags.POS import POS


'''
Created on ٢٩‏/٠٥‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Models.Tagging.POSTags.POS import *;

class CliticlessPOSConstants(POSConstants):
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0BgLY35Ed-gg8GOK1TmhA
    """
    class Gender:
        #غير معالج = 0,
        Unprocessed = 0; 
        #مذكّر  = 1, 
        Feminine = 1;
        #مؤنّث = 2, 
        Masculine = 2;
        #حميع الحالات = 3
        all_Cases = 3;
        
        #عدد البتات اللازمة: 2
        Number_of_bits = 2;
                
    class Number:
        #غير معالج = 0, 
        Unprocessed = 0;
        #مفرد = 1, 
        Singular = 1;
        #مثنى  = 2, 
        Dual = 2;
        #جمع = 4, 
        Plural = 4;
        #حميع الحالات = 7
        all_Cases = 7;
        
        #عدد البتات اللازمة: 3
        Number_of_bits = 3;
        
    class CaseAndMood:
        #غير معالج = 0, 
        Unprocessed = 0;
        #مرفوع = 1, 
        Inapplicable = 1;
        #مرفوع = 1, 
        NominativeOrIndicative = 2;
        #منصوب  = 2, 
        AccusativeOrSubjunctive = 4;
        #مجرور أو مجزوم = 4,
        GenitiveOrJussive = 8; 
        #حميع الحالات = 7
        all_Cases = 15;
        
        #عدد البتات اللازمة: 3
        Number_of_bits = 4;

    class Person:
        #Person الشخص المتكلّم أو المخاطب:
        
        #غير معالج = 0, 
        Unprocessed = 0;
        #المتكلّم = 1,  
        First_Person = 1;
        #المخاطب = 2, 
        Second_Person = 2; 
        #الغائب = 4, 
        Third_Person = 4; 
        #حميع الحالات = 7 
        all_Cases = 7;
        
        #عدد البتات اللازمة: 3 
        Number_of_bits = 3;
        

class CliticlessPOS(POS):
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0BgLo35Ed-gg8GOK1TmhA
    """
    '''
    classdocs
    '''


    Gender = 0;
    '''
    غير معالج = 0, 
    مذكّر  = 1, 
    مؤنّث = 2, 
    حميع الحالات = 3

    عدد البتات اللازمة: 2
    
    يمكن تعبئتها من الخليل
    '''
    
    Number = 0;
    '''
    غير معالج = 0, 
    مفرد = 1, 
    مثنى  = 2, 
    جمع = 4, 
    حميع الحالات = 7
    
    عدد البتات اللازمة: 3
    
    Number: singular, dual, plural
    
    يمكن تعبئتها من الخليل
    '''
    
    CaseAndMood = 0;
    '''
    غير معالج = 0, 
    مرفوع = 1, 
    منصوب  = 2, 
    مجرور أو مجزوم = 4, 
    حميع الحالات = 7
    
    عدد البتات اللازمة: 3
    
    يمكن تعبئتها من الخليل
    
    Case: Nominative/Indicative, Accusative/Subjunctive, Genitive/Jussive
    '''
    
    
    Person = 0;
    '''
    غير معالج = 0, 
    المتكلّم = 1, 
    المخاطب = 2, 
    الغائب = 4, 
    حميع الحالات = 7
    
    Person: First Person, Second Person, Third Person
    عدد البتات اللازمة: 3
    
    يمكن تعبئتها من الخليل
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    pass
        
    def WriteGenderArabicText(self, stringStream):
        stringList = [];
        if(self.Gender == CliticlessPOSConstants.Gender.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Gender & CliticlessPOSConstants.Gender.Masculine != 0):
                stringList.append('مذكر');
            if(self.Gender & CliticlessPOSConstants.Gender.Feminine != 0):
                stringList.append('مؤنث');
                
        stringStream.write(' أو '.join(stringList));
    pass

    def WriteGenderTag(self, stringStream):
        stringList = [];
        if(self.Gender == CliticlessPOSConstants.Gender.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Gender & CliticlessPOSConstants.Gender.Masculine != 0):
                stringList.append('m');
            if(self.Gender & CliticlessPOSConstants.Gender.Feminine != 0):
                stringList.append('f');
                
        stringStream.write(''.join(stringList));
    pass

    def WriteNumberArabicText(self, stringStream):
        stringList = [];
        if(self.Number == CliticlessPOSConstants.Number.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Number & CliticlessPOSConstants.Number.Singular != 0):
                stringList.append('مفرد');
            if(self.Number & CliticlessPOSConstants.Number.Dual != 0):
                stringList.append('مثنى');                
            if(self.Number & CliticlessPOSConstants.Number.Plural != 0):
                stringList.append('جمع');
                
        stringStream.write(' أو '.join(stringList));
    pass

    def WriteNumberTag(self, stringStream):
        stringList = [];
        if(self.Number == CliticlessPOSConstants.Number.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Number & CliticlessPOSConstants.Number.Singular != 0):
                stringList.append('s');
            if(self.Number & CliticlessPOSConstants.Number.Dual != 0):
                stringList.append('d');                
            if(self.Number & CliticlessPOSConstants.Number.Plural != 0):
                stringList.append('p');
                
        stringStream.write(''.join(stringList));
    pass

    def WriteCaseAndMoodArabicText(self, stringStream):
        stringList = [];
        if(self.CaseAndMood == CliticlessPOSConstants.CaseAndMood.Unprocessed):
            stringList.append('؟');
        elif(self.CaseAndMood == CliticlessPOSConstants.CaseAndMood.Inapplicable):
            stringList.append('-');
        else:            
            if(self.CaseAndMood & CliticlessPOSConstants.CaseAndMood.NominativeOrIndicative != 0):
                stringList.append('مرفوع');
            if(self.CaseAndMood & CliticlessPOSConstants.CaseAndMood.AccusativeOrSubjunctive != 0):
                stringList.append('منصوب');
            if(self.CaseAndMood & CliticlessPOSConstants.CaseAndMood.GenitiveOrJussive != 0):
                if(self.MainClass & POSConstants.MainClass.Noun != 0):
                    stringList.append('مجرور');
                if(self.MainClass & POSConstants.MainClass.Verb != 0):
                    stringList.append('مجزوم');
                
        stringStream.write(' أو '.join(stringList));
    pass

    def WriteCaseAndMoodTag(self, stringStream):
        stringList = [];
        if(self.CaseAndMood == CliticlessPOSConstants.CaseAndMood.Unprocessed):
            stringList.append('؟');        
        elif(self.CaseAndMood == CliticlessPOSConstants.CaseAndMood.Inapplicable):
            stringList.append('-');
        else:            
            if(self.CaseAndMood & CliticlessPOSConstants.CaseAndMood.NominativeOrIndicative != 0):
                stringList.append('n');#مرفوع
            if(self.CaseAndMood & CliticlessPOSConstants.CaseAndMood.AccusativeOrSubjunctive != 0):
                stringList.append('a');#منصوب
            if(self.CaseAndMood & CliticlessPOSConstants.CaseAndMood.GenitiveOrJussive != 0):
                if(self.MainClass & POSConstants.MainClass.Noun != 0):
                    stringList.append('g');#مجرور
                if(self.MainClass & POSConstants.MainClass.Verb != 0):
                    stringList.append('g');#مجزوم
                
        stringStream.write(''.join(stringList));
    pass

    def WritePersonArabicText(self, stringStream):
        stringList = [];
        if(self.Person == CliticlessPOSConstants.Person.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Person & CliticlessPOSConstants.Person.First_Person != 0):
                stringList.append('مسند إلى المتكلّم');
            if(self.Person & CliticlessPOSConstants.Person.Second_Person != 0):
                stringList.append('مسند إلى المخاطب');
            if(self.Person & CliticlessPOSConstants.Person.Third_Person != 0):
                stringList.append('مسند إلى الغائب');
                
        stringStream.write(' أو '.join(stringList));
    pass

    def WritePersonTag(self, stringStream):
        stringList = [];
        if(self.Person == CliticlessPOSConstants.Person.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Person & CliticlessPOSConstants.Person.First_Person != 0):
                stringList.append('f');#مسند إلى المتكلّم
            if(self.Person & CliticlessPOSConstants.Person.Second_Person != 0):
                stringList.append('s');#مسند إلى المخاطب
            if(self.Person & CliticlessPOSConstants.Person.Third_Person != 0):
                stringList.append('t');#مسند إلى الغائب
                
        stringStream.write(''.join(stringList));
    pass
    def WriteArabicText(self, stringStream):
        POS.WriteArabicText(self, stringStream);
        stringStream.write(', ');
        self.WriteGenderArabicText(stringStream);
        stringStream.write(', ');
        self.WriteNumberArabicText(stringStream);
        stringStream.write(', ');
        self.WritePersonArabicText(stringStream);
        stringStream.write(', ');
        self.WriteCaseAndMoodArabicText(stringStream);
        
    pass
    
    def WriteTag(self, stringStream):
        POS.WriteTag(self, stringStream);
        stringStream.write(',');
        self.WriteGenderTag(stringStream);
        stringStream.write(',');
        self.WriteNumberTag(stringStream);
        stringStream.write(',');
        self.WritePersonTag(stringStream);
        stringStream.write(',');
        self.WriteCaseAndMoodTag(stringStream);
        
    pass

    def Clone(self):
        pos = CliticlessPOS();
        pos.MainClass = self.MainClass;
        pos.StringTag = self.StringTag;
        pos.FullArabicTextTag = self.FullArabicTextTag;
        pos.BinaryTag = self.BinaryTag;
        
        pos.Gender = self.Gender;
        pos.Number = self.Number;
        pos.CaseAndMood = self.CaseAndMood;
                
        return pos;
    pass
        

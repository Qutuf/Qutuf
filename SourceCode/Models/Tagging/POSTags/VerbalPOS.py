from Tagging.POSTags.CliticlessPOS import CliticlessPOSConstants
from Tagging.POSTags.CliticlessPOS import CliticlessPOS


'''
Created on ٢٩‏/٠٥‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Models.Tagging.POSTags.CliticlessPOS import *;


class VerbalPOSConstants(CliticlessPOSConstants):
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0LQto35Ed-gg8GOK1TmhA
    """
    
    class Aspect:
        #الصيغة
        
        #غير معالج = 0, 
        Unprocessed = 0;
        #ماض  = 1, 
        Perfective = 1;
        #مضارع = 2, 
        Imperfective = 2;
        #أمر = 4, 
        Imperative = 4;
        #حميع الحالات = 7
        all_Cases = 7;
        
#    
#    class Tense:
#                
#        #غير معالج = 0, 
#        Unprocessed = 0;
#        #ماض  = 1, 
#        Past = 1;
#        #حاضر = 2, 
#        Present = 2;
#        #مستقبل = 4, 
#        Future = 4;
#        #حميع الحالات = 7
#        all_Cases = 7;
#        
#        #عدد البتات اللازمة: 3
#        Number_of_bits = 3;
#        
#        
   
    class Activeness:
        #Active مبني للمعلوم أو المجهول:
        
        #غير معالج = 0, 
        Unprocessed = 0;
        #مبني للمعلوم  = 1, 
        Active = 1;
        #مبني للمجهول = 2, 
        Passive = 2;
        #حميع الحالات = 3
        all_Cases = 3;
        
        #عدد البتات اللازمة: 2
        Number_of_bits = 2;
        
    class Transitive:
        #Transitive = التعدي:
        #غير معالج = 0, 
        Unprocessed = 0;
        #لازم  = 1, 
        Intransitive = 1;
        #متعد لمفعول = 2, 
        Transitive_for_1 = 2;
        #متعد لمفعولين = 4,
        Transitive_for_2 = 4; 
        #متعد لثلاثة مفاعيل = 8,
        Transitive_for_3 = 8; 
        #حميع الحالات = 15
        all_Cases = 15;
        
        #عدد البتات اللازمة: 4
        Number_of_bits = 4;
        
    class Asserted:
        #Asserted مؤكّد:
        
        #غير معالج = 0, 
        Unprocessed = 0;
        #غير مؤكّد  = 1, 
        Unasserted = 1;
        #مؤكّد = 2, 
        Asserted = 2;
        #حميع الحالات = 3
        all_Cases = 3;
        
        #عدد البتات اللازمة: 2
        Number_of_bits = 2;


    class Perfectness:
        #Active مبني للمعلوم أو المجهول:
        
        #غير معالج = 0, 
        Unprocessed = 0;
        #تام  = 1, 
        Perfect = 1;
        # ناقص - أخوات كان= 2, 
        Imperfect_Verb_To_Be = 2;
        
        #ناقص - أخوات كاد = 2, 
        Imperfect_Almost_Being = 4;
        #حميع الحالات
        all_Cases = 7;
        
        #عدد البتات اللازمة: 2
        Number_of_bits = 3;

class VerbalPOS(CliticlessPOS):
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0LQt435Ed-gg8GOK1TmhA
    """
    '''
    classdocs
    '''

    Aspect = 0;    
    '''
    غير معالج = 0, 
    ماض  = 1, 
    مضارع = 2, 
    أمر = 4, 
    حميع الحالات = 7
    
    عدد البتات اللازمة: 3

    Aspect: perfective, imperfective, imperative
    
    يمكن تعبئتها من الخليل
    '''
#    
#    Tense = 0;
#    '''
#    غير معالج = 0, 
#    ماض  = 1, 
#    حاضر = 2, 
#    مستقبل = 4, 
#    حميع الحالات = 7
#    
#    عدد البتات اللازمة: 3
#    
#    Tense: past, present, future
#    '''

#    
#    Mood = 0;
#    '''
#    الصيغة
#    غير معالج = 0, 
#    مرفوع = 1,
#    منصوب = 2, 
#    مجزوم = 4, 
#    حميع الحالات = 7
#    
#    عدد البتات اللازمة: 3
#    
#    Mood: indicative, subjunctive, jussive
#
#    هذه الخاصية موجودة في الأب حيث تم دمجها مع الحالة الإعرابية
#    case.
#    '''
    
    Activeness = 0;
    '''
    غير معالج = 0, 
    مبني للمعلوم  = 1, 
    مبني للمجهول = 2, 
    حميع الحالات = 3
    
    Active: Active, Passive
    عدد البتات اللازمة: 2
    
    يمكن تعبئتها من الخليل
    '''
    
    Transitive = 0;
    '''
    غير معالج = 0, 
    لازم  = 1, 
    متعد لمفعول = 2, 
    متعد لمفعولين = 4, 
    متعد لثلاثة مفاعيل = 8, 
    حميع الحالات = 15
    
    Transitive: Intransitive, Transitive for 1, Intransitive for 2, Intransitive for 3
    عدد البتات اللازمة: 4
    
    يمكن تعبئتها من الخليل
    '''
        
    Asserted = 0;
    '''
    غير معالج = 0, 
    غير مؤكّد  = 1, 
    مؤكّد = 2, 
    حميع الحالات = 3
    
    Asserted: Asserted, Unasserted.
    عدد البتات اللازمة: 2
    
    يمكن تعبئتها من الخليل
    '''
    
    IsAugmented = None;
    '''
    غير معروف = None, 
    مجرّد = False, 
    مزيد= True
    
    يمكن تعبئتها من الخليل
    '''
    

    Perfectness = 0;

    def __init__(self):
        '''
        Constructor
        '''
        self.MainClass = POSConstants.MainClass.Verb;
    pass


    def WriteAspectArabicText(self, stringStream):
        stringList = [];
        if(self.Aspect == VerbalPOSConstants.Aspect.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Aspect & VerbalPOSConstants.Aspect.Perfective != 0):
                stringList.append('ماض');
            if(self.Aspect & VerbalPOSConstants.Aspect.Imperfective != 0):
                stringList.append('مضارع');
            if(self.Aspect & VerbalPOSConstants.Aspect.Imperative != 0):
                stringList.append('أمر');
                
        stringStream.write(' أو '.join(stringList));
    pass

    def WriteAspectTag(self, stringStream):
        stringList = [];
        if(self.Aspect == VerbalPOSConstants.Aspect.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Aspect & VerbalPOSConstants.Aspect.Perfective != 0):
                stringList.append('p');
            if(self.Aspect & VerbalPOSConstants.Aspect.Imperfective != 0):
                stringList.append('c');
            if(self.Aspect & VerbalPOSConstants.Aspect.Imperative != 0):
                stringList.append('i');
                
        stringStream.write(''.join(stringList));
    pass

    def WriteActiveArabicText(self, stringStream):
        stringList = [];
        if(self.Aspect == VerbalPOSConstants.Aspect.Imperative):
            stringList.append('-');
        elif(self.Activeness == VerbalPOSConstants.Activeness.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Activeness & VerbalPOSConstants.Activeness.Active != 0):
                stringList.append('مبني للمعلوم');
            if(self.Activeness & VerbalPOSConstants.Activeness.Passive != 0):
                stringList.append('مبني للمجهول');
                
        stringStream.write(' أو '.join(stringList));
    pass

    def WriteActiveTag(self, stringStream):
        stringList = [];
        if(self.Aspect == VerbalPOSConstants.Aspect.Imperative):
            stringList.append('-');
        elif(self.Activeness == VerbalPOSConstants.Activeness.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Activeness & VerbalPOSConstants.Activeness.Active != 0):
                stringList.append('a');#مبني للمعلوم
            if(self.Activeness & VerbalPOSConstants.Activeness.Passive != 0):
                stringList.append('p');#مبني للمجهول
                
        stringStream.write(''.join(stringList));
    pass

    def WriteTransitiveArabicText(self, stringStream):
        stringList = [];
        if(self.Transitive == VerbalPOSConstants.Transitive.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Transitive & VerbalPOSConstants.Transitive.Intransitive != 0):
                stringList.append('لازمٌ');
            
            if(self.Transitive & VerbalPOSConstants.Transitive.Transitive_for_1 != 0
               and self.Transitive & VerbalPOSConstants.Transitive.Transitive_for_2 != 0
               and self.Transitive & VerbalPOSConstants.Transitive.Transitive_for_3 != 0):
                stringList.append('مُتعدٍ');
            else:
                if(self.Transitive & VerbalPOSConstants.Transitive.Transitive_for_1 != 0):
                    stringList.append('يتعدى لمفعول واحد');
                if(self.Transitive & VerbalPOSConstants.Transitive.Transitive_for_2 != 0):
                    stringList.append('يتعدى لمفوعلين');
                if(self.Transitive & VerbalPOSConstants.Transitive.Transitive_for_3 != 0):
                    stringList.append('يتعدى لثلاثة مفاعيل');
                
        stringStream.write(' أو '.join(stringList));
    pass

    def WriteTransitiveTag(self, stringStream):
        stringList = [];
        if(self.Transitive == VerbalPOSConstants.Transitive.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Transitive & VerbalPOSConstants.Transitive.Intransitive != 0):
                stringList.append('i');#لازمٌ
            
            if(self.Transitive & VerbalPOSConstants.Transitive.Transitive_for_1 != 0
               and self.Transitive & VerbalPOSConstants.Transitive.Transitive_for_2 != 0
               and self.Transitive & VerbalPOSConstants.Transitive.Transitive_for_3 != 0):
                stringList.append('obt');#مُتعدٍ
            else:
                if(self.Transitive & VerbalPOSConstants.Transitive.Transitive_for_1 != 0):
                    stringList.append('o');#يتعدى لمفعول واحد
                if(self.Transitive & VerbalPOSConstants.Transitive.Transitive_for_2 != 0):
                    stringList.append('b');#يتعدى لمفوعلين
                if(self.Transitive & VerbalPOSConstants.Transitive.Transitive_for_3 != 0):
                    stringList.append('t');#يتعدى لثلاثة مفاعيل
                
        stringStream.write(''.join(stringList));
    pass

    
    def WritePerfectnessTag(self, stringStream):
        stringList = [];
        if(self.Perfectness == VerbalPOSConstants.Perfectness.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Perfectness & VerbalPOSConstants.Perfectness.Perfect != 0):
                stringList.append('p');
            if(self.Perfectness & VerbalPOSConstants.Perfectness.Imperfect_Verb_To_Be != 0):
                stringList.append('n');
            if(self.Perfectness & VerbalPOSConstants.Perfectness.Imperfect_Almost_Being != 0):
                stringList.append('d');
        
        stringStream.write(''.join(stringList));
    pass

    def WritePerfectnessArabicText(self, stringStream):
        stringList = [];
        if(self.Perfectness == VerbalPOSConstants.Perfectness.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Perfectness & VerbalPOSConstants.Perfectness.Perfect != 0):
                stringList.append('تام');
            if(self.Perfectness & VerbalPOSConstants.Perfectness.Imperfect_Verb_To_Be != 0):
                stringList.append('ناقص (أخوات كان)');
            if(self.Perfectness & VerbalPOSConstants.Perfectness.Imperfect_Almost_Being != 0):
                stringList.append('ناقص (أخوات كاد)');
                
        stringStream.write(' أو '.join(stringList));
    pass
#    def WriteAssertedTag(self, stringStream):
#        stringList = [];
#        if(self.Aspect == VerbalPOSConstants.Aspect.Perfective):
#            stringList.append('-');
#        elif(self.Asserted == VerbalPOSConstants.Asserted.Unprocessed):
#            stringList.append('؟');
#        else:            
#            if(self.Asserted & VerbalPOSConstants.Asserted.Asserted != 0):
#                stringList.append('m');#مؤكد
#            if(self.Asserted & VerbalPOSConstants.Asserted.Unasserted != 0):
#                stringList.append('n');#غير مؤكد
#                
#        stringStream.write(''.join(stringList));
#    pass

    def WriteAssertedTag(self, stringStream):
        stringList = [];
        if(self.Aspect == VerbalPOSConstants.Aspect.Perfective):
            stringList.append('-');
        elif(self.Asserted == VerbalPOSConstants.Asserted.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Asserted & VerbalPOSConstants.Asserted.Asserted != 0):
                stringList.append('m');#مؤكد
            if(self.Asserted & VerbalPOSConstants.Asserted.Unasserted != 0):
                stringList.append('n');#غير مؤكد
                
        stringStream.write(''.join(stringList));
    pass

    def WriteAssertedArabicText(self, stringStream):
        stringList = [];
        if(self.Aspect == VerbalPOSConstants.Aspect.Perfective):
            stringList.append('-');
        elif(self.Asserted == VerbalPOSConstants.Asserted.Unprocessed):
            stringList.append('؟');
        else:
            if(self.Asserted & VerbalPOSConstants.Asserted.Asserted != 0):
                stringList.append('مؤكد');
            if(self.Asserted & VerbalPOSConstants.Asserted.Unasserted != 0):
                stringList.append('غير مؤكد');
                
        stringStream.write(' أو '.join(stringList));
    pass

    def WriteIsAugmentedArabicText(self, stringStream):
        if(self.IsAugmented == False):
            stringStream.write('مجرد');
        elif(self.IsAugmented == True):
            stringStream.write('مزيد');
        else:
            stringStream.write(str(self.IsAugmented));
    pass
    def WriteArabicText(self, stringStream):
        CliticlessPOS.WriteArabicText(self, stringStream);
        stringStream.write(', ');
        self.WriteAspectArabicText(stringStream);
        stringStream.write(', ');
        self.WriteActiveArabicText(stringStream);
        stringStream.write(', ');
        self.WriteTransitiveArabicText(stringStream);
        stringStream.write(', ');
        self.WritePerfectnessArabicText(stringStream);
        stringStream.write(', ');
        self.WriteAssertedArabicText(stringStream);
        stringStream.write(', ');
        self.WriteIsAugmentedArabicText(stringStream);
    pass
    
    def WriteTag(self, stringStream):
        CliticlessPOS.WriteTag(self, stringStream);
        stringStream.write(',');
        self.WriteAspectTag(stringStream);
        stringStream.write(',');
        self.WriteActiveTag(stringStream);
        stringStream.write(',');
        self.WriteTransitiveTag(stringStream);
        stringStream.write(',');
        self.WritePerfectnessTag(stringStream);
    pass
    
    def Clone(self):
        pos = VerbalPOS();
        pos.MainClass = self.MainClass;
        pos.BinaryTag = self.BinaryTag;
        
        pos.Gender = self.Gender;
        pos.Number = self.Number;
        pos.CaseAndMood = self.CaseAndMood;
        
        pos.Aspect = self.Aspect;
        pos.Person = self.Person;
        pos.Activeness = self.Activeness;
        pos.Transitive = self.Transitive;
        pos.Asserted = self.Asserted;
        pos.IsAugmented = self.IsAugmented;
        
        return pos;
    pass

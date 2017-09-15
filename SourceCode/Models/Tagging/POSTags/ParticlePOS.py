# -*- coding: utf-8 -*-
'''
Created on ٢٩‏/٠٥‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Models.Tagging.POSTags.POS import POS;
from POSTags.POS import POSConstants;

class ParticlePOSConstants(POSConstants):
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0LQZY35Ed-gg8GOK1TmhA
    """
    class SubClass:
        #غير معالج
        Unprocessed = 0
        #حرف جر
        Preposition = 1     
        #حرف جزم
        Apocopative = 2
        #حرف نصب
        Accusative = 4
        #حرف ناسخ
        Annuler = 8
        #حرف عطف
        Conjunction = 16
        #حرف نداء
        Vocative = 32
        #حرف استثناء
        Exceptive = 64
        #حرف استفهام
        Interrogative = 128
        #حرف استقبال
        Futurity = 256
        #حرف المستقبل القريب - السين
        ForthcomingFuturity = 512
        #حرف شرط
        Conditional = 1024
        
        #حرف تحقيق وتقريب
        RealizationORAlmost = 2048
        
        #حرف النصب الفرعي
        PartialAccusative  = 4096
        #حرف تعليل
        Causative = 8192
        #حرف نفي
        Negative = 16384
        #حرف قسَم
        Jurative = 32768
        
        #استئناف - الفاء
        Resumption = 65536
        #ابتداء للتوكيد - اللام
        EmphasisStarter = 131072
        
        #الأمر - اللام
        Imperative = 262144
        
        #أداة - لا محل لها من الإعراب
        Appendix = 524288
        
        #جميع الحالات
        all_Cases = 1048575
        
        #عدد البتات اللازمة
        Number_of_bits = 20;
        
    class Substantivness:
        #غير معالجة
        Unprocessed = 0;
        #مضمرة - محذوفة - مقدّرة
        Hidden = 1;
        #ظاهرة
        Substantive = 2;
        #جميع الاحتمالات
        all_Cases = 3;

class ParticlePOS(POS):
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0LQZo35Ed-gg8GOK1TmhA
    """
    '''
    classdocs
    '''

    SubClass = 0;    
    '''
    حرف جر = 1    
    حرف جزم = 2
    حرف نصب = 4
    حرف ناسخ = 8
    حرف عطف = 16
    حرف نداء = 32
    حرف استثناء = 64
    حرف استفهام = 128
    حرف استقبال = 256
    حرف شرط = 512
    
    حرف تحقيق = 1024
    
    حرف النصب الفرعي = 2048
    حرف تعليل = 4096
    حرف نفي = 8192
    حرف قسًم = 16384

    جميع الحالات = 32767
    
    عدد البتات اللازمة = 14
    '''
    
    '''
    الإظهار - الحذف
    '''
    Substantivness = 0;

    def __init__(self):
        '''
        Constructor
        '''
        self.MainClass = POSConstants.MainClass.Particle;
        self.Substantivness = ParticlePOSConstants.Substantivness.Substantive;
    pass


    def WriteSubClassText(self, stringStream):
        stringList = [];
        if(self.SubClass == ParticlePOSConstants.SubClass.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.SubClass & ParticlePOSConstants.SubClass.Preposition != 0):
                stringList.append('حرف جر');
            if(self.SubClass & ParticlePOSConstants.SubClass.Apocopative != 0):
                stringList.append('حرف جزم');
            if(self.SubClass & ParticlePOSConstants.SubClass.Accusative != 0):
                stringList.append('حرف نصب');
            if(self.SubClass & ParticlePOSConstants.SubClass.Annuler != 0):
                stringList.append('حرف ناسخ');
            if(self.SubClass & ParticlePOSConstants.SubClass.Conjunction != 0):
                stringList.append('حرف عطف');
            if(self.SubClass & ParticlePOSConstants.SubClass.Vocative != 0):
                stringList.append('حرف نداء');
            if(self.SubClass & ParticlePOSConstants.SubClass.Exceptive != 0):
                stringList.append('حرف استثناء');
            if(self.SubClass & ParticlePOSConstants.SubClass.Interrogative != 0):
                stringList.append('حرف استفهام');
            if(self.SubClass & ParticlePOSConstants.SubClass.Futurity != 0):
                stringList.append('حرف استقبال');
            if(self.SubClass & ParticlePOSConstants.SubClass.Conditional != 0):
                stringList.append('حرف شرط');
            if(self.SubClass & ParticlePOSConstants.SubClass.RealizationORAlmost != 0):
                stringList.append('حرف تحقيق وتقريب');
            if(self.SubClass & ParticlePOSConstants.SubClass.PartialAccusative != 0):
                stringList.append('حرف نصب فرعي');
            if(self.SubClass & ParticlePOSConstants.SubClass.Causative != 0):
                stringList.append('حرف تعليل');
            if(self.SubClass & ParticlePOSConstants.SubClass.Negative != 0):
                stringList.append('حرف نفي');
            if(self.SubClass & ParticlePOSConstants.SubClass.Jurative != 0):
                stringList.append('حرف قسَم');
            if(self.SubClass & ParticlePOSConstants.SubClass.Resumption != 0):
                stringList.append('استئناف');
            if(self.SubClass & ParticlePOSConstants.SubClass.EmphasisStarter != 0):
                stringList.append('ابتداء للتوكيد');
            if(self.SubClass & ParticlePOSConstants.SubClass.Imperative != 0):
                stringList.append('لام الأمر');
            if(self.SubClass & ParticlePOSConstants.SubClass.Appendix != 0):
                stringList.append('لا محل له من الإعراب');
        
                
        stringStream.write(' أو '.join(stringList));
    pass

    def WriteSubstantivnessText(self, stringStream):
        stringList = [];
        if(self.Substantivness == ParticlePOSConstants.SubClass.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.Substantivness & ParticlePOSConstants.Substantivness.Hidden != 0):
                stringList.append('مقدّر');
            if(self.Substantivness & ParticlePOSConstants.Substantivness.Substantive != 0):
                stringList.append('ظاهر');
        
                
        stringStream.write(' أو '.join(stringList));
    pass

    def WriteArabicText(self, stringStream):
        POS.WriteArabicText(self, stringStream);
        stringStream.write(', ');
        self.WriteSubClassText(stringStream);
        stringStream.write(', ');
        self.WriteSubstantivnessText(stringStream);
        
    pass
    
    def WriteSubClassTag(self, stringStream):
        stringList = [];
        if(self.SubClass == ParticlePOSConstants.SubClass.Unprocessed):
            stringList.append('؟');
        else:            
            if(self.SubClass & ParticlePOSConstants.SubClass.Preposition != 0):
                stringList.append('p');#حرف جر
            if(self.SubClass & ParticlePOSConstants.SubClass.Apocopative != 0):
                stringList.append('j');#حرف جزم
            if(self.SubClass & ParticlePOSConstants.SubClass.Accusative != 0):
                stringList.append('o');#حرف نصب
            if(self.SubClass & ParticlePOSConstants.SubClass.Annuler != 0):
                stringList.append('a');#حرف ناسخ
            if(self.SubClass & ParticlePOSConstants.SubClass.Conjunction != 0):
                stringList.append('c');#حرف عطف
            if(self.SubClass & ParticlePOSConstants.SubClass.Vocative != 0):
                stringList.append('v');#حرف نداء
            if(self.SubClass & ParticlePOSConstants.SubClass.Exceptive != 0):
                stringList.append('x');#حرف استثناء
            if(self.SubClass & ParticlePOSConstants.SubClass.Interrogative != 0):
                stringList.append('i');#حرف استفهام
            if(self.SubClass & ParticlePOSConstants.SubClass.Futurity != 0):
                stringList.append('f');#حرف استقبال
            if(self.SubClass & ParticlePOSConstants.SubClass.Conditional != 0):
                stringList.append('k');#حرف شرط
            if(self.SubClass & ParticlePOSConstants.SubClass.RealizationORAlmost != 0):
                stringList.append('r');#حرف تحقيق وتقريب
            if(self.SubClass & ParticlePOSConstants.SubClass.PartialAccusative != 0):
                stringList.append('u');#حرف نصب فرعي
            if(self.SubClass & ParticlePOSConstants.SubClass.Causative != 0):
                stringList.append('s');#حرف تعليل
            if(self.SubClass & ParticlePOSConstants.SubClass.Negative != 0):
                stringList.append('n');#حرف نفي
            if(self.SubClass & ParticlePOSConstants.SubClass.Jurative != 0):
                stringList.append('q');#حرف قسَم
            if(self.SubClass & ParticlePOSConstants.SubClass.Resumption != 0):
                stringList.append('e');#استئناف
            if(self.SubClass & ParticlePOSConstants.SubClass.EmphasisStarter != 0):
                stringList.append('h');#ابتداء للتوكيد
            if(self.SubClass & ParticlePOSConstants.SubClass.Imperative != 0):
                stringList.append('y');#لام الأمر
            if(self.SubClass & ParticlePOSConstants.SubClass.Appendix != 0):
                stringList.append('%');#زائد
        
                
        stringStream.write(''.join(stringList));
    pass

    def WriteTag(self, stringStream):
        POS.WriteTag(self, stringStream);
        stringStream.write(',');
        self.WriteSubClassTag(stringStream);
        
    pass
    
    def Clone(self):
        pos = ParticlePOS();
        pos.MainClass = self.MainClass;
        pos.BinaryTag = self.BinaryTag;
                        
        pos.SubClass = self.SubClass;
        return pos;
    pass

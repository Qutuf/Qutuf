# -*- coding: utf-8 -*-
'''
Created on ٢٧‏/٠٥‏/٢٠١٠

@Created by: Muhammad Altabba
'''
class POSConstants:
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0LQkI35Ed-gg8GOK1TmhA
    """
    class MainClass:
        #غير معالج = 0, 
        Unprocessed = 0;
        #اسم = 1, 
        Noun = 1;
        #فعل = 2, 
        Verb = 2;
        #حرف = 4, 
        Particle = 4;
        #حميع الحالات = 7
        all_Cases = 7;
        
        #عدد البتات اللازمة: 3
        Number_of_bits = 3;


class POS(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0LQkY35Ed-gg8GOK1TmhA
    """
    '''
    Word (or Clitic) Part of Speech
    '''
    
    MainClass = 0;
    '''
    غير معالج = 0, 
    اسم = 1, 
    فعل = 2, 
    حرف = 4, 
    حميع الحالات = 7
    
    عدد البتات اللازمة: 3
    
    MainClass: Noun, Verb, Particle
    '''

    
    BinaryTag = 0;
    '''
    Empty unless AssignBinaryTag is coaled.
    '''
        

    def __init__(self):
        '''
        Constructor
        '''        
        self.MainClass = POSConstants.MainClass.Unprocessed;
    
    def AssignBinaryTag(self):
        self.BinaryTag = self.MainClass;
    pass    


    def WriteMainClassArabicText(self, stringStream):
        stringList = [];
        if(self.MainClass == POSConstants.MainClass.Unprocessed):
            stringList.append('؟');
        else:
            if(self.MainClass & POSConstants.MainClass.Noun != 0):
                stringList.append('اسم');
            elif(self.MainClass & POSConstants.MainClass.Verb != 0):
                stringList.append('فعل');
            elif(self.MainClass & POSConstants.MainClass.Particle != 0):
                stringList.append('حرف');
        stringStream.write(' أو '.join(stringList));
    pass

    def WriteMainClassTag(self, stringStream):
        if(self.MainClass == POSConstants.MainClass.Unprocessed):
            stringStream.write('?');
        else:
            if(self.MainClass & POSConstants.MainClass.Noun != 0):
                stringStream.write('n');
            elif(self.MainClass & POSConstants.MainClass.Verb != 0):
                stringStream.write('v');
            elif(self.MainClass & POSConstants.MainClass.Particle != 0):
                stringStream.write('p');
    pass
    
    

    def WriteArabicText(self, stringStream):
        self.WriteMainClassArabicText(stringStream);
    pass

    def WriteTag(self, stringStream):
        self.WriteMainClassTag(stringStream);
    pass
    
    def Clone(self):
        pos = POS();
        pos.MainClass = self.MainClass;
        pos.StringTag = self.StringTag;
        pos.FullArabicTextTag = self.FullArabicTextTag;
        pos.BinaryTag = self.BinaryTag;
        
        return pos;
    pass

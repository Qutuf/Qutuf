
'''
Created on ١٣‏/٠٦‏/٢٠١٠

@Created by: Muhammad Altabba
'''

class DiacriticsConstants:
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0BftI35Ed-gg8GOK1TmhA
    """
    '''
    Diacritics
    '''
    Fatha = 'َ';
    DoubleFatha = 'ً';
    Damma = 'ُ';
    DoubleDamma = 'ٌ';
    Kasra = 'ِ';
    DoubleKasra = 'ٍ';
    Sukoon = 'ْ';
    Shadda = 'ّ';
    
    AllDiacritics = [];


DiacriticsConstants.AllDiacritics.append(DiacriticsConstants.Fatha);
DiacriticsConstants.AllDiacritics.append(DiacriticsConstants.DoubleFatha);
DiacriticsConstants.AllDiacritics.append(DiacriticsConstants.Damma);
DiacriticsConstants.AllDiacritics.append(DiacriticsConstants.DoubleDamma);
DiacriticsConstants.AllDiacritics.append(DiacriticsConstants.Kasra);
DiacriticsConstants.AllDiacritics.append(DiacriticsConstants.DoubleKasra);
DiacriticsConstants.AllDiacritics.append(DiacriticsConstants.Sukoon);
DiacriticsConstants.AllDiacritics.append(DiacriticsConstants.Shadda);


class HamzaConstants:
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0Bfx435Ed-gg8GOK1TmhA
    """
    '''
    Hamza Forms
    '''
    OnAlif = 'أ';
    UnderAlif = 'إ';
    OnWaw = 'ؤ';
    OnYa = 'ئ';
    OnLine = 'ء';
    
    AllHamzas = [];

    def __init__(self):
        '''
        Constructor
        '''
        
HamzaConstants.AllHamzas.append(HamzaConstants.OnAlif);
HamzaConstants.AllHamzas.append(HamzaConstants.UnderAlif);
HamzaConstants.AllHamzas.append(HamzaConstants.OnWaw);
HamzaConstants.AllHamzas.append(HamzaConstants.OnYa);
HamzaConstants.AllHamzas.append(HamzaConstants.OnLine);

class EllaConstants:
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0Bfx435Ed-gg8GOK1TmhA
    """
    '''
    Ahrof Ella
    '''
    Alif = 'ا';
    AlifMaksora = 'ى';
    Waw = 'و';
    Ya = 'ي';
    
    AllAhrofElla = [];

    def __init__(self):
        '''
        Constructor
        '''
        
EllaConstants.AllAhrofElla.append(EllaConstants.Alif);
EllaConstants.AllAhrofElla.append(EllaConstants.AlifMaksora);
EllaConstants.AllAhrofElla.append(EllaConstants.Waw);
EllaConstants.AllAhrofElla.append(EllaConstants.Ya);


class ArabicLetters:
    
    AllLetters = [];
    
    def __init__(self):
        '''
        Constructor
        '''
    
ArabicLetters.AllLetters = [];
ArabicLetters.AllLetters.append("ء");
ArabicLetters.AllLetters.append("أ");
ArabicLetters.AllLetters.append("إ");
ArabicLetters.AllLetters.append("آ"); 
ArabicLetters.AllLetters.append("ؤ");
ArabicLetters.AllLetters.append("ئ");
ArabicLetters.AllLetters.append("ا");
ArabicLetters.AllLetters.append("ى");
ArabicLetters.AllLetters.append("ب");
ArabicLetters.AllLetters.append("ت");
ArabicLetters.AllLetters.append("ة");
ArabicLetters.AllLetters.append("ث");
ArabicLetters.AllLetters.append("ج");
ArabicLetters.AllLetters.append("ح");
ArabicLetters.AllLetters.append("خ");
ArabicLetters.AllLetters.append("د");
ArabicLetters.AllLetters.append("ذ");
ArabicLetters.AllLetters.append("ر");
ArabicLetters.AllLetters.append("ز");
ArabicLetters.AllLetters.append("س");
ArabicLetters.AllLetters.append("ش");
ArabicLetters.AllLetters.append("ص");
ArabicLetters.AllLetters.append("ض");
ArabicLetters.AllLetters.append("ط");
ArabicLetters.AllLetters.append("ظ");
ArabicLetters.AllLetters.append("ع");
ArabicLetters.AllLetters.append("غ");
ArabicLetters.AllLetters.append("ف");
ArabicLetters.AllLetters.append("ق");
ArabicLetters.AllLetters.append("ك");
ArabicLetters.AllLetters.append("ل");
ArabicLetters.AllLetters.append("م");
ArabicLetters.AllLetters.append("ن");
ArabicLetters.AllLetters.append("ه");
ArabicLetters.AllLetters.append("و");
ArabicLetters.AllLetters.append("ي");


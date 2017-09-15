
'''
Created on ٢٨‏/٠٦‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Models.Lexicon.LettersConstants import DiacriticsConstants

class ArabicStringUtility(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qysDPI35Ed-gg8GOK1TmhA
    """
    '''
    Arabic String Utility
    '''

    def __init__(self, string):
        '''
        Constructor
        '''
    pass


    def IsCompatible(self, string, voweledForm):
        stringIndexer = 0;
        voweledPatternsIndexer = 0;
        while stringIndexer < len(string):                    
            while stringIndexer < len(string) and voweledPatternsIndexer < len(voweledForm)\
                and (voweledForm[voweledPatternsIndexer] == string[stringIndexer]\
                     or (string[stringIndexer] not in DiacriticsConstants.AllDiacritics and voweledForm[voweledPatternsIndexer] in ['ل','ع','ف'])):
                stringIndexer += 1;
                voweledPatternsIndexer += 1;
            if voweledPatternsIndexer == len(voweledForm):
                return True;
            while (stringIndexer < len(string)\
                   and voweledForm[voweledPatternsIndexer] not in DiacriticsConstants.AllDiacritics\
                   and string[stringIndexer] in DiacriticsConstants.AllDiacritics):
                stringIndexer += 1;
            if stringIndexer == len(string):
                return True;
            
            if (string[stringIndexer] in DiacriticsConstants.AllDiacritics\
            and voweledForm[voweledPatternsIndexer] in DiacriticsConstants.AllDiacritics):
                #ويكون عندها التشكيلين غير متساويين بسبب الحلقة الصغيرة السابقة
                return False;
            while (voweledForm[voweledPatternsIndexer] in DiacriticsConstants.AllDiacritics):
                voweledPatternsIndexer += 1;
        return True;
    pass

    def ClipString(self, string, lettersCountFromStart, lettersCountFromEnd):
        
        if(lettersCountFromStart+lettersCountFromEnd >= len(string) or len(string) == 0):
            return '';
#        print('------------------------------------------------------------');
        startIndex = 0;
        lettersCounter = 0;
        try:
            while (lettersCounter < lettersCountFromStart): 
#                print('1 len(string) = startIndex = '+str(startIndex)\
#                                +', lettersCounter = '+str(lettersCounter)\
#                                +', string = ' +string+ ', len = '+str(len(string))\
#                                 + ', lettersCountFromStart = ' +str(lettersCountFromStart)\
#                                 + ', lettersCountFromEnd = ' +str(lettersCountFromEnd));            
                startIndex += 1;
                lettersCounter += 1;
#                print("1 startIndex == len(string) = "+str(startIndex == len(string))+\
#                      ', '+str(startIndex)+' == '+str(len(string)));
                if(startIndex == len(string)):
#                    print('2 len(string) = startIndex = '+str(startIndex)\
#                                    +', lettersCounter = '+str(lettersCounter)\
#                                    +', string = ' +string+ ', len = '+str(len(string))\
#                                     + ', lettersCountFromStart = ' +str(lettersCountFromStart)\
#                                     + ', lettersCountFromEnd = ' +str(lettersCountFromEnd));   
                    startIndex -= 1;
                    lettersCounter += 1;
                    break;
                    raise Exception('len(string) = startIndex = '+str(startIndex)\
                                    +', lettersCounter = '+str(lettersCounter)\
                                    +', string = ' +string+ ', len = '+str(len(string))\
                                     + ', lettersCountFromStart = ' +str(lettersCountFromStart)\
                                     + ', lettersCountFromEnd = ' +str(lettersCountFromEnd));
                while (string[startIndex] in DiacriticsConstants.AllDiacritics):
#                    print('3 len(string) = startIndex = '+str(startIndex)\
#                                    +', lettersCounter = '+str(lettersCounter)\
#                                    +', string = ' +string+ ', len = '+str(len(string))\
#                                     + ', lettersCountFromStart = ' +str(lettersCountFromStart)\
#                                     + ', lettersCountFromEnd = ' +str(lettersCountFromEnd));
                    startIndex += 1;
                    if(startIndex == len(string)):
#                        print("2 startIndex == len(string) = "+str(startIndex == len(string))+\
#                              ', '+str(startIndex)+' == '+str(len(string)));
    #                    print('len(string) = startIndex = '+str(startIndex)\
    #                                    +', lettersCounter = '+str(lettersCounter)\
    #                                    +', string = ' +string+ ', len = '+str(len(string))\
    #                                     + ', lettersCountFromStart = ' +str(lettersCountFromStart)\
    #                                     + ', lettersCountFromEnd = ' +str(lettersCountFromEnd));
    #                    raise Exception('len(string) = startIndex = '+str(startIndex)\
    #                                    +', lettersCounter = '+str(lettersCounter)\
    #                                    +', string = ' +string+ ', len = '+str(len(string))\
    #                                     + ', lettersCountFromStart = ' +str(lettersCountFromStart)\
    #                                     + ', lettersCountFromEnd = ' +str(lettersCountFromEnd));
                        startIndex -= 1;
                        break;
        except:
            print('e len(string) = startIndex = '+str(startIndex)\
                            +', lettersCounter = '+str(lettersCounter)\
                            +', string = ' +string+ ', len = '+str(len(string))\
                             + ', lettersCountFromStart = ' +str(lettersCountFromStart)\
                             + ', lettersCountFromEnd = ' +str(lettersCountFromEnd));
            raise Exception('len(string) = startIndex = '+str(startIndex)\
                            +', lettersCounter = '+str(lettersCounter)\
                            +', string = ' +string+ ', len = '+str(len(string))\
                             + ', lettersCountFromStart = ' +str(lettersCountFromStart)\
                             + ', lettersCountFromEnd = ' +str(lettersCountFromEnd));
            
        
        endIndex = 0;
        lettersCounter = 0;
        while (lettersCounter < lettersCountFromEnd):
            if (string[len(string)-1 -endIndex] not in DiacriticsConstants.AllDiacritics):
                lettersCounter += 1;
            endIndex += 1;
#        print('string[startIndex:len(string)-endIndex] = ' + \
#              string[startIndex:len(string)-endIndex]);
        return string[startIndex:len(string)-endIndex];
    pass
    
    def GetDiacratic(self, string, char, startIndex, searchFromRight = False):
#        print(string);
#        print(char);
#        print(startIndex);
#        print(str(searchFromRight));
        
        if(searchFromRight == True):
            if(string.rfind(char, startIndex) == len(string)-1):
                return None;
            letter = string[string.rfind(char, startIndex)+1];
            if(letter in DiacriticsConstants.AllDiacritics):
                return letter;
            else:
                return None;
            
            
        else:            
            if(string.find(char, startIndex) == len(string)-1):
                return None;
            letter = string[string.find(char, startIndex)+1];
            if(letter in DiacriticsConstants.AllDiacritics):
                return letter;
            else:
                return None;
    pass

    def AddDiacratics(self, string, diacratics):
        
        #يمكن معالجة موضوع الشدة لاحقاً فهو الآن غير معالج
        if(len(string)!=len(diacratics)):
            raise Exception('string ['+string+'] with length ['+str(len(string))+']'+\
                            'is not compatible with diacratics ['+diacratics+'] with length ['+str(len(diacratics))+']');
        voweledForm = '';        
        for i in range(len(string)):
            voweledForm = ''.join([voweledForm, string[i],diacratics[i]]);
        return voweledForm;
    pass

    def ColorizeDiacraticInHtml(self, text, cssClassName = "diacritic"):
        resSeq = [];
        for char in text[:]:
            if(char in DiacriticsConstants.AllDiacritics):
                resSeq.append(''.join(['<span class=',cssClassName,'>', char, '</span>']));
            else:
                resSeq.append(char);
        return ''.join(resSeq);
    pass

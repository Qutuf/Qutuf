'''
Created on ١١‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''
#from Lexicon.NormalizationRulesDict import SecondNormDict

'''
This dictionary stores regular expressions... for the normalization phase.
To see this file clear just copy and paste on notepad!
'''
FirstNormDict = dict()
#FirstNormDict[char()] = char()+char();
FirstNormDict[chr(1600)] = ''   #hyphen 
FirstNormDict[chr(1570)] = 'ءا' #alef-mada



'''
This dictionary stores regular expressions... for the normalization phase.
To see this file clear just copy and paste on notepad!
'''
SecondNormDict = dict()
SecondNormDict[chr(1611)] = ''   # fathatan ً ً ً ً ً (SHIFT+W)
SecondNormDict[chr(1612)] = ''   #damatan  ٌ ٌ ٌ ٌ ٌ (SHIFT+R)
SecondNormDict[chr(1613)] = ''   #kasratan ٍ ٍ ٍ ٍ ٍ (SHIFT+S)
SecondNormDict[chr(1614)] = ''   #fathaَََََ (SHIFT+Q)
SecondNormDict[chr(1615)] = ''   #dama ُ ُ ُ ُ ُ (SHIFT+E)
SecondNormDict[chr(1616)] = ''   #kasra ِ ِ ِ ِ ِ (SHIFT+A)
SecondNormDict[chr(1617)] = ''   #shada ّ ّ ّ ّ ّ (SHIFT+`)
SecondNormDict[chr(1618)] = ''   #sokon ْ ْ ْ ْ ْ (SHIFT+X)
#SecondNormDict['ئ'] = 'ء'
#SecondNormDict['ؤ'] = 'ء'
#SecondNormDict['أ'] = 'ء'
#SecondNormDict['إ'] = 'ء'


# -*- coding: utf-8 -*-
'''
Created on ٠٢‏/٠٤‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Morphology.AffixParser import *
from Tokenization.Tokenizer import *

import codecs;



if __name__ == "__main__":
    
    f = codecs.open('..\\..\\Data\\AffixParser_test.txt', 'r', 'utf-8');
    str = f.read();
    print('file encoding: ', f.encoding)
    f.close();
    tok = Tokenizer(str);
    
    ap = AffixParser(tok.Sentences);
    ap.ParsePrefix('..\\..\\Data\\MorphologyTransducers\\Proclitics.xml');
    ap.ParseSuffix('..\\..\\Data\\MorphologyTransducers\\Enclitics.xml');
    
    #Print
    print(tok); 
    print(tok.Sentences[0].Words[0].GetAffixationPosibilities()); 
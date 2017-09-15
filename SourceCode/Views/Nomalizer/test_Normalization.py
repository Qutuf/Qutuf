'''
Created on ١٠‏/٠٣‏/٢٠١٠
ن
@Created by: Muhammad Altabba
'''

from Morphology.MorphologicalAnalyzer import *
from PrematureTagger import PrematureTagger
from Tokenization.Tokenizer import *
from Normalization.Normalizer import Normalizer

if __name__ == '__main__':
    tok = Tokenizer("الْعَرَبــــــِيّةُ");
    norm = Normalizer(tok.Sentences);
    norm.Normalize();

    for i in range(len(norm.Sentences)):
        for j in range(len(norm.Sentences[i].Words)):
            print(norm.Sentences[i].Words[j].OriginalString)
            print(norm.Sentences[i].Words[j].FirstNormalizationForm)
            print(norm.Sentences[i].Words[j].SecondNormalizationForm)
#            
    x = 0;

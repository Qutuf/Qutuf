
'''
Created on ١٠‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from Morphology.MorphologicalAnalyzer import *
from Controllers.Tagging.PrematureTagging.PrematureTagger import PrematureTagger
from Controllers.Tokenization.Tokenizer import *
from Controllers.Normalization.Normalizer import Normalizer

import codecs



if __name__ == '__main__':
    import sys
    print('default encoding: ', sys.getdefaultencoding() );
#    'إذا ما أحببت يمكنك أن تعالج اذا ما بدون همزة أو مع همزة'
#    'كلما رأيت إذا ما. اذا ما وجدت'
    str = '';
    str += 'معالجة إذا ما مع همزة, ';
#    str += 'أو اذا ما بدون همزة.';
#    str += 'إذا رأيت. ';
#    str += 'إذا الشعب يوماً أراد الحياة. ';
    f = codecs.open('..\\..\\Data\\input_test.txt', 'r', 'utf-8');
    str = f.read();
    print('file encoding: ', f.encoding)
    f.close();

    tok = Tokenizer();
    sentences = tok.Tokenize(str);
#    norm = Normalizer(tok.Sentences);
#    norm.Normalize();
    prematureTagger = PrematureTagger(sentences);
    prematureTagger.TagStopWords();
    
    
    prematureTagger.ApplyTaggingRules('..\\..\\Data\\TaggingRepository\\PrematureTaggingRules.xml');
    prematureTagger.InferPrematureTags();
    
    #Print
    print(sentences); 

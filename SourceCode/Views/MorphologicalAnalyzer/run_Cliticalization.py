'''
Created on ٢٢‏/٠٧‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from Models.Lexicon.RootsAndPatternsRepository import *;
from Models.Lexicon.SpecialWords.StandAloneParticle import *;
from Models.Lexicon.SpecialWords.ProperNoun import *;

from Controllers.TextEntities.TextEncapsulator import *;
from Controllers.TextEntities.Word import *;
from Controllers.Tokenization.Tokenizer import *;
from Controllers.Normalization.Normalizer import *;
from Controllers.Morphology.AffixParser import *;
from Controllers.Morphology.MorphologicalAnalyzer import *;

import codecs;
import io;



procliticsXmlFile = '..\\..\\Data\\MorphologyTransducers\\Proclitics.xml';
encliticsXmlFile = '..\\..\\Data\\MorphologyTransducers\\Enclitics.xml';


text = TextEncapsulator();
text.LoadFromFiles(None, None, \
                   procliticsXmlFile, encliticsXmlFile,\
                   None, \
                   None);


f = codecs.open('..\\..\\Data\\Cliticalization_test.txt', 'r', 'utf-8');
string = f.read();
f.close();

text.String = string;
text.Tokenize();
text.Normalize(2);


text.ParseClitics();

print('---------------------------------------------------------------------------');
text.PrintForClitics();
print('---------------------------------------------------------------------------');


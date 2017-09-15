'''
Created on ١١‏/٠٥‏/٢٠١٠

@author: Muhammad Altabba
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

#Set Files Locations Variables:
'''
Change the next few parameters as appropriate.
'''
baseDirectory = "D:\\Qutuf\\Development\\";
baseDirectoryOfQutufDB = baseDirectory + "Data\\";
inputTextFile = baseDirectoryOfQutufDB + 'test_Qutuf.txt';
baseDirectoryOfAlKhalilDB = baseDirectory + 'AlKhalil_V1_Modified\\db\\';
ouputXmlFile = 'D:\\Qutuf\\Development\\Output\\test.xml';
ouputHtmlFile = 'D:\\Qutuf\\Development\\Output\\test.html';


#Set Operations Variables:
prematureTaggingPositiveThreshold = 0.0;
prematureTaggingNegativeThreshold = -0.0;

overdureTaggingThreshold  = None;
overdureTaggingTopReservants  = None;




'''
The next few parameters are fixed do not change them.
'''
procliticsXmlFile = baseDirectoryOfQutufDB + 'MorphologyTransducers\\Proclitics.xml';
encliticsXmlFile = baseDirectoryOfQutufDB + 'MorphologyTransducers\\Enclitics.xml';
prematureTaggingRulesXmlFile = baseDirectoryOfQutufDB + 'TaggingRepository\\PrematureTaggingRules.xml';
overdueTaggingRulesXmlFile = baseDirectoryOfQutufDB + 'TaggingRepository\\OverdueTaggingRules.xml';
rootsFolder = 'roots2'


#Initialize:
text = TextEncapsulator();

#Load Data from Files:
text.LoadFromFiles(baseDirectoryOfAlKhalilDB, rootsFolder, \
                   procliticsXmlFile, encliticsXmlFile,\
                   prematureTaggingRulesXmlFile, \
                   overdueTaggingRulesXmlFile);


#Read input text into Qutuf:
f = codecs.open(inputTextFile, 'r', 'utf-8');
string = f.read();
f.close();
text.String = string;

#Operate:
text.Tokenize();

text.Normalize(2);

text.CompoundParsing();

text.PrematureTagging();

text.ParseClitics();

text.PatternMatching(prematureTaggingPositiveThreshold, prematureTaggingNegativeThreshold);
         
text.OverdueTagging(overdureTaggingThreshold, overdureTaggingTopReservants);


#Print:
print('---------------------------------------------------------------------------');
text.Print();
print('---------------------------------------------------------------------------');


#Write Output Files:
xmlStreamWriter = io.StringIO();
text.RenderHtml(xmlStreamWriter);
writer = codecs.open(ouputHtmlFile, 'w', 'utf-8');
writer.write(xmlStreamWriter.getvalue());
writer.close();

xmlStreamWriter = io.StringIO();
text.RenderXml(xmlStreamWriter);
writer = codecs.open(ouputXmlFile, 'w', 'utf-8');
writer.write(xmlStreamWriter.getvalue());
writer.close();

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
import os;
from os.path import join, getsize;



compoundNounsXmlFile = '../../Data/MorphologyTransducers/Proclitics.xml';
procliticsXmlFile = '../../Data/MorphologyTransducers/Proclitics.xml';
encliticsXmlFile = '../../Data/MorphologyTransducers/Enclitics.xml';
prematureTaggingRulesXmlFile = '../../Data/TaggingRepository/PrematureTaggingRules.xml';
overdueTaggingRulesXmlFile = '../../Data/TaggingRepository/OverdueTaggingRules.xml';
baseDirectoryOfAlKhalil = 'D:/temp/AlKhalil_1/db/'
rootsFolder = 'roots2'

prematureTaggingPositiveThreshold = None;


overdureTaggingThreshold  = None;
overdureTaggingTopReservants  = None;

text = TextEncapsulator();
text.LoadFromFiles(baseDirectoryOfAlKhalil, rootsFolder, \
                   procliticsXmlFile, encliticsXmlFile,\
                   prematureTaggingRulesXmlFile, \
                   overdueTaggingRulesXmlFile);

base = 'D:/temp/Latifa2/'




for root, dirs, files in os.walk(base):
        for file in files:
            if file.endswith('.txt') and file.find('-') == -1 : 
                print('\tStart parsing file: ['+file+']');
                
                f = codecs.open('/'.join([root, file]), 'r', 'utf-8');
                string = f.read();
                f.close();
                
                text.String = string;
                text.Tokenize();
                text.Normalize(2);
                
                text.ParseClitics();
                
                print('\tProcessing...');
                
                rootsAndStems = text.StemmingAndRooting();
                
                print('\tWriting...');
                
                xmlStreamWriter = io.StringIO();
                text.RenderXmlStemsAndRootsFlat(xmlStreamWriter, rootsAndStems);
                writer = codecs.open('/'.join([root, file.replace('.txt','.xml')]), 'w', 'utf-8');
                writer.write(xmlStreamWriter.getvalue());
                xmlStreamWriter.close();
                writer.close();
                
                print ('\tEnd parsing file: ['+file+']');
                print('------------------------------------------------------');
#                exit(0);
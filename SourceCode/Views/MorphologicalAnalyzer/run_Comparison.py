

'''
Created on ١١‏/٠٥‏/٢٠١٠

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



compoundNounsXmlFile = '..\\..\\Data\\MorphologyTransducers\\Proclitics.xml';
procliticsXmlFile = '..\\..\\Data\\MorphologyTransducers\\Proclitics.xml';
encliticsXmlFile = '..\\..\\Data\\MorphologyTransducers\\Enclitics.xml';
prematureTaggingRulesXmlFile = '..\\..\\Data\\TaggingRepository\\PrematureTaggingRules.xml';
overdueTaggingRulesXmlFile = '..\\..\\Data\\TaggingRepository\\OverdueTaggingRules.xml';
baseDirectoryOfAlKhalil = 'D:\\temp\\AlKhalil_1\\db\\'
rootsFolder = 'roots2'


text = TextEncapsulator();
text.LoadFromFiles(baseDirectoryOfAlKhalil, rootsFolder, \
                   procliticsXmlFile, encliticsXmlFile,\
                   prematureTaggingRulesXmlFile, \
                   overdueTaggingRulesXmlFile);

base = 'D:\\temp\\Latifa2\\'




for root, dirs, files in os.walk(base):
    for dir in dirs:
        print('Start parsing directory: ['+dir+']');
        for subroot, subdirs, subfiles in os.walk(root+dir):
            for file in subfiles:
                if file.endswith('.txt') and file.find('-') == -1 :  
                    if(file.find('Edu') == -1 ):
                        continue;
                    print('\tStart parsing file: ['+file+']');
                    
                    f = codecs.open('\\'.join([subroot, file]), 'r', 'utf-8');
                    string = f.read();
                    f.close();
                    
                    text.String = string;
                    text.Tokenize();
                    text.Normalize(2);
                    
                    text.ParseClitics();
                    
                    print('\tProcessing...');
                    
                    text.PatternMatchingSimpleStem();
                    
                    print('\tWriting...');
                    
                    xmlStreamWriter = io.StringIO();
                    text.RenderTextSimpleStem(xmlStreamWriter);
                    writer = codecs.open('\\'.join([subroot, file.replace('.txt','-Qutuf.txt')]), 'w', 'utf-8');
                    writer.write(xmlStreamWriter.getvalue());
                    xmlStreamWriter.close();
                    writer.close();
                    
                    print ('\tEnd parsing file: ['+file+']');
                    print('------------------------------------------------------');
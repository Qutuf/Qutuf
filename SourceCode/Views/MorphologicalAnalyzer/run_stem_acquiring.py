# -*- coding: utf-8 -*-
'''
Created on ١٧‏/٠٥‏/٢٠١٠

@Created by: Muhammad Altabba

'''

from Lexicon.RootsAndPatternsRepository import *;
from TextEntities.Word import *;
from Tokenization.Tokenizer import *
from Normalization.Normalizer import *
from Morphology.AffixParser import *
from Morphology.MorphologicalAnalyzer import *;

import codecs;
import io;

MAX_EXAMPLES_COUNT = 15;

def GetAppliedRootsWithExamples(pattern, rootRule, conditionallyApplicableRoots):
    applicableRoots = [];
    examples = [];
    
    for i in range(len(conditionallyApplicableRoots)):
        if(len(rootRule) != len(conditionallyApplicableRoots[i].String)):
            continue;
        
        generatedWord = io.StringIO();
        
        rootIndexCounter = 0;
        for j in range(len(pattern.String)):
            while(rootIndexCounter < len(rootRule) and not rootRule[rootIndexCounter].isdigit()):
                rootIndexCounter += 1;
            if(rootIndexCounter < len(rootRule)):
                index = int(rootRule[rootIndexCounter]) - 1;
                if(j == index):
#                    if(len(conditionallyApplicableRoots[i].String) <= rootIndexCounter):
#                        break;
                    generatedWord.write(conditionallyApplicableRoots[i].String[rootIndexCounter]);
                    rootIndexCounter +=1 ;
                else:
                    generatedWord.write(pattern.String[j]);
            else:
                generatedWord.write(pattern.String[j]);
        
        generatedWord = generatedWord.getvalue();
        newRoot = '';
        for k in range(len(rootRule)):
            if(rootRule[k].isnumeric()):
                newRoot += generatedWord[int(rootRule[k])-1];
            else:
                newRoot += rootRule[k];
        
        if (newRoot ==  conditionallyApplicableRoots[i].String):
            applicableRoots.append(newRoot);
            examples.append(generatedWord);
        if(i > MAX_EXAMPLES_COUNT):
            break;
    
    return [applicableRoots, examples];



def SaveAcquire(unvoweledPatterns, roots, fileName):
    f = codecs.open(fileName, 'w', 'utf-8');
    counter = 1;
    for patternLength, patterns in unvoweledPatterns.items():
#        row = io.StringIO();
        f.write('\n;الأوزان التي بطول (' + str(patternLength) + ') وعددها (' + str(len(patterns)) + '):');
        f.write('\nالرقم;الوزن;الجذور;;الأصل;الجذوع;أمثلة على الجذور;');
#        f.write(row.getvalue());
        for patternString, pattern in patterns.items():
            
            f.write('\n');
            f.write(str(counter));
            f.write(';');
            f.write(patternString);
            f.write(';');
            
            [rootStrings, rootRules] = pattern.GetRootsStringsAndRules(None);
            
            
            conditionallyApplicableRoots = [];
            for letter, rootItems in roots.items():
                for rootString, rootItem in rootItems.items():
                    for k in range(len(pattern.IDs)):                        
                        if(rootItem.PatternsIDs.count(pattern.IDs[k]) > 0 \
                           and conditionallyApplicableRoots.count(rootItem) == 0):
                            conditionallyApplicableRoots.append(rootItem);
            
            for j in range(len(rootStrings)):
                if j != 0:
                    f.write('\n');
                    f.write(str(counter));
                    f.write(';');
                    f.write(';');
                counter += 1;
                f.write(''.join(list(rootRules[j])) + ';(' + rootStrings[j] + ')');
                [applicableRoots, examples] = GetAppliedRootsWithExamples(pattern, rootRules[j], conditionallyApplicableRoots);
                
                for k in range(len(applicableRoots)):
                    f.write(''.join([';', applicableRoots[k], ';', examples[k]]));

            
                
            f.write(';');            
                
            f.flush();
                
                                        
    
    f.close();
    pass



wordDB = RootsAndPatternsRepository();
wordDB.Load('D:\\temp\\AlKhalil_1\\db\\', 'roots2');

SaveAcquire(wordDB.UnvoweledVerbalPatterns, wordDB.VerbalRoots, '..\\..\\Data\\stem_acquiring_verbal.csv')

SaveAcquire(wordDB.UnvoweledNominalPatterns, wordDB.NominalRoots, '..\\..\\Data\\stem_acquiring_nominal.csv')


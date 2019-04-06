
'''
Created on ٢٩‏/٠٤‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from ..Lexicon.RootAndPatterns.Root import *;
from ..Lexicon.RootAndPatterns.UnvoweledPattern import *;
from ..Lexicon.RootAndPatterns.VoweledPattern import *;
from ..Lexicon.RootAndPatterns.VoweledNominalPattern import *;
from ..Lexicon.RootAndPatterns.VoweledVerbalPattern import *;

from xml.dom import minidom;
import os;
from os.path import join, getsize;

Error_Log = [];

class RootsAndPatternsRepository(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0Bf1435Ed-gg8GOK1TmhA
    """
    '''
    classdocs
    '''
    NominalRoots = dict();
    VoweledNominalPatterns = dict();
    UnvoweledNominalPatterns = dict();
    
    VerbalRoots = dict();
    VoweledVerbalPatterns = dict();
    UnvoweledVerbalPatterns = dict();
    
    
    
    def __init__(self):
        '''
        Constructor
        '''
        self.NominalRoots = [];
        self.VoweledNominalPatterns = {};
        self.UnvoweledNominalPatterns = {};
        
        self.VerbalRoots = [];
        self.VoweledVerbalPatterns = {};
        self.UnvoweledVerbalPatterns = {};
        
    pass
    
    def Load(self, basePath, rootsFolder):
        #example: basePath= 'D:\1\Learning\NLP\برامج\الخليل\AlKhalil_1\db\';
                
        self.NominalRoots = self.LoadRoots(basePath + 'nouns/'+ rootsFolder +'/');
        self.VerbalRoots = self.LoadRoots(basePath + 'verbs/'+ rootsFolder +'/');
        self.UnvoweledNominalPatterns = self.LoadUnvoweledPatterns(basePath + 'nouns/patterns/Unvoweled/');
        self.UnvoweledVerbalPatterns = self.LoadUnvoweledPatterns(basePath + 'verbs/patterns/Unvoweled/');
        self.VoweledNominalPatterns = self.LoadVoweledNominalPatterns(basePath + 'nouns/patterns/Voweled/');
        self.VoweledVerbalPatterns = self.LoadVoweledVerbalPatterns(basePath + 'verbs/patterns/Voweled/');
        
        
    pass
    
    # Return Roots in an in-memory dictionary:
    def LoadRoots(self, path):
        
        tempDict = dict();
        
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.xml'):
                    tempSubDict = {};
                    xmldoc = minidom.parse(root+file);
                    for xmlRoot in xmldoc.getElementsByTagName('root'):
                        val = xmlRoot.attributes['val'].value;
                        vect = xmlRoot.attributes['vect'].value.split();
                        vect = [int(x) for x in vect];
                        
                        tempSubDict[val] = Root(val,vect);
                    tempDict[file[0]] = tempSubDict;

        return tempDict;
    pass
    
    # Return Unvoweled Patterns in an in-memory dictionary:
    def LoadUnvoweledPatterns(self, path):
        
        tempDict = {}; #Based on word length.
        
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.xml'):
                    tempSubDict = {}; #Based on the String of the Pattern 
                    tempDict[int(file[file.find('.')-1])] = tempSubDict;
                    xmldoc = minidom.parse(root+file);
                    for xmlRoot in xmldoc.getElementsByTagName('pattern'):
                        value = xmlRoot.attributes['value'].value;
                        rules = xmlRoot.attributes['rules'].value.split();
                        ids = xmlRoot.attributes['ids'].value.split();
                        ids = [int(x) for x in ids];
                        tempSubDict[value] = UnvoweledPattern(value, rules, ids);

        return tempDict;
    pass
        
    # Return Voweled Patterns in an in-memory dictionary:
    def LoadVoweledNominalPatterns(self, path):
        
        tempDict = {}; #Based on word length.
        
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.xml'):
                    tempSubDict = {}; #Based on IDs
                    tempDict[int(file[file.find('.')-1])] = tempSubDict;
                    xmldoc = minidom.parse(root+file);
                    for xmlRoot in xmldoc.getElementsByTagName('pattern'):
                        id = int(xmlRoot.attributes['id'].value);
                        diac = xmlRoot.attributes['diac'].value;
                        canonic = xmlRoot.attributes['canonic'].value;
                        type = xmlRoot.attributes['type'].value;
                        cas = xmlRoot.attributes['cas'].value;
                        ncg = xmlRoot.attributes['ncg'].value;
                        
                        if(ncg == ''):
                            Error_Log.append('Error At file [VoweledNominalPattern'+file[file.find('.')-1]+'.xml], for pattern with [id = '+str(id)+']'\
                                             +'\n\tthe [type] attribute\'s value ['+type+']!, '\
                                             +'\n\tthe [cas] attribute\'s value ['+cas+']!'\
                                             +'\n\t and the [ncg] attribute is empty!')
                            ncg = cas;
                            cas = type;
                            type = '';
                        
                        voweledPattern = VoweledNominalPattern(id, diac, canonic);
                        
                        if(type == 'ص'):
                            Error_Log.append('Error At file [VoweledNominalPattern'+file[file.find('.')-1]+'.xml], for pattern with [id = '+str(id)+']'\
                                             +'\n\tthe [type] attribute\'s value ['+type+']! which is undefined,'\
                                             +'\n\tthe [cas] attribute\'s value ['+cas+']'\
                                             +'\n\tand the [ncg] attribute\'s value ['+ncg+'!')
                            type = "صأ"
                            
                        voweledPattern.AssignFromAlKhalilDB(type, cas, ncg);
                        tempSubDict[id] = voweledPattern;

        return tempDict;
    pass
        
    # Return Voweled Verbal Patterns in an in-memory dictionary:
    def LoadVoweledVerbalPatterns(self, path):
        
        tempDict = {}; #Based on word length.
        
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.xml'):
                    tempSubDict = {}; #Based on IDs
                    tempDict[int(file[file.find('.')-1])] = tempSubDict;
                    xmldoc = minidom.parse(root+file);
                    for xmlRoot in xmldoc.getElementsByTagName('pattern'):
                        id = int(xmlRoot.attributes['id'].value);
                        diac = xmlRoot.attributes['diac'].value;
                        canonic = xmlRoot.attributes['canonic'].value;
                        type = xmlRoot.attributes['type'].value;
                        cas = xmlRoot.attributes['cas'].value;
                        ncg = xmlRoot.attributes['ncg'].value;
                        aug = xmlRoot.attributes['aug'].value;
                        trans = xmlRoot.attributes['trans'].value;
                        
                        voweledPattern = VoweledVerbalPattern(id, diac, canonic);
                        voweledPattern.AssignFromAlKhalilDB(type, cas, ncg, aug, trans);
                        tempSubDict[id] = voweledPattern;

        return tempDict;
    pass

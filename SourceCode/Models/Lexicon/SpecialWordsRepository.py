
'''
Created on ٢٨‏/٠٦‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from xml.dom import minidom

from ..Lexicon.SpecialWords.StandAloneParticle import *;
from ..Lexicon.SpecialWords.ProperNoun import *;
from ..Lexicon.SpecialWords.ClosedNouns import *;

from ...Controllers.Morphology.Entities.UnderivedCliticless import UnderivedCliticless;
from ..Tagging.POSTags.POS import POSConstants;
from ..Tagging.POSTags.NominalPOS import *;

class SpecialWordsRepository(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_q0BgAo35Ed-gg8GOK1TmhA
    """
    '''
    Special Words Loader
    '''

    ProperNouns = dict();
    
    Particles = dict();
    
    ClosedNouns = dict();
    
    CompoundNouns = dict();
    
    def __init__(self):
        '''
        Constructor
        '''
        
        self.ProperNouns = dict();
        
        self.Particles = dict();
        
        self.ClosedNouns = dict();
        
        self.CompoundNouns = dict();
    pass

    def Load(self, basePath):

        self.ProperNouns = self.LoadProperNouns(basePath + 'specialwords/');
        self.Particles = self.LoadParticles(basePath + 'specialwords/');
        
        file = 'closednouns.xml';
        self.ClosedNouns = self.LoadClosedNouns(basePath + 'specialwords/', file);
        file = 'compoundnouns.xml';
        self.CompoundNouns = self.LoadClosedNouns(basePath + 'specialwords/', file);
    pass


    def LoadProperNouns(self, path):
        
        file = 'propernouns.xml';
        tempDict = dict();
        xmldoc = minidom.parse(path + file);
        for xmlRoot in xmldoc.getElementsByTagName('propernoun'):
            unvoweled = xmlRoot.attributes['unvoweledform'].value;
            voweled = xmlRoot.attributes['voweledform'].value;
            
#            tempDict[unvoweled] = ProperNoun(unvoweled, voweled);

            if(unvoweled not in tempDict.keys()):
                tempDict[unvoweled] = [ProperNoun(unvoweled, voweled)];
            else:
#                print(str(type(tempDict[unvoweled])));
                tempDict[unvoweled].append(ProperNoun(unvoweled, voweled));
            
        return tempDict;
    pass
    
    
    def LoadClosedNouns(self, path, file):
        
        tempDict = dict();
        xmldoc = minidom.parse(path + file);
        for xmlRoot in xmldoc.getElementsByTagName('noun'):
            unvoweled = xmlRoot.attributes['unvoweledform'].value;
            voweled = xmlRoot.attributes['voweledform'].value;
            prefixeclass = xmlRoot.attributes['prefixeclass'].value;
            suffixeclass = xmlRoot.attributes['suffixeclass'].value;
            type = xmlRoot.attributes['type'].value;
            
            if('case' in xmlRoot.attributes.keys()):
                case = xmlRoot.attributes['case'].value;
            else:
                case = '';                
            
            if('gender' in xmlRoot.attributes.keys()):
                gender = xmlRoot.attributes['gender'].value;
            else:
                gender = '';
                
            
            if('number' in xmlRoot.attributes.keys()):
                number = xmlRoot.attributes['number'].value;
            else:
                number = '';
               
            definiteness = xmlRoot.attributes['definiteness'].value;
            
            closedNoun = ClosedNoun(unvoweled, voweled);
            closedNoun.AssignFromAlKalilDB(prefixeclass, suffixeclass,\
                type, definiteness, gender, case, number);
            
            if(unvoweled not in tempDict.keys()):
                tempDict[unvoweled] = [closedNoun];
            else:
                tempDict[unvoweled].append(closedNoun);
            
        return tempDict;
    pass
    
    
    def LoadParticles(self, path):
        
        file = 'standaloneparticles.xml';
        
        tempDict = dict();
        tempList = [];
        xmldoc = minidom.parse(path + file);
        for xmlRoot in xmldoc.getElementsByTagName('particle'):
            unvoweled = xmlRoot.attributes['unvoweledform'].value;
            voweled = xmlRoot.attributes['voweledform'].value;
            prefixeclass = xmlRoot.attributes['prefixeclass'].value;
            suffixeclass = xmlRoot.attributes['suffixeclass'].value;
            type = xmlRoot.attributes['type'].value;
            
            particle = StandAloneParticle();
            particle.AssignFromAlKalilDB(unvoweled, voweled, prefixeclass, suffixeclass, type);
            
            tempList.append(particle);            
            if(unvoweled not in tempDict.keys()):
                tempDict[unvoweled] = [];
            tempDict[unvoweled].append(len(tempList)-1);
            
        return [tempDict, tempList];
    pass
    

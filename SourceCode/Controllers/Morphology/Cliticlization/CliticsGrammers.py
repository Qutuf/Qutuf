
'''
Created on ٠٢‏/٠٧‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from ...General.ArabicStringUtility import ArabicStringUtility;
from ...Morphology.Entities.Particle import *;
from ....Models.Tagging.POSTags.ParticlePOS import *;
from ....Models.Tagging.POSTags.POS import *;
from ....Models.Tagging.POSTags.CliticlessPOS import CliticlessPOSConstants, CliticlessPOS;

from ...Morphology.Cliticlization.EncliticGrammer import EncliticGrammer;


class CliticsGrammers(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_hULWbY34Ed-gg8GOK1TmhA
    """
    '''
    classdocs
    '''

    GrammersDict = {};

    def __init__(self):
        '''
        Constructor
        '''
    pass

    

    def GetConsistentClitics(self, word, allCliticlesses, cliticsStrings, cliticState):

        if(len(cliticsStrings)== 0 or (len(cliticsStrings) ==1 and cliticsStrings[0][0] == '')):
            consistentClitics = [];
            
            #need to be changed!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            consistentClitics.append([]);
            consistentClitics[0].append([]);
            consistentClitics[0].append(allCliticlesses);
#            for i in range(len(allCliticlesses)):
#                consistentClitics.append([]);
#                hiddenClitic = self.GetHiddenClitics(allCliticlesses[i], cliticState);
#                consistentClitics[i].append(hiddenClitic);
#                consistentClitics[i].append(allCliticlesses[i]);
            return consistentClitics;
        
        
        allCliticsPossibilities = [];
        for j in range(len(cliticsStrings)):
            clticString = cliticsStrings[j][0];
            if(clticString == ''):
                continue;
            if(clticString not in self.GrammersDict.keys()):
                raise Exception('cltic ['+str(clticString)+'] is not found in the CliticsGrammers Dictionary! at ['+str(type(self))+']');
        
            oneCliticPossibilities = {};
            
            #Get all possibilities of particles with their grammars:
            if(cliticState == ParticleConstants.State.Enclitic):
                clticDiacratic = word.GetDiacratic(clticString, True);
            else:
                clticDiacratic = word.GetDiacratic(clticString, False);
                
            for diacratic, procliticGrammers in self.GrammersDict[clticString].items():
                if(clticDiacratic != None and clticDiacratic != diacratic):
                    continue;
                for cliticGrammer in procliticGrammers:
                    clticWithDiacritics = ArabicStringUtility.AddDiacratics(ArabicStringUtility, clticString, diacratic)
                    particle = cliticGrammer.CreateClitic(clticString, clticWithDiacritics, cliticState);
                    particle.Grammar = cliticGrammer;
        
                    for k in range(len(allCliticlesses)):
                        cliticless = allCliticlesses[k];
                        
                        #إذا لم تتوافق أحد اللواصق البادئة مع الكلمة فلا يجب أن تضاف
                        if(not cliticGrammer.IsCompatible(cliticless)):
                            continue;              

                        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        #Add hook: من أجل الواو الناتجة عن إشباع ضمة الميم
                        if(not (type(cliticless) is Particle) and clticString == 'و' and cliticState == ParticleConstants.State.Enclitic and
                           j == 0):
                            if(cliticless.POS.Gender != CliticlessPOSConstants.Gender.Masculine or\
                               cliticless.POS.Number != CliticlessPOSConstants.Number.Plural or\
                               cliticless.POS.Person != CliticlessPOSConstants.Person.Third_Person):
                                continue;                   

                        if(particle not in oneCliticPossibilities.keys()):
                            oneCliticPossibilities[particle] = [];
                        oneCliticPossibilities[particle].append(cliticless);
                    
                    
                
            
            allCliticsPossibilities.append(oneCliticPossibilities);
        
        #إعادة ترتيب
        seq = [];
        for k in range(len(allCliticsPossibilities)):
            seq.append([]);
            counter = 0;
            for key, value in allCliticsPossibilities[k].items():
                if(k ==0):
                    seq[k].append( [[key],value] );
                else:
                    for s in range(len(seq[k-1])):
                        if(not key.Grammar.IsConsistentWith(seq[k-1][s][0])):
                            continue;
                        intersection = self.__Intersect(value, seq[k-1][s][1]);
                        if(intersection == []):
                            continue;
                        li = [x for x in seq[k-1][s][0]];
                        li.append(key);
                        seq[k].append([li, intersection]);

                counter += 1; 


        ##################################################
        #need testing:
        result = self.GetHiddenClitics(word);
        ##################################################
        if(len(seq) > 1):
            result.extend(seq[len(seq)-1]);
        elif(seq != []):
            result.extend(seq[0]);
        else:
            result.extend(seq);
            
            
        return result;
    pass

    def GetHiddenClitics(self, cliticlessWord):

        return [];
    pass


    def __Intersect(self, list1, list2):
        intersection = [];
        for i in range(len(list1)):
            for j in range(len(list2)):
                if(list1[i] == list2[j]):
                    intersection.append(list1[i]);
        return intersection;
    pass

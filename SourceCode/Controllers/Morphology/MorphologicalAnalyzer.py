'''
Created on ١١‏/٠٥‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Models.Lexicon.RootsAndPatternsRepository import *;
from Models.Lexicon.LettersConstants import *;
from Models.Lexicon.LettersConstants import *;
from Models.Tagging.POSTags.CliticlessPOS import *;
from Models.Tagging.POSTags.NominalPOS import NominalPOSConstants;

from Controllers.General.ArabicStringUtility import ArabicStringUtility;
from Controllers.Morphology.Cliticlization.ProcliticsGrammers import ProcliticsGrammers;
from Controllers.Morphology.Cliticlization.EncliticsGrammers import EncliticsGrammers;
from Controllers.Morphology.Entities.Particle import *;
from Controllers.Morphology.Entities.DerivedCliticless import DerivedCliticless;
from Controllers.Morphology.Entities.UnderivedCliticless import UnderivedCliticless;
from Controllers.Morphology.Entities.SurfaceFormMorphemes import SurfaceFormMorphemes;


class MorphologicalAnalyzer(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyiSy435Ed-gg8GOK1TmhA
    """
    '''
    Pattern Matcher
    '''
    __RootsAndPatternsRepository = None;
    __SpecialWordsRepository = None;
    
    PrematureTaggingPositiveThreshold = None;
    PrematureTaggingNegativeThreshold = None;
    
    def __init__(self):
        '''
        Constructor
        '''
        
        self.__RootsAndPatternsRepository = None;
        self.__SpecialWordsRepository = None;
        
        self.PrematureTaggingPositiveThreshold = None;
        self.PrematureTaggingNegativeThreshold = None;
    pass

    def SetRepositories(self, rootsAndPatternsRepository, specialWordsRepository):

        self.__RootsAndPatternsRepository = rootsAndPatternsRepository;
        self.__SpecialWordsRepository = specialWordsRepository;
        
    pass

    def __SubMatch(self, word, string, cliticlessWithDiacritics, allRoots, unvoweledPatterns, voweledPatterns, affixationPossibility):
        unvoweledPatterns = unvoweledPatterns[len(string)];
        matchedUnvoweledPatterns = self.MatchStringWithUnvoweledPatterns(string, unvoweledPatterns);
        underivedCliticlesss = [];
        if len(matchedUnvoweledPatterns) > 0:
            string = affixationPossibility[1];
            #استخراج الجذور لكل وزن:
            possibleRoots = self.__GetRoots(string, matchedUnvoweledPatterns, allRoots);
            # أخذ التقاطعات للأوزان المشّكلة بين قائمة الجذور وقائمة الأوزان الغير مشكّلة:
            if(len(matchedUnvoweledPatterns) == 0):
                return [];
            matchedVoweledPatterns = self.__GetIntersectionsOfVoweledPatterns(matchedUnvoweledPatterns, possibleRoots, voweledPatterns);
            subMatches = self.GetRefinedMatchStructure(cliticlessWithDiacritics, possibleRoots, matchedUnvoweledPatterns, matchedVoweledPatterns);
            
            subMatches = self.EliminateInconsistentMatches(subMatches);
            
            underivedCliticlesss = self.FillIntoDerivedCliticlesss(subMatches);
        
        return underivedCliticlesss;
    pass


    def FillIntoDerivedCliticlesss(self, subMatches):
        derivedWords = [];
        for i in range(len(subMatches)):
            cliticlessWithDiacritics = subMatches[i][0];
            root = subMatches[i][1];
            unvoweledpattern = subMatches[i][2];
            voweledpatterns = subMatches[i][3];
            
            for j in range(len(voweledpatterns)):
                derivedWord = DerivedCliticless(cliticlessWithDiacritics, root, unvoweledpattern, voweledpatterns[j]);
                ###############################################################
                if(derivedWord.IsHamzaCompatibleWithVoweldForm()):
                    derivedWords.append(derivedWord);
        return derivedWords;
    pass





    def __MatchVerbs(self, word, string, cliticlessWithDiacritics, affixationPossibility):
        
        if (len(string) in self.__RootsAndPatternsRepository.UnvoweledVerbalPatterns.keys()):
            
            allRoots = self.__RootsAndPatternsRepository.VerbalRoots;
            unvoweledPatterns = self.__RootsAndPatternsRepository.UnvoweledVerbalPatterns;
            voweledPatterns = self.__RootsAndPatternsRepository.VoweledVerbalPatterns;
            subMatch = self.__SubMatch(word, string, cliticlessWithDiacritics, allRoots, unvoweledPatterns, voweledPatterns, affixationPossibility);

            return subMatch;
        else:
            return [];
    
    pass

    def __MatchNouns(self, word, string, cliticlessWithDiacritics, affixationPossibility, isIndefiniteNoun):
        
        subMatch = [];
        #الأسماء المحددة - (المحصورة بقوائم) مثل الأسماء الموصولة والضمائر                 
        if(isIndefiniteNoun != True and string in self.__SpecialWordsRepository.ClosedNouns.keys()):
            for closedNoun in self.__SpecialWordsRepository.ClosedNouns[string]:
#               closedNoun = self.__SpecialWordsRepository.ClosedNouns[string];
                isCompatible = ArabicStringUtility.IsCompatible(ArabicStringUtility, cliticlessWithDiacritics, closedNoun.VoweledForm);
                if(isCompatible == True):
                    subMatch.append(closedNoun.ReturnAsUnderivedCliticless());
        
        
        #أسماء العلم
#       if(isIndefiniteNoun != True and string in self.__SpecialWordsRepository.ProperNouns.keys()):
        if(string in self.__SpecialWordsRepository.ProperNouns.keys()):   
            for properNoun in self.__SpecialWordsRepository.ProperNouns[string]:
#       properNoun = self.__SpecialWordsRepository.ProperNouns[string];
                isCompatible = ArabicStringUtility.IsCompatible(ArabicStringUtility, cliticlessWithDiacritics, properNoun.VoweledForm);
                if(isCompatible == True):                            
                    underivedCliticless = properNoun.ReturnAsUnderivedCliticless();
                    underivedCliticless.OriginalString = cliticlessWithDiacritics;

        #يمكن استخدامها بعد معالجة الحالات الممنوعة من الصرف
#       lastDiacritic = cliticlessWithDiacritics[len(cliticlessWithDiacritics)-1];
#       if(lastDiacritic in DiacriticsConstants.AllDiacritics):
#           self.AssignCaseAccordingToLastDiacritic(underivedCliticless.POS, lastDiacritic);
                    subMatch.append(underivedCliticless);
        
        
        #معالجة الأسماء المشتقة
        if len(string) in self.__RootsAndPatternsRepository.UnvoweledNominalPatterns.keys():
            allRoots = self.__RootsAndPatternsRepository.NominalRoots;
            unvoweledPatterns = self.__RootsAndPatternsRepository.UnvoweledNominalPatterns;
            voweledPatterns = self.__RootsAndPatternsRepository.VoweledNominalPatterns;
            
            derivedMatches = self.__SubMatch(word, string, cliticlessWithDiacritics, allRoots, unvoweledPatterns, voweledPatterns, affixationPossibility);
            
            for derivedMatch in derivedMatches:
                if(affixationPossibility[0][len(affixationPossibility[0])-1][0] != 'ال' and \
                    derivedMatch.POS.Definiteness & NominalPOSConstants.Definiteness.Definite_by_Itself != 0):
                    derivedMatch.POS.Definiteness -= NominalPOSConstants.Definiteness.Definite_by_Itself;
            subMatch.extend(derivedMatches);
                


        return subMatch;
    
    pass

    def Match(self, word):
        
        affixationPossibilities = word.GetAffixationPosibilities();

        isIndefiniteNoun = False;
        isVerb = None;
        
        if(word.OriginalString[len(word.OriginalString)-1] in ['ً', 'ٍ', 'ٌ']):
            #إذا كانت منوّنة فهي اسم نكرة
            isIndefiniteNoun = True;
            

        matches = [];
        i = 0;
        while i < len(affixationPossibilities):
            string = affixationPossibilities[i][1];
            affixationPossibility = affixationPossibilities[i];
            subMatches = [];
            prefixType = affixationPossibility[0][len(affixationPossibility[0])-1][1];
            suffixType = affixationPossibility[2][len(affixationPossibility[2])-1][1];
            
            #للحصول على الكلمة المدخلة بتشكيلها ولكن بدون لواصق 
            procliticsLen = 0;
            for k in range(len(affixationPossibility[0])):
                procliticsLen += len(affixationPossibility[0][k][0]);
            encliticsLen = 0;
            for k in range(len(affixationPossibility[2])):
                encliticsLen += len(affixationPossibility[2][k][0]);            
            cliticlessWithDiacritics = word.ClipString(1, procliticsLen, encliticsLen);
            
            if(len(cliticlessWithDiacritics) == 0):
                affixationPossibilities.remove(affixationPossibilities[i]);
                continue;
            
            
            #إذا انتهت الكلمة بساكن ليس حرف علة فهي حتماً فعل  
            if(cliticlessWithDiacritics.endswith(DiacriticsConstants.Sukoon) and \
               cliticlessWithDiacritics[len(cliticlessWithDiacritics)-2] not in EllaConstants.AllAhrofElla):
                isVerb = True;
        
            
#            print('PrematureTaggingPositiveThreshold = ', self.PrematureTaggingPositiveThreshold);
#            print(', prematureTaggingNegativeThreshold = ', self.PrematureTaggingNegativeThreshold);
#            print('word.PrematureTags = ', word.PrematureTags);
            
            
            topKeys = word.GetTopPrematureTagsKeys(word)
#            print('max = ', str(max), ', topKeys = ', str(topKeys));
            
            
            #معالجة الأفعال
            if(isIndefiniteNoun != True and prefixType in ['c','v'] and suffixType in ['c','v']\
                and ('Verb' in topKeys \
                    or \
                    'Verb' not in word.PrematureTags.keys() \
                    or \
                    ((self.PrematureTaggingPositiveThreshold == None or \
                        word.PrematureTags['Verb'] < 0 or \
                        word.PrematureTags['Verb'] >= 0 and word.PrematureTags['Verb'] >= self.PrematureTaggingPositiveThreshold)
                    and \
                    (self.PrematureTaggingNegativeThreshold == None or \
                    word.PrematureTags['Verb'] >= 0 or \
                    word.PrematureTags['Verb'] < 0 and word.PrematureTags['Verb'] >= self.PrematureTaggingNegativeThreshold)))):
                
                subMatch = self.__MatchVerbs(word, string, cliticlessWithDiacritics, affixationPossibility);

                #if the enclitics has more than ('', 'c') and the verb ends with 'و'
                if (len(affixationPossibility[2]) > 1 and string.endswith('و')):
#                    print('منته بواو')
                    verbSubMatches = self.__MatchVerbs(word, string + 'ا', cliticlessWithDiacritics + 'ا', affixationPossibility);

                    for match in verbSubMatches:
                        match.OriginalString = cliticlessWithDiacritics;
                        match.UnvoweledForm = string;
                        match.VoweledForm = match.VoweledForm[0:match.VoweledForm.rfind('ا')];
                    subMatch.extend(verbSubMatches);

                subMatches.extend(subMatch);
            
            
            #معالجة الأحرف
            if(isIndefiniteNoun != True and prefixType in ['c'] and suffixType in ['c']\
                and ('Particle' in topKeys or \
                    self.PrematureTaggingPositiveThreshold == None or \
                    'Particle' not in word.PrematureTags.keys() or \
                    word.PrematureTags['Particle'] >= self.PrematureTaggingPositiveThreshold)\
                and isVerb != True):
                #إذا انتهت الكلمة بساكن ليس حرف علة فهي حتماً فعل  
#                if(cliticlessWithDiacritics.endwith(sokoon) and \
#                   cliticlessWithDiacritics[len(cliticlessWithDiacritics)-2] not in ahrof_ella):
#                      continue;
                if(string in self.__SpecialWordsRepository.Particles[0].keys()):
                    for j in self.__SpecialWordsRepository.Particles[0][string]:                        
                        standAloneParticle = self.__SpecialWordsRepository.Particles[1][j];
                        isCompatible = ArabicStringUtility.IsCompatible(ArabicStringUtility,cliticlessWithDiacritics, standAloneParticle.VoweledForm);
                        if(isCompatible == True):
                            subMatches.append(standAloneParticle.ReturnAsParticle());
            
            
            #معالجة الأسماء
            if(prefixType in ['c','n'] and suffixType in ['c','n']\
                and ('Noun' in topKeys or \
                    self.PrematureTaggingPositiveThreshold == None or \
                    'Noun' not in word.PrematureTags.keys() or \
                    word.PrematureTags['Noun'] >= self.PrematureTaggingPositiveThreshold)\
                and isVerb != True):  
                
                #إذا انتهت الكلمة بساكن ليس حرف علة فهي حتماً فعل
#                if(cliticlessWithDiacritics.endwith(sokoon) and \
#                   cliticlessWithDiacritics[len(cliticlessWithDiacritics)-2] not in ahrof_ella):
#                      continue;

                subMatch = self.__MatchNouns(word, string, cliticlessWithDiacritics, affixationPossibility, isIndefiniteNoun);
                
                if (len(affixationPossibility[2]) > 1 and string.endswith('ت')):
                    subNominalMatch = self.__MatchNouns(word, string[0:len(string)-1]+'ة', cliticlessWithDiacritics[0:len(cliticlessWithDiacritics)-1]+'ة', affixationPossibility, isIndefiniteNoun);
                    
                    for match in subNominalMatch:
                        match.OriginalString = cliticlessWithDiacritics;
                        match.UnvoweledForm = match.UnvoweledForm.replace('ة', 'ت');
                        match.VoweledForm = match.VoweledForm.replace('ة', 'ت');
                    subMatch.extend(subNominalMatch);
                    
                    
                subMatches.extend(subMatch);
                
            
            if subMatches != []:
                matches.append([affixationPossibility, subMatches]);
                
                i += 1;
                continue;
            else:
                affixationPossibilities.remove(affixationPossibilities[i]);
                continue;
            
        return matches;
        
    pass


    #يجب معالجة الحالة عندما تكون الكلمة ممنوعة من الصرف
    #؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
    def AssignCaseAccordingToLastDiacritic(self, pos, diacritic):
        
        if(diacritic == DiacriticsConstants.Damma\
           or diacritic == DiacriticsConstants.DoubleDamma):
            pos.CaseAndMood = CliticlessPOSConstants.CaseAndMood.NominativeOrIndicative;
        if(diacritic == DiacriticsConstants.Fatha\
           or diacritic == DiacriticsConstants.DoubleFatha):
            pos.CaseAndMood = CliticlessPOSConstants.CaseAndMood.AccusativeOrSubjunctive;
        if(diacritic == DiacriticsConstants.Kasra\
           or diacritic == DiacriticsConstants.DoubleKasra):
            pos.CaseAndMood = CliticlessPOSConstants.CaseAndMood.GenitiveOrJussive;
            
    pass
    
    def FillWithMatchesSimpleStem(self, word):
        matches = self.Match(word);
        
        for i in range(len(matches)):
            cliticlesses = matches[i][1];
            for cliticless in cliticlesses[:]:
                word.SurfaceFormMorphemes.append(SurfaceFormMorphemes([], cliticless, []));
        
        
    pass

    def FillWithStemsAndRoots(self, word):
#        print('--------------------------------------------------');
        matches = self.Match(word);
        
        for i in range(len(matches)):
            cliticlesses = matches[i][1];
            for cliticless in cliticlesses[:]:
                
                if(type(cliticless) is DerivedCliticless):
                    cliticless.UpdateInternalEnclitic();
                    
                exitsWithSameStemAndRoot = False;
            
                for surfaceFormMorphemes in word.SurfaceFormMorphemes[:]:
                    if(type(surfaceFormMorphemes.Cliticless) !=  type(cliticless)):
                        continue;
                    if(type(cliticless) is DerivedCliticless):
#                        print('################ DerivedCliticless #######################');
#                        print('surfaceFormMorphemes.Cliticless.Root.String = ' + surfaceFormMorphemes.Cliticless.Root.String)
#                        print('cliticless.Root.String = ' + cliticless.Root.String)
#                        print('surfaceFormMorphemes.Cliticless.GetStemString() = ' + surfaceFormMorphemes.Cliticless.GetStemString())
#                        print('cliticless.GetStemString() = ' + cliticless.GetStemString())

                        if(surfaceFormMorphemes.Cliticless.Root.String == cliticless.Root.String and \
                           surfaceFormMorphemes.Cliticless.GetStemString() == cliticless.GetStemString()):
                            exitsWithSameStemAndRoot = True;
                            break;
                    else:
                        if(surfaceFormMorphemes.Cliticless.UnvoweledForm == cliticless.UnvoweledForm):
                            exitsWithSameStemAndRoot = True;
                            break;
                    
                if(exitsWithSameStemAndRoot == False):
                    word.SurfaceFormMorphemes.append(SurfaceFormMorphemes([], cliticless, []));
        
    pass

    def FillWithStemsAndRootsAcurateClitics(self, word):
        self.FillWithMatches(word);
        
        rootAndStems = [];
        rootAndStems.append([]);
        rootAndStems.append([]);
        for surfaceFormMorphemes in word.SurfaceFormMorphemes[:]:
            if(type(surfaceFormMorphemes.Cliticless) !=  DerivedCliticless):
                if(surfaceFormMorphemes.Cliticless.UnvoweledForm not in rootAndStems[0]):
                    rootAndStems[0].append(surfaceFormMorphemes.Cliticless.UnvoweledForm);
                    rootAndStems[1].append(surfaceFormMorphemes.Cliticless.UnvoweledForm);
                continue;
            elif(type(surfaceFormMorphemes.Cliticless) is DerivedCliticless):
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #تحتاج إلى تحقق من عدم توافق التشابه بين الجذر والجذع معاً
                root = surfaceFormMorphemes.Cliticless.Root.String;
                stem = surfaceFormMorphemes.Cliticless.GetStemString();
                length = len(rootAndStems[0]); 
#                if(length != 0):
#                    print('root = ', root, ', rootAndStems[0][length-1]= ', rootAndStems[0][length-1], \
#                          ', stem = ', stem, ', rootAndStems[1][length-1] = ', rootAndStems[1][length-1]);
                if(length == 0 
                   or (root != rootAndStems[0][length-1] or \
                   stem != rootAndStems[1][length-1])): 
                   
                    rootAndStems[0].append(root);
                    rootAndStems[1].append(stem);
                    
            else:
                raise Exception('Unknown type for cliticless at method: FillWithStemsAndRootsAcurateWithClitics');
                
            
        return rootAndStems;
#        exit(0);
    pass

    def FillWithMatches(self, word):
        matches = self.Match(word);
        
        for i in range(len(matches)):
            procliticsStrings = matches[i][0][0];
            unvoweledForm = matches[i][0][1];
            encliticsStrings = matches[i][0][2];    
            
            consistentProclitics = [];
            
            
            cliticsStrings = matches[i][0][0];
            cliticlesses = matches[i][1];
            procliticsGrammers = ProcliticsGrammers();
            consistentProclitics = procliticsGrammers.GetConsistentClitics(word, cliticlesses, cliticsStrings, ParticleConstants.State.Proclitic);
            
            
            enclitics = [];
            
            for k in range(len(consistentProclitics)):
                proclitics = consistentProclitics[k][0];                
                cliticlesses = consistentProclitics[k][1];  
                
                cliticsStrings = matches[i][0][2];
                
                
                encliticsGrammers = EncliticsGrammers();
                consistentEnclitics = encliticsGrammers.GetConsistentClitics(word, cliticlesses, cliticsStrings, ParticleConstants.State.Enclitic);

                for r in range(len(consistentEnclitics)):
                    enclitics = consistentEnclitics[r][0];                
                    cliticlesses = consistentEnclitics[r][1]; 
                    
                    for cliticless in cliticlesses[:]:
                        word.SurfaceFormMorphemes.append(SurfaceFormMorphemes(proclitics, cliticless, enclitics));
        
        
    pass


    def __Intersect(self, list1, list2):
        intersection = [];
        for i in range(len(list1)):
            for j in range(len(list2)):
                if(list1[i] == list2[j]):
                    intersection.append(list1[i]);
        return intersection;
    pass
               
    def EliminateInconsistentMatches(self, matches):
        '''
        حذف الحلول التي لا تتوافق مع التشكيل المدخل لبعض أو جميع أحرف الكلمة
        '''
        i = 0;
        while i < len(matches):
            string = matches[i][0]
            voweledPatterns = matches[i][3];
            j = 0;
            while j < len(voweledPatterns):                
                isCompatible = ArabicStringUtility.IsCompatible(ArabicStringUtility,string, voweledPatterns[j].VoweledForm);                                
                if(isCompatible == True):
                    j += 1;
                else:
                    voweledPatterns.remove(voweledPatterns[j]);
            if( len(voweledPatterns) == 0 ):
                matches.remove(matches[i]);
            else:
                i += 1;
        return matches;
    pass
    
    def GetRefinedMatchStructure(self, cliticlessWithDiacritics, roots, matchedUnvoweledPatterns, matchedVoweledPatterns):
        RefinedMatches = [];
        for i in range(len(roots)):
            for j in range(len(roots[i])):
                RefinedMatches.append([cliticlessWithDiacritics, roots[i][j], matchedUnvoweledPatterns[i], matchedVoweledPatterns[i][j]]);
        return RefinedMatches;
    pass
    
    def __GetIntersectionsOfVoweledPatterns(self, matchedPatterns, roots, voweledPatterns):
        '''
        أخذ التقاطعات للأوزان المشّكلة, بين قائمة الجذر وقائمة الأوزان الغير مشكّلة
        يعيد قائمة بحيث:
            من أجل كل وزن غير مشكول هناك مجموعة جذور
            ومن أجل كل جذر هناك عدد من الأوزان الشكولة
        '''
        
        wordLength = len(matchedPatterns[0].String);
        intersections = [];
        for i in range(len(matchedPatterns)):
            subList = [];
            for j in range(len(roots[i])):
                subSubList = [];
                for k in range(len(matchedPatterns[i].IDs)):
                    if (matchedPatterns[i].IDs[k] in roots[i][j].PatternsIDs):
                        subSubList.append(voweledPatterns[wordLength][matchedPatterns[i].IDs[k]]);
                subList.append(subSubList);
            intersections.append(subList);
            
        return intersections;
    pass
    
    def __GetRoots(self, string, unvoweledPatterns, allRoots):
        '''
        استخراج الجذور من كل وزن
        '''
        
        roots = [];  
        i = 0; 
        while( i < len(unvoweledPatterns) ):
            rootsSubList = [];
            for j in range(len(unvoweledPatterns[i].Rules)):
                rootString = '';
                
                for k in range(len(unvoweledPatterns[i].Rules[j])):
                    if(unvoweledPatterns[i].Rules[j][k].isnumeric()):
                        #إن كان موقع أخر حرف في الجذر أكبر من عدد الأحرف فتجاوز هذه الحالة
                        if(int(unvoweledPatterns[i].Rules[j][k]) > len(string)):
                            rootString = '';
                            break;
                        rootString += string[int(unvoweledPatterns[i].Rules[j][k])-1];
                    else:
                        rootString += unvoweledPatterns[i].Rules[j][k];
                if(rootString == ''):
                    continue;
                
                for c in ['أ','إ','ؤ','ئ']:
                    rootString  = rootString.replace(c,'ء');
                firstLetter = rootString[0];

                if(firstLetter != 'ا' and firstLetter != 'ى' and rootString in allRoots[firstLetter].keys()):
                    rootsSubList.append(allRoots[firstLetter][rootString]);
            
            if(len(rootsSubList) == 0):
                unvoweledPatterns.remove(unvoweledPatterns[i])
            else:
                roots.append(rootsSubList);
                i += 1;
            
        return roots;
    pass
    
    def MatchStringWithUnvoweledPatterns(self, string, unvoweledPatterns):
        matchedPatterns = [];
        for key, value in unvoweledPatterns.items():
            isMatched = True;
            for j in range(len(string)):
                if(key[j] not in ['ف','ع','ل'] and \
                   string[j] != key[j]):
                    isMatched = False;
                    break;
            if(isMatched == True):
                matchedPatterns.append(value);
        return matchedPatterns;
                
    pass

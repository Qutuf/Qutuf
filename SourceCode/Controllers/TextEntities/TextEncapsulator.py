
'''
Created on ١٥‏/٠٦‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from .Word import *;
from ...Controllers.Tokenization.Tokenizer import *;
from ...Controllers.Normalization.Normalizer import *;
from ...Controllers.Morphology.Compounding.CompoundParsing import CompoundParsing;
from ...Controllers.Morphology.AffixParser import AffixParser;
from ...Controllers.Morphology.MorphologicalAnalyzer import MorphologicalAnalyzer;
from ...Controllers.Morphology.Entities.DerivedCliticless import DerivedCliticless;
from ...Controllers.Morphology.Entities.UnderivedCliticless import UnderivedCliticless;
from ...Controllers.Tagging.OverdueTagging.OverdueTagger import OverdueTagger;
from ...Controllers.Tagging.PrematureTagging.PrematureTagger import PrematureTagger;

from ...Models.Lexicon.LettersConstants import ArabicLetters;
from ...Models.Lexicon.SpecialWordsRepository import SpecialWordsRepository;
from ...Models.Lexicon.RootsAndPatternsRepository import RootsAndPatternsRepository;
from ...Models.Lexicon.SpecialWords.StandAloneParticle import *;
from ...Models.Lexicon.SpecialWords.ProperNoun import *;
from ...Models.General.TransducersXmlLoader import *



import io;

class TextEncapsulator(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qyYg9o35Ed-gg8GOK1TmhA
    """
    '''
    Text
    '''
    
    String = '';
    
    Sentences = [];

    __RootsAndPatternsRepository = None;
    __SpecialWordsRepository = None;
    
    def __init__(self, string = None):
        '''
        Constructor
        '''
        self.String = string;        
        
        self.__RootsAndPatternsRepository = RootsAndPatternsRepository();
        
        self.__SpecialWordsRepository = SpecialWordsRepository();
                        
        self.__Tokenizer = Tokenizer();
        self.__Normalizer = Normalizer();
        self.__CompoundParsing = CompoundParsing();
        self.__PrematureTagger = PrematureTagger();
        self.__AffixParser = AffixParser();
        self.__OverdueTagger = OverdueTagger();
        self.__MorphologicalAnalyzer = MorphologicalAnalyzer();
    pass

    def LoadFromFiles(self, baseDirectory, rootsFolder, \
                             procliticsXmlFileName, encliticsXmlFileName, \
                             prematureRulesXmlFile = None, \
                             overdueTaggingRulesXmlFile = None):


        if(baseDirectory != None):
            self.__RootsAndPatternsRepository.Load(baseDirectory, rootsFolder);        
    
            self.__SpecialWordsRepository.Load(baseDirectory);
            
            self.__MorphologicalAnalyzer.SetRepositories(self.__RootsAndPatternsRepository, self.__SpecialWordsRepository);
            
        
        if(procliticsXmlFileName != None):
            TransLoader = TransducersXmlLoader(procliticsXmlFileName);
            self.__ProcliticsStatesGraphs = TransLoader.StatesGraphs;
        if(encliticsXmlFileName != None):
            TransLoader = TransducersXmlLoader(encliticsXmlFileName);
            self.__EncliticsStatesGraphs = TransLoader.StatesGraphs;
    
        if(prematureRulesXmlFile != None):
            TransLoader = TransducersXmlLoader(prematureRulesXmlFile);
            self.__PrematureStatesGraphs = TransLoader.StatesGraphs;
            
        if(overdueTaggingRulesXmlFile != None):
            TransLoader = TransducersXmlLoader(overdueTaggingRulesXmlFile);
            self.__OverdueStatesGraphs = TransLoader.StatesGraphs;
    pass
    
    def Tokenize(self):
        if(self.String == None):
            raise Exception('Attribute [String] of class [TextEncapsulator] is not provided!');
        
        self.Sentences = self.__Tokenizer.Tokenize(self.String);
    pass
    
    def Normalize(self, updateBy):
        
        self.__Normalizer.Normalize(self.Sentences, updateBy);
    pass

    def CompoundParsing(self):        
        self.__CompoundParsing.Parsing(self, self.__SpecialWordsRepository);
    pass

    def PrematureTagging(self):
        
        self.__PrematureTagger.TagStopWords(self);        
        
        self.__PrematureTagger.ApplyTaggingRules(self, self.__PrematureStatesGraphs);
        self.__PrematureTagger.InferPrematureTags(self);
    pass
    
    def ParseClitics(self):
        
        
        self.__AffixParser.ParsePrefix(self.Sentences, self.__ProcliticsStatesGraphs);
        self.__AffixParser.ParseSuffix(self.Sentences, self.__EncliticsStatesGraphs);
    pass

    def PatternMatching(self, \
            prematureTaggingPositiveThreshold = None, prematureTaggingNegativeThreshold = None):
        
        self.__MorphologicalAnalyzer.PrematureTaggingPositiveThreshold = prematureTaggingPositiveThreshold;
        self.__MorphologicalAnalyzer.PrematureTaggingNegativeThreshold = prematureTaggingNegativeThreshold;
        
        for si in range(len(self.Sentences)):
            for wi in range(len(self.Sentences[si].Words)):
                if(self.Sentences[si].Words[wi].TokenType.Id == TokenType.Constants.Id.ArabicText \
                   and not self.Sentences[si].Words[wi].MorphologicalParsingCompleted):
                    self.__MorphologicalAnalyzer.FillWithMatches(self.Sentences[si].Words[wi]);
    pass

    def PatternMatchingSimpleStem(self):
        for si in range(len(self.Sentences)):
            for wi in range(len(self.Sentences[si].Words)):
                if(self.Sentences[si].Words[wi].TokenType.Id == TokenType.Constants.Id.ArabicText \
                   and not self.Sentences[si].Words[wi].MorphologicalParsingCompleted):
#                    cont = False;
#                    for i in range(len(self.Sentences[si].Words[wi].String)):
#                        if(self.Sentences[si].Words[wi].String[i] not in ArabicLetters.AllLetters):
#                            print('Token error at: ', self.Sentences[si].Words[wi].String,\
#                                  ', Token type = ',str(self.Sentences[si].Words[wi].TokenType.Id));
#                            cont = True;
#                            break;
#                    if(cont == True):
#                        continue;
                    self.__MorphologicalAnalyzer.FillWithMatchesSimpleStem(self.Sentences[si].Words[wi]);

    pass

    def StemmingAndRooting(self):
        
        rootsAndStems = [];
        rootsAndStems.append([]);
        rootsAndStems.append([]);
        for si in range(len(self.Sentences)):
            for wi in range(len(self.Sentences[si].Words)):
                if(self.Sentences[si].Words[wi].TokenType.Id == TokenType.Constants.Id.ArabicText \
                   and not self.Sentences[si].Words[wi].MorphologicalParsingCompleted):
        # self.__MorphologicalAnalyzer.FillWithStemsAndRoots(self.Sentences[si].Words[wi]);
                    subRootsAndStems = self.__MorphologicalAnalyzer.FillWithStemsAndRootsAcurateClitics(self.Sentences[si].Words[wi]);
                    
                    rootsAndStems[0].extend(subRootsAndStems[0]);
                    rootsAndStems[1].extend(subRootsAndStems[1]);
        # print(rootsAndStems);
        return rootsAndStems;
    pass
    
    def OverdueTagging(self, overdureTaggingThreshold = None, overdureTaggingTopReservants = None):
        
        self.__OverdueTagger.ApplyTaggingRules(self, self.__OverdueStatesGraphs);
        
        self.__OverdueTagger.SortAndUseThresholds(self, overdureTaggingThreshold, overdureTaggingTopReservants);
    pass

    
    def PrintTokens(self):
        for si in range(len(self.Sentences)):
            for wi in range(len(self.Sentences[si].Words)):
                print('Original String: ' + self.Sentences[si].Words[wi].OriginalString, \
                      ', TokenType.Id = ', self.Sentences[si].Words[wi].TokenType.Id);
    pass
    def Print(self):
        #Printing:
        for si in range(len(self.Sentences)):
            for wi in range(len(self.Sentences[si].Words)):
                print('Original String: ' + self.Sentences[si].Words[wi].OriginalString + \
                      ', Cliticlization Possibilities: '+str(len(self.Sentences[si].Words[wi].SurfaceFormMorphemes)) );
                
                for i in range(len(self.Sentences[si].Words[wi].SurfaceFormMorphemes)):
                    surfaceFormMorphemes = self.Sentences[si].Words[wi].SurfaceFormMorphemes[i];
                    proclitics = surfaceFormMorphemes.Proclitics;
                    cliticless = surfaceFormMorphemes.Cliticless;
                    enclitics = surfaceFormMorphemes.Enclitics;
                    output = io.StringIO();
                    output.write('    Certainty: '+str(surfaceFormMorphemes.GetCertainty())+'\n')
                    output.write('\tCliticless String: ' + cliticless.OriginalString+'\n');
                    output.write('\tProclitics: \n');
                    for proclitic in proclitics[:]:
                        output.write('\t\t');
                        proclitic.POS.WriteArabicText(output);
                        output.write('\n');
                    output.write('\tEnclitics: \n');
                    for enclitics in enclitics[:]:
                        output.write('\t\t');
                        enclitics.POS.WriteArabicText(output);
                        output.write('\n');

                    if (type(cliticless) is Particle):
                        output.write(''.join(['\tParticle: ' , cliticless.UnvoweledForm, ', Voweled: ', cliticless.VoweledForm, '\n']));
                    elif (type(cliticless) is UnderivedCliticless):                    
                        output.write(''.join(['\tUnderived Word: ' , cliticless.UnvoweledForm, ', Voweled: ', cliticless.VoweledForm, '\n']));
                    elif (type(cliticless) is DerivedCliticless):                    
                        output.write(''.join(['\tDerived Word: ' , cliticless.UnvoweledForm, ', Voweled: ', \
                              cliticless.VoweledForm, ' Pattern: ', cliticless.VoweledPattern.VoweledForm, \
                              ', ID=[', str(cliticless.VoweledPattern.ID), '] ,'\
                              'Root: ', cliticless.Root.String, '\n']));

                    output.write('\tDescription: ');
                    cliticless.POS.WriteArabicText(output);
                    output.write('\n\tTag: ');
                    cliticless.POS.WriteTag(output);
                    print (output.getvalue()+'\n');
                    output.close();
    pass
    
    def Print0(self):
        str = '';
        for i in range(len(self.Sentences)):
            str += self.Sentences[i].__str__();
        print(str);
    pass

    def PrintForClitics(self):
        str = '';
        for si in range(len(self.Sentences)):
            for wi in range(len(self.Sentences[si].Words)):
                str += 'Original:' + self.Sentences[si].Words[wi].OriginalString;
                str += '\nGreedy Morphemes: ' + self.Sentences[si].Words[wi].GreedyMorphemes.__str__();
                str += '\n------------------------------------------------------\n';
        print(str);
    pass

    def RenderXml(self, stream, functionality):
        
        from xml.dom.minidom import getDOMImplementation;
        impl = getDOMImplementation();
        
        newdoc = impl.createDocument(None, "Text", None);
        top_element = newdoc.documentElement;       
        
        for si in range(len(self.Sentences)):
            sentenceNode = newdoc.createElement('Sentence');
            top_element.appendChild(sentenceNode);
            sentenceNode.setAttribute('original_string', self.Sentences[si].OriginalString);  
            for wi in range(len(self.Sentences[si].Words)):                   
                originalString = self.Sentences[si].Words[wi].OriginalString;
                numberOfPossibilities = len(self.Sentences[si].Words[wi].SurfaceFormMorphemes)                
                
                wordNode = newdoc.createElement('Word');
                sentenceNode.appendChild(wordNode);
                wordNode.setAttribute('number_of_possibilities', str(numberOfPossibilities));
                wordNode.setAttribute('original_string', originalString);

                if functionality == 'lemma':
                    if(self.Sentences[si].Words[wi].TokenType.Id != TokenType.Constants.Id.ArabicText):
                        continue;
                    # TODO: wordNode.setAttribute('certain_diacrats', 'التشكيل المؤكد');
                    wordNode.setAttribute('lemmas', ', '.join(self.Sentences[si].Words[wi].Lemmas) \
                        # TODO: For every lemma compute the Certainty, accumulating for all similar lemma of the word
                        # '<span dir=ltr class="Certainty">', 'مقدار الثقة','</span>',\
                    )
                    wordNode.setAttribute('has_been_identified', 'true' if numberOfPossibilities > 0 else 'false');
                    
                else:
                    for i in range(len(self.Sentences[si].Words[wi].SurfaceFormMorphemes)):
                        surfaceFormMorphemesNode = newdoc.createElement('SurfaceFormMorphemes');
                        wordNode.appendChild(surfaceFormMorphemesNode);
                        surfaceFormMorphemes = self.Sentences[si].Words[wi].SurfaceFormMorphemes[i];
                        
                        voweled_form = surfaceFormMorphemes.VoweledForm;
                        surfaceFormMorphemesNode.setAttribute('voweled_form', voweled_form);
                        certainty = surfaceFormMorphemes.GetCertainty();
                        surfaceFormMorphemesNode.setAttribute('certainty', str(certainty));
                                            
                        proclitics = surfaceFormMorphemes.Proclitics;
                        cliticless = surfaceFormMorphemes.Cliticless;
                        enclitics = surfaceFormMorphemes.Enclitics;
                    
                        procliticsNode = newdoc.createElement('Proclitcs');
                        surfaceFormMorphemesNode.appendChild(procliticsNode);
                        for proclitic in proclitics[:]:
                            procliticNode = newdoc.createElement('Proclitc');
                            procliticsNode.appendChild(procliticNode);
                            output = io.StringIO();
                            proclitic.POS.WriteTag(output);
                            tag = output.getvalue();
                            output.close();
                            output = io.StringIO();
                            procliticNode.setAttribute('tag', tag);
                            proclitic.POS.WriteArabicText(output);
                            arabicDesc = output.getvalue();
                            output.close();
                            procliticNode.setAttribute('arabic_description', arabicDesc);                            
                            procliticNode.setAttribute('voweled_text', proclitic.VoweledForm);
                            
                            
                        cliticlessNode = newdoc.createElement('Cliticless');
                        surfaceFormMorphemesNode.appendChild(cliticlessNode);
                        output = io.StringIO();
                        cliticless.POS.WriteTag(output);
                        tag = output.getvalue();
                        output.close();
                        output = io.StringIO();
                        cliticlessNode.setAttribute('tag', tag);
                        cliticless.POS.WriteArabicText(output);
                        arabicDesc = output.getvalue();
                        output.close();
                        cliticlessNode.setAttribute('arabic_description', arabicDesc);
                        
                        if (type(cliticless) is DerivedCliticless):
                            unvoweledPattern = cliticless.UnvoweledPattern.String;
                            voweledPattern = cliticless.VoweledPattern.VoweledForm;
                            root = cliticless.Root.String;
                            stem = cliticless.GetStemString();
                            # stem = cliticless.UnvoweledPattern.String;
                            patternNode = newdoc.createElement('Pattern');
                            cliticlessNode.appendChild(patternNode);
                            patternNode.setAttribute('unoweled', unvoweledPattern);
                            patternNode.setAttribute('voweled', voweledPattern);
                            patternNode.setAttribute('root', root);
                            patternNode.setAttribute('Lemma', stem);
                            
                        encliticsNode = newdoc.createElement('Enclitics');
                        surfaceFormMorphemesNode.appendChild(encliticsNode);
                        for enclitic in enclitics[:]:
                            encliticNode = newdoc.createElement('Enclitic');
                            encliticsNode.appendChild(encliticNode);
                            output = io.StringIO();
                            enclitic.POS.WriteTag(output);
                            tag = output.getvalue();
                            output.close();
                            output = io.StringIO();
                            encliticNode.setAttribute('tag', tag);
                            enclitic.POS.WriteArabicText(output);
                            arabicDesc = output.getvalue();
                            output.close();                        
                            encliticNode.setAttribute('arabic_description', arabicDesc);                            
                            encliticNode.setAttribute('voweled_text', enclitic.VoweledForm);

       
        newdoc.writexml(stream, '', '\t', '\r\n', 'utf-8');
    pass

    def RenderTextSimpleStem(self, stream):
        
        for si in range(len(self.Sentences)):
            for wi in range(len(self.Sentences[si].Words)):
                for i in range(len(self.Sentences[si].Words[wi].SurfaceFormMorphemes)):
                    surfaceFormMorphemes = self.Sentences[si].Words[wi].SurfaceFormMorphemes[i];
                    
                    cliticless = surfaceFormMorphemes.Cliticless;
                    
                    stream.write(''.join([self.Sentences[si].Words[wi].OriginalString,' : ']));
                    cliticless.POS.WriteTag(stream);
                    stream.write('\r\n');
    pass

    def RenderXmlStemsAndRoots(self, stream):
        
        from xml.dom.minidom import getDOMImplementation;
        impl = getDOMImplementation();
        
        newdoc = impl.createDocument(None, "Text", None);
        top_element = newdoc.documentElement;       
        
        

        
        
        for si in range(len(self.Sentences)):
            sentenceNode = newdoc.createElement('Sentence');
            top_element.appendChild(sentenceNode);
            for wi in range(len(self.Sentences[si].Words)):
                wordNode = newdoc.createElement('Word');
                sentenceNode.appendChild(wordNode);
                wordString = self.Sentences[si].Words[wi].String;
                wordNode.setAttribute('string', wordString);
                for i in range(len(self.Sentences[si].Words[wi].SurfaceFormMorphemes)):
                    surfaceFormMorphemesNode = newdoc.createElement('Possibility');
                    wordNode.appendChild(surfaceFormMorphemesNode);
                    surfaceFormMorphemes = self.Sentences[si].Words[wi].SurfaceFormMorphemes[i];
                    
                    cliticless = surfaceFormMorphemes.Cliticless;
                    if (type(cliticless) is DerivedCliticless):
                        root = cliticless.Root.String;
                        stem = cliticless.GetStemString();
                        #stem = cliticless.UnvoweledPattern.String;
                        surfaceFormMorphemesNode.setAttribute('root', root);
                        surfaceFormMorphemesNode.setAttribute('Lemma', stem);
                    else:
                        surfaceFormMorphemesNode.setAttribute('word', cliticless.UnvoweledForm);
                        
        
        newdoc.writexml(stream, '', '\t', '\r\n', 'utf-8');
    pass

    def RenderXmlStemsAndRootsFlat(self, stream, rootAndStems):
        
        from xml.dom.minidom import getDOMImplementation;
        impl = getDOMImplementation();
        
        newdoc = impl.createDocument(None, "Words", None);
        top_element = newdoc.documentElement;       
        
               
        
        for i in range(len(rootAndStems[0])):
            chileNode = newdoc.createElement('Word');
            top_element.appendChild(chileNode);
        
            root = rootAndStems[0][i];
            stem = rootAndStems[1][i];
            chileNode.setAttribute('Root', root);
            chileNode.setAttribute('Lemma', stem);
        
        newdoc.writexml(stream, '', '\t', '\r\n', 'utf-8');
    pass

    def RenderHtml(self, stream, functionality):
        
        stream.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\
        <style>\
        body{font-family:Traditional Arabic; }\
        table{border:solid thin black;}\
        td{border:solid 1px black; font-size:14pt; font-weight:900;}\
        .Tag{width:40%; font-size:12pt; font-family:Courier New;font-weight:bold;}\
        .title{background-color:#6666BB; font-size:16pt; text-align:center;}\
        .subtitle{background-color:#6666FF; font-size:14pt; text-align:center;}\
        .NestedTableData.{vertical-align:top;}\
        .NestedTable{width:100%; height:100%; border: solid 1px black;}\
        .DiacratizedText{color:Green; font-size:large; text-align:center;}\
        .diacritic{color:Red;}\
        .Certainty{width: 8%;font-size:12pt; font-family:Courier New;font-weight:bold;}\
        </style></head><body dir=rtl>');
        
        stream.write('<table cellspacing=0 class=NestedTable>\n');

        for si in range(len(self.Sentences)):

            originalString = self.Sentences[si].OriginalString;
            for wi in range(len(self.Sentences[si].Words)):   
                numberOfPossibilities = len(self.Sentences[si].Words[wi].SurfaceFormMorphemes) ;             
                if functionality == 'lemma':
                    if(self.Sentences[si].Words[wi].TokenType.Id != TokenType.Constants.Id.ArabicText):
                        continue;
                    
                    stream.write(''.join(['<tr class=title>', \
                                            '<td>', 'الكلمة </td>', \
                                            # '<td>', 'التشكيل المؤكد','</td>', \
                                            '<td>', 'المفردة-الجذع (Lemma/stem)','</td>', \
                                            '<td>', 'هل تم التعرف عليها؟','</td>',\
                                            '</tr>']));
                    
                    leftTableData = '\n'.join(['<td class=subtitle style="{font-size:24pt;}">', self.Sentences[si].Words[wi].OriginalString,'</td>']);
                                            
                    stream.write('\n'.join(['<tr>', \
                        leftTableData, \
                        # '<td>', 'To do', '</td>',\
                        '<td>', ', '.join(self.Sentences[si].Words[wi].Lemmas), \
                        # TODO: For every lemma compute the Certainty, accumulating for all similar lemma of the word
                        # '<span dir=ltr class="Certainty">', 'مقدار الثقة','</span>',\
                        '</td>', \
                        '<td>',  'نعم' if numberOfPossibilities > 0 else 'لا', '</td>',\
                        '</tr>']));                        

                else:
                    if(self.Sentences[si].Words[wi].TokenType.Id != TokenType.Constants.Id.ArabicText):
                        continue;
                    originalString = ArabicStringUtility.ColorizeDiacraticInHtml(ArabicStringUtility, self.Sentences[si].Words[wi].OriginalString);

                    
                    stream.write(''.join(['<tr class=title>', \
                                            '<td rowspan=2>', 'الكلمة (',originalString,')','</td>', \
                                            '<td rowspan=2>', 'مشكّلة','</td>', \
                                            '<td rowspan=2 dir=ltr class="Certainty">', 'مقدار <br/> الثقة','</td>',\
                                            '<td colspan=3>', 'المقاطع (عدد التراكيب المحتملة ',str(numberOfPossibilities),')','</td>',\
                                            '</tr>']));
                    
                    stream.write('\n'.join(['<tr class=title>', \
                                            '<td width=18%>', 'اللواصق السابقة','</td>', \
                                            '<td width=50%>', 'المفردة','</td>',\
                                            '<td width=27%>', 'اللواصق الاحقة','</td>',\
                                            '</tr>']));
                    
                    leftTableData = ''.join(['<td class=subtitle style="{font-size:24pt;}" rowspan=',str(numberOfPossibilities),'>', originalString,'</td>']);
                        
                    for surfaceFormMorphemes in self.Sentences[si].Words[wi].SurfaceFormMorphemes:
                        if(surfaceFormMorphemes == self.Sentences[si].Words[wi].SurfaceFormMorphemes[0]):
                            self.RenderSurfaceFormMorphemesHtml(stream, surfaceFormMorphemes, leftTableData);
                        else:
                            self.RenderSurfaceFormMorphemesHtml(stream, surfaceFormMorphemes, '');
                    #else:
                    #   stream.write('\n'.join(['<tr>', \
                    #       '<td>', '-','</td>', \
                    #       '<td>', '-','</td>', \
                    #       '<td>', '-','</td>',\
                    #       '<td colspan=3>', '-','</td>',\
                    #       '</tr>']));

                    
        stream.write('</table>\n');
        stream.write('</body></html>');
    pass

    def RenderSurfaceFormMorphemesHtml(self, stream, surfaceFormMorphemes, leftTableData = ''):
                                        
        voweled_form = ArabicStringUtility.ColorizeDiacraticInHtml(ArabicStringUtility, surfaceFormMorphemes.VoweledForm);
        
        certainty = surfaceFormMorphemes.GetCertainty();
        
        tempStream = io.StringIO();        
        self.RenderCliticsHtml(tempStream, surfaceFormMorphemes.Proclitics);
        proTable = tempStream.getvalue();
        tempStream.close();
        
        tempStream = io.StringIO();        
        self.RenderCliticlessHtml(tempStream, surfaceFormMorphemes.Cliticless);
        cliticlessTable = tempStream.getvalue();
        tempStream.close();
        
        tempStream = io.StringIO();        
        self.RenderCliticsHtml(tempStream, surfaceFormMorphemes.Enclitics);
        enTable = tempStream.getvalue();
        tempStream.close();

        
        stream.write('\n'.join(['<tr>', \
                                leftTableData, \
                                '<td class="DiacratizedText">', voweled_form,'</td>', \
                                '<td dir=ltr class="Certainty">', str(round(certainty,3)),'</td>',\
                                '<td class=NestedTableData>', proTable,'</td>', \
                                '<td class=NestedTableData>', cliticlessTable ,'</td>',\
                                '<td class=NestedTableData>', enTable,'</td>',\
                                '</tr>']));
    pass

    def RenderCliticsHtml(self, stream, clitics):
            
        stream.write('<table cellspacing=0 class=NestedTable>\n');
        if(clitics != []):
            stream.write('\n'.join(['<tr class=subtitle>', \
                                    '<td>', 'النص','</td>', \
                                    '<td>', 'الوصف','</td>',\
                                    '<td>', 'الوسم','</td>',\
                                    '</tr>']));
            
        else:
            stream.write('<tr><td style="vertical-align:center; text-align:center;">لا يوجد</tr></td>');
            
        
        for clitic in clitics[:]:
            output = io.StringIO();
            clitic.POS.WriteTag(output);
            tag = output.getvalue();
            output.close();
            
            output = io.StringIO();            
            clitic.POS.WriteArabicText(output);
            arabicDesc = output.getvalue();
            output.close();
                        
            stream.write('\n'.join(['<tr>', \
                                    '<td>', clitic.VoweledForm,'</td>', \
                                    '<td>', arabicDesc,'</td>',\
                                    '<td class=Tag dir=ltr>', tag,'</td>',\
                                    '</tr>']));


        stream.write('</table>\n');
    pass

    def RenderCliticlessHtml(self, stream, cliticless):
        
        stream.write('<table cellspacing=0 class=NestedTable>\n');
        
        stream.write('\n'.join(['<tr class=subtitle>', \
                                '<td>', 'النص','</td>', \
                                '<td width=50%>', 'الوصف','</td>',\
                                '<td width=28%>', 'الوسم','</td>',\
                                '<td>', 'الوزن','</td>',\
                                '<td>', 'الجذر','</td>',\
                                '<td>', 'الجذع','</td>',\
                                '</tr>']));
                                
        output = io.StringIO();        
        cliticless.POS.WriteTag(output);
        tag = output.getvalue();
        output.close();
        
        output = io.StringIO();        
        cliticless.POS.WriteArabicText(output);
        arabicDesc = output.getvalue();
        output.close();
        
        
        
        if (type(cliticless) is DerivedCliticless):
            unvoweledPattern = cliticless.UnvoweledPattern.String;
            voweledPattern = cliticless.VoweledPattern.VoweledForm;
            root = cliticless.Root.String;
            stem = cliticless.GetStemString();
        # stem = cliticless.UnvoweledPattern.String;
        else:
            unvoweledPattern = '-';
            voweledPattern = '-';
            root = '-';
            stem = '-';
        stream.write('\n'.join(['<tr>', \
                                '<td>', cliticless.VoweledForm,'</td>',\
                                '<td>', arabicDesc,'</td>',\
                                '<td class=Tag dir=ltr>', tag,'</td>',\
                                '<td>', voweledPattern,'</td>', \
                                '<td>', root,'</td>',\
                                '<td>', stem,'</td>',\
                                '</tr>']));


        stream.write('</table>\n');
    pass

    def exposeLemma(self):
        for si in range(len(self.Sentences)):
            originalString = self.Sentences[si].OriginalString;
            for wi in range(len(self.Sentences[si].Words)):  
                self.Sentences[si].Words[wi].fillLemmas()
                    
                    
    pass
#
#    def Render(self, stream):
#        output = io.StringIO();
#        for si in range(len(self.Sentences)):
#            for wi in range(len(self.Sentences[si].Words)):
#                originalString = self.Sentences[si].Words[wi].OriginalString;
#                numberOfPossibilities = len(self.Sentences[si].Words[wi].SurfaceFormMorphemes) ;
#                for i in range(len(self.Sentences[si].Words[wi].SurfaceFormMorphemes)):
#                    surfaceFormMorphemes = self.Sentences[si].Words[wi].SurfaceFormMorphemes[i];
#                    
#                    certainty = surfaceFormMorphemes.GetCertainty();
#                    voweled_form = surfaceFormMorphemes.VoweledForm;
#                                        
#                    proclitics = surfaceFormMorphemes.Proclitics;
#                    cliticless = surfaceFormMorphemes.Cliticless;
#                    enclitics = surfaceFormMorphemes.Enclitics;
#                    
#                    for proclitic in proclitics[:]:
#                        proclitic.POS.WriteTag(output);
#                        tag = output.getvalue();
#                        output.flush();
#                        proclitic.POS.WriteArabicText(output);
#                        arabicDesc = output.getvalue();
#                        output.flush();
#                        
#                        
#                    cliticless.POS.WriteTag(output);
#                    tag = output.getvalue();
#                    output.flush();
#                    cliticless.POS.WriteArabicText(output);
#                    arabicDesc = output.getvalue();
#                    output.flush();
#                        
#                    for enclitic in enclitics[:]:
#                        enclitic.POS.WriteTag(output);
#                        tag = output.getvalue();
#                        output.flush();
#                        enclitic.POS.WriteArabicText(output);
#                        arabicDesc = output.getvalue();
#                        output.flush();
#
#                    if (type(cliticless) is DerivedCliticless):
#                        unvoweledPattern = cliticless.UnvoweledPattern.String;
#                        voweledPattern = cliticless.VoweledPattern.VoweledForm;
#                        root = cliticless.Root.String;
##                        stem = cliticless.StemString;
#                        stem = cliticless.UnvoweledPattern.String;
#        
#    pass

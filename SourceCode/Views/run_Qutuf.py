'''
Created on ١١‏/٠٥‏/٢٠١٠

@author: Muhammad Altabba
'''

import codecs
import io
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))+'/../..'

from ..Controllers.TextEntities.TextEncapsulator import *

#Set Files Locations Variables:
'''
Change the next few parameters as appropriate.
'''

baseDirectory = ROOT_DIR
baseDirectoryOfQutufDB = os.path.join(baseDirectory,'Data')
inputTextFile = os.path.join(baseDirectoryOfQutufDB,'test_Qutuf.txt')
baseDirectoryOfAlKhalilDB = os.path.join(baseDirectory,'AlKhalil_V1_Modified','db/')
# ouputXmlFile = os.path.join(baseDirectory,'Output','test.xml')
# ouputHtmlFile = os.path.join(baseDirectory,'Output','test.html')


#Set Operations Variables:
prematureTaggingPositiveThreshold = 0.0
prematureTaggingNegativeThreshold = -0.0

overdureTaggingThreshold  = None
overdureTaggingTopReservants  = None


'''
The next few parameters are fixed do not change them.
'''
procliticsXmlFile = os.path.join(baseDirectoryOfQutufDB, 'MorphologyTransducers','Proclitics.xml')
encliticsXmlFile = os.path.join(baseDirectoryOfQutufDB,'MorphologyTransducers','Enclitics.xml')
prematureTaggingRulesXmlFile = os.path.join(baseDirectoryOfQutufDB, 'TaggingRepository','PrematureTaggingRules.xml')
overdueTaggingRulesXmlFile = os.path.join(baseDirectoryOfQutufDB, 'TaggingRepository','OverdueTaggingRules.xml')
rootsFolder = 'roots2'

# Initialize:
text = TextEncapsulator()

# Load Data from Files:
text.LoadFromFiles(baseDirectoryOfAlKhalilDB, rootsFolder,
                    procliticsXmlFile, encliticsXmlFile,
                    prematureTaggingRulesXmlFile,
                    overdueTaggingRulesXmlFile)

def runit(phrase, functionality, outputFormat):


    # Read input text into Qutuf:
    text.String = phrase

    # Process:
    text.Tokenize()

    text.Normalize(2)

    text.CompoundParsing()

    text.PrematureTagging()

    text.ParseClitics()

    text.PatternMatching(prematureTaggingPositiveThreshold, prematureTaggingNegativeThreshold)

    text.OverdueTagging(overdureTaggingThreshold, overdureTaggingTopReservants)

    if functionality == 'lemma':
        text.exposeLemma()

    # Write Output:
    
    streamWriter = io.StringIO()
    if outputFormat == 'html':
        text.RenderHtml(streamWriter, functionality)
    else:
        text.RenderXml(streamWriter, functionality)
    output = streamWriter.getvalue()

    # Log to terminal:
    # print('---------------------------------------------------------------------------')
    # text.Print()
    # print('---------------------------------------------------------------------------')

    # Log to file:
    # writer = codecs.open(ouputFile, 'w', 'utf-8')
    # writer.write(output)
    # writer.close()

    return output

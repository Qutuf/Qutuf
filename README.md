# Arabic Morphological Analyzer (with Stemmer) and Part-Of-Speech Tagger

Qutuf (قُطُوْف): An Arabic Morphological Analyzer (Including Stemming and Root Extraction) and Part-Of-Speech Tagger as an Expert System.

Qutuf is aimed to be the Core of a Framework for Arabic NLP (Natural Language Processing)

At Qutuf, some new concepts have been identified and implemented. Like First Normalization and Second Normalization text forms at the preprocessing phase and the Premature and Overdue Tagging at the Part-Of-Speech tagging task. Moreover, the POS tagging is designed and implemented as a rule-based expert system. A POS tagset, which is built based on a morphological feature tagset, has been designed and used in Qutuf.

Morphological Analysis Includes both Stemming (light stemming) and Root Extraction (heavy stemming). It achive this by using finite state automates and rules for agreement developed for cliticization parsing. It also uses AlKhalil Morpho Sys open source database for root extraction, pattern matching, morphological feature and POS assignment and closed nouns after enriching it.

## Execute
As Qutuf serves as a framework, you can run for the processing phase you need and passing the applicable parameter for each processing phase.

Check full test running code at:
/SourceCode/Views/run_Qutuf.py

### Text Processing

    text.Tokenize();
    
    text.Normalize(2);
    
    text.CompoundParsing();
    
    text.PrematureTagging();
    
    text.ParseClitics();
    
    text.PatternMatching(prematureTaggingPositiveThreshold, prematureTaggingNegativeThreshold);
             
    text.OverdueTagging(overdureTaggingThreshold, overdureTaggingTopReservants);

To understand the processing happen at each step, please refer to the [publication](https://www.academia.edu/8222523/Arabic_Morphological_Analyzer_with_Stemmer_and_Part-Of-Speech_Tagger._The_Core_of_a_Framework_for_Arabic_Language_Processing_as_an_Expert_System)
## Output
You can get the output in one of the following formats:
#### XML format

    xmlStreamWriter = io.StringIO();
    text.RenderHtml(xmlStreamWriter);

#### HTML format

    xmlStreamWriter = io.StringIO();
    text.RenderXml(xmlStreamWriter);

#### Sample XML output
The following is the real output of the processed word "غير".


		<Word number_of_possibilities="6" original_string="غير">
			<SurfaceFormMorphemes certainty="0.96484375" voweled_form="غَيْر">
				<Proclitcs/>
				<Cliticless arabic_description="حرف, حرف استثناء, ظاهر" tag="p,x"/>
				<Enclitics/>
			</SurfaceFormMorphemes>
			<SurfaceFormMorphemes certainty="0.859375" voweled_form="غَيَّرَ">
				<Proclitcs/>
				<Cliticless arabic_description="فعل, مذكر, مفرد, مسند إلى الغائب, -, ماض, مبني للمعلوم, لازمٌ أو مُتعدٍ, ؟, -, مزيد" tag="v,m,s,t,-,p,a,iobt,؟">
					<Pattern Lemma="غير" root="غير" unoweled="فعل" voweled="فَعَّلَ"/>
				</Cliticless>
				<Enclitics/>
			</SurfaceFormMorphemes>
			<SurfaceFormMorphemes certainty="0.8125" voweled_form="غِيرَ">
				<Proclitcs/>
				<Cliticless arabic_description="فعل, مذكر, مفرد, مسند إلى الغائب, -, ماض, مبني للمجهول, لازمٌ أو مُتعدٍ, ؟, -, مجرد" tag="v,m,s,t,-,p,p,iobt,؟">
					<Pattern Lemma="غير" root="غور" unoweled="فيل" voweled="فِيلَ"/>
				</Cliticless>
				<Enclitics/>
			</SurfaceFormMorphemes>
			<SurfaceFormMorphemes certainty="0.8125" voweled_form="غُيِّرَ">
				<Proclitcs/>
				<Cliticless arabic_description="فعل, مذكر, مفرد, مسند إلى الغائب, -, ماض, مبني للمجهول, لازمٌ أو مُتعدٍ, ؟, -, مزيد" tag="v,m,s,t,-,p,p,iobt,؟">
					<Pattern Lemma="غير" root="غير" unoweled="فعل" voweled="فُعِّلَ"/>
				</Cliticless>
				<Enclitics/>
			</SurfaceFormMorphemes>
			<SurfaceFormMorphemes certainty="0.8125" voweled_form="غِيرَ">
				<Proclitcs/>
				<Cliticless arabic_description="فعل, مذكر, مفرد, مسند إلى الغائب, -, ماض, مبني للمجهول, لازمٌ أو مُتعدٍ, ؟, -, مجرد" tag="v,m,s,t,-,p,p,iobt,؟">
					<Pattern Lemma="غير" root="غير" unoweled="فعل" voweled="فِعلَ"/>
				</Cliticless>
				<Enclitics/>
			</SurfaceFormMorphemes>
			<SurfaceFormMorphemes certainty="0.5" voweled_form="غَيِّرْ">
				<Proclitcs/>
				<Cliticless arabic_description="فعل, مذكر, مفرد, مسند إلى المخاطب, -, أمر, -, لازمٌ أو مُتعدٍ, ؟, غير مؤكد, مزيد" tag="v,m,s,s,-,i,-,iobt,؟">
					<Pattern Lemma="غير" root="غير" unoweled="فعل" voweled="فَعِّلْ"/>
				</Cliticless>
				<Enclitics>
					<Enclitic arabic_description="اسم, مذكر, مفرد, ؟, مرفوع, ضمير رفع, معرفة, مضمر/مقدّر" tag="n,m,s,؟,n,p,d"/>
				</Enclitics>
			</SurfaceFormMorphemes>
		</Word>

To use the output as an input for another processing phase/program you develop, you will take thae "tag" of each Proclitcs, Cliticless (the stemm) and Enclitics when applicable.

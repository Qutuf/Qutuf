# Arabic Morphological Analyzer (with Stemmer) and Part-Of-Speech Tagger



Qutuf (قُطُوْف): An Arabic Morphological Analyzer (Including Stemming and Root Extraction) and Part-Of-Speech Tagger as an Expert System.



Qutuf is aimed to be the Core of a Framework for Arabic NLP (Natural Language Processing)



At Qutuf, some new concepts have been identified and implemented. Like First Normalization and Second Normalization text forms at the preprocessing phase and the Premature and Overdue Tagging at the Part-Of-Speech tagging task. Moreover, the POS tagging is designed and implemented as a rule-based expert system. A POS tagset, which is built based on a morphological feature tagset, has been designed and used in Qutuf.



Morphological Analysis Includes both Stemming (light stemming) and Root Extraction (heavy stemming). It achieve this by using finite state automates and rules for agreement developed for cliticization parsing. It also uses AlKhalil Morpho Sys open source database for root extraction, pattern matching, morphological feature and POS assignment and closed nouns after enriching it.



## Execution

As Qutuf serves as a framework, you can run for the processing phase you need and passing the applicable parameter for each processing phase.



The entry code for running all features can be found at:

[SourceCode/Views/run_Qutuf.py](./SourceCode/Views/run_Qutuf.py)



And you can check the free web-service online as you can see in [Qutuf as-a-Service](#qutuf-as-a-service) section. However, we encourage you to run qutuf on your machine and start adding additional text processing steps on top of the existing ones.



### Text Processing



    text.Tokenize();

    

    text.Normalize(2);

    

    text.CompoundParsing();

    

    text.PrematureTagging();

    

    text.ParseClitics();

    

    text.PatternMatching(prematureTaggingPositiveThreshold, prematureTaggingNegativeThreshold);

             

    text.OverdueTagging(overdureTaggingThreshold, overdureTaggingTopReservants);



To understand the processing happen at each step, please refer to the [publication](https://www.academia.edu/8222523/Arabic_Morphological_Analyzer_with_Stemmer_and_Part-Of-Speech_Tagger._The_Core_of_a_Framework_for_Arabic_Language_Processing_as_an_Expert_System)



## Qutuf as-a-Service

Qutuf is available as an experimental service at https://qutuf.herokuapp.com.

You can get the output in json, xml or html (default) by using the following url parameter:



`outputformat = [json|xml|html]`



#### JSON format

To process the word غير for example and get the result in JSON:



https://qutuf.herokuapp.com/?outputformat=json&text=غير





#### XML format



Similarly, to process the word غير for example and get the result in XML:



https://qutuf.herokuapp.com/?outputformat=xml&text=غير





#### HTML format



HTML is the default format. The following will give the output for the word غير in HTML:



https://qutuf.herokuapp.com/?text=غير





#### Using Qutuf for Lemmatization (you may call it Stemming)



Similar to `outputformat` mentioned above, there is an optional URL parameter to use when getting only the possible lemma(s) / Stem(s) of every word.



`functionality=[lemma]`



<a href="https://qutuf.herokuapp.com/?functionality=lemma&outputformat=html&text= الملك بالملك فالملك وملك والملك">https://qutuf.herokuapp.com/?functionality=lemma&outputformat=html&text= الملك بالملك فالملك وملك والملك</a>



This URL parameter is optional and not passing it will tell Qutuf to give a detailed output.



#### Sample JSON output







##### Sample Lemmatization (Stemming)

If it is intended to get only the lemma/stem of the given words. Qutuf will do all the processing but will output only the lemma(s).



Bellow, is the output for 'الملك بالملك فالملك وملك والملك'. Note that if the string was not a word (like space, semicolon, exclamation marks, and etc.), there will be no `lemmas` attribute.



If Qutuf could not identify the word, it will mark `has_been_identified` as `false` and will return the original word as the lemma. This will happen if the word is not in the dictionaries nor it has a valid root-and-pattern.



```

{"Word":[{"@number_of_possibilities":"0","@original_string":" "},{"@has_been_identified":"true","@lemmas":"ملك","@number_of_possibilities":"10","@original_string":"الملك"},{"@number_of_possibilities":"0","@original_string":" "},{"@has_been_identified":"true","@lemmas":"ملك","@number_of_possibilities":"8","@original_string":"بالملك"},{"@number_of_possibilities":"0","@original_string":" "},{"@has_been_identified":"true","@lemmas":"ملك","@number_of_possibilities":"20","@original_string":"فالملك"},{"@number_of_possibilities":"0","@original_string":" "},{"@has_been_identified":"true","@lemmas":"ملك, مل","@number_of_possibilities":"60","@original_string":"وملك"},{"@number_of_possibilities":"0","@original_string":" "},{"@has_been_identified":"true","@lemmas":"ملك","@number_of_possibilities":"28","@original_string":"والملك"},{"@number_of_possibilities":"0","@original_string":"."}]}

```





##### Sample Full output



The following is the full output of the processed word "غير".

```

{  

  "Word":[  

  {  

    "@number_of_possibilities":"10",

    "@original_string":"غير",

    "SurfaceFormMorphemes":[  

      {  

        "@certainty":"0.98681640625",

        "@voweled_form":"غَيْر",

        "Proclitcs":null,

        "Cliticless":{  

        "@arabic_description":"حرف, حرف استثناء, ظاهر",

        "@tag":"p,x"

        },

        "Enclitics":null

      }, {  

        "@certainty":"0.96484375",

        "@voweled_form":"غَيْر",

        "Proclitcs":null,

        "Cliticless":{  

        "@arabic_description":"اسم, مذكر, مفرد, ؟, مرفوع أو منصوب أو مجرور, اسم جامد, معرَّف بالإضافة أو نكرة, ظاهر",

        "@tag":"n,m,s,؟,nag,q,ai",

        "Pattern":{  

          "@Lemma":"غير",

          "@root":"غير",

          "@unoweled":"فعل",

          "@voweled":"فَعْل"

        }

        },

        "Enclitics":null

      }, {  

        "@certainty":"0.953125",

        "@voweled_form":"غَيْرٌ",

        "Proclitcs":null,

        "Cliticless":{  

        "@arabic_description":"اسم, مذكر, مفرد, ؟, مرفوع, مصدر أصلي, نكرة, ظاهر",

        "@tag":"n,m,s,؟,n,g,i",

        "Pattern":{  

          "@Lemma":"غير",

          "@root":"غير",

          "@unoweled":"فعل",

          "@voweled":"فَعْلٌ"

        }

        },

        "Enclitics":null

      }, {  

        "@certainty":"0.953125",

        "@voweled_form":"غَيْرُ",

        "Proclitcs":null,

        "Cliticless":{  

        "@arabic_description":"اسم, مذكر, مفرد, ؟, مرفوع, مصدر أصلي, معرَّف بالإضافة, ظاهر",

        "@tag":"n,m,s,؟,n,g,a",

        "Pattern":{  

          "@Lemma":"غير",

          "@root":"غير",

          "@unoweled":"فعل",

          "@voweled":"فَعْلُ"

        }

        },

        "Enclitics":null

      }, {  

        "@certainty":"0.9296875",

        "@voweled_form":"غَيْرَ",

        "Proclitcs":null,

        "Cliticless":{  

        "@arabic_description":"اسم, مذكر, مفرد, ؟, منصوب, مصدر أصلي, معرَّف بالإضافة, ظاهر",

        "@tag":"n,m,s,؟,a,g,a",

        "Pattern":{  

          "@Lemma":"غير",

          "@root":"غير",

          "@unoweled":"فعل",

          "@voweled":"فَعْلَ"

        }

        },

        "Enclitics":null

      }, {  

        "@certainty":"0.859375",

        "@voweled_form":"غَيَّرَ",

        "Proclitcs":null,

        "Cliticless":{  

        "@arabic_description":"فعل, مذكر, مفرد, مسند إلى الغائب, -, ماض, مبني للمعلوم, لازمٌ أو مُتعدٍ, ؟, -, مزيد",

        "@tag":"v,m,s,t,-,p,a,iobt,؟",

        "Pattern":{  

          "@Lemma":"غير",

          "@root":"غير",

          "@unoweled":"فعل",

          "@voweled":"فَعَّلَ"

        }

        },

        "Enclitics":null

      }, {  

        "@certainty":"0.8125",

        "@voweled_form":"غُيِّرَ",

        "Proclitcs":null,

        "Cliticless":{  

        "@arabic_description":"فعل, مذكر, مفرد, مسند إلى الغائب, -, ماض, مبني للمجهول, لازمٌ أو مُتعدٍ, ؟, -, مزيد",

        "@tag":"v,m,s,t,-,p,p,iobt,؟",

        "Pattern":{  

          "@Lemma":"غير",

          "@root":"غير",

          "@unoweled":"فعل",

          "@voweled":"فُعِّلَ"

        }

        },

        "Enclitics":null

      }, {  

        "@certainty":"0.8125",

        "@voweled_form":"غِيرَ",

        "Proclitcs":null,

        "Cliticless":{  

        "@arabic_description":"فعل, مذكر, مفرد, مسند إلى الغائب, -, ماض, مبني للمجهول, لازمٌ أو مُتعدٍ, ؟, -, مجرد",

        "@tag":"v,m,s,t,-,p,p,iobt,؟",

        "Pattern":{  

          "@Lemma":"غير",

          "@root":"غير",

          "@unoweled":"فعل",

          "@voweled":"فِعلَ"

        }

        },

        "Enclitics":null

      }, {  

        "@certainty":"0.8125",

        "@voweled_form":"غِيرَ",

        "Proclitcs":null,

        "Cliticless":{  

        "@arabic_description":"فعل, مذكر, مفرد, مسند إلى الغائب, -, ماض, مبني للمجهول, لازمٌ أو مُتعدٍ, ؟, -, مجرد",

        "@tag":"v,m,s,t,-,p,p,iobt,؟",

        "Pattern":{  

          "@Lemma":"غير",

          "@root":"غور",

          "@unoweled":"فيل",

          "@voweled":"فِيلَ"

        }

        },

        "Enclitics":null

      }, {  

        "@certainty":"0.5",

        "@voweled_form":"غَيِّرْ",

        "Proclitcs":null,

        "Cliticless":{  

        "@arabic_description":"فعل, مذكر, مفرد, مسند إلى المخاطب, -, أمر, -, لازمٌ أو مُتعدٍ, ؟, غير مؤكد, مزيد",

        "@tag":"v,m,s,s,-,i,-,iobt,؟",

        "Pattern":{  

          "@Lemma":"غير",

          "@root":"غير",

          "@unoweled":"فعل",

          "@voweled":"فَعِّلْ"

        }

        },

        "Enclitics":{  

        "Enclitic":{  

          "@arabic_description":"اسم, مذكر, مفرد, ؟, مرفوع, ضمير رفع, معرفة, مضمر/مقدّر",

          "@tag":"n,m,s,؟,n,p,d"

            }

          }

        }

      ]

    }

  ]

}

```





To use the output as an input for another processing phase/program you develop, you may use, for example, the "tag" of each Proclitcs, Cliticless (the stem) and Enclitics when applicable.



# Support & Contribute!

Your are welcome to contribution and support. Start by pressing `Star` and `Fork` for this repository, implement new features, create a pull request and we will be happy to review and accept your valuable features, enhancements and bug-fixes.



For any bug, question or feature-request, feel free to open an Issue at this repository.



For more, check http://qutuf.com and contact maltabba@qutuf.com.
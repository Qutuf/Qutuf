# Arabic Morphological Analyzer (with Stemmer) and Part-Of-Speech Tagger

Qutuf (قُطُوْف): An Arabic Morphological Analyzer (Including Stemming and Root Extraction) and Part-Of-Speech Tagger as an Expert System.

Qutuf is aimed to be the Core of a Framework for Arabic NLP (Natural Language Processing)

At Qutuf, some new concepts have been identified and implemented. Like First Normalization and Second Normalization text forms at the preprocessing phase and the Premature and Overdue Tagging at the Part-Of-Speech tagging task. Moreover, the POS tagging is designed and implemented as a rule-based expert system. A POS tagset, which is built based on a morphological feature tagset, has been designed and used in Qutuf.

Morphological Analysis Includes both Stemming (light stemming) and Root Extraction (heavy stemming). It achive this by using finite state automates and rules for agreement developed for cliticization parsing. It also uses AlKhalil Morpho Sys open source database for root extraction, pattern matching, morphological feature and POS assignment and closed nouns after enriching it.

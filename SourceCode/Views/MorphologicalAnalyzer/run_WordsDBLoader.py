# -*- coding: utf-8 -*-
'''
Created on ١١‏/٠٥‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from RootsAndPatternsRepository import *;

rap = RootsAndPatternsRepository();
rap.Load('D:/temp/AlKhalil_1/db/', 'roots2');

print('Nominal Roots = ', len(rap.NominalRoots ));
for k, v in rap.NominalRoots.items():
    print('\tPattern length = ', k, ', count = ', len(v));
    
print('Verbal Roots = ', len(rap.VerbalRoots ));
for k, v in rap.VerbalRoots.items():
    print('\tPattern length = ', k, ', count = ', len(v));
    
print('Unvoweled Nominal Patterns = ', len(rap.UnvoweledNominalPatterns));
for k, v in rap.UnvoweledNominalPatterns.items():
    print('\tPattern length = ', k, ', count = ', len(v));
    
print('Unvoweled Verbal Patterns = ', len(rap.UnvoweledVerbalPatterns));
for k, v in rap.UnvoweledVerbalPatterns.items():
    print('\tPattern length = ', k, ', count = ', len(v));

print('Voweled Nominal Patterns = ', len(rap.VoweledNominalPatterns));
for k, v in rap.UnvoweledVerbalPatterns.items():
    print('\tPattern length = ', k, ', count = ', len(v));

print('Voweled Verbal Patterns = ', len(rap.VoweledVerbalPatterns));
for k, v in rap.UnvoweledVerbalPatterns.items():
    print('\tPattern length = ', k, ', count = ', len(v));


print('Number of Errors: ', len(Error_Log));
for i in range(len(Error_Log)):
    print(Error_Log[i]);
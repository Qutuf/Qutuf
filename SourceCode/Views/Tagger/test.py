import re;
#pattern = '[^((أيها)|(أيتها))]'
#pattern = 'اي?'
#print (re.match(pattern, "أيها"));
#print (re.match(pattern, "كلمة"));
#print (re.match(pattern, "يها"));
#print (re.match(pattern, "أيتها"));

pattern = '.*?[^ا]$'
pattern = '(?!ال).*?'
pattern = '(?!ال).*?[^ا]$'
pattern = '(?!ال).*?ا$'
pattern = '(?!ال).*$'
pattern = '(?!ال).*?[^ا]$'
pattern = 'ال$'
pattern = '(?!ال)';
pattern = '^(?!ال)';
print (re.search(pattern, "ال"));
print (re.search(pattern, "اللعبة"));
print (re.search(pattern, "الرجل"));
print (re.search(pattern, "الباقات"));
print (re.search(pattern, "الشعب"));
print (re.search(pattern, "على البال"));
print (re.search(pattern, "لعبة"));
print (re.search(pattern, "رجل"));
print (re.search(pattern, "رجلا"));
print (re.search(pattern, "باقة"));

class TestClass(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_hUBlT434Ed-gg8GOK1TmhA
    """
    att1 = ''
    
c1 = TestClass();
c1.__setattr__('att1',[1, '23']);
#print (c1.att1);


'''
Created on ١٠‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''

TokenTypeDict = dict();
TokenTypeDict[None] = "Unspecified"
TokenTypeDict[0] = "Text"
TokenTypeDict[1] = "Numbers"
TokenTypeDict[2] = "White Space"
TokenTypeDict[3] = "Punctuation"
TokenTypeDict[4] = "Unknown Character"

WhiteSpacesList = [];
WhiteSpacesList.append(" ");
WhiteSpacesList.append("\t");
WhiteSpacesList.append("\n");
WhiteSpacesList.append("\r");


#def Digit list
isDigit = [];
isDigit.append("1");
isDigit.append("2");
isDigit.append("3");
isDigit.append("4");
isDigit.append("5");
isDigit.append("6");
isDigit.append("7");
isDigit.append("8");
isDigit.append("9");
isDigit.append("0");

#def Sep list;
isSep = [];
isSep.append(" ");
isSep.append("\n"); 
#Added by Muhammad
isSep.append("\r");
isSep.append("\t");
isSep.append("_");
#Added by Muhammad
isSep.append(";");
#Added by Muhammad
isSep.append("؛");
#Added by Muhammad:
isSep.append("!");
#Added by Muhammad:
isSep.append("?");
#Added by Muhammad:
isSep.append("؟");
isSep.append("\0"); #Used as End_Of_File

#def new Ambiguous lists ; 
isAmbiguousA = [] ;
isAmbiguousB = [] ;
isAmbiguousC = [] ;
isAmbiguousD = [] ;

#new list A for Ambiguous ;
isAmbiguousA.append(".");
#new list B for Ambiguous ;       
isAmbiguousB.append("/");
isAmbiguousB.append(",");
isAmbiguousB.append("،");
isAmbiguousB.append(":");
#new list C for Ambiguous ;
#Removed by Muhammad:
#isAmbiguousC.append("!");
#Removed by Muhammad:
#isAmbiguousC.append("?");
isAmbiguousC.append("\'");
isAmbiguousC.append("\"");
isAmbiguousC.append("[");
isAmbiguousC.append("]");
isAmbiguousC.append("{");
isAmbiguousC.append("}");
isAmbiguousC.append("(");
isAmbiguousC.append(")");
#Added by Muhammad
isAmbiguousC.append("«");
#Added by Muhammad
isAmbiguousC.append("»");
#Added by Muhammad
isAmbiguousC.append("<");
#Added by Muhammad
isAmbiguousC.append(">");
isAmbiguousC.append("$");
#new list D for Math operator Ambiguous ;
isAmbiguousD.append("+");
isAmbiguousD.append("-");
isAmbiguousD.append("*");
isAmbiguousD.append("&");
isAmbiguousD.append("^");
isAmbiguousD.append("%");
isAmbiguousD.append("#");
isAmbiguousD.append("@");
isAmbiguousD.append("-");
isAmbiguousD.append("~");
isAmbiguousD.append("=");
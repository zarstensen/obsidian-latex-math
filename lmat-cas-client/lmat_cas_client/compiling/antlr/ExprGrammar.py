# Generated from ExprGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import lmat_cas_client.compiling.antlr.Ast as Ast
from typing import cast, Type

def rule_t[T](_t: Type[T], v: T | None = None) -> T:
	return cast(T, v)

def serializedATN():
    return [
        4,1,81,748,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,75,8,1,1,1,1,1,1,2,1,2,3,2,81,8,
        2,1,3,1,3,1,3,5,3,86,8,3,10,3,12,3,89,9,3,1,3,5,3,92,8,3,10,3,12,
        3,95,9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,109,
        8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,134,8,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,150,8,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,163,8,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,176,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,192,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,
        216,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,228,8,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,238,8,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,282,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,297,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,312,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,341,8,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,349,8,6,10,6,12,
        6,352,9,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,361,8,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,3,9,371,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,3,10,384,8,10,1,11,3,11,387,8,11,1,11,1,11,3,
        11,391,8,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,3,13,407,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,3,14,417,8,14,1,14,1,14,1,14,1,14,1,14,1,14,4,14,425,8,14,
        11,14,12,14,426,1,14,3,14,430,8,14,1,14,1,14,1,14,3,14,435,8,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        3,15,450,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        3,16,462,8,16,1,17,4,17,465,8,17,11,17,12,17,466,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,481,8,18,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,3,19,503,8,19,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,5,20,515,8,20,10,20,12,20,518,9,20,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        3,21,546,8,21,1,22,1,22,1,22,1,22,3,22,552,8,22,1,23,1,23,1,23,1,
        23,1,24,1,24,1,24,1,24,1,24,1,24,3,24,564,8,24,1,25,1,25,3,25,568,
        8,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,5,25,577,8,25,10,25,12,25,
        580,9,25,3,25,582,8,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,3,25,596,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,3,26,635,8,26,1,27,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,1,27,3,27,661,8,27,1,28,1,28,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,3,28,682,8,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,1,28,3,28,695,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,5,
        29,704,8,29,10,29,12,29,707,9,29,3,29,709,8,29,1,30,1,30,1,30,1,
        30,1,30,1,30,1,30,5,30,718,8,30,10,30,12,30,721,9,30,1,30,5,30,724,
        8,30,10,30,12,30,727,9,30,3,30,729,8,30,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,3,31,739,8,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,
        1,32,0,1,12,33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,0,9,1,0,28,29,1,0,12,
        17,2,0,40,40,42,42,2,0,8,8,41,41,2,0,45,45,49,49,2,0,37,37,39,39,
        1,0,6,7,2,0,37,37,59,59,2,0,11,11,38,38,816,0,66,1,0,0,0,2,74,1,
        0,0,0,4,80,1,0,0,0,6,82,1,0,0,0,8,96,1,0,0,0,10,108,1,0,0,0,12,281,
        1,0,0,0,14,353,1,0,0,0,16,360,1,0,0,0,18,370,1,0,0,0,20,383,1,0,
        0,0,22,386,1,0,0,0,24,394,1,0,0,0,26,406,1,0,0,0,28,434,1,0,0,0,
        30,449,1,0,0,0,32,461,1,0,0,0,34,464,1,0,0,0,36,480,1,0,0,0,38,502,
        1,0,0,0,40,504,1,0,0,0,42,545,1,0,0,0,44,551,1,0,0,0,46,553,1,0,
        0,0,48,563,1,0,0,0,50,595,1,0,0,0,52,634,1,0,0,0,54,660,1,0,0,0,
        56,694,1,0,0,0,58,708,1,0,0,0,60,728,1,0,0,0,62,738,1,0,0,0,64,742,
        1,0,0,0,66,67,3,2,1,0,67,68,6,0,-1,0,68,1,1,0,0,0,69,70,3,12,6,0,
        70,71,6,1,-1,0,71,75,1,0,0,0,72,75,3,10,5,0,73,75,3,8,4,0,74,69,
        1,0,0,0,74,72,1,0,0,0,74,73,1,0,0,0,75,76,1,0,0,0,76,77,5,0,0,1,
        77,3,1,0,0,0,78,81,3,12,6,0,79,81,3,10,5,0,80,78,1,0,0,0,80,79,1,
        0,0,0,81,5,1,0,0,0,82,87,3,4,2,0,83,84,5,71,0,0,84,86,3,4,2,0,85,
        83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,93,1,0,0,
        0,89,87,1,0,0,0,90,92,5,71,0,0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,
        1,0,0,0,93,94,1,0,0,0,94,7,1,0,0,0,95,93,1,0,0,0,96,97,5,68,0,0,
        97,98,3,6,3,0,98,99,5,69,0,0,99,9,1,0,0,0,100,101,3,12,6,0,101,102,
        3,14,7,0,102,103,3,10,5,0,103,109,1,0,0,0,104,105,3,12,6,0,105,106,
        3,14,7,0,106,107,3,12,6,0,107,109,1,0,0,0,108,100,1,0,0,0,108,104,
        1,0,0,0,109,11,1,0,0,0,110,111,6,6,-1,0,111,112,5,26,0,0,112,113,
        3,30,15,0,113,114,5,20,0,0,114,115,5,43,0,0,115,116,5,27,0,0,116,
        117,3,12,6,0,117,118,5,44,0,0,118,119,3,18,9,0,119,120,6,6,-1,0,
        120,282,1,0,0,0,121,122,5,26,0,0,122,123,3,30,15,0,123,124,3,12,
        6,0,124,125,5,27,0,0,125,126,3,12,6,25,126,127,6,6,-1,0,127,282,
        1,0,0,0,128,133,5,29,0,0,129,130,5,49,0,0,130,131,3,12,6,0,131,132,
        5,50,0,0,132,134,1,0,0,0,133,129,1,0,0,0,133,134,1,0,0,0,134,135,
        1,0,0,0,135,136,3,18,9,0,136,137,5,43,0,0,137,138,3,12,6,0,138,139,
        5,44,0,0,139,140,5,43,0,0,140,141,3,12,6,0,141,142,5,44,0,0,142,
        143,6,6,-1,0,143,282,1,0,0,0,144,149,7,0,0,0,145,146,5,49,0,0,146,
        147,3,12,6,0,147,148,5,50,0,0,148,150,1,0,0,0,149,145,1,0,0,0,149,
        150,1,0,0,0,150,151,1,0,0,0,151,152,3,18,9,0,152,153,5,43,0,0,153,
        154,3,12,6,0,154,155,5,44,0,0,155,156,6,6,-1,0,156,282,1,0,0,0,157,
        162,7,0,0,0,158,159,5,49,0,0,159,160,3,12,6,0,160,161,5,50,0,0,161,
        163,1,0,0,0,162,158,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,
        165,3,18,9,0,165,166,3,12,6,21,166,167,6,6,-1,0,167,282,1,0,0,0,
        168,169,5,20,0,0,169,170,5,43,0,0,170,175,5,27,0,0,171,172,5,49,
        0,0,172,173,3,12,6,0,173,174,5,50,0,0,174,176,1,0,0,0,175,171,1,
        0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,178,3,12,6,0,178,179,5,
        44,0,0,179,180,5,43,0,0,180,181,3,34,17,0,181,182,5,44,0,0,182,183,
        6,6,-1,0,183,282,1,0,0,0,184,185,5,20,0,0,185,186,5,43,0,0,186,191,
        5,27,0,0,187,188,5,49,0,0,188,189,3,12,6,0,189,190,5,50,0,0,190,
        192,1,0,0,0,191,187,1,0,0,0,191,192,1,0,0,0,192,193,1,0,0,0,193,
        194,5,44,0,0,194,195,5,43,0,0,195,196,3,34,17,0,196,197,5,44,0,0,
        197,198,3,12,6,19,198,199,6,6,-1,0,199,282,1,0,0,0,200,201,5,30,
        0,0,201,202,5,38,0,0,202,203,5,43,0,0,203,204,3,48,24,0,204,205,
        5,31,0,0,205,206,3,12,6,0,206,207,3,36,18,0,207,208,5,44,0,0,208,
        209,3,12,6,18,209,210,6,6,-1,0,210,282,1,0,0,0,211,212,5,32,0,0,
        212,216,6,6,-1,0,213,214,5,33,0,0,214,216,6,6,-1,0,215,211,1,0,0,
        0,215,213,1,0,0,0,216,217,1,0,0,0,217,218,3,38,19,0,218,219,5,45,
        0,0,219,220,3,12,6,0,220,221,5,46,0,0,221,222,6,6,-1,0,222,282,1,
        0,0,0,223,224,5,32,0,0,224,228,6,6,-1,0,225,226,5,33,0,0,226,228,
        6,6,-1,0,227,223,1,0,0,0,227,225,1,0,0,0,228,229,1,0,0,0,229,230,
        3,38,19,0,230,231,3,12,6,14,231,232,6,6,-1,0,232,282,1,0,0,0,233,
        234,5,6,0,0,234,238,6,6,-1,0,235,236,5,7,0,0,236,238,6,6,-1,0,237,
        233,1,0,0,0,237,235,1,0,0,0,238,239,1,0,0,0,239,240,3,12,6,12,240,
        241,6,6,-1,0,241,282,1,0,0,0,242,243,5,45,0,0,243,244,3,12,6,0,244,
        245,5,46,0,0,245,246,5,59,0,0,246,247,3,42,21,0,247,248,6,6,-1,0,
        248,282,1,0,0,0,249,250,5,3,0,0,250,251,3,12,6,0,251,252,5,59,0,
        0,252,253,3,42,21,0,253,254,6,6,-1,0,254,282,1,0,0,0,255,256,5,49,
        0,0,256,257,3,12,6,0,257,258,5,50,0,0,258,259,3,42,21,0,259,260,
        6,6,-1,0,260,282,1,0,0,0,261,262,3,54,27,0,262,263,6,6,-1,0,263,
        282,1,0,0,0,264,265,3,52,26,0,265,266,6,6,-1,0,266,282,1,0,0,0,267,
        268,3,56,28,0,268,269,6,6,-1,0,269,282,1,0,0,0,270,271,3,62,31,0,
        271,272,6,6,-1,0,272,282,1,0,0,0,273,274,3,64,32,0,274,275,6,6,-1,
        0,275,282,1,0,0,0,276,277,3,48,24,0,277,278,6,6,-1,0,278,282,1,0,
        0,0,279,280,5,73,0,0,280,282,6,6,-1,0,281,110,1,0,0,0,281,121,1,
        0,0,0,281,128,1,0,0,0,281,144,1,0,0,0,281,157,1,0,0,0,281,168,1,
        0,0,0,281,184,1,0,0,0,281,200,1,0,0,0,281,215,1,0,0,0,281,227,1,
        0,0,0,281,237,1,0,0,0,281,242,1,0,0,0,281,249,1,0,0,0,281,255,1,
        0,0,0,281,261,1,0,0,0,281,264,1,0,0,0,281,267,1,0,0,0,281,270,1,
        0,0,0,281,273,1,0,0,0,281,276,1,0,0,0,281,279,1,0,0,0,282,350,1,
        0,0,0,283,296,10,17,0,0,284,285,5,8,0,0,285,297,6,6,-1,0,286,287,
        5,19,0,0,287,297,6,6,-1,0,288,289,5,9,0,0,289,297,6,6,-1,0,290,291,
        5,25,0,0,291,297,6,6,-1,0,292,293,5,18,0,0,293,297,6,6,-1,0,294,
        295,5,10,0,0,295,297,6,6,-1,0,296,284,1,0,0,0,296,286,1,0,0,0,296,
        288,1,0,0,0,296,290,1,0,0,0,296,292,1,0,0,0,296,294,1,0,0,0,297,
        298,1,0,0,0,298,299,3,12,6,18,299,300,6,6,-1,0,300,349,1,0,0,0,301,
        302,10,16,0,0,302,303,4,6,2,0,303,304,3,12,6,17,304,305,6,6,-1,0,
        305,349,1,0,0,0,306,311,10,13,0,0,307,308,5,6,0,0,308,312,6,6,-1,
        0,309,310,5,7,0,0,310,312,6,6,-1,0,311,307,1,0,0,0,311,309,1,0,0,
        0,312,313,1,0,0,0,313,314,3,12,6,14,314,315,6,6,-1,0,315,349,1,0,
        0,0,316,317,10,29,0,0,317,318,5,11,0,0,318,319,3,20,10,0,319,320,
        5,38,0,0,320,321,3,28,14,0,321,322,6,6,-1,0,322,349,1,0,0,0,323,
        324,10,28,0,0,324,325,5,11,0,0,325,326,3,20,10,0,326,327,6,6,-1,
        0,327,349,1,0,0,0,328,329,10,27,0,0,329,330,5,38,0,0,330,331,3,28,
        14,0,331,332,6,6,-1,0,332,349,1,0,0,0,333,340,10,24,0,0,334,335,
        5,34,0,0,335,341,6,6,-1,0,336,337,5,35,0,0,337,341,6,6,-1,0,338,
        339,5,36,0,0,339,341,6,6,-1,0,340,334,1,0,0,0,340,336,1,0,0,0,340,
        338,1,0,0,0,341,342,1,0,0,0,342,349,6,6,-1,0,343,344,10,8,0,0,344,
        345,5,59,0,0,345,346,3,42,21,0,346,347,6,6,-1,0,347,349,1,0,0,0,
        348,283,1,0,0,0,348,301,1,0,0,0,348,306,1,0,0,0,348,316,1,0,0,0,
        348,323,1,0,0,0,348,328,1,0,0,0,348,333,1,0,0,0,348,343,1,0,0,0,
        349,352,1,0,0,0,350,348,1,0,0,0,350,351,1,0,0,0,351,13,1,0,0,0,352,
        350,1,0,0,0,353,354,7,1,0,0,354,15,1,0,0,0,355,356,3,44,22,0,356,
        357,6,8,-1,0,357,361,1,0,0,0,358,359,5,73,0,0,359,361,6,8,-1,0,360,
        355,1,0,0,0,360,358,1,0,0,0,361,17,1,0,0,0,362,363,3,16,8,0,363,
        364,6,9,-1,0,364,371,1,0,0,0,365,366,5,43,0,0,366,367,3,12,6,0,367,
        368,5,44,0,0,368,369,6,9,-1,0,369,371,1,0,0,0,370,362,1,0,0,0,370,
        365,1,0,0,0,371,19,1,0,0,0,372,373,3,16,8,0,373,374,6,10,-1,0,374,
        384,1,0,0,0,375,376,3,56,28,0,376,377,6,10,-1,0,377,384,1,0,0,0,
        378,379,5,43,0,0,379,380,3,12,6,0,380,381,5,44,0,0,381,382,6,10,
        -1,0,382,384,1,0,0,0,383,372,1,0,0,0,383,375,1,0,0,0,383,378,1,0,
        0,0,384,21,1,0,0,0,385,387,3,12,6,0,386,385,1,0,0,0,386,387,1,0,
        0,0,387,388,1,0,0,0,388,390,7,2,0,0,389,391,3,12,6,0,390,389,1,0,
        0,0,390,391,1,0,0,0,391,392,1,0,0,0,392,393,6,11,-1,0,393,23,1,0,
        0,0,394,395,7,3,0,0,395,25,1,0,0,0,396,397,3,12,6,0,397,398,6,13,
        -1,0,398,407,1,0,0,0,399,400,3,22,11,0,400,401,6,13,-1,0,401,407,
        1,0,0,0,402,403,3,24,12,0,403,404,6,13,-1,0,404,407,1,0,0,0,405,
        407,6,13,-1,0,406,396,1,0,0,0,406,399,1,0,0,0,406,402,1,0,0,0,406,
        405,1,0,0,0,407,27,1,0,0,0,408,409,3,16,8,0,409,410,6,14,-1,0,410,
        435,1,0,0,0,411,412,3,56,28,0,412,413,6,14,-1,0,413,435,1,0,0,0,
        414,416,5,43,0,0,415,417,7,4,0,0,416,415,1,0,0,0,416,417,1,0,0,0,
        417,418,1,0,0,0,418,419,3,26,13,0,419,424,6,14,-1,0,420,421,7,5,
        0,0,421,422,3,26,13,0,422,423,6,14,-1,0,423,425,1,0,0,0,424,420,
        1,0,0,0,425,426,1,0,0,0,426,424,1,0,0,0,426,427,1,0,0,0,427,429,
        1,0,0,0,428,430,7,4,0,0,429,428,1,0,0,0,429,430,1,0,0,0,430,431,
        1,0,0,0,431,432,5,44,0,0,432,433,6,14,-1,0,433,435,1,0,0,0,434,408,
        1,0,0,0,434,411,1,0,0,0,434,414,1,0,0,0,435,29,1,0,0,0,436,437,5,
        11,0,0,437,438,3,18,9,0,438,439,5,38,0,0,439,440,3,18,9,0,440,441,
        6,15,-1,0,441,450,1,0,0,0,442,443,5,38,0,0,443,444,3,18,9,0,444,
        445,5,11,0,0,445,446,3,18,9,0,446,447,6,15,-1,0,447,450,1,0,0,0,
        448,450,6,15,-1,0,449,436,1,0,0,0,449,442,1,0,0,0,449,448,1,0,0,
        0,450,31,1,0,0,0,451,452,5,27,0,0,452,453,3,12,6,0,453,454,5,11,
        0,0,454,455,3,18,9,0,455,456,6,16,-1,0,456,462,1,0,0,0,457,458,5,
        27,0,0,458,459,3,12,6,0,459,460,6,16,-1,0,460,462,1,0,0,0,461,451,
        1,0,0,0,461,457,1,0,0,0,462,33,1,0,0,0,463,465,3,32,16,0,464,463,
        1,0,0,0,465,466,1,0,0,0,466,464,1,0,0,0,466,467,1,0,0,0,467,35,1,
        0,0,0,468,481,6,18,-1,0,469,470,5,11,0,0,470,471,5,43,0,0,471,472,
        7,6,0,0,472,473,5,44,0,0,473,481,6,18,-1,0,474,475,5,11,0,0,475,
        476,5,6,0,0,476,481,6,18,-1,0,477,478,5,11,0,0,478,479,5,7,0,0,479,
        481,6,18,-1,0,480,468,1,0,0,0,480,469,1,0,0,0,480,474,1,0,0,0,480,
        477,1,0,0,0,481,37,1,0,0,0,482,483,5,38,0,0,483,484,5,43,0,0,484,
        485,3,12,6,0,485,486,5,12,0,0,486,487,3,12,6,0,487,488,5,44,0,0,
        488,489,5,11,0,0,489,490,3,20,10,0,490,491,6,19,-1,0,491,503,1,0,
        0,0,492,493,5,11,0,0,493,494,3,20,10,0,494,495,5,38,0,0,495,496,
        5,43,0,0,496,497,3,12,6,0,497,498,5,12,0,0,498,499,3,12,6,0,499,
        500,5,44,0,0,500,501,6,19,-1,0,501,503,1,0,0,0,502,482,1,0,0,0,502,
        492,1,0,0,0,503,39,1,0,0,0,504,505,3,12,6,0,505,506,5,12,0,0,506,
        507,3,12,6,0,507,516,6,20,-1,0,508,509,5,37,0,0,509,510,3,12,6,0,
        510,511,5,12,0,0,511,512,3,12,6,0,512,513,6,20,-1,0,513,515,1,0,
        0,0,514,508,1,0,0,0,515,518,1,0,0,0,516,514,1,0,0,0,516,517,1,0,
        0,0,517,41,1,0,0,0,518,516,1,0,0,0,519,520,5,38,0,0,520,521,5,43,
        0,0,521,522,3,40,20,0,522,523,5,44,0,0,523,524,6,21,-1,0,524,546,
        1,0,0,0,525,526,5,38,0,0,526,527,5,43,0,0,527,528,3,40,20,0,528,
        529,5,44,0,0,529,530,5,11,0,0,530,531,5,43,0,0,531,532,3,40,20,0,
        532,533,5,44,0,0,533,534,6,21,-1,0,534,546,1,0,0,0,535,536,5,11,
        0,0,536,537,5,43,0,0,537,538,3,40,20,0,538,539,5,44,0,0,539,540,
        5,38,0,0,540,541,5,43,0,0,541,542,3,40,20,0,542,543,5,44,0,0,543,
        544,6,21,-1,0,544,546,1,0,0,0,545,519,1,0,0,0,545,525,1,0,0,0,545,
        535,1,0,0,0,546,43,1,0,0,0,547,548,5,78,0,0,548,552,6,22,-1,0,549,
        550,5,79,0,0,550,552,6,22,-1,0,551,547,1,0,0,0,551,549,1,0,0,0,552,
        45,1,0,0,0,553,554,5,77,0,0,554,555,3,44,22,0,555,556,6,23,-1,0,
        556,47,1,0,0,0,557,558,3,44,22,0,558,559,6,24,-1,0,559,564,1,0,0,
        0,560,561,3,46,23,0,561,562,6,24,-1,0,562,564,1,0,0,0,563,557,1,
        0,0,0,563,560,1,0,0,0,564,49,1,0,0,0,565,568,5,1,0,0,566,568,5,2,
        0,0,567,565,1,0,0,0,567,566,1,0,0,0,568,569,1,0,0,0,569,581,5,45,
        0,0,570,571,3,12,6,0,571,578,6,25,-1,0,572,573,5,37,0,0,573,574,
        3,12,6,0,574,575,6,25,-1,0,575,577,1,0,0,0,576,572,1,0,0,0,577,580,
        1,0,0,0,578,576,1,0,0,0,578,579,1,0,0,0,579,582,1,0,0,0,580,578,
        1,0,0,0,581,570,1,0,0,0,581,582,1,0,0,0,582,583,1,0,0,0,583,584,
        5,46,0,0,584,596,6,25,-1,0,585,586,5,2,0,0,586,587,5,43,0,0,587,
        588,3,12,6,0,588,589,5,44,0,0,589,590,6,25,-1,0,590,596,1,0,0,0,
        591,592,5,2,0,0,592,593,3,12,6,0,593,594,6,25,-1,0,594,596,1,0,0,
        0,595,567,1,0,0,0,595,585,1,0,0,0,595,591,1,0,0,0,596,51,1,0,0,0,
        597,598,5,45,0,0,598,599,3,12,6,0,599,600,5,46,0,0,600,601,6,26,
        -1,0,601,635,1,0,0,0,602,603,5,49,0,0,603,604,3,12,6,0,604,605,5,
        50,0,0,605,606,6,26,-1,0,606,635,1,0,0,0,607,608,5,59,0,0,608,609,
        3,12,6,0,609,610,5,59,0,0,610,611,6,26,-1,0,611,635,1,0,0,0,612,
        613,5,60,0,0,613,614,3,12,6,0,614,615,5,60,0,0,615,616,6,26,-1,0,
        616,635,1,0,0,0,617,618,5,55,0,0,618,619,3,12,6,0,619,620,5,56,0,
        0,620,621,6,26,-1,0,621,635,1,0,0,0,622,623,5,53,0,0,623,624,3,12,
        6,0,624,625,5,54,0,0,625,626,6,26,-1,0,626,635,1,0,0,0,627,628,5,
        57,0,0,628,629,3,12,6,0,629,630,7,7,0,0,630,631,3,12,6,0,631,632,
        5,58,0,0,632,633,6,26,-1,0,633,635,1,0,0,0,634,597,1,0,0,0,634,602,
        1,0,0,0,634,607,1,0,0,0,634,612,1,0,0,0,634,617,1,0,0,0,634,622,
        1,0,0,0,634,627,1,0,0,0,635,53,1,0,0,0,636,637,5,43,0,0,637,638,
        7,8,0,0,638,639,3,12,6,0,639,640,5,78,0,0,640,641,4,27,9,1,641,642,
        5,11,0,0,642,643,3,12,6,0,643,644,5,44,0,0,644,645,6,27,-1,0,645,
        661,1,0,0,0,646,647,5,43,0,0,647,648,5,78,0,0,648,649,4,27,10,1,
        649,650,5,11,0,0,650,651,3,12,6,0,651,652,5,44,0,0,652,653,6,27,
        -1,0,653,661,1,0,0,0,654,655,5,43,0,0,655,656,5,34,0,0,656,657,3,
        12,6,0,657,658,5,44,0,0,658,659,6,27,-1,0,659,661,1,0,0,0,660,636,
        1,0,0,0,660,646,1,0,0,0,660,654,1,0,0,0,661,55,1,0,0,0,662,663,5,
        20,0,0,663,664,3,18,9,0,664,665,3,18,9,0,665,666,6,28,-1,0,666,695,
        1,0,0,0,667,668,5,21,0,0,668,669,3,18,9,0,669,670,3,18,9,0,670,671,
        6,28,-1,0,671,695,1,0,0,0,672,673,5,22,0,0,673,674,3,18,9,0,674,
        675,6,28,-1,0,675,695,1,0,0,0,676,681,5,22,0,0,677,678,5,49,0,0,
        678,679,3,12,6,0,679,680,5,50,0,0,680,682,1,0,0,0,681,677,1,0,0,
        0,681,682,1,0,0,0,682,683,1,0,0,0,683,684,3,18,9,0,684,685,6,28,
        -1,0,685,695,1,0,0,0,686,687,5,23,0,0,687,688,3,18,9,0,688,689,6,
        28,-1,0,689,695,1,0,0,0,690,691,5,24,0,0,691,692,3,18,9,0,692,693,
        6,28,-1,0,693,695,1,0,0,0,694,662,1,0,0,0,694,667,1,0,0,0,694,672,
        1,0,0,0,694,676,1,0,0,0,694,686,1,0,0,0,694,690,1,0,0,0,695,57,1,
        0,0,0,696,709,1,0,0,0,697,698,3,12,6,0,698,705,6,29,-1,0,699,700,
        5,70,0,0,700,701,3,12,6,0,701,702,6,29,-1,0,702,704,1,0,0,0,703,
        699,1,0,0,0,704,707,1,0,0,0,705,703,1,0,0,0,705,706,1,0,0,0,706,
        709,1,0,0,0,707,705,1,0,0,0,708,696,1,0,0,0,708,697,1,0,0,0,709,
        59,1,0,0,0,710,729,1,0,0,0,711,712,3,58,29,0,712,719,6,30,-1,0,713,
        714,5,71,0,0,714,715,3,58,29,0,715,716,6,30,-1,0,716,718,1,0,0,0,
        717,713,1,0,0,0,718,721,1,0,0,0,719,717,1,0,0,0,719,720,1,0,0,0,
        720,725,1,0,0,0,721,719,1,0,0,0,722,724,5,71,0,0,723,722,1,0,0,0,
        724,727,1,0,0,0,725,723,1,0,0,0,725,726,1,0,0,0,726,729,1,0,0,0,
        727,725,1,0,0,0,728,710,1,0,0,0,728,711,1,0,0,0,729,61,1,0,0,0,730,
        731,5,62,0,0,731,732,3,60,30,0,732,733,5,63,0,0,733,739,1,0,0,0,
        734,735,5,66,0,0,735,736,3,60,30,0,736,737,5,67,0,0,737,739,1,0,
        0,0,738,730,1,0,0,0,738,734,1,0,0,0,739,740,1,0,0,0,740,741,6,31,
        -1,0,741,63,1,0,0,0,742,743,5,64,0,0,743,744,3,60,30,0,744,745,5,
        65,0,0,745,746,6,32,-1,0,746,65,1,0,0,0,52,74,80,87,93,108,133,149,
        162,175,191,215,227,237,281,296,311,340,348,350,360,370,383,386,
        390,406,416,426,429,434,449,461,466,480,502,516,545,551,563,567,
        578,581,595,634,660,681,694,705,708,719,725,728,738
    ]

class ExprGrammar ( Parser ):

    grammarFileName = "ExprGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'^'", "'='", 
                     "<INVALID>", "'<'", "<INVALID>", "'>'", "<INVALID>", 
                     "'\\times'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\sqrt'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\lim'", "<INVALID>", "'\\sum'", "'\\prod'", "'!'", 
                     "'\\%'", "'\\textperthousand'", "','", "'_'", "';'", 
                     "':'", "'\\star'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'&'", "'\\\\'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\Delta'" ]

    symbolicNames = [ "<INVALID>", "FUNC_ID", "FUNC_CMD", "LBLANK", "RBLANK", 
                      "IGNORE", "PLUS", "MINUS", "MULT", "DIV", "XPROD", 
                      "POW", "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "TIMES", 
                      "DOT_PROD", "FRAC", "BINOM", "SQRT", "CONJUGATE", 
                      "VEC_UNIT", "MOD", "INT", "DIFFERENTIAL", "PHYS_DERIVATIVE", 
                      "PHYS_PARTIAL_DERIVATIVE", "LIMIT", "LIMIT_ARROW", 
                      "SUM", "PRODUCT", "BANG", "PERCENT", "PERMILLE", "COMMA", 
                      "UNDERSCORE", "SEMICOLON", "COLON", "STAR", "DOTS", 
                      "LBRACE", "RBRACE", "LPAREN", "RPAREN", "LBRACE_LITERAL", 
                      "RBRACE_LITERAL", "LBRACKET", "RBRACKET", "LBRACK_CMD", 
                      "RBRACK_CMD", "LCEIL", "RCEIL", "LFLOOR", "RFLOOR", 
                      "LANGLE", "RANGLE", "BAR", "DOUBLE_BAR", "DOT", "BEGIN_MATRIX", 
                      "END_MATRIX", "BEGIN_V_MATRIX", "END_V_MATRIX", "BEGIN_ARRAY", 
                      "END_ARRAY", "BEGIN_ENV", "END_ENV", "ENV_EL_SEP", 
                      "ENV_ROW_SEP", "ENV_SEP_SKIP", "NUMBER", "BIN_NUMBER", 
                      "OCT_NUMBER", "HEX_NUMBER", "DELTA", "ID", "COMMAND", 
                      "ARG_COMM", "ARG_WS" ]

    RULE_debug = 0
    RULE_a_lmat_expr = 1
    RULE_system_el = 2
    RULE_system_body = 3
    RULE_system = 4
    RULE_relation = 5
    RULE_a_expr = 6
    RULE_rel_op = 7
    RULE_atom = 8
    RULE_latex_cmd_arg = 9
    RULE_pow_arg = 10
    RULE_range_index = 11
    RULE_all_index = 12
    RULE_index_entry = 13
    RULE_index_arg = 14
    RULE_int_bounds = 15
    RULE_diff_var = 16
    RULE_diff_vars = 17
    RULE_limit_dir = 18
    RULE_series_range_args = 19
    RULE_eval_at_sub_vars = 20
    RULE_eval_at_arg = 21
    RULE_primary_symbol = 22
    RULE_delta_symbol = 23
    RULE_symbol = 24
    RULE_function = 25
    RULE_delim_expr = 26
    RULE_combinatorial = 27
    RULE_cmd_func = 28
    RULE_matrix_row = 29
    RULE_matrix_body = 30
    RULE_matrix = 31
    RULE_det_matrix = 32

    ruleNames =  [ "debug", "a_lmat_expr", "system_el", "system_body", "system", 
                   "relation", "a_expr", "rel_op", "atom", "latex_cmd_arg", 
                   "pow_arg", "range_index", "all_index", "index_entry", 
                   "index_arg", "int_bounds", "diff_var", "diff_vars", "limit_dir", 
                   "series_range_args", "eval_at_sub_vars", "eval_at_arg", 
                   "primary_symbol", "delta_symbol", "symbol", "function", 
                   "delim_expr", "combinatorial", "cmd_func", "matrix_row", 
                   "matrix_body", "matrix", "det_matrix" ]

    EOF = Token.EOF
    FUNC_ID=1
    FUNC_CMD=2
    LBLANK=3
    RBLANK=4
    IGNORE=5
    PLUS=6
    MINUS=7
    MULT=8
    DIV=9
    XPROD=10
    POW=11
    EQ=12
    NEQ=13
    LT=14
    LTE=15
    GT=16
    GTE=17
    TIMES=18
    DOT_PROD=19
    FRAC=20
    BINOM=21
    SQRT=22
    CONJUGATE=23
    VEC_UNIT=24
    MOD=25
    INT=26
    DIFFERENTIAL=27
    PHYS_DERIVATIVE=28
    PHYS_PARTIAL_DERIVATIVE=29
    LIMIT=30
    LIMIT_ARROW=31
    SUM=32
    PRODUCT=33
    BANG=34
    PERCENT=35
    PERMILLE=36
    COMMA=37
    UNDERSCORE=38
    SEMICOLON=39
    COLON=40
    STAR=41
    DOTS=42
    LBRACE=43
    RBRACE=44
    LPAREN=45
    RPAREN=46
    LBRACE_LITERAL=47
    RBRACE_LITERAL=48
    LBRACKET=49
    RBRACKET=50
    LBRACK_CMD=51
    RBRACK_CMD=52
    LCEIL=53
    RCEIL=54
    LFLOOR=55
    RFLOOR=56
    LANGLE=57
    RANGLE=58
    BAR=59
    DOUBLE_BAR=60
    DOT=61
    BEGIN_MATRIX=62
    END_MATRIX=63
    BEGIN_V_MATRIX=64
    END_V_MATRIX=65
    BEGIN_ARRAY=66
    END_ARRAY=67
    BEGIN_ENV=68
    END_ENV=69
    ENV_EL_SEP=70
    ENV_ROW_SEP=71
    ENV_SEP_SKIP=72
    NUMBER=73
    BIN_NUMBER=74
    OCT_NUMBER=75
    HEX_NUMBER=76
    DELTA=77
    ID=78
    COMMAND=79
    ARG_COMM=80
    ARG_WS=81

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    func_set: set[str] = set()



    class DebugContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AExpr)
            self._a_lmat_expr = None # A_lmat_exprContext

        def a_lmat_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_lmat_exprContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_debug

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDebug" ):
                listener.enterDebug(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDebug" ):
                listener.exitDebug(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDebug" ):
                return visitor.visitDebug(self)
            else:
                return visitor.visitChildren(self)




    def debug(self):

        localctx = ExprGrammar.DebugContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_debug)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            localctx._a_lmat_expr = self.a_lmat_expr()
            localctx.res = localctx._a_lmat_expr.res
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A_lmat_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AExpr)
            self._a_expr = None # A_exprContext

        def EOF(self):
            return self.getToken(ExprGrammar.EOF, 0)

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def relation(self):
            return self.getTypedRuleContext(ExprGrammar.RelationContext,0)


        def system(self):
            return self.getTypedRuleContext(ExprGrammar.SystemContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_a_lmat_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA_lmat_expr" ):
                listener.enterA_lmat_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA_lmat_expr" ):
                listener.exitA_lmat_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA_lmat_expr" ):
                return visitor.visitA_lmat_expr(self)
            else:
                return visitor.visitChildren(self)




    def a_lmat_expr(self):

        localctx = ExprGrammar.A_lmat_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_a_lmat_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 69
                localctx._a_expr = self.a_expr(0)
                localctx.res = localctx._a_expr.res
                pass

            elif la_ == 2:
                self.state = 72
                self.relation()
                pass

            elif la_ == 3:
                self.state = 73
                self.system()
                pass


            self.state = 76
            self.match(ExprGrammar.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class System_elContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def relation(self):
            return self.getTypedRuleContext(ExprGrammar.RelationContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_system_el

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSystem_el" ):
                listener.enterSystem_el(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSystem_el" ):
                listener.exitSystem_el(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSystem_el" ):
                return visitor.visitSystem_el(self)
            else:
                return visitor.visitChildren(self)




    def system_el(self):

        localctx = ExprGrammar.System_elContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_system_el)
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.a_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.relation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class System_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def system_el(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.System_elContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.System_elContext,i)


        def ENV_ROW_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.ENV_ROW_SEP)
            else:
                return self.getToken(ExprGrammar.ENV_ROW_SEP, i)

        def getRuleIndex(self):
            return ExprGrammar.RULE_system_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSystem_body" ):
                listener.enterSystem_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSystem_body" ):
                listener.exitSystem_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSystem_body" ):
                return visitor.visitSystem_body(self)
            else:
                return visitor.visitChildren(self)




    def system_body(self):

        localctx = ExprGrammar.System_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_system_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.system_el()
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 83
                    self.match(ExprGrammar.ENV_ROW_SEP)
                    self.state = 84
                    self.system_el() 
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==71:
                self.state = 90
                self.match(ExprGrammar.ENV_ROW_SEP)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SystemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_ENV(self):
            return self.getToken(ExprGrammar.BEGIN_ENV, 0)

        def system_body(self):
            return self.getTypedRuleContext(ExprGrammar.System_bodyContext,0)


        def END_ENV(self):
            return self.getToken(ExprGrammar.END_ENV, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_system

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSystem" ):
                listener.enterSystem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSystem" ):
                listener.exitSystem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSystem" ):
                return visitor.visitSystem(self)
            else:
                return visitor.visitChildren(self)




    def system(self):

        localctx = ExprGrammar.SystemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_system)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(ExprGrammar.BEGIN_ENV)
            self.state = 97
            self.system_body()
            self.state = 98
            self.match(ExprGrammar.END_ENV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)


        def rel_op(self):
            return self.getTypedRuleContext(ExprGrammar.Rel_opContext,0)


        def relation(self):
            return self.getTypedRuleContext(ExprGrammar.RelationContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)




    def relation(self):

        localctx = ExprGrammar.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relation)
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.a_expr(0)
                self.state = 101
                self.rel_op()
                self.state = 102
                self.relation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.a_expr(0)
                self.state = 105
                self.rel_op()
                self.state = 106
                self.a_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AExpr)
            self.node_t = rule_t(type)
            self.base = None # A_exprContext
            self.op = None # A_exprContext
            self.lhs = None # A_exprContext
            self.expr = None # A_exprContext
            self._int_bounds = None # Int_boundsContext
            self.diff = None # A_exprContext
            self._a_expr = None # A_exprContext
            self.recip_integrand = None # Latex_cmd_argContext
            self._latex_cmd_arg = None # Latex_cmd_argContext
            self.integrand = None # A_exprContext
            self.diff_l = None # A_exprContext
            self.diff_r = None # A_exprContext
            self.degree = None # A_exprContext
            self.diffand_last = None # A_exprContext
            self._diff_vars = None # Diff_varsContext
            self.lim_var = None # SymbolContext
            self._symbol = None # SymbolContext
            self.lim_poa = None # A_exprContext
            self._limit_dir = None # Limit_dirContext
            self._series_range_args = None # Series_range_argsContext
            self._eval_at_arg = None # Eval_at_argContext
            self._combinatorial = None # CombinatorialContext
            self._delim_expr = None # Delim_exprContext
            self._cmd_func = None # Cmd_funcContext
            self._matrix = None # MatrixContext
            self._det_matrix = None # Det_matrixContext
            self._NUMBER = None # Token
            self.rhs = None # A_exprContext
            self.exp = None # Pow_argContext
            self.index = None # Index_argContext

        def INT(self):
            return self.getToken(ExprGrammar.INT, 0)

        def int_bounds(self):
            return self.getTypedRuleContext(ExprGrammar.Int_boundsContext,0)


        def FRAC(self):
            return self.getToken(ExprGrammar.FRAC, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.LBRACE)
            else:
                return self.getToken(ExprGrammar.LBRACE, i)

        def DIFFERENTIAL(self):
            return self.getToken(ExprGrammar.DIFFERENTIAL, 0)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.RBRACE)
            else:
                return self.getToken(ExprGrammar.RBRACE, i)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)


        def latex_cmd_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Latex_cmd_argContext,0)


        def PHYS_PARTIAL_DERIVATIVE(self):
            return self.getToken(ExprGrammar.PHYS_PARTIAL_DERIVATIVE, 0)

        def LBRACKET(self):
            return self.getToken(ExprGrammar.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(ExprGrammar.RBRACKET, 0)

        def PHYS_DERIVATIVE(self):
            return self.getToken(ExprGrammar.PHYS_DERIVATIVE, 0)

        def diff_vars(self):
            return self.getTypedRuleContext(ExprGrammar.Diff_varsContext,0)


        def LIMIT(self):
            return self.getToken(ExprGrammar.LIMIT, 0)

        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)

        def LIMIT_ARROW(self):
            return self.getToken(ExprGrammar.LIMIT_ARROW, 0)

        def limit_dir(self):
            return self.getTypedRuleContext(ExprGrammar.Limit_dirContext,0)


        def symbol(self):
            return self.getTypedRuleContext(ExprGrammar.SymbolContext,0)


        def series_range_args(self):
            return self.getTypedRuleContext(ExprGrammar.Series_range_argsContext,0)


        def LPAREN(self):
            return self.getToken(ExprGrammar.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExprGrammar.RPAREN, 0)

        def SUM(self):
            return self.getToken(ExprGrammar.SUM, 0)

        def PRODUCT(self):
            return self.getToken(ExprGrammar.PRODUCT, 0)

        def PLUS(self):
            return self.getToken(ExprGrammar.PLUS, 0)

        def MINUS(self):
            return self.getToken(ExprGrammar.MINUS, 0)

        def BAR(self):
            return self.getToken(ExprGrammar.BAR, 0)

        def eval_at_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Eval_at_argContext,0)


        def LBLANK(self):
            return self.getToken(ExprGrammar.LBLANK, 0)

        def combinatorial(self):
            return self.getTypedRuleContext(ExprGrammar.CombinatorialContext,0)


        def delim_expr(self):
            return self.getTypedRuleContext(ExprGrammar.Delim_exprContext,0)


        def cmd_func(self):
            return self.getTypedRuleContext(ExprGrammar.Cmd_funcContext,0)


        def matrix(self):
            return self.getTypedRuleContext(ExprGrammar.MatrixContext,0)


        def det_matrix(self):
            return self.getTypedRuleContext(ExprGrammar.Det_matrixContext,0)


        def NUMBER(self):
            return self.getToken(ExprGrammar.NUMBER, 0)

        def MULT(self):
            return self.getToken(ExprGrammar.MULT, 0)

        def DOT_PROD(self):
            return self.getToken(ExprGrammar.DOT_PROD, 0)

        def DIV(self):
            return self.getToken(ExprGrammar.DIV, 0)

        def MOD(self):
            return self.getToken(ExprGrammar.MOD, 0)

        def TIMES(self):
            return self.getToken(ExprGrammar.TIMES, 0)

        def XPROD(self):
            return self.getToken(ExprGrammar.XPROD, 0)

        def POW(self):
            return self.getToken(ExprGrammar.POW, 0)

        def pow_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Pow_argContext,0)


        def index_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Index_argContext,0)


        def BANG(self):
            return self.getToken(ExprGrammar.BANG, 0)

        def PERCENT(self):
            return self.getToken(ExprGrammar.PERCENT, 0)

        def PERMILLE(self):
            return self.getToken(ExprGrammar.PERMILLE, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_a_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA_expr" ):
                listener.enterA_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA_expr" ):
                listener.exitA_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA_expr" ):
                return visitor.visitA_expr(self)
            else:
                return visitor.visitChildren(self)



    def a_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprGrammar.A_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_a_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 111
                self.match(ExprGrammar.INT)
                self.state = 112
                localctx._int_bounds = self.int_bounds()
                self.state = 113
                self.match(ExprGrammar.FRAC)
                self.state = 114
                self.match(ExprGrammar.LBRACE)
                self.state = 115
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 116
                localctx.diff = localctx._a_expr = self.a_expr(0)
                self.state = 117
                self.match(ExprGrammar.RBRACE)
                self.state = 118
                localctx.recip_integrand = localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Integral(localctx, Ast.DivOp(localctx.recip_integrand, Ast.Number(localctx.recip_integrand, "1"), localctx.recip_integrand.res), localctx.diff.res, localctx._int_bounds.bounds)
                pass

            elif la_ == 2:
                self.state = 121
                self.match(ExprGrammar.INT)
                self.state = 122
                localctx._int_bounds = self.int_bounds()
                self.state = 123
                localctx.integrand = localctx._a_expr = self.a_expr(0)
                self.state = 124
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 125
                localctx.diff = localctx._a_expr = self.a_expr(25)
                localctx.res = Ast.Integral(localctx, localctx.integrand.res, localctx.diff.res, localctx._int_bounds.bounds)
                pass

            elif la_ == 3:
                self.state = 128
                self.match(ExprGrammar.PHYS_PARTIAL_DERIVATIVE)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 129
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 130
                    localctx._a_expr = self.a_expr(0)
                    self.state = 131
                    self.match(ExprGrammar.RBRACKET)


                self.state = 135
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 136
                self.match(ExprGrammar.LBRACE)
                self.state = 137
                localctx.diff_l = localctx._a_expr = self.a_expr(0)
                self.state = 138
                self.match(ExprGrammar.RBRACE)
                self.state = 139
                self.match(ExprGrammar.LBRACE)
                self.state = 140
                localctx.diff_r = localctx._a_expr = self.a_expr(0)
                self.state = 141
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._latex_cmd_arg.res, [(localctx.diff_l.res, None), (localctx.diff_r.res, None)])
                pass

            elif la_ == 4:
                self.state = 144
                _la = self._input.LA(1)
                if not(_la==28 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 145
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 146
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 147
                    self.match(ExprGrammar.RBRACKET)


                self.state = 151
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 152
                self.match(ExprGrammar.LBRACE)
                self.state = 153
                localctx._a_expr = self.a_expr(0)
                self.state = 154
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._latex_cmd_arg.res, [(localctx._a_expr.res, localctx.degree.res)])
                pass

            elif la_ == 5:
                self.state = 157
                _la = self._input.LA(1)
                if not(_la==28 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 158
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 159
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 160
                    self.match(ExprGrammar.RBRACKET)


                self.state = 164
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 165
                localctx.diffand_last = localctx._a_expr = self.a_expr(21)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, [(localctx._latex_cmd_arg.res, localctx.degree.res)])
                pass

            elif la_ == 6:
                self.state = 168
                self.match(ExprGrammar.FRAC)
                self.state = 169
                self.match(ExprGrammar.LBRACE)
                self.state = 170
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 175
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 171
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 172
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 173
                    self.match(ExprGrammar.RBRACKET)


                self.state = 177
                localctx._a_expr = self.a_expr(0)
                self.state = 178
                self.match(ExprGrammar.RBRACE)
                self.state = 179
                self.match(ExprGrammar.LBRACE)
                self.state = 180
                localctx._diff_vars = self.diff_vars()
                self.state = 181
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, localctx._diff_vars.res)
                pass

            elif la_ == 7:
                self.state = 184
                self.match(ExprGrammar.FRAC)
                self.state = 185
                self.match(ExprGrammar.LBRACE)
                self.state = 186
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 187
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 188
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 189
                    self.match(ExprGrammar.RBRACKET)


                self.state = 193
                self.match(ExprGrammar.RBRACE)
                self.state = 194
                self.match(ExprGrammar.LBRACE)
                self.state = 195
                localctx._diff_vars = self.diff_vars()
                self.state = 196
                self.match(ExprGrammar.RBRACE)
                self.state = 197
                localctx._a_expr = self.a_expr(19)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, localctx._diff_vars.res)
                pass

            elif la_ == 8:
                self.state = 200
                self.match(ExprGrammar.LIMIT)
                self.state = 201
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 202
                self.match(ExprGrammar.LBRACE)
                self.state = 203
                localctx.lim_var = localctx._symbol = self.symbol()
                self.state = 204
                self.match(ExprGrammar.LIMIT_ARROW)
                self.state = 205
                localctx.lim_poa = localctx._a_expr = self.a_expr(0)
                self.state = 206
                localctx._limit_dir = self.limit_dir()
                self.state = 207
                self.match(ExprGrammar.RBRACE)
                self.state = 208
                localctx._a_expr = self.a_expr(18)
                localctx.res = Ast.Limit(localctx._a_expr.res, localctx.lim_var.res, localctx.lim_poa.res, localctx._limit_dir.res)
                pass

            elif la_ == 9:
                self.state = 215
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32]:
                    self.state = 211
                    self.match(ExprGrammar.SUM)
                    localctx.node_t = Ast.Sum
                    pass
                elif token in [33]:
                    self.state = 213
                    self.match(ExprGrammar.PRODUCT)
                    localctx.node_t = Ast.Product
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 217
                localctx._series_range_args = self.series_range_args()
                self.state = 218
                self.match(ExprGrammar.LPAREN)
                self.state = 219
                localctx._a_expr = self.a_expr(0)
                self.state = 220
                self.match(ExprGrammar.RPAREN)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res, localctx._series_range_args.symb, (localctx._series_range_args.start, localctx._series_range_args.end))
                pass

            elif la_ == 10:
                self.state = 227
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32]:
                    self.state = 223
                    self.match(ExprGrammar.SUM)
                    localctx.node_t = Ast.Sum
                    pass
                elif token in [33]:
                    self.state = 225
                    self.match(ExprGrammar.PRODUCT)
                    localctx.node_t = Ast.Product
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 229
                localctx._series_range_args = self.series_range_args()
                self.state = 230
                localctx._a_expr = self.a_expr(14)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res, localctx._series_range_args.symb, (localctx._series_range_args.start, localctx._series_range_args.end))
                pass

            elif la_ == 11:
                self.state = 237
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 233
                    self.match(ExprGrammar.PLUS)
                    localctx.node_t = Ast.UPlusOp
                    pass
                elif token in [7]:
                    self.state = 235
                    self.match(ExprGrammar.MINUS)
                    localctx.node_t = Ast.UMinusOp
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 239
                localctx._a_expr = self.a_expr(12)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res)
                pass

            elif la_ == 12:
                self.state = 242
                self.match(ExprGrammar.LPAREN)
                self.state = 243
                localctx.expr = localctx._a_expr = self.a_expr(0)
                self.state = 244
                self.match(ExprGrammar.RPAREN)
                self.state = 245
                self.match(ExprGrammar.BAR)
                self.state = 246
                localctx._eval_at_arg = self.eval_at_arg()
                localctx.res = Ast.EvalAt(localctx, localctx.expr.res, localctx._eval_at_arg.subs_start, localctx._eval_at_arg.subs_end)
                pass

            elif la_ == 13:
                self.state = 249
                self.match(ExprGrammar.LBLANK)
                self.state = 250
                localctx.expr = localctx._a_expr = self.a_expr(0)
                self.state = 251
                self.match(ExprGrammar.BAR)
                self.state = 252
                localctx._eval_at_arg = self.eval_at_arg()
                localctx.res = Ast.EvalAt(localctx, localctx.expr.res, localctx._eval_at_arg.subs_start, localctx._eval_at_arg.subs_end)
                pass

            elif la_ == 14:
                self.state = 255
                self.match(ExprGrammar.LBRACKET)
                self.state = 256
                localctx.expr = localctx._a_expr = self.a_expr(0)
                self.state = 257
                self.match(ExprGrammar.RBRACKET)
                self.state = 258
                localctx._eval_at_arg = self.eval_at_arg()
                localctx.res = Ast.EvalAt(localctx, localctx.expr.res, localctx._eval_at_arg.subs_start, localctx._eval_at_arg.subs_end)
                pass

            elif la_ == 15:
                self.state = 261
                localctx._combinatorial = self.combinatorial()
                localctx.res = localctx._combinatorial.res
                pass

            elif la_ == 16:
                self.state = 264
                localctx._delim_expr = self.delim_expr()
                localctx.res = localctx._delim_expr.res
                pass

            elif la_ == 17:
                self.state = 267
                localctx._cmd_func = self.cmd_func()
                localctx.res = localctx._cmd_func.res
                pass

            elif la_ == 18:
                self.state = 270
                localctx._matrix = self.matrix()
                localctx.res = localctx._matrix.res 
                pass

            elif la_ == 19:
                self.state = 273
                localctx._det_matrix = self.det_matrix()
                localctx.res = localctx._det_matrix.res
                pass

            elif la_ == 20:
                self.state = 276
                localctx._symbol = self.symbol()
                localctx.res = localctx._symbol.res
                pass

            elif la_ == 21:
                self.state = 279
                localctx._NUMBER = self.match(ExprGrammar.NUMBER)
                localctx.res = Ast.Number(localctx, (None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 350
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 348
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 283
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 296
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [8]:
                            self.state = 284
                            self.match(ExprGrammar.MULT)
                            localctx.node_t = Ast.MultOp
                            pass
                        elif token in [19]:
                            self.state = 286
                            self.match(ExprGrammar.DOT_PROD)
                            localctx.node_t = Ast.MultOp
                            pass
                        elif token in [9]:
                            self.state = 288
                            self.match(ExprGrammar.DIV)
                            localctx.node_t = Ast.DivOp
                            pass
                        elif token in [25]:
                            self.state = 290
                            self.match(ExprGrammar.MOD)
                            localctx.node_t = Ast.ModOp
                            pass
                        elif token in [18]:
                            self.state = 292
                            self.match(ExprGrammar.TIMES)
                            localctx.node_t = Ast.XProdOp
                            pass
                        elif token in [10]:
                            self.state = 294
                            self.match(ExprGrammar.XPROD)
                            localctx.node_t = Ast.XProdOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 298
                        localctx.rhs = localctx._a_expr = self.a_expr(18)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 2:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 301
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 302
                        if not ((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS)):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS))")
                        self.state = 303
                        localctx.rhs = localctx._a_expr = self.a_expr(17)
                        localctx.res = Ast.MultOp(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 3:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 306
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 311
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [6]:
                            self.state = 307
                            self.match(ExprGrammar.PLUS)
                            localctx.node_t = Ast.AddOp
                            pass
                        elif token in [7]:
                            self.state = 309
                            self.match(ExprGrammar.MINUS)
                            localctx.node_t = Ast.SubOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 313
                        localctx.rhs = localctx._a_expr = self.a_expr(14)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 4:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 316
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 317
                        self.match(ExprGrammar.POW)
                        self.state = 318
                        localctx.exp = self.pow_arg()
                        self.state = 319
                        self.match(ExprGrammar.UNDERSCORE)
                        self.state = 320
                        localctx.index = self.index_arg()
                        localctx.res=Ast.ExpOp(localctx, localctx.base.res, localctx.exp.res)
                        pass

                    elif la_ == 5:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 323
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 324
                        self.match(ExprGrammar.POW)
                        self.state = 325
                        localctx.exp = self.pow_arg()
                        localctx.res=Ast.ExpOp(localctx, localctx.base.res, localctx.exp.res)
                        pass

                    elif la_ == 6:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 328
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 329
                        self.match(ExprGrammar.UNDERSCORE)
                        self.state = 330
                        localctx.index = self.index_arg()
                        localctx.res = Ast.IndexOp(localctx, localctx.base.res, localctx.index.res)
                        pass

                    elif la_ == 7:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.op = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 333
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 340
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [34]:
                            self.state = 334
                            self.match(ExprGrammar.BANG)
                            localctx.node_t = Ast.Factorial
                            pass
                        elif token in [35]:
                            self.state = 336
                            self.match(ExprGrammar.PERCENT)
                            localctx.node_t = Ast.Percent
                            pass
                        elif token in [36]:
                            self.state = 338
                            self.match(ExprGrammar.PERMILLE)
                            localctx.node_t = Ast.Permille
                            pass
                        else:
                            raise NoViableAltException(self)

                        localctx.res = localctx.node_t(localctx, localctx.op.res)
                        pass

                    elif la_ == 8:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.expr = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 343
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 344
                        self.match(ExprGrammar.BAR)
                        self.state = 345
                        localctx._eval_at_arg = self.eval_at_arg()
                        localctx.res = Ast.EvalAt(localctx, localctx.expr.res, localctx._eval_at_arg.subs_start, localctx._eval_at_arg.subs_end)
                        pass

             
                self.state = 352
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Rel_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(ExprGrammar.EQ, 0)

        def NEQ(self):
            return self.getToken(ExprGrammar.NEQ, 0)

        def LT(self):
            return self.getToken(ExprGrammar.LT, 0)

        def LTE(self):
            return self.getToken(ExprGrammar.LTE, 0)

        def GT(self):
            return self.getToken(ExprGrammar.GT, 0)

        def GTE(self):
            return self.getToken(ExprGrammar.GTE, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_rel_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel_op" ):
                listener.enterRel_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel_op" ):
                listener.exitRel_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_op" ):
                return visitor.visitRel_op(self)
            else:
                return visitor.visitChildren(self)




    def rel_op(self):

        localctx = ExprGrammar.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AExpr)
            self._primary_symbol = None # Primary_symbolContext
            self._NUMBER = None # Token

        def primary_symbol(self):
            return self.getTypedRuleContext(ExprGrammar.Primary_symbolContext,0)


        def NUMBER(self):
            return self.getToken(ExprGrammar.NUMBER, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ExprGrammar.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atom)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [78, 79]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                localctx._primary_symbol = self.primary_symbol()
                localctx.res = localctx._primary_symbol.res
                pass
            elif token in [73]:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                localctx._NUMBER = self.match(ExprGrammar.NUMBER)
                localctx.res = Ast.Number(localctx, (None if localctx._NUMBER is None else localctx._NUMBER.text))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Latex_cmd_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AExpr)
            self._atom = None # AtomContext
            self._a_expr = None # A_exprContext

        def atom(self):
            return self.getTypedRuleContext(ExprGrammar.AtomContext,0)


        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_latex_cmd_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLatex_cmd_arg" ):
                listener.enterLatex_cmd_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLatex_cmd_arg" ):
                listener.exitLatex_cmd_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLatex_cmd_arg" ):
                return visitor.visitLatex_cmd_arg(self)
            else:
                return visitor.visitChildren(self)




    def latex_cmd_arg(self):

        localctx = ExprGrammar.Latex_cmd_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_latex_cmd_arg)
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [73, 78, 79]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.match(ExprGrammar.LBRACE)
                self.state = 366
                localctx._a_expr = self.a_expr(0)
                self.state = 367
                self.match(ExprGrammar.RBRACE)
                localctx.res = localctx._a_expr.res
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pow_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AExpr)
            self._atom = None # AtomContext
            self._cmd_func = None # Cmd_funcContext
            self._a_expr = None # A_exprContext

        def atom(self):
            return self.getTypedRuleContext(ExprGrammar.AtomContext,0)


        def cmd_func(self):
            return self.getTypedRuleContext(ExprGrammar.Cmd_funcContext,0)


        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_pow_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPow_arg" ):
                listener.enterPow_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow_arg" ):
                listener.exitPow_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow_arg" ):
                return visitor.visitPow_arg(self)
            else:
                return visitor.visitChildren(self)




    def pow_arg(self):

        localctx = ExprGrammar.Pow_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_pow_arg)
        try:
            self.state = 383
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [73, 78, 79]:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass
            elif token in [20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                localctx._cmd_func = self.cmd_func()
                localctx.res = localctx._cmd_func.res
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.match(ExprGrammar.LBRACE)
                self.state = 379
                localctx._a_expr = self.a_expr(0)
                self.state = 380
                self.match(ExprGrammar.RBRACE)
                localctx.res = localctx._a_expr.res
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(tuple[Ast.AExpr | None, Ast.AExpr | None])
            self.beg = None # A_exprContext
            self.end = None # A_exprContext

        def COLON(self):
            return self.getToken(ExprGrammar.COLON, 0)

        def DOTS(self):
            return self.getToken(ExprGrammar.DOTS, 0)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)


        def getRuleIndex(self):
            return ExprGrammar.RULE_range_index

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_index" ):
                listener.enterRange_index(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_index" ):
                listener.exitRange_index(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_index" ):
                return visitor.visitRange_index(self)
            else:
                return visitor.visitChildren(self)




    def range_index(self):

        localctx = ExprGrammar.Range_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_range_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6530826404969316552) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 57861) != 0):
                self.state = 385
                localctx.beg = self.a_expr(0)


            self.state = 388
            _la = self._input.LA(1)
            if not(_la==40 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 389
                localctx.end = self.a_expr(0)


            localctx.res = (localctx.beg.res, localctx.end.res)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(ExprGrammar.MULT, 0)

        def STAR(self):
            return self.getToken(ExprGrammar.STAR, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_all_index

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_index" ):
                listener.enterAll_index(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_index" ):
                listener.exitAll_index(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_index" ):
                return visitor.visitAll_index(self)
            else:
                return visitor.visitChildren(self)




    def all_index(self):

        localctx = ExprGrammar.All_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_all_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            _la = self._input.LA(1)
            if not(_la==8 or _la==41):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_entryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.IndexOp.IndexEntry)
            self._a_expr = None # A_exprContext
            self._range_index = None # Range_indexContext

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def range_index(self):
            return self.getTypedRuleContext(ExprGrammar.Range_indexContext,0)


        def all_index(self):
            return self.getTypedRuleContext(ExprGrammar.All_indexContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_index_entry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_entry" ):
                listener.enterIndex_entry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_entry" ):
                listener.exitIndex_entry(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_entry" ):
                return visitor.visitIndex_entry(self)
            else:
                return visitor.visitChildren(self)




    def index_entry(self):

        localctx = ExprGrammar.Index_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_index_entry)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                localctx._a_expr = self.a_expr(0)
                localctx.res = localctx._a_expr.res
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                localctx._range_index = self.range_index()
                localctx.res = localctx._range_index.res
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 402
                self.all_index()
                localctx.res = None
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                localctx.res = None
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(tuple[Ast.IndexOp.IndexEntry, ...])
            self._atom = None # AtomContext
            self._cmd_func = None # Cmd_funcContext
            self._index_entry = None # Index_entryContext

        def atom(self):
            return self.getTypedRuleContext(ExprGrammar.AtomContext,0)


        def cmd_func(self):
            return self.getTypedRuleContext(ExprGrammar.Cmd_funcContext,0)


        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)

        def index_entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.Index_entryContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.Index_entryContext,i)


        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.LBRACKET)
            else:
                return self.getToken(ExprGrammar.LBRACKET, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.LPAREN)
            else:
                return self.getToken(ExprGrammar.LPAREN, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.COMMA)
            else:
                return self.getToken(ExprGrammar.COMMA, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.SEMICOLON)
            else:
                return self.getToken(ExprGrammar.SEMICOLON, i)

        def getRuleIndex(self):
            return ExprGrammar.RULE_index_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_arg" ):
                listener.enterIndex_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_arg" ):
                listener.exitIndex_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_arg" ):
                return visitor.visitIndex_arg(self)
            else:
                return visitor.visitChildren(self)




    def index_arg(self):

        localctx = ExprGrammar.Index_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_index_arg)
        self._la = 0 # Token type
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [73, 78, 79]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                localctx._atom = self.atom()
                localctx.res = (localctx._atom.res,)
                pass
            elif token in [20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                localctx._cmd_func = self.cmd_func()
                localctx.res = (localctx._cmd_func.res,)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.match(ExprGrammar.LBRACE)
                self.state = 416
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 415
                    _la = self._input.LA(1)
                    if not(_la==45 or _la==49):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 418
                localctx._index_entry = self.index_entry()
                localctx.res = [localctx._index_entry.res]
                self.state = 424 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 420
                    _la = self._input.LA(1)
                    if not(_la==37 or _la==39):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 421
                    localctx._index_entry = self.index_entry()
                    localctx.res.append(localctx._index_entry.res)
                    self.state = 426 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==37 or _la==39):
                        break

                self.state = 429
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45 or _la==49:
                    self.state = 428
                    _la = self._input.LA(1)
                    if not(_la==45 or _la==49):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 431
                self.match(ExprGrammar.RBRACE)
                localctx.res = tuple(localctx.res)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_boundsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.bounds = rule_t(tuple[Ast.AExpr, Ast.AExpr] | None)
            self.upper = None # Latex_cmd_argContext
            self.lower = None # Latex_cmd_argContext

        def POW(self):
            return self.getToken(ExprGrammar.POW, 0)

        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)

        def latex_cmd_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.Latex_cmd_argContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.Latex_cmd_argContext,i)


        def getRuleIndex(self):
            return ExprGrammar.RULE_int_bounds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_bounds" ):
                listener.enterInt_bounds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_bounds" ):
                listener.exitInt_bounds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_bounds" ):
                return visitor.visitInt_bounds(self)
            else:
                return visitor.visitChildren(self)




    def int_bounds(self):

        localctx = ExprGrammar.Int_boundsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_int_bounds)
        try:
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(ExprGrammar.POW)
                self.state = 437
                localctx.upper = self.latex_cmd_arg()
                self.state = 438
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 439
                localctx.lower = self.latex_cmd_arg()
                localctx.bounds = (localctx.lower.res, localctx.upper.res)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 443
                localctx.lower = self.latex_cmd_arg()
                self.state = 444
                self.match(ExprGrammar.POW)
                self.state = 445
                localctx.upper = self.latex_cmd_arg()
                localctx.bounds = (localctx.lower.res, localctx.upper.res)
                pass
            elif token in [3, 6, 7, 20, 21, 22, 23, 24, 26, 28, 29, 30, 32, 33, 43, 45, 49, 53, 55, 57, 59, 60, 62, 64, 66, 73, 77, 78, 79]:
                self.enterOuterAlt(localctx, 3)
                localctx.bounds = None
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Diff_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.deg = None
            self._a_expr = None # A_exprContext
            self._latex_cmd_arg = None # Latex_cmd_argContext

        def DIFFERENTIAL(self):
            return self.getToken(ExprGrammar.DIFFERENTIAL, 0)

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def POW(self):
            return self.getToken(ExprGrammar.POW, 0)

        def latex_cmd_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Latex_cmd_argContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_diff_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiff_var" ):
                listener.enterDiff_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiff_var" ):
                listener.exitDiff_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiff_var" ):
                return visitor.visitDiff_var(self)
            else:
                return visitor.visitChildren(self)




    def diff_var(self):

        localctx = ExprGrammar.Diff_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_diff_var)
        try:
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 452
                localctx._a_expr = self.a_expr(0)
                self.state = 453
                self.match(ExprGrammar.POW)
                self.state = 454
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.getInvokingContext(17).res.append((localctx._a_expr.res, localctx._latex_cmd_arg.res))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 458
                localctx._a_expr = self.a_expr(0)
                self.getInvokingContext(17).res.append((localctx._a_expr.res, None))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Diff_varsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(list[tuple[Ast.AExpr, Ast.AExpr | None]], [])

        def diff_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.Diff_varContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.Diff_varContext,i)


        def getRuleIndex(self):
            return ExprGrammar.RULE_diff_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiff_vars" ):
                listener.enterDiff_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiff_vars" ):
                listener.exitDiff_vars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiff_vars" ):
                return visitor.visitDiff_vars(self)
            else:
                return visitor.visitChildren(self)




    def diff_vars(self):

        localctx = ExprGrammar.Diff_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_diff_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 463
                self.diff_var()
                self.state = 466 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==27):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Limit_dirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.LimitDir)

        def POW(self):
            return self.getToken(ExprGrammar.POW, 0)

        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

        def PLUS(self):
            return self.getToken(ExprGrammar.PLUS, 0)

        def MINUS(self):
            return self.getToken(ExprGrammar.MINUS, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_limit_dir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimit_dir" ):
                listener.enterLimit_dir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimit_dir" ):
                listener.exitLimit_dir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimit_dir" ):
                return visitor.visitLimit_dir(self)
            else:
                return visitor.visitChildren(self)




    def limit_dir(self):

        localctx = ExprGrammar.Limit_dirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_limit_dir)
        self._la = 0 # Token type
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                localctx.res = Ast.LimitDir.BOTH
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 469
                self.match(ExprGrammar.POW)
                self.state = 470
                self.match(ExprGrammar.LBRACE)
                self.state = 471
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 472
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.LimitDir.BOTH
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 474
                self.match(ExprGrammar.POW)
                self.state = 475
                self.match(ExprGrammar.PLUS)
                localctx.res = Ast.LimitDir.POSITIVE
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 477
                self.match(ExprGrammar.POW)
                self.state = 478
                self.match(ExprGrammar.MINUS)
                localctx.res = Ast.LimitDir.NEGATIVE
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Series_range_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.symb = rule_t(Ast.AExpr)
            self.start = rule_t(Ast.AExpr)
            self.end = rule_t(Ast.AExpr)
            self.var = None # A_exprContext
            self.s = None # A_exprContext
            self.e = None # Pow_argContext

        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)

        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)

        def EQ(self):
            return self.getToken(ExprGrammar.EQ, 0)

        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

        def POW(self):
            return self.getToken(ExprGrammar.POW, 0)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)


        def pow_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Pow_argContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_series_range_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeries_range_args" ):
                listener.enterSeries_range_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeries_range_args" ):
                listener.exitSeries_range_args(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeries_range_args" ):
                return visitor.visitSeries_range_args(self)
            else:
                return visitor.visitChildren(self)




    def series_range_args(self):

        localctx = ExprGrammar.Series_range_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_series_range_args)
        try:
            self.state = 502
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 483
                self.match(ExprGrammar.LBRACE)
                self.state = 484
                localctx.var = self.a_expr(0)
                self.state = 485
                self.match(ExprGrammar.EQ)
                self.state = 486
                localctx.s = self.a_expr(0)
                self.state = 487
                self.match(ExprGrammar.RBRACE)
                self.state = 488
                self.match(ExprGrammar.POW)
                self.state = 489
                localctx.e = self.pow_arg()

                localctx.symb = localctx.var.res
                localctx.start = localctx.s.res
                localctx.end = localctx.e.res

                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
                self.match(ExprGrammar.POW)
                self.state = 493
                localctx.e = self.pow_arg()
                self.state = 494
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 495
                self.match(ExprGrammar.LBRACE)
                self.state = 496
                localctx.var = self.a_expr(0)
                self.state = 497
                self.match(ExprGrammar.EQ)
                self.state = 498
                localctx.s = self.a_expr(0)
                self.state = 499
                self.match(ExprGrammar.RBRACE)

                localctx.symb = localctx.var.res
                localctx.start = localctx.s.res
                localctx.end = localctx.e.res

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eval_at_sub_varsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(list[tuple[Ast.AExpr, Ast.AExpr], ...], [])
            self.var = None # A_exprContext
            self.sub = None # A_exprContext

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.EQ)
            else:
                return self.getToken(ExprGrammar.EQ, i)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.COMMA)
            else:
                return self.getToken(ExprGrammar.COMMA, i)

        def getRuleIndex(self):
            return ExprGrammar.RULE_eval_at_sub_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEval_at_sub_vars" ):
                listener.enterEval_at_sub_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEval_at_sub_vars" ):
                listener.exitEval_at_sub_vars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEval_at_sub_vars" ):
                return visitor.visitEval_at_sub_vars(self)
            else:
                return visitor.visitChildren(self)




    def eval_at_sub_vars(self):

        localctx = ExprGrammar.Eval_at_sub_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_eval_at_sub_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            localctx.var = self.a_expr(0)
            self.state = 505
            self.match(ExprGrammar.EQ)
            self.state = 506
            localctx.sub = self.a_expr(0)
            localctx.res.append((localctx.var.res, localctx.sub.res))
            self.state = 516
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 508
                self.match(ExprGrammar.COMMA)
                self.state = 509
                localctx.var = self.a_expr(0)
                self.state = 510
                self.match(ExprGrammar.EQ)
                self.state = 511
                localctx.sub = self.a_expr(0)
                localctx.res.append((localctx.var.res, localctx.sub.res))
                self.state = 518
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eval_at_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.subs_start = rule_t(tuple[tuple[Ast.AExpr, Ast.AExpr], ...])
            self.subs_end = rule_t(tuple[tuple[Ast.AExpr, Ast.AExpr], ...] | None)
            self._eval_at_sub_vars = None # Eval_at_sub_varsContext
            self.sstart = None # Eval_at_sub_varsContext
            self.send = None # Eval_at_sub_varsContext

        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.LBRACE)
            else:
                return self.getToken(ExprGrammar.LBRACE, i)

        def eval_at_sub_vars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.Eval_at_sub_varsContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.Eval_at_sub_varsContext,i)


        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.RBRACE)
            else:
                return self.getToken(ExprGrammar.RBRACE, i)

        def POW(self):
            return self.getToken(ExprGrammar.POW, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_eval_at_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEval_at_arg" ):
                listener.enterEval_at_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEval_at_arg" ):
                listener.exitEval_at_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEval_at_arg" ):
                return visitor.visitEval_at_arg(self)
            else:
                return visitor.visitChildren(self)




    def eval_at_arg(self):

        localctx = ExprGrammar.Eval_at_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_eval_at_arg)
        try:
            self.state = 545
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 520
                self.match(ExprGrammar.LBRACE)
                self.state = 521
                localctx._eval_at_sub_vars = self.eval_at_sub_vars()
                self.state = 522
                self.match(ExprGrammar.RBRACE)
                localctx.subs_start = tuple(localctx._eval_at_sub_vars.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 526
                self.match(ExprGrammar.LBRACE)
                self.state = 527
                localctx.sstart = self.eval_at_sub_vars()
                self.state = 528
                self.match(ExprGrammar.RBRACE)
                self.state = 529
                self.match(ExprGrammar.POW)
                self.state = 530
                self.match(ExprGrammar.LBRACE)
                self.state = 531
                localctx.send = self.eval_at_sub_vars()
                self.state = 532
                self.match(ExprGrammar.RBRACE)

                localctx.subs_start = tuple(localctx.sstart.res)
                localctx.subs_end=tuple(localctx.send.res)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 535
                self.match(ExprGrammar.POW)
                self.state = 536
                self.match(ExprGrammar.LBRACE)
                self.state = 537
                localctx.send = self.eval_at_sub_vars()
                self.state = 538
                self.match(ExprGrammar.RBRACE)
                self.state = 539
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 540
                self.match(ExprGrammar.LBRACE)
                self.state = 541
                localctx.sstart = self.eval_at_sub_vars()
                self.state = 542
                self.match(ExprGrammar.RBRACE)

                localctx.subs_start = tuple(localctx.sstart.res)
                localctx.subs_end=tuple(localctx.send.res)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AExpr)
            self._ID = None # Token
            self._COMMAND = None # Token

        def ID(self):
            return self.getToken(ExprGrammar.ID, 0)

        def COMMAND(self):
            return self.getToken(ExprGrammar.COMMAND, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_primary_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_symbol" ):
                listener.enterPrimary_symbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_symbol" ):
                listener.exitPrimary_symbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_symbol" ):
                return visitor.visitPrimary_symbol(self)
            else:
                return visitor.visitChildren(self)




    def primary_symbol(self):

        localctx = ExprGrammar.Primary_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primary_symbol)
        try:
            self.state = 551
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [78]:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                localctx._ID = self.match(ExprGrammar.ID)
                localctx.res = Ast.Symbol(localctx, (None if localctx._ID is None else localctx._ID.text))
                pass
            elif token in [79]:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
                localctx._COMMAND = self.match(ExprGrammar.COMMAND)
                localctx.res = Ast.Symbol(localctx, (None if localctx._COMMAND is None else localctx._COMMAND.text))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Delta_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AExpr)
            self._DELTA = None # Token
            self._primary_symbol = None # Primary_symbolContext

        def DELTA(self):
            return self.getToken(ExprGrammar.DELTA, 0)

        def primary_symbol(self):
            return self.getTypedRuleContext(ExprGrammar.Primary_symbolContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_delta_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelta_symbol" ):
                listener.enterDelta_symbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelta_symbol" ):
                listener.exitDelta_symbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelta_symbol" ):
                return visitor.visitDelta_symbol(self)
            else:
                return visitor.visitChildren(self)




    def delta_symbol(self):

        localctx = ExprGrammar.Delta_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_delta_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            localctx._DELTA = self.match(ExprGrammar.DELTA)
            self.state = 554
            localctx._primary_symbol = self.primary_symbol()
            localctx.res = Ast.Symbol(localctx, f"{(None if localctx._DELTA is None else localctx._DELTA.text)} {localctx._primary_symbol.res.symbol}")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AExpr)
            self._primary_symbol = None # Primary_symbolContext
            self._delta_symbol = None # Delta_symbolContext

        def primary_symbol(self):
            return self.getTypedRuleContext(ExprGrammar.Primary_symbolContext,0)


        def delta_symbol(self):
            return self.getTypedRuleContext(ExprGrammar.Delta_symbolContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbol" ):
                listener.enterSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbol" ):
                listener.exitSymbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbol" ):
                return visitor.visitSymbol(self)
            else:
                return visitor.visitChildren(self)




    def symbol(self):

        localctx = ExprGrammar.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_symbol)
        try:
            self.state = 563
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [78, 79]:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                localctx._primary_symbol = self.primary_symbol()
                localctx.res = localctx._primary_symbol.res
                pass
            elif token in [77]:
                self.enterOuterAlt(localctx, 2)
                self.state = 560
                localctx._delta_symbol = self.delta_symbol()
                localctx.res = localctx._delta_symbol.res
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.ApplyFunc)
            self.args = rule_t(list[Ast.AExpr], [])
            self.func = None # Token
            self._a_expr = None # A_exprContext
            self._FUNC_CMD = None # Token

        def LPAREN(self):
            return self.getToken(ExprGrammar.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExprGrammar.RPAREN, 0)

        def FUNC_ID(self):
            return self.getToken(ExprGrammar.FUNC_ID, 0)

        def FUNC_CMD(self):
            return self.getToken(ExprGrammar.FUNC_CMD, 0)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.COMMA)
            else:
                return self.getToken(ExprGrammar.COMMA, i)

        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ExprGrammar.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.state = 595
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 567
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 565
                    localctx.func = self.match(ExprGrammar.FUNC_ID)
                    pass
                elif token in [2]:
                    self.state = 566
                    localctx.func = self.match(ExprGrammar.FUNC_CMD)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 569
                self.match(ExprGrammar.LPAREN)
                self.state = 581
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6530826404969316552) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 57861) != 0):
                    self.state = 570
                    localctx._a_expr = self.a_expr(0)
                    localctx.args.append(localctx._a_expr.res)
                    self.state = 578
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==37:
                        self.state = 572
                        self.match(ExprGrammar.COMMA)
                        self.state = 573
                        localctx._a_expr = self.a_expr(0)
                        localctx.args.append(localctx._a_expr.res)
                        self.state = 580
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 583
                self.match(ExprGrammar.RPAREN)
                localctx.res = Ast.ApplyFunc(Ast.Function((None if localctx.func is None else localctx.func.text), tuple(localctx.args)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 585
                localctx._FUNC_CMD = self.match(ExprGrammar.FUNC_CMD)
                self.state = 586
                self.match(ExprGrammar.LBRACE)
                self.state = 587
                localctx._a_expr = self.a_expr(0)
                self.state = 588
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.ApplyFunc(Ast.Function((None if localctx._FUNC_CMD is None else localctx._FUNC_CMD.text), (localctx._a_expr.res,)))
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 591
                localctx._FUNC_CMD = self.match(ExprGrammar.FUNC_CMD)
                self.state = 592
                localctx._a_expr = self.a_expr(0)
                localctx.res = Ast.ApplyFunc(Ast.Function((None if localctx._FUNC_CMD is None else localctx._FUNC_CMD.text), (localctx._a_expr.res,)))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Delim_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AExpr)
            self._a_expr = None # A_exprContext
            self.lhs = None # A_exprContext
            self.rhs = None # A_exprContext

        def LPAREN(self):
            return self.getToken(ExprGrammar.LPAREN, 0)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)


        def RPAREN(self):
            return self.getToken(ExprGrammar.RPAREN, 0)

        def LBRACKET(self):
            return self.getToken(ExprGrammar.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(ExprGrammar.RBRACKET, 0)

        def BAR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.BAR)
            else:
                return self.getToken(ExprGrammar.BAR, i)

        def DOUBLE_BAR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.DOUBLE_BAR)
            else:
                return self.getToken(ExprGrammar.DOUBLE_BAR, i)

        def LFLOOR(self):
            return self.getToken(ExprGrammar.LFLOOR, 0)

        def RFLOOR(self):
            return self.getToken(ExprGrammar.RFLOOR, 0)

        def LCEIL(self):
            return self.getToken(ExprGrammar.LCEIL, 0)

        def RCEIL(self):
            return self.getToken(ExprGrammar.RCEIL, 0)

        def LANGLE(self):
            return self.getToken(ExprGrammar.LANGLE, 0)

        def RANGLE(self):
            return self.getToken(ExprGrammar.RANGLE, 0)

        def COMMA(self):
            return self.getToken(ExprGrammar.COMMA, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_delim_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelim_expr" ):
                listener.enterDelim_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelim_expr" ):
                listener.exitDelim_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelim_expr" ):
                return visitor.visitDelim_expr(self)
            else:
                return visitor.visitChildren(self)




    def delim_expr(self):

        localctx = ExprGrammar.Delim_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_delim_expr)
        self._la = 0 # Token type
        try:
            self.state = 634
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 597
                self.match(ExprGrammar.LPAREN)
                self.state = 598
                localctx._a_expr = self.a_expr(0)
                self.state = 599
                self.match(ExprGrammar.RPAREN)
                localctx.res = localctx._a_expr.res.mut_ctx(localctx)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 602
                self.match(ExprGrammar.LBRACKET)
                self.state = 603
                localctx._a_expr = self.a_expr(0)
                self.state = 604
                self.match(ExprGrammar.RBRACKET)
                localctx.res = localctx._a_expr.res.mut_ctx(localctx)
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 3)
                self.state = 607
                self.match(ExprGrammar.BAR)
                self.state = 608
                localctx._a_expr = self.a_expr(0)
                self.state = 609
                self.match(ExprGrammar.BAR)
                localctx.res = Ast.Abs(localctx, localctx._a_expr.res)
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 4)
                self.state = 612
                self.match(ExprGrammar.DOUBLE_BAR)
                self.state = 613
                localctx._a_expr = self.a_expr(0)
                self.state = 614
                self.match(ExprGrammar.DOUBLE_BAR)
                localctx.res = Ast.Norm(localctx, localctx._a_expr.res)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 5)
                self.state = 617
                self.match(ExprGrammar.LFLOOR)
                self.state = 618
                localctx._a_expr = self.a_expr(0)
                self.state = 619
                self.match(ExprGrammar.RFLOOR)
                localctx.res = Ast.Floor(localctx, localctx._a_expr.res)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 6)
                self.state = 622
                self.match(ExprGrammar.LCEIL)
                self.state = 623
                localctx._a_expr = self.a_expr(0)
                self.state = 624
                self.match(ExprGrammar.RCEIL)
                localctx.res = Ast.Ceil(localctx, localctx._a_expr.res)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 7)
                self.state = 627
                self.match(ExprGrammar.LANGLE)
                self.state = 628
                localctx.lhs = self.a_expr(0)
                self.state = 629
                _la = self._input.LA(1)
                if not(_la==37 or _la==59):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 630
                localctx.rhs = self.a_expr(0)
                self.state = 631
                self.match(ExprGrammar.RANGLE)
                localctx.res = Ast.DotProd(localctx, localctx.lhs.res, localctx.rhs.res)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CombinatorialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AExpr)
            self.n = None # A_exprContext
            self.op = None # Token
            self.k = None # A_exprContext
            self._ID = None # Token

        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)

        def POW(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.POW)
            else:
                return self.getToken(ExprGrammar.POW, i)

        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)


        def ID(self):
            return self.getToken(ExprGrammar.ID, 0)

        def BANG(self):
            return self.getToken(ExprGrammar.BANG, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_combinatorial

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCombinatorial" ):
                listener.enterCombinatorial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCombinatorial" ):
                listener.exitCombinatorial(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCombinatorial" ):
                return visitor.visitCombinatorial(self)
            else:
                return visitor.visitChildren(self)




    def combinatorial(self):

        localctx = ExprGrammar.CombinatorialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_combinatorial)
        self._la = 0 # Token type
        try:
            self.state = 660
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 636
                self.match(ExprGrammar.LBRACE)
                self.state = 637
                _la = self._input.LA(1)
                if not(_la==11 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 638
                localctx.n = self.a_expr(0)
                self.state = 639
                localctx.op = self.match(ExprGrammar.ID)
                self.state = 640
                if not ((None if localctx.op is None else localctx.op.text) in Ast.CombOpId):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "($op.text in Ast.CombOpId)")
                self.state = 641
                self.match(ExprGrammar.POW)
                self.state = 642
                localctx.k = self.a_expr(0)
                self.state = 643
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.combOpFromId(localctx, localctx.n.res, localctx.k.res, Ast.CombOpId((None if localctx.op is None else localctx.op.text)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 646
                self.match(ExprGrammar.LBRACE)
                self.state = 647
                localctx._ID = self.match(ExprGrammar.ID)
                self.state = 648
                if not (None if localctx._ID is None else localctx._ID.text) == 'D':
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$ID.text == 'D'")
                self.state = 649
                self.match(ExprGrammar.POW)
                self.state = 650
                localctx.n = self.a_expr(0)
                self.state = 651
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Derangements(localctx, localctx.n.res)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 654
                self.match(ExprGrammar.LBRACE)
                self.state = 655
                self.match(ExprGrammar.BANG)
                self.state = 656
                localctx.n = self.a_expr(0)
                self.state = 657
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Derangements(localctx, localctx.n.res)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AExpr)
            self.num = None # Latex_cmd_argContext
            self.den = None # Latex_cmd_argContext
            self.n = None # Latex_cmd_argContext
            self.k = None # Latex_cmd_argContext
            self._latex_cmd_arg = None # Latex_cmd_argContext
            self.root_index = None # A_exprContext

        def FRAC(self):
            return self.getToken(ExprGrammar.FRAC, 0)

        def latex_cmd_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.Latex_cmd_argContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.Latex_cmd_argContext,i)


        def BINOM(self):
            return self.getToken(ExprGrammar.BINOM, 0)

        def SQRT(self):
            return self.getToken(ExprGrammar.SQRT, 0)

        def LBRACKET(self):
            return self.getToken(ExprGrammar.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(ExprGrammar.RBRACKET, 0)

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def CONJUGATE(self):
            return self.getToken(ExprGrammar.CONJUGATE, 0)

        def VEC_UNIT(self):
            return self.getToken(ExprGrammar.VEC_UNIT, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_cmd_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd_func" ):
                listener.enterCmd_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd_func" ):
                listener.exitCmd_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd_func" ):
                return visitor.visitCmd_func(self)
            else:
                return visitor.visitChildren(self)




    def cmd_func(self):

        localctx = ExprGrammar.Cmd_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_cmd_func)
        self._la = 0 # Token type
        try:
            self.state = 694
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 662
                self.match(ExprGrammar.FRAC)
                self.state = 663
                localctx.num = self.latex_cmd_arg()
                self.state = 664
                localctx.den = self.latex_cmd_arg()
                localctx.res = Ast.DivOp(localctx, localctx.num.res, localctx.den.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 667
                self.match(ExprGrammar.BINOM)
                self.state = 668
                localctx.n = self.latex_cmd_arg()
                self.state = 669
                localctx.k = self.latex_cmd_arg()
                localctx.res = Ast.Binom(localctx, localctx.n.res, localctx.k.res)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 672
                self.match(ExprGrammar.SQRT)
                self.state = 673
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Root(localctx, localctx._latex_cmd_arg.res, None) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 676
                self.match(ExprGrammar.SQRT)
                self.state = 681
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 677
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 678
                    localctx.root_index = self.a_expr(0)
                    self.state = 679
                    self.match(ExprGrammar.RBRACKET)


                self.state = 683
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Root(localctx, localctx._latex_cmd_arg.res, localctx.root_index.res)
                        
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 686
                self.match(ExprGrammar.CONJUGATE)
                self.state = 687
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Conjugate(localctx, localctx._latex_cmd_arg.res)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 690
                self.match(ExprGrammar.VEC_UNIT)
                self.state = 691
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.VecUnit(localctx, localctx._latex_cmd_arg.res)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_rowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(list[Ast.AExpr])
            self._a_expr = None # A_exprContext

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)


        def ENV_EL_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.ENV_EL_SEP)
            else:
                return self.getToken(ExprGrammar.ENV_EL_SEP, i)

        def getRuleIndex(self):
            return ExprGrammar.RULE_matrix_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix_row" ):
                listener.enterMatrix_row(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix_row" ):
                listener.exitMatrix_row(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix_row" ):
                return visitor.visitMatrix_row(self)
            else:
                return visitor.visitChildren(self)




    def matrix_row(self):

        localctx = ExprGrammar.Matrix_rowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_matrix_row)
        self._la = 0 # Token type
        try:
            self.state = 708
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63, 65, 67, 71]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [3, 6, 7, 20, 21, 22, 23, 24, 26, 28, 29, 30, 32, 33, 43, 45, 49, 53, 55, 57, 59, 60, 62, 64, 66, 73, 77, 78, 79]:
                self.enterOuterAlt(localctx, 2)
                self.state = 697
                localctx._a_expr = self.a_expr(0)
                localctx.res = [localctx._a_expr.res]
                self.state = 705
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==70:
                    self.state = 699
                    self.match(ExprGrammar.ENV_EL_SEP)
                    self.state = 700
                    localctx._a_expr = self.a_expr(0)
                    localctx.res.append(localctx._a_expr.res)
                    self.state = 707
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(list[list[Ast.AExpr]], [])
            self._matrix_row = None # Matrix_rowContext

        def matrix_row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.Matrix_rowContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.Matrix_rowContext,i)


        def ENV_ROW_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.ENV_ROW_SEP)
            else:
                return self.getToken(ExprGrammar.ENV_ROW_SEP, i)

        def getRuleIndex(self):
            return ExprGrammar.RULE_matrix_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix_body" ):
                listener.enterMatrix_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix_body" ):
                listener.exitMatrix_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix_body" ):
                return visitor.visitMatrix_body(self)
            else:
                return visitor.visitChildren(self)




    def matrix_body(self):

        localctx = ExprGrammar.Matrix_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_matrix_body)
        self._la = 0 # Token type
        try:
            self.state = 728
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 711
                localctx._matrix_row = self.matrix_row()
                localctx.res = [localctx._matrix_row.res]
                self.state = 719
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 713
                        self.match(ExprGrammar.ENV_ROW_SEP)
                        self.state = 714
                        localctx._matrix_row = self.matrix_row()
                        localctx.res.append(localctx._matrix_row.res) 
                    self.state = 721
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

                self.state = 725
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==71:
                    self.state = 722
                    self.match(ExprGrammar.ENV_ROW_SEP)
                    self.state = 727
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.Matrix)
            self.beg = None # Token
            self._matrix_body = None # Matrix_bodyContext
            self.end = None # Token

        def matrix_body(self):
            return self.getTypedRuleContext(ExprGrammar.Matrix_bodyContext,0)


        def BEGIN_MATRIX(self):
            return self.getToken(ExprGrammar.BEGIN_MATRIX, 0)

        def END_MATRIX(self):
            return self.getToken(ExprGrammar.END_MATRIX, 0)

        def BEGIN_ARRAY(self):
            return self.getToken(ExprGrammar.BEGIN_ARRAY, 0)

        def END_ARRAY(self):
            return self.getToken(ExprGrammar.END_ARRAY, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_matrix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix" ):
                listener.enterMatrix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix" ):
                listener.exitMatrix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix" ):
                return visitor.visitMatrix(self)
            else:
                return visitor.visitChildren(self)




    def matrix(self):

        localctx = ExprGrammar.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 738
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
                self.state = 730
                localctx.beg = self.match(ExprGrammar.BEGIN_MATRIX)
                self.state = 731
                localctx._matrix_body = self.matrix_body()
                self.state = 732
                localctx.end = self.match(ExprGrammar.END_MATRIX)
                pass
            elif token in [66]:
                self.state = 734
                localctx.beg = self.match(ExprGrammar.BEGIN_ARRAY)
                self.state = 735
                localctx._matrix_body = self.matrix_body()
                self.state = 736
                localctx.end = self.match(ExprGrammar.END_ARRAY)
                pass
            else:
                raise NoViableAltException(self)

            localctx.res = Ast.Matrix(localctx, localctx._matrix_body.res, (None if localctx.beg is None else localctx.beg.text), (None if localctx.end is None else localctx.end.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Det_matrixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AExpr)
            self._matrix_body = None # Matrix_bodyContext

        def BEGIN_V_MATRIX(self):
            return self.getToken(ExprGrammar.BEGIN_V_MATRIX, 0)

        def matrix_body(self):
            return self.getTypedRuleContext(ExprGrammar.Matrix_bodyContext,0)


        def END_V_MATRIX(self):
            return self.getToken(ExprGrammar.END_V_MATRIX, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_det_matrix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDet_matrix" ):
                listener.enterDet_matrix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDet_matrix" ):
                listener.exitDet_matrix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDet_matrix" ):
                return visitor.visitDet_matrix(self)
            else:
                return visitor.visitChildren(self)




    def det_matrix(self):

        localctx = ExprGrammar.Det_matrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_det_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 742
            self.match(ExprGrammar.BEGIN_V_MATRIX)
            self.state = 743
            localctx._matrix_body = self.matrix_body()
            self.state = 744
            self.match(ExprGrammar.END_V_MATRIX)
            localctx.res = Ast.DetMatrix(localctx, localctx._matrix_body.res)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.a_expr_sempred
        self._predicates[27] = self.combinatorial_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def a_expr_sempred(self, localctx:A_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return ((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS))
         

            if predIndex == 3:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 8)
         

    def combinatorial_sempred(self, localctx:CombinatorialContext, predIndex:int):
            if predIndex == 9:
                return ((None if localctx.op is None else localctx.op.text) in Ast.CombOpId)
         

            if predIndex == 10:
                return (None if localctx._ID is None else localctx._ID.text) == 'D'
         





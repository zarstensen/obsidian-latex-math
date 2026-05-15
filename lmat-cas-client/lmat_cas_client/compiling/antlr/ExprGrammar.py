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

def rule_t[T](t: Type[T], v: T | None = None) -> T:
	return cast(T, v)

def serializedATN():
    return [
        4,1,81,711,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,3,1,73,8,1,1,1,1,1,1,2,1,2,3,2,79,8,2,1,3,1,3,
        1,3,5,3,84,8,3,10,3,12,3,87,9,3,1,3,5,3,90,8,3,10,3,12,3,93,9,3,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,107,8,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,132,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,148,8,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,161,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,3,6,174,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,190,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,5,6,204,8,6,10,6,12,6,207,9,6,3,6,209,8,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,3,6,234,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,3,6,246,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,256,8,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,3,6,295,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,3,6,310,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,3,6,325,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,3,6,354,8,6,1,6,1,6,1,6,1,6,5,6,360,8,6,10,6,12,6,363,
        9,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,372,8,8,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,3,9,382,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,3,10,395,8,10,1,11,3,11,398,8,11,1,11,1,11,3,11,402,
        8,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,3,13,418,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        3,14,428,8,14,1,14,1,14,1,14,1,14,1,14,1,14,4,14,436,8,14,11,14,
        12,14,437,1,14,3,14,441,8,14,1,14,1,14,1,14,3,14,446,8,14,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,461,
        8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,473,
        8,16,1,17,4,17,476,8,17,11,17,12,17,477,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,492,8,18,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,3,19,514,8,19,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,5,20,524,8,20,10,20,12,20,527,9,20,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,3,21,552,8,21,1,22,1,22,1,22,1,22,
        3,22,558,8,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,
        3,24,570,8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,3,25,599,8,25,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,3,26,625,8,26,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,3,27,646,8,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,3,27,659,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,5,28,
        668,8,28,10,28,12,28,671,9,28,3,28,673,8,28,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,5,29,682,8,29,10,29,12,29,685,9,29,1,29,5,29,688,
        8,29,10,29,12,29,691,9,29,3,29,693,8,29,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,3,30,703,8,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,
        0,1,12,32,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,0,9,1,0,28,29,1,0,12,17,2,0,
        40,40,42,42,2,0,8,8,41,41,2,0,45,45,49,49,2,0,37,37,39,39,1,0,6,
        7,2,0,37,37,59,59,2,0,11,11,38,38,779,0,64,1,0,0,0,2,72,1,0,0,0,
        4,78,1,0,0,0,6,80,1,0,0,0,8,94,1,0,0,0,10,106,1,0,0,0,12,294,1,0,
        0,0,14,364,1,0,0,0,16,371,1,0,0,0,18,381,1,0,0,0,20,394,1,0,0,0,
        22,397,1,0,0,0,24,405,1,0,0,0,26,417,1,0,0,0,28,445,1,0,0,0,30,460,
        1,0,0,0,32,472,1,0,0,0,34,475,1,0,0,0,36,491,1,0,0,0,38,513,1,0,
        0,0,40,515,1,0,0,0,42,551,1,0,0,0,44,557,1,0,0,0,46,559,1,0,0,0,
        48,569,1,0,0,0,50,598,1,0,0,0,52,624,1,0,0,0,54,658,1,0,0,0,56,672,
        1,0,0,0,58,692,1,0,0,0,60,702,1,0,0,0,62,706,1,0,0,0,64,65,3,2,1,
        0,65,66,6,0,-1,0,66,1,1,0,0,0,67,68,3,12,6,0,68,69,6,1,-1,0,69,73,
        1,0,0,0,70,73,3,10,5,0,71,73,3,8,4,0,72,67,1,0,0,0,72,70,1,0,0,0,
        72,71,1,0,0,0,73,74,1,0,0,0,74,75,5,0,0,1,75,3,1,0,0,0,76,79,3,12,
        6,0,77,79,3,10,5,0,78,76,1,0,0,0,78,77,1,0,0,0,79,5,1,0,0,0,80,85,
        3,4,2,0,81,82,5,71,0,0,82,84,3,4,2,0,83,81,1,0,0,0,84,87,1,0,0,0,
        85,83,1,0,0,0,85,86,1,0,0,0,86,91,1,0,0,0,87,85,1,0,0,0,88,90,5,
        71,0,0,89,88,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,
        7,1,0,0,0,93,91,1,0,0,0,94,95,5,68,0,0,95,96,3,6,3,0,96,97,5,69,
        0,0,97,9,1,0,0,0,98,99,3,12,6,0,99,100,3,14,7,0,100,101,3,10,5,0,
        101,107,1,0,0,0,102,103,3,12,6,0,103,104,3,14,7,0,104,105,3,12,6,
        0,105,107,1,0,0,0,106,98,1,0,0,0,106,102,1,0,0,0,107,11,1,0,0,0,
        108,109,6,6,-1,0,109,110,5,26,0,0,110,111,3,30,15,0,111,112,5,20,
        0,0,112,113,5,43,0,0,113,114,5,27,0,0,114,115,3,12,6,0,115,116,5,
        44,0,0,116,117,3,18,9,0,117,118,6,6,-1,0,118,295,1,0,0,0,119,120,
        5,26,0,0,120,121,3,30,15,0,121,122,3,12,6,0,122,123,5,27,0,0,123,
        124,3,12,6,28,124,125,6,6,-1,0,125,295,1,0,0,0,126,131,5,29,0,0,
        127,128,5,49,0,0,128,129,3,12,6,0,129,130,5,50,0,0,130,132,1,0,0,
        0,131,127,1,0,0,0,131,132,1,0,0,0,132,133,1,0,0,0,133,134,3,18,9,
        0,134,135,5,43,0,0,135,136,3,12,6,0,136,137,5,44,0,0,137,138,5,43,
        0,0,138,139,3,12,6,0,139,140,5,44,0,0,140,141,6,6,-1,0,141,295,1,
        0,0,0,142,147,7,0,0,0,143,144,5,49,0,0,144,145,3,12,6,0,145,146,
        5,50,0,0,146,148,1,0,0,0,147,143,1,0,0,0,147,148,1,0,0,0,148,149,
        1,0,0,0,149,150,3,18,9,0,150,151,5,43,0,0,151,152,3,12,6,0,152,153,
        5,44,0,0,153,154,6,6,-1,0,154,295,1,0,0,0,155,160,7,0,0,0,156,157,
        5,49,0,0,157,158,3,12,6,0,158,159,5,50,0,0,159,161,1,0,0,0,160,156,
        1,0,0,0,160,161,1,0,0,0,161,162,1,0,0,0,162,163,3,18,9,0,163,164,
        3,12,6,24,164,165,6,6,-1,0,165,295,1,0,0,0,166,167,5,20,0,0,167,
        168,5,43,0,0,168,173,5,27,0,0,169,170,5,49,0,0,170,171,3,12,6,0,
        171,172,5,50,0,0,172,174,1,0,0,0,173,169,1,0,0,0,173,174,1,0,0,0,
        174,175,1,0,0,0,175,176,3,12,6,0,176,177,5,44,0,0,177,178,5,43,0,
        0,178,179,3,34,17,0,179,180,5,44,0,0,180,181,6,6,-1,0,181,295,1,
        0,0,0,182,183,5,20,0,0,183,184,5,43,0,0,184,189,5,27,0,0,185,186,
        5,49,0,0,186,187,3,12,6,0,187,188,5,50,0,0,188,190,1,0,0,0,189,185,
        1,0,0,0,189,190,1,0,0,0,190,191,1,0,0,0,191,192,5,44,0,0,192,193,
        5,43,0,0,193,194,3,34,17,0,194,195,5,44,0,0,195,196,3,12,6,22,196,
        197,6,6,-1,0,197,295,1,0,0,0,198,199,5,1,0,0,199,208,5,45,0,0,200,
        205,3,12,6,0,201,202,5,37,0,0,202,204,3,12,6,0,203,201,1,0,0,0,204,
        207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,209,1,0,0,0,207,
        205,1,0,0,0,208,200,1,0,0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,
        295,5,46,0,0,211,212,5,1,0,0,212,213,5,43,0,0,213,214,3,12,6,0,214,
        215,5,44,0,0,215,295,1,0,0,0,216,217,5,1,0,0,217,295,3,12,6,19,218,
        219,5,30,0,0,219,220,5,38,0,0,220,221,5,43,0,0,221,222,3,48,24,0,
        222,223,5,31,0,0,223,224,3,12,6,0,224,225,3,36,18,0,225,226,5,44,
        0,0,226,227,3,12,6,18,227,228,6,6,-1,0,228,295,1,0,0,0,229,230,5,
        32,0,0,230,234,6,6,-1,0,231,232,5,33,0,0,232,234,6,6,-1,0,233,229,
        1,0,0,0,233,231,1,0,0,0,234,235,1,0,0,0,235,236,3,38,19,0,236,237,
        5,45,0,0,237,238,3,12,6,0,238,239,5,46,0,0,239,240,6,6,-1,0,240,
        295,1,0,0,0,241,242,5,32,0,0,242,246,6,6,-1,0,243,244,5,33,0,0,244,
        246,6,6,-1,0,245,241,1,0,0,0,245,243,1,0,0,0,246,247,1,0,0,0,247,
        248,3,38,19,0,248,249,3,12,6,14,249,250,6,6,-1,0,250,295,1,0,0,0,
        251,252,5,6,0,0,252,256,6,6,-1,0,253,254,5,7,0,0,254,256,6,6,-1,
        0,255,251,1,0,0,0,255,253,1,0,0,0,256,257,1,0,0,0,257,258,3,12,6,
        12,258,259,6,6,-1,0,259,295,1,0,0,0,260,261,5,45,0,0,261,262,3,12,
        6,0,262,263,5,46,0,0,263,264,5,59,0,0,264,265,3,42,21,0,265,295,
        1,0,0,0,266,267,5,3,0,0,267,268,3,12,6,0,268,269,5,59,0,0,269,270,
        3,42,21,0,270,295,1,0,0,0,271,272,5,49,0,0,272,273,3,12,6,0,273,
        274,5,50,0,0,274,275,3,42,21,0,275,295,1,0,0,0,276,277,3,52,26,0,
        277,278,6,6,-1,0,278,295,1,0,0,0,279,280,3,50,25,0,280,281,6,6,-1,
        0,281,295,1,0,0,0,282,283,3,54,27,0,283,284,6,6,-1,0,284,295,1,0,
        0,0,285,286,3,60,30,0,286,287,6,6,-1,0,287,295,1,0,0,0,288,295,3,
        62,31,0,289,290,3,48,24,0,290,291,6,6,-1,0,291,295,1,0,0,0,292,293,
        5,73,0,0,293,295,6,6,-1,0,294,108,1,0,0,0,294,119,1,0,0,0,294,126,
        1,0,0,0,294,142,1,0,0,0,294,155,1,0,0,0,294,166,1,0,0,0,294,182,
        1,0,0,0,294,198,1,0,0,0,294,211,1,0,0,0,294,216,1,0,0,0,294,218,
        1,0,0,0,294,233,1,0,0,0,294,245,1,0,0,0,294,255,1,0,0,0,294,260,
        1,0,0,0,294,266,1,0,0,0,294,271,1,0,0,0,294,276,1,0,0,0,294,279,
        1,0,0,0,294,282,1,0,0,0,294,285,1,0,0,0,294,288,1,0,0,0,294,289,
        1,0,0,0,294,292,1,0,0,0,295,361,1,0,0,0,296,309,10,17,0,0,297,298,
        5,8,0,0,298,310,6,6,-1,0,299,300,5,18,0,0,300,310,6,6,-1,0,301,302,
        5,10,0,0,302,310,6,6,-1,0,303,304,5,19,0,0,304,310,6,6,-1,0,305,
        306,5,9,0,0,306,310,6,6,-1,0,307,308,5,25,0,0,308,310,6,6,-1,0,309,
        297,1,0,0,0,309,299,1,0,0,0,309,301,1,0,0,0,309,303,1,0,0,0,309,
        305,1,0,0,0,309,307,1,0,0,0,310,311,1,0,0,0,311,312,3,12,6,18,312,
        313,6,6,-1,0,313,360,1,0,0,0,314,315,10,16,0,0,315,316,4,6,2,0,316,
        317,3,12,6,17,317,318,6,6,-1,0,318,360,1,0,0,0,319,324,10,13,0,0,
        320,321,5,6,0,0,321,325,6,6,-1,0,322,323,5,7,0,0,323,325,6,6,-1,
        0,324,320,1,0,0,0,324,322,1,0,0,0,325,326,1,0,0,0,326,327,3,12,6,
        14,327,328,6,6,-1,0,328,360,1,0,0,0,329,330,10,32,0,0,330,331,5,
        11,0,0,331,332,3,20,10,0,332,333,5,38,0,0,333,334,3,28,14,0,334,
        335,6,6,-1,0,335,360,1,0,0,0,336,337,10,31,0,0,337,338,5,11,0,0,
        338,339,3,20,10,0,339,340,6,6,-1,0,340,360,1,0,0,0,341,342,10,30,
        0,0,342,343,5,38,0,0,343,344,3,28,14,0,344,345,6,6,-1,0,345,360,
        1,0,0,0,346,353,10,27,0,0,347,348,5,34,0,0,348,354,6,6,-1,0,349,
        350,5,35,0,0,350,354,6,6,-1,0,351,352,5,36,0,0,352,354,6,6,-1,0,
        353,347,1,0,0,0,353,349,1,0,0,0,353,351,1,0,0,0,354,355,1,0,0,0,
        355,360,6,6,-1,0,356,357,10,8,0,0,357,358,5,59,0,0,358,360,3,42,
        21,0,359,296,1,0,0,0,359,314,1,0,0,0,359,319,1,0,0,0,359,329,1,0,
        0,0,359,336,1,0,0,0,359,341,1,0,0,0,359,346,1,0,0,0,359,356,1,0,
        0,0,360,363,1,0,0,0,361,359,1,0,0,0,361,362,1,0,0,0,362,13,1,0,0,
        0,363,361,1,0,0,0,364,365,7,1,0,0,365,15,1,0,0,0,366,367,3,44,22,
        0,367,368,6,8,-1,0,368,372,1,0,0,0,369,370,5,73,0,0,370,372,6,8,
        -1,0,371,366,1,0,0,0,371,369,1,0,0,0,372,17,1,0,0,0,373,374,3,16,
        8,0,374,375,6,9,-1,0,375,382,1,0,0,0,376,377,5,43,0,0,377,378,3,
        12,6,0,378,379,5,44,0,0,379,380,6,9,-1,0,380,382,1,0,0,0,381,373,
        1,0,0,0,381,376,1,0,0,0,382,19,1,0,0,0,383,384,3,16,8,0,384,385,
        6,10,-1,0,385,395,1,0,0,0,386,387,3,54,27,0,387,388,6,10,-1,0,388,
        395,1,0,0,0,389,390,5,43,0,0,390,391,3,12,6,0,391,392,5,44,0,0,392,
        393,6,10,-1,0,393,395,1,0,0,0,394,383,1,0,0,0,394,386,1,0,0,0,394,
        389,1,0,0,0,395,21,1,0,0,0,396,398,3,12,6,0,397,396,1,0,0,0,397,
        398,1,0,0,0,398,399,1,0,0,0,399,401,7,2,0,0,400,402,3,12,6,0,401,
        400,1,0,0,0,401,402,1,0,0,0,402,403,1,0,0,0,403,404,6,11,-1,0,404,
        23,1,0,0,0,405,406,7,3,0,0,406,25,1,0,0,0,407,408,3,12,6,0,408,409,
        6,13,-1,0,409,418,1,0,0,0,410,411,3,22,11,0,411,412,6,13,-1,0,412,
        418,1,0,0,0,413,414,3,24,12,0,414,415,6,13,-1,0,415,418,1,0,0,0,
        416,418,6,13,-1,0,417,407,1,0,0,0,417,410,1,0,0,0,417,413,1,0,0,
        0,417,416,1,0,0,0,418,27,1,0,0,0,419,420,3,16,8,0,420,421,6,14,-1,
        0,421,446,1,0,0,0,422,423,3,54,27,0,423,424,6,14,-1,0,424,446,1,
        0,0,0,425,427,5,43,0,0,426,428,7,4,0,0,427,426,1,0,0,0,427,428,1,
        0,0,0,428,429,1,0,0,0,429,430,3,26,13,0,430,435,6,14,-1,0,431,432,
        7,5,0,0,432,433,3,26,13,0,433,434,6,14,-1,0,434,436,1,0,0,0,435,
        431,1,0,0,0,436,437,1,0,0,0,437,435,1,0,0,0,437,438,1,0,0,0,438,
        440,1,0,0,0,439,441,7,4,0,0,440,439,1,0,0,0,440,441,1,0,0,0,441,
        442,1,0,0,0,442,443,5,44,0,0,443,444,6,14,-1,0,444,446,1,0,0,0,445,
        419,1,0,0,0,445,422,1,0,0,0,445,425,1,0,0,0,446,29,1,0,0,0,447,448,
        5,11,0,0,448,449,3,18,9,0,449,450,5,38,0,0,450,451,3,18,9,0,451,
        452,6,15,-1,0,452,461,1,0,0,0,453,454,5,38,0,0,454,455,3,18,9,0,
        455,456,5,11,0,0,456,457,3,18,9,0,457,458,6,15,-1,0,458,461,1,0,
        0,0,459,461,6,15,-1,0,460,447,1,0,0,0,460,453,1,0,0,0,460,459,1,
        0,0,0,461,31,1,0,0,0,462,463,5,27,0,0,463,464,3,12,6,0,464,465,5,
        11,0,0,465,466,3,18,9,0,466,467,6,16,-1,0,467,473,1,0,0,0,468,469,
        5,27,0,0,469,470,3,12,6,0,470,471,6,16,-1,0,471,473,1,0,0,0,472,
        462,1,0,0,0,472,468,1,0,0,0,473,33,1,0,0,0,474,476,3,32,16,0,475,
        474,1,0,0,0,476,477,1,0,0,0,477,475,1,0,0,0,477,478,1,0,0,0,478,
        35,1,0,0,0,479,492,6,18,-1,0,480,481,5,11,0,0,481,482,5,43,0,0,482,
        483,7,6,0,0,483,484,5,44,0,0,484,492,6,18,-1,0,485,486,5,11,0,0,
        486,487,5,6,0,0,487,492,6,18,-1,0,488,489,5,11,0,0,489,490,5,7,0,
        0,490,492,6,18,-1,0,491,479,1,0,0,0,491,480,1,0,0,0,491,485,1,0,
        0,0,491,488,1,0,0,0,492,37,1,0,0,0,493,494,5,38,0,0,494,495,5,43,
        0,0,495,496,3,12,6,0,496,497,5,12,0,0,497,498,3,12,6,0,498,499,5,
        44,0,0,499,500,5,11,0,0,500,501,3,20,10,0,501,502,6,19,-1,0,502,
        514,1,0,0,0,503,504,5,11,0,0,504,505,3,20,10,0,505,506,5,38,0,0,
        506,507,5,43,0,0,507,508,3,12,6,0,508,509,5,12,0,0,509,510,3,12,
        6,0,510,511,5,44,0,0,511,512,6,19,-1,0,512,514,1,0,0,0,513,493,1,
        0,0,0,513,503,1,0,0,0,514,39,1,0,0,0,515,516,3,12,6,0,516,517,5,
        12,0,0,517,525,3,12,6,0,518,519,5,37,0,0,519,520,3,12,6,0,520,521,
        5,12,0,0,521,522,3,12,6,0,522,524,1,0,0,0,523,518,1,0,0,0,524,527,
        1,0,0,0,525,523,1,0,0,0,525,526,1,0,0,0,526,41,1,0,0,0,527,525,1,
        0,0,0,528,529,5,38,0,0,529,530,5,43,0,0,530,531,3,40,20,0,531,532,
        5,44,0,0,532,552,1,0,0,0,533,534,5,38,0,0,534,535,5,43,0,0,535,536,
        3,40,20,0,536,537,5,44,0,0,537,538,5,11,0,0,538,539,5,43,0,0,539,
        540,3,40,20,0,540,541,5,44,0,0,541,552,1,0,0,0,542,543,5,11,0,0,
        543,544,5,43,0,0,544,545,3,40,20,0,545,546,5,44,0,0,546,547,5,38,
        0,0,547,548,5,43,0,0,548,549,3,40,20,0,549,550,5,44,0,0,550,552,
        1,0,0,0,551,528,1,0,0,0,551,533,1,0,0,0,551,542,1,0,0,0,552,43,1,
        0,0,0,553,554,5,78,0,0,554,558,6,22,-1,0,555,556,5,79,0,0,556,558,
        6,22,-1,0,557,553,1,0,0,0,557,555,1,0,0,0,558,45,1,0,0,0,559,560,
        5,77,0,0,560,561,3,44,22,0,561,562,6,23,-1,0,562,47,1,0,0,0,563,
        564,3,44,22,0,564,565,6,24,-1,0,565,570,1,0,0,0,566,567,3,46,23,
        0,567,568,6,24,-1,0,568,570,1,0,0,0,569,563,1,0,0,0,569,566,1,0,
        0,0,570,49,1,0,0,0,571,572,5,45,0,0,572,573,3,12,6,0,573,574,5,46,
        0,0,574,575,6,25,-1,0,575,599,1,0,0,0,576,577,5,59,0,0,577,578,3,
        12,6,0,578,579,5,59,0,0,579,599,1,0,0,0,580,581,5,60,0,0,581,582,
        3,12,6,0,582,583,5,60,0,0,583,599,1,0,0,0,584,585,5,55,0,0,585,586,
        3,12,6,0,586,587,5,56,0,0,587,599,1,0,0,0,588,589,5,53,0,0,589,590,
        3,12,6,0,590,591,5,54,0,0,591,599,1,0,0,0,592,593,5,57,0,0,593,594,
        3,12,6,0,594,595,7,7,0,0,595,596,3,12,6,0,596,597,5,58,0,0,597,599,
        1,0,0,0,598,571,1,0,0,0,598,576,1,0,0,0,598,580,1,0,0,0,598,584,
        1,0,0,0,598,588,1,0,0,0,598,592,1,0,0,0,599,51,1,0,0,0,600,601,5,
        43,0,0,601,602,7,8,0,0,602,603,3,12,6,0,603,604,5,78,0,0,604,605,
        4,26,9,1,605,606,5,11,0,0,606,607,3,12,6,0,607,608,5,44,0,0,608,
        609,6,26,-1,0,609,625,1,0,0,0,610,611,5,43,0,0,611,612,5,78,0,0,
        612,613,4,26,10,1,613,614,5,11,0,0,614,615,3,12,6,0,615,616,5,44,
        0,0,616,617,6,26,-1,0,617,625,1,0,0,0,618,619,5,43,0,0,619,620,5,
        34,0,0,620,621,3,12,6,0,621,622,5,44,0,0,622,623,6,26,-1,0,623,625,
        1,0,0,0,624,600,1,0,0,0,624,610,1,0,0,0,624,618,1,0,0,0,625,53,1,
        0,0,0,626,627,5,20,0,0,627,628,3,18,9,0,628,629,3,18,9,0,629,630,
        6,27,-1,0,630,659,1,0,0,0,631,632,5,21,0,0,632,633,3,18,9,0,633,
        634,3,18,9,0,634,635,6,27,-1,0,635,659,1,0,0,0,636,637,5,22,0,0,
        637,638,3,18,9,0,638,639,6,27,-1,0,639,659,1,0,0,0,640,645,5,22,
        0,0,641,642,5,49,0,0,642,643,3,12,6,0,643,644,5,50,0,0,644,646,1,
        0,0,0,645,641,1,0,0,0,645,646,1,0,0,0,646,647,1,0,0,0,647,648,3,
        18,9,0,648,649,6,27,-1,0,649,659,1,0,0,0,650,651,5,23,0,0,651,652,
        3,18,9,0,652,653,6,27,-1,0,653,659,1,0,0,0,654,655,5,24,0,0,655,
        656,3,18,9,0,656,657,6,27,-1,0,657,659,1,0,0,0,658,626,1,0,0,0,658,
        631,1,0,0,0,658,636,1,0,0,0,658,640,1,0,0,0,658,650,1,0,0,0,658,
        654,1,0,0,0,659,55,1,0,0,0,660,673,1,0,0,0,661,662,3,12,6,0,662,
        669,6,28,-1,0,663,664,5,70,0,0,664,665,3,12,6,0,665,666,6,28,-1,
        0,666,668,1,0,0,0,667,663,1,0,0,0,668,671,1,0,0,0,669,667,1,0,0,
        0,669,670,1,0,0,0,670,673,1,0,0,0,671,669,1,0,0,0,672,660,1,0,0,
        0,672,661,1,0,0,0,673,57,1,0,0,0,674,693,1,0,0,0,675,676,3,56,28,
        0,676,683,6,29,-1,0,677,678,5,71,0,0,678,679,3,56,28,0,679,680,6,
        29,-1,0,680,682,1,0,0,0,681,677,1,0,0,0,682,685,1,0,0,0,683,681,
        1,0,0,0,683,684,1,0,0,0,684,689,1,0,0,0,685,683,1,0,0,0,686,688,
        5,71,0,0,687,686,1,0,0,0,688,691,1,0,0,0,689,687,1,0,0,0,689,690,
        1,0,0,0,690,693,1,0,0,0,691,689,1,0,0,0,692,674,1,0,0,0,692,675,
        1,0,0,0,693,59,1,0,0,0,694,695,5,62,0,0,695,696,3,58,29,0,696,697,
        5,63,0,0,697,703,1,0,0,0,698,699,5,66,0,0,699,700,3,58,29,0,700,
        701,5,67,0,0,701,703,1,0,0,0,702,694,1,0,0,0,702,698,1,0,0,0,703,
        704,1,0,0,0,704,705,6,30,-1,0,705,61,1,0,0,0,706,707,5,64,0,0,707,
        708,3,58,29,0,708,709,5,65,0,0,709,63,1,0,0,0,50,72,78,85,91,106,
        131,147,160,173,189,205,208,233,245,255,294,309,324,353,359,361,
        371,381,394,397,401,417,427,437,440,445,460,472,477,491,513,525,
        551,557,569,598,624,645,658,669,672,683,689,692,702
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

    symbolicNames = [ "<INVALID>", "FUNCTION", "CMD_FUNCTION", "LBLANK", 
                      "RBLANK", "IGNORE", "PLUS", "MINUS", "MULT", "DIV", 
                      "XPROD", "POW", "EQ", "NEQ", "LT", "LTE", "GT", "GTE", 
                      "TIMES", "DOT_PROD", "FRAC", "BINOM", "SQRT", "CONJUGATE", 
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
    RULE_delim_expr = 25
    RULE_combinatorial = 26
    RULE_cmd_func = 27
    RULE_matrix_row = 28
    RULE_matrix_body = 29
    RULE_matrix = 30
    RULE_det_matrix = 31

    ruleNames =  [ "debug", "a_lmat_expr", "system_el", "system_body", "system", 
                   "relation", "a_expr", "rel_op", "atom", "latex_cmd_arg", 
                   "pow_arg", "range_index", "all_index", "index_entry", 
                   "index_arg", "int_bounds", "diff_var", "diff_vars", "limit_dir", 
                   "series_range_args", "eval_at_sub_vars", "eval_at_arg", 
                   "primary_symbol", "delta_symbol", "symbol", "delim_expr", 
                   "combinatorial", "cmd_func", "matrix_row", "matrix_body", 
                   "matrix", "det_matrix" ]

    EOF = Token.EOF
    FUNCTION=1
    CMD_FUNCTION=2
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
            self.state = 64
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
            self.res = cast(Ast.AExpr, None)
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
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 67
                localctx._a_expr = self.a_expr(0)
                localctx.res = localctx._a_expr.res
                pass

            elif la_ == 2:
                self.state = 70
                self.relation()
                pass

            elif la_ == 3:
                self.state = 71
                self.system()
                pass


            self.state = 74
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
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.a_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
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
            self.state = 80
            self.system_el()
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 81
                    self.match(ExprGrammar.ENV_ROW_SEP)
                    self.state = 82
                    self.system_el() 
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==71:
                self.state = 88
                self.match(ExprGrammar.ENV_ROW_SEP)
                self.state = 93
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
            self.state = 94
            self.match(ExprGrammar.BEGIN_ENV)
            self.state = 95
            self.system_body()
            self.state = 96
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
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.a_expr(0)
                self.state = 99
                self.rel_op()
                self.state = 100
                self.relation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.a_expr(0)
                self.state = 103
                self.rel_op()
                self.state = 104
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
            self.res = cast(Ast.AExpr, None)
            self.node_t = None


        def getRuleIndex(self):
            return ExprGrammar.RULE_a_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.res = ctx.res
            self.node_t = ctx.node_t


    class CombContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self._combinatorial = None # CombinatorialContext
            self.copyFrom(ctx)

        def combinatorial(self):
            return self.getTypedRuleContext(ExprGrammar.CombinatorialContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComb" ):
                listener.enterComb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComb" ):
                listener.exitComb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComb" ):
                return visitor.visitComb(self)
            else:
                return visitor.visitChildren(self)


    class DelimitedExprContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self._delim_expr = None # Delim_exprContext
            self.copyFrom(ctx)

        def delim_expr(self):
            return self.getTypedRuleContext(ExprGrammar.Delim_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelimitedExpr" ):
                listener.enterDelimitedExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelimitedExpr" ):
                listener.exitDelimitedExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelimitedExpr" ):
                return visitor.visitDelimitedExpr(self)
            else:
                return visitor.visitChildren(self)


    class EvalAtContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self._a_expr = None # A_exprContext
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ExprGrammar.LPAREN, 0)
        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)

        def RPAREN(self):
            return self.getToken(ExprGrammar.RPAREN, 0)
        def BAR(self):
            return self.getToken(ExprGrammar.BAR, 0)
        def eval_at_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Eval_at_argContext,0)

        def LBLANK(self):
            return self.getToken(ExprGrammar.LBLANK, 0)
        def LBRACKET(self):
            return self.getToken(ExprGrammar.LBRACKET, 0)
        def RBRACKET(self):
            return self.getToken(ExprGrammar.RBRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvalAt" ):
                listener.enterEvalAt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvalAt" ):
                listener.exitEvalAt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvalAt" ):
                return visitor.visitEvalAt(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicativeOpContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self.lhs = None # A_exprContext
            self.rhs = None # A_exprContext
            self._a_expr = None # A_exprContext
            self.copyFrom(ctx)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)

        def MULT(self):
            return self.getToken(ExprGrammar.MULT, 0)
        def TIMES(self):
            return self.getToken(ExprGrammar.TIMES, 0)
        def XPROD(self):
            return self.getToken(ExprGrammar.XPROD, 0)
        def DOT_PROD(self):
            return self.getToken(ExprGrammar.DOT_PROD, 0)
        def DIV(self):
            return self.getToken(ExprGrammar.DIV, 0)
        def MOD(self):
            return self.getToken(ExprGrammar.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeOp" ):
                listener.enterMultiplicativeOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeOp" ):
                listener.exitMultiplicativeOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeOp" ):
                return visitor.visitMultiplicativeOp(self)
            else:
                return visitor.visitChildren(self)


    class UAdditiveOpContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self._a_expr = None # A_exprContext
            self.copyFrom(ctx)

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)

        def PLUS(self):
            return self.getToken(ExprGrammar.PLUS, 0)
        def MINUS(self):
            return self.getToken(ExprGrammar.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUAdditiveOp" ):
                listener.enterUAdditiveOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUAdditiveOp" ):
                listener.exitUAdditiveOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUAdditiveOp" ):
                return visitor.visitUAdditiveOp(self)
            else:
                return visitor.visitChildren(self)


    class IndexPowContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self.base = None # A_exprContext
            self.exp = None # Pow_argContext
            self.index = None # Index_argContext
            self.copyFrom(ctx)

        def POW(self):
            return self.getToken(ExprGrammar.POW, 0)
        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)
        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)

        def pow_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Pow_argContext,0)

        def index_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Index_argContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexPow" ):
                listener.enterIndexPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexPow" ):
                listener.exitIndexPow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexPow" ):
                return visitor.visitIndexPow(self)
            else:
                return visitor.visitChildren(self)


    class StubContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self._cmd_func = None # Cmd_funcContext
            self._matrix = None # MatrixContext
            self._symbol = None # SymbolContext
            self._NUMBER = None # Token
            self.copyFrom(ctx)

        def cmd_func(self):
            return self.getTypedRuleContext(ExprGrammar.Cmd_funcContext,0)

        def matrix(self):
            return self.getTypedRuleContext(ExprGrammar.MatrixContext,0)

        def det_matrix(self):
            return self.getTypedRuleContext(ExprGrammar.Det_matrixContext,0)

        def symbol(self):
            return self.getTypedRuleContext(ExprGrammar.SymbolContext,0)

        def NUMBER(self):
            return self.getToken(ExprGrammar.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStub" ):
                listener.enterStub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStub" ):
                listener.exitStub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStub" ):
                return visitor.visitStub(self)
            else:
                return visitor.visitChildren(self)


    class IndexContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self.base = None # A_exprContext
            self.index = None # Index_argContext
            self.copyFrom(ctx)

        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)
        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)

        def index_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Index_argContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex" ):
                listener.enterIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex" ):
                listener.exitIndex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)


    class PrefixContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self.op = None # A_exprContext
            self.copyFrom(ctx)

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)

        def BANG(self):
            return self.getToken(ExprGrammar.BANG, 0)
        def PERCENT(self):
            return self.getToken(ExprGrammar.PERCENT, 0)
        def PERMILLE(self):
            return self.getToken(ExprGrammar.PERMILLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefix" ):
                listener.enterPrefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefix" ):
                listener.exitPrefix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefix" ):
                return visitor.visitPrefix(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self._int_bounds = None # Int_boundsContext
            self.diff = None # A_exprContext
            self._a_expr = None # A_exprContext
            self.recip_integrand = None # Latex_cmd_argContext
            self._latex_cmd_arg = None # Latex_cmd_argContext
            self.integrand = None # A_exprContext
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ExprGrammar.INT, 0)
        def int_bounds(self):
            return self.getTypedRuleContext(ExprGrammar.Int_boundsContext,0)

        def FRAC(self):
            return self.getToken(ExprGrammar.FRAC, 0)
        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)
        def DIFFERENTIAL(self):
            return self.getToken(ExprGrammar.DIFFERENTIAL, 0)
        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)
        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)

        def latex_cmd_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Latex_cmd_argContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class FunctionContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self._a_expr = None # A_exprContext
            self.copyFrom(ctx)

        def FUNCTION(self):
            return self.getToken(ExprGrammar.FUNCTION, 0)
        def LPAREN(self):
            return self.getToken(ExprGrammar.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(ExprGrammar.RPAREN, 0)
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


    class SeriesContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self._series_range_args = None # Series_range_argsContext
            self._a_expr = None # A_exprContext
            self.copyFrom(ctx)

        def series_range_args(self):
            return self.getTypedRuleContext(ExprGrammar.Series_range_argsContext,0)

        def LPAREN(self):
            return self.getToken(ExprGrammar.LPAREN, 0)
        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)

        def RPAREN(self):
            return self.getToken(ExprGrammar.RPAREN, 0)
        def SUM(self):
            return self.getToken(ExprGrammar.SUM, 0)
        def PRODUCT(self):
            return self.getToken(ExprGrammar.PRODUCT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeries" ):
                listener.enterSeries(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeries" ):
                listener.exitSeries(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeries" ):
                return visitor.visitSeries(self)
            else:
                return visitor.visitChildren(self)


    class DerivContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self._a_expr = None # A_exprContext
            self._latex_cmd_arg = None # Latex_cmd_argContext
            self.diff_l = None # A_exprContext
            self.diff_r = None # A_exprContext
            self.degree = None # A_exprContext
            self.diffand_last = None # A_exprContext
            self._diff_vars = None # Diff_varsContext
            self.copyFrom(ctx)

        def PHYS_PARTIAL_DERIVATIVE(self):
            return self.getToken(ExprGrammar.PHYS_PARTIAL_DERIVATIVE, 0)
        def latex_cmd_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Latex_cmd_argContext,0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.LBRACE)
            else:
                return self.getToken(ExprGrammar.LBRACE, i)
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

        def LBRACKET(self):
            return self.getToken(ExprGrammar.LBRACKET, 0)
        def RBRACKET(self):
            return self.getToken(ExprGrammar.RBRACKET, 0)
        def PHYS_DERIVATIVE(self):
            return self.getToken(ExprGrammar.PHYS_DERIVATIVE, 0)
        def FRAC(self):
            return self.getToken(ExprGrammar.FRAC, 0)
        def DIFFERENTIAL(self):
            return self.getToken(ExprGrammar.DIFFERENTIAL, 0)
        def diff_vars(self):
            return self.getTypedRuleContext(ExprGrammar.Diff_varsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeriv" ):
                listener.enterDeriv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeriv" ):
                listener.exitDeriv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeriv" ):
                return visitor.visitDeriv(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveOpContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self.lhs = None # A_exprContext
            self.rhs = None # A_exprContext
            self._a_expr = None # A_exprContext
            self.copyFrom(ctx)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)

        def PLUS(self):
            return self.getToken(ExprGrammar.PLUS, 0)
        def MINUS(self):
            return self.getToken(ExprGrammar.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveOp" ):
                listener.enterAdditiveOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveOp" ):
                listener.exitAdditiveOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveOp" ):
                return visitor.visitAdditiveOp(self)
            else:
                return visitor.visitChildren(self)


    class PowContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self.base = None # A_exprContext
            self.exp = None # Pow_argContext
            self.copyFrom(ctx)

        def POW(self):
            return self.getToken(ExprGrammar.POW, 0)
        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)

        def pow_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Pow_argContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPow" ):
                listener.enterPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow" ):
                listener.exitPow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow" ):
                return visitor.visitPow(self)
            else:
                return visitor.visitChildren(self)


    class LimitContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self.lim_var = None # SymbolContext
            self._symbol = None # SymbolContext
            self.lim_poa = None # A_exprContext
            self._a_expr = None # A_exprContext
            self._limit_dir = None # Limit_dirContext
            self.copyFrom(ctx)

        def LIMIT(self):
            return self.getToken(ExprGrammar.LIMIT, 0)
        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)
        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)
        def LIMIT_ARROW(self):
            return self.getToken(ExprGrammar.LIMIT_ARROW, 0)
        def limit_dir(self):
            return self.getTypedRuleContext(ExprGrammar.Limit_dirContext,0)

        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)
        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)

        def symbol(self):
            return self.getTypedRuleContext(ExprGrammar.SymbolContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimit" ):
                listener.enterLimit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimit" ):
                listener.exitLimit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimit" ):
                return visitor.visitLimit(self)
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
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = ExprGrammar.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 109
                self.match(ExprGrammar.INT)
                self.state = 110
                localctx._int_bounds = self.int_bounds()
                self.state = 111
                self.match(ExprGrammar.FRAC)
                self.state = 112
                self.match(ExprGrammar.LBRACE)
                self.state = 113
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 114
                localctx.diff = localctx._a_expr = self.a_expr(0)
                self.state = 115
                self.match(ExprGrammar.RBRACE)
                self.state = 116
                localctx.recip_integrand = localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Integral(localctx, Ast.DivOp(localctx.recip_integrand, Ast.Number(localctx.recip_integrand, "1"), localctx.recip_integrand.res), localctx.diff.res, localctx._int_bounds.bounds)
                pass

            elif la_ == 2:
                localctx = ExprGrammar.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.match(ExprGrammar.INT)
                self.state = 120
                localctx._int_bounds = self.int_bounds()
                self.state = 121
                localctx.integrand = localctx._a_expr = self.a_expr(0)
                self.state = 122
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 123
                localctx.diff = localctx._a_expr = self.a_expr(28)
                localctx.res = Ast.Integral(localctx, localctx.integrand.res, localctx.diff.res, localctx._int_bounds.bounds)
                pass

            elif la_ == 3:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 126
                self.match(ExprGrammar.PHYS_PARTIAL_DERIVATIVE)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 127
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 128
                    localctx._a_expr = self.a_expr(0)
                    self.state = 129
                    self.match(ExprGrammar.RBRACKET)


                self.state = 133
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 134
                self.match(ExprGrammar.LBRACE)
                self.state = 135
                localctx.diff_l = localctx._a_expr = self.a_expr(0)
                self.state = 136
                self.match(ExprGrammar.RBRACE)
                self.state = 137
                self.match(ExprGrammar.LBRACE)
                self.state = 138
                localctx.diff_r = localctx._a_expr = self.a_expr(0)
                self.state = 139
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._latex_cmd_arg.res, [(localctx.diff_l.res, None), (localctx.diff_r.res, None)])
                pass

            elif la_ == 4:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                _la = self._input.LA(1)
                if not(_la==28 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 143
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 144
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 145
                    self.match(ExprGrammar.RBRACKET)


                self.state = 149
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 150
                self.match(ExprGrammar.LBRACE)
                self.state = 151
                localctx._a_expr = self.a_expr(0)
                self.state = 152
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._latex_cmd_arg.res, [(localctx._a_expr.res, localctx.degree.res)])
                pass

            elif la_ == 5:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 155
                _la = self._input.LA(1)
                if not(_la==28 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 156
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 157
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 158
                    self.match(ExprGrammar.RBRACKET)


                self.state = 162
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 163
                localctx.diffand_last = localctx._a_expr = self.a_expr(24)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, [(localctx._latex_cmd_arg.res, localctx.degree.res)])
                pass

            elif la_ == 6:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 166
                self.match(ExprGrammar.FRAC)
                self.state = 167
                self.match(ExprGrammar.LBRACE)
                self.state = 168
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 173
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 169
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 170
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 171
                    self.match(ExprGrammar.RBRACKET)


                self.state = 175
                localctx._a_expr = self.a_expr(0)
                self.state = 176
                self.match(ExprGrammar.RBRACE)
                self.state = 177
                self.match(ExprGrammar.LBRACE)
                self.state = 178
                localctx._diff_vars = self.diff_vars()
                self.state = 179
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, localctx._diff_vars.res)
                pass

            elif la_ == 7:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 182
                self.match(ExprGrammar.FRAC)
                self.state = 183
                self.match(ExprGrammar.LBRACE)
                self.state = 184
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 185
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 186
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 187
                    self.match(ExprGrammar.RBRACKET)


                self.state = 191
                self.match(ExprGrammar.RBRACE)
                self.state = 192
                self.match(ExprGrammar.LBRACE)
                self.state = 193
                localctx._diff_vars = self.diff_vars()
                self.state = 194
                self.match(ExprGrammar.RBRACE)
                self.state = 195
                localctx._a_expr = self.a_expr(22)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, localctx._diff_vars.res)
                pass

            elif la_ == 8:
                localctx = ExprGrammar.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 198
                self.match(ExprGrammar.FUNCTION)
                self.state = 199
                self.match(ExprGrammar.LPAREN)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6530826404969316554) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 57861) != 0):
                    self.state = 200
                    localctx._a_expr = self.a_expr(0)
                    self.state = 205
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==37:
                        self.state = 201
                        self.match(ExprGrammar.COMMA)
                        self.state = 202
                        localctx._a_expr = self.a_expr(0)
                        self.state = 207
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 210
                self.match(ExprGrammar.RPAREN)
                pass

            elif la_ == 9:
                localctx = ExprGrammar.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 211
                self.match(ExprGrammar.FUNCTION)
                self.state = 212
                self.match(ExprGrammar.LBRACE)
                self.state = 213
                localctx._a_expr = self.a_expr(0)
                self.state = 214
                self.match(ExprGrammar.RBRACE)
                pass

            elif la_ == 10:
                localctx = ExprGrammar.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 216
                self.match(ExprGrammar.FUNCTION)
                self.state = 217
                localctx._a_expr = self.a_expr(19)
                pass

            elif la_ == 11:
                localctx = ExprGrammar.LimitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 218
                self.match(ExprGrammar.LIMIT)
                self.state = 219
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 220
                self.match(ExprGrammar.LBRACE)
                self.state = 221
                localctx.lim_var = localctx._symbol = self.symbol()
                self.state = 222
                self.match(ExprGrammar.LIMIT_ARROW)
                self.state = 223
                localctx.lim_poa = localctx._a_expr = self.a_expr(0)
                self.state = 224
                localctx._limit_dir = self.limit_dir()
                self.state = 225
                self.match(ExprGrammar.RBRACE)
                self.state = 226
                localctx._a_expr = self.a_expr(18)
                localctx.res = Ast.Limit(localctx._a_expr.res, localctx.lim_var.res, localctx.lim_poa.res, localctx._limit_dir.res)
                pass

            elif la_ == 12:
                localctx = ExprGrammar.SeriesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 233
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32]:
                    self.state = 229
                    self.match(ExprGrammar.SUM)
                    localctx.node_t = Ast.Sum
                    pass
                elif token in [33]:
                    self.state = 231
                    self.match(ExprGrammar.PRODUCT)
                    localctx.node_t = Ast.Product
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 235
                localctx._series_range_args = self.series_range_args()
                self.state = 236
                self.match(ExprGrammar.LPAREN)
                self.state = 237
                localctx._a_expr = self.a_expr(0)
                self.state = 238
                self.match(ExprGrammar.RPAREN)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res, localctx._series_range_args.symb, (localctx._series_range_args.start, localctx._series_range_args.end))
                pass

            elif la_ == 13:
                localctx = ExprGrammar.SeriesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 245
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32]:
                    self.state = 241
                    self.match(ExprGrammar.SUM)
                    localctx.node_t = Ast.Sum
                    pass
                elif token in [33]:
                    self.state = 243
                    self.match(ExprGrammar.PRODUCT)
                    localctx.node_t = Ast.Product
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 247
                localctx._series_range_args = self.series_range_args()
                self.state = 248
                localctx._a_expr = self.a_expr(14)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res, localctx._series_range_args.symb, (localctx._series_range_args.start, localctx._series_range_args.end))
                pass

            elif la_ == 14:
                localctx = ExprGrammar.UAdditiveOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 255
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 251
                    self.match(ExprGrammar.PLUS)
                    localctx.node_t = Ast.UPlusOp
                    pass
                elif token in [7]:
                    self.state = 253
                    self.match(ExprGrammar.MINUS)
                    localctx.node_t = Ast.UMinusOp
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 257
                localctx._a_expr = self.a_expr(12)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res)
                pass

            elif la_ == 15:
                localctx = ExprGrammar.EvalAtContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 260
                self.match(ExprGrammar.LPAREN)
                self.state = 261
                localctx._a_expr = self.a_expr(0)
                self.state = 262
                self.match(ExprGrammar.RPAREN)
                self.state = 263
                self.match(ExprGrammar.BAR)
                self.state = 264
                self.eval_at_arg()
                pass

            elif la_ == 16:
                localctx = ExprGrammar.EvalAtContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 266
                self.match(ExprGrammar.LBLANK)
                self.state = 267
                localctx._a_expr = self.a_expr(0)
                self.state = 268
                self.match(ExprGrammar.BAR)
                self.state = 269
                self.eval_at_arg()
                pass

            elif la_ == 17:
                localctx = ExprGrammar.EvalAtContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 271
                self.match(ExprGrammar.LBRACKET)
                self.state = 272
                localctx._a_expr = self.a_expr(0)
                self.state = 273
                self.match(ExprGrammar.RBRACKET)
                self.state = 274
                self.eval_at_arg()
                pass

            elif la_ == 18:
                localctx = ExprGrammar.CombContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 276
                localctx._combinatorial = self.combinatorial()
                localctx.res = localctx._combinatorial.res
                pass

            elif la_ == 19:
                localctx = ExprGrammar.DelimitedExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 279
                localctx._delim_expr = self.delim_expr()
                localctx.res = localctx._delim_expr.res
                pass

            elif la_ == 20:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 282
                localctx._cmd_func = self.cmd_func()
                localctx.res = localctx._cmd_func.res
                pass

            elif la_ == 21:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 285
                localctx._matrix = self.matrix()
                localctx.res = localctx._matrix.res 
                pass

            elif la_ == 22:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 288
                self.det_matrix()
                pass

            elif la_ == 23:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 289
                localctx._symbol = self.symbol()
                localctx.res = localctx._symbol.res
                pass

            elif la_ == 24:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 292
                localctx._NUMBER = self.match(ExprGrammar.NUMBER)
                localctx.res = Ast.Number(localctx, (None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 361
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 359
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = ExprGrammar.MultiplicativeOpContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 296
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 309
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [8]:
                            self.state = 297
                            self.match(ExprGrammar.MULT)
                            localctx.node_t = Ast.MultOp
                            pass
                        elif token in [18]:
                            self.state = 299
                            self.match(ExprGrammar.TIMES)
                            localctx.node_t = Ast.MultOp
                            pass
                        elif token in [10]:
                            self.state = 301
                            self.match(ExprGrammar.XPROD)
                            localctx.node_t = Ast.MultOp
                            pass
                        elif token in [19]:
                            self.state = 303
                            self.match(ExprGrammar.DOT_PROD)
                            localctx.node_t = Ast.MultOp
                            pass
                        elif token in [9]:
                            self.state = 305
                            self.match(ExprGrammar.DIV)
                            localctx.node_t = Ast.DivOp
                            pass
                        elif token in [25]:
                            self.state = 307
                            self.match(ExprGrammar.MOD)
                            localctx.node_t = Ast.ModOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 311
                        localctx.rhs = localctx._a_expr = self.a_expr(18)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 2:
                        localctx = ExprGrammar.MultiplicativeOpContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 314
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 315
                        if not ((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS)):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS))")
                        self.state = 316
                        localctx.rhs = localctx._a_expr = self.a_expr(17)
                        localctx.res = Ast.MultOp(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 3:
                        localctx = ExprGrammar.AdditiveOpContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 319
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 324
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [6]:
                            self.state = 320
                            self.match(ExprGrammar.PLUS)
                            localctx.node_t = Ast.AddOp
                            pass
                        elif token in [7]:
                            self.state = 322
                            self.match(ExprGrammar.MINUS)
                            localctx.node_t = Ast.SubOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 326
                        localctx.rhs = localctx._a_expr = self.a_expr(14)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 4:
                        localctx = ExprGrammar.IndexPowContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 329
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 330
                        self.match(ExprGrammar.POW)
                        self.state = 331
                        localctx.exp = self.pow_arg()
                        self.state = 332
                        self.match(ExprGrammar.UNDERSCORE)
                        self.state = 333
                        localctx.index = self.index_arg()
                        localctx.res=Ast.ExpOp(localctx, localctx.base.res, localctx.exp.res)
                        pass

                    elif la_ == 5:
                        localctx = ExprGrammar.PowContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 336
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 337
                        self.match(ExprGrammar.POW)
                        self.state = 338
                        localctx.exp = self.pow_arg()
                        localctx.res=Ast.ExpOp(localctx, localctx.base.res, localctx.exp.res)
                        pass

                    elif la_ == 6:
                        localctx = ExprGrammar.IndexContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 341
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 342
                        self.match(ExprGrammar.UNDERSCORE)
                        self.state = 343
                        localctx.index = self.index_arg()
                        localctx.res = Ast.IndexOp(localctx, localctx.base.res, localctx.index.res)
                        pass

                    elif la_ == 7:
                        localctx = ExprGrammar.PrefixContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.op = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 346
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 353
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [34]:
                            self.state = 347
                            self.match(ExprGrammar.BANG)
                            localctx.node_t = Ast.Factorial
                            pass
                        elif token in [35]:
                            self.state = 349
                            self.match(ExprGrammar.PERCENT)
                            localctx.node_t = Ast.Percent
                            pass
                        elif token in [36]:
                            self.state = 351
                            self.match(ExprGrammar.PERMILLE)
                            localctx.node_t = Ast.Permille
                            pass
                        else:
                            raise NoViableAltException(self)

                        localctx.res = localctx.node_t(localctx, localctx.op.res)
                        pass

                    elif la_ == 8:
                        localctx = ExprGrammar.EvalAtContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 356
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 357
                        self.match(ExprGrammar.BAR)
                        self.state = 358
                        self.eval_at_arg()
                        pass

             
                self.state = 363
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            self.state = 364
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
            self.res = None
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
            self.state = 371
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [78, 79]:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                localctx._primary_symbol = self.primary_symbol()
                localctx.res = localctx._primary_symbol.res
                pass
            elif token in [73]:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
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
            self.res = None
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
            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [73, 78, 79]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.match(ExprGrammar.LBRACE)
                self.state = 377
                localctx._a_expr = self.a_expr(0)
                self.state = 378
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
            self.res = None
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
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [73, 78, 79]:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass
            elif token in [20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                localctx._cmd_func = self.cmd_func()
                localctx.res = localctx._cmd_func.res
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 389
                self.match(ExprGrammar.LBRACE)
                self.state = 390
                localctx._a_expr = self.a_expr(0)
                self.state = 391
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
            self.res = None
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
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6530826404969316554) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 57861) != 0):
                self.state = 396
                localctx.beg = self.a_expr(0)


            self.state = 399
            _la = self._input.LA(1)
            if not(_la==40 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 400
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
            self.state = 405
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
            self.res = None
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
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                localctx._a_expr = self.a_expr(0)
                localctx.res = localctx._a_expr.res
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                localctx._range_index = self.range_index()
                localctx.res = localctx._range_index.res
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 413
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
            self.res = None
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
            self.state = 445
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [73, 78, 79]:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                localctx._atom = self.atom()
                localctx.res = (localctx._atom.res,)
                pass
            elif token in [20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                localctx._cmd_func = self.cmd_func()
                localctx.res = (localctx._cmd_func.res,)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 425
                self.match(ExprGrammar.LBRACE)
                self.state = 427
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 426
                    _la = self._input.LA(1)
                    if not(_la==45 or _la==49):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 429
                localctx._index_entry = self.index_entry()
                localctx.res = [localctx._index_entry.res]
                self.state = 435 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 431
                    _la = self._input.LA(1)
                    if not(_la==37 or _la==39):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 432
                    localctx._index_entry = self.index_entry()
                    localctx.res.append(localctx._index_entry.res)
                    self.state = 437 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==37 or _la==39):
                        break

                self.state = 440
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45 or _la==49:
                    self.state = 439
                    _la = self._input.LA(1)
                    if not(_la==45 or _la==49):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 442
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
            self.bounds = None
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
            self.state = 460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(ExprGrammar.POW)
                self.state = 448
                localctx.upper = self.latex_cmd_arg()
                self.state = 449
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 450
                localctx.lower = self.latex_cmd_arg()
                localctx.bounds = (localctx.lower.res, localctx.upper.res)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 454
                localctx.lower = self.latex_cmd_arg()
                self.state = 455
                self.match(ExprGrammar.POW)
                self.state = 456
                localctx.upper = self.latex_cmd_arg()
                localctx.bounds = (localctx.lower.res, localctx.upper.res)
                pass
            elif token in [1, 3, 6, 7, 20, 21, 22, 23, 24, 26, 28, 29, 30, 32, 33, 43, 45, 49, 53, 55, 57, 59, 60, 62, 64, 66, 73, 77, 78, 79]:
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
            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 463
                localctx._a_expr = self.a_expr(0)
                self.state = 464
                self.match(ExprGrammar.POW)
                self.state = 465
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.getInvokingContext(17).res.append((localctx._a_expr.res, localctx._latex_cmd_arg.res))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 469
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
            self.res = []

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
            self.state = 475 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 474
                self.diff_var()
                self.state = 477 
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
            self.res = None

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
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                localctx.res = Ast.LimitDir.BOTH
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
                self.match(ExprGrammar.POW)
                self.state = 481
                self.match(ExprGrammar.LBRACE)
                self.state = 482
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 483
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.LimitDir.BOTH
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 485
                self.match(ExprGrammar.POW)
                self.state = 486
                self.match(ExprGrammar.PLUS)
                localctx.res = Ast.LimitDir.POSITIVE
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 488
                self.match(ExprGrammar.POW)
                self.state = 489
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
            self.symb = None
            self.start = None
            self.end = None
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
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 494
                self.match(ExprGrammar.LBRACE)
                self.state = 495
                localctx.var = self.a_expr(0)
                self.state = 496
                self.match(ExprGrammar.EQ)
                self.state = 497
                localctx.s = self.a_expr(0)
                self.state = 498
                self.match(ExprGrammar.RBRACE)
                self.state = 499
                self.match(ExprGrammar.POW)
                self.state = 500
                localctx.e = self.pow_arg()

                localctx.symb = localctx.var.res
                localctx.start = localctx.s.res
                localctx.end = localctx.e.res

                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.match(ExprGrammar.POW)
                self.state = 504
                localctx.e = self.pow_arg()
                self.state = 505
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 506
                self.match(ExprGrammar.LBRACE)
                self.state = 507
                localctx.var = self.a_expr(0)
                self.state = 508
                self.match(ExprGrammar.EQ)
                self.state = 509
                localctx.s = self.a_expr(0)
                self.state = 510
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

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.EQ)
            else:
                return self.getToken(ExprGrammar.EQ, i)

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
            self.state = 515
            self.a_expr(0)
            self.state = 516
            self.match(ExprGrammar.EQ)
            self.state = 517
            self.a_expr(0)
            self.state = 525
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 518
                self.match(ExprGrammar.COMMA)
                self.state = 519
                self.a_expr(0)
                self.state = 520
                self.match(ExprGrammar.EQ)
                self.state = 521
                self.a_expr(0)
                self.state = 527
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
            self.state = 551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 528
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 529
                self.match(ExprGrammar.LBRACE)
                self.state = 530
                self.eval_at_sub_vars()
                self.state = 531
                self.match(ExprGrammar.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 534
                self.match(ExprGrammar.LBRACE)
                self.state = 535
                self.eval_at_sub_vars()
                self.state = 536
                self.match(ExprGrammar.RBRACE)
                self.state = 537
                self.match(ExprGrammar.POW)
                self.state = 538
                self.match(ExprGrammar.LBRACE)
                self.state = 539
                self.eval_at_sub_vars()
                self.state = 540
                self.match(ExprGrammar.RBRACE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 542
                self.match(ExprGrammar.POW)
                self.state = 543
                self.match(ExprGrammar.LBRACE)
                self.state = 544
                self.eval_at_sub_vars()
                self.state = 545
                self.match(ExprGrammar.RBRACE)
                self.state = 546
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 547
                self.match(ExprGrammar.LBRACE)
                self.state = 548
                self.eval_at_sub_vars()
                self.state = 549
                self.match(ExprGrammar.RBRACE)
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
            self.res = None
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
            self.state = 557
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [78]:
                self.enterOuterAlt(localctx, 1)
                self.state = 553
                localctx._ID = self.match(ExprGrammar.ID)
                localctx.res = Ast.Symbol(localctx, (None if localctx._ID is None else localctx._ID.text))
                pass
            elif token in [79]:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
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
            self.res = None
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
            self.state = 559
            localctx._DELTA = self.match(ExprGrammar.DELTA)
            self.state = 560
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
            self.res = None
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
            self.state = 569
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [78, 79]:
                self.enterOuterAlt(localctx, 1)
                self.state = 563
                localctx._primary_symbol = self.primary_symbol()
                localctx.res = localctx._primary_symbol.res
                pass
            elif token in [77]:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
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


    class Delim_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self._a_expr = None # A_exprContext

        def LPAREN(self):
            return self.getToken(ExprGrammar.LPAREN, 0)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)


        def RPAREN(self):
            return self.getToken(ExprGrammar.RPAREN, 0)

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
        self.enterRule(localctx, 50, self.RULE_delim_expr)
        self._la = 0 # Token type
        try:
            self.state = 598
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 571
                self.match(ExprGrammar.LPAREN)
                self.state = 572
                localctx._a_expr = self.a_expr(0)
                self.state = 573
                self.match(ExprGrammar.RPAREN)
                localctx.res = localctx._a_expr.res.mut_ctx(localctx)
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 576
                self.match(ExprGrammar.BAR)
                self.state = 577
                self.a_expr(0)
                self.state = 578
                self.match(ExprGrammar.BAR)
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 3)
                self.state = 580
                self.match(ExprGrammar.DOUBLE_BAR)
                self.state = 581
                self.a_expr(0)
                self.state = 582
                self.match(ExprGrammar.DOUBLE_BAR)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 4)
                self.state = 584
                self.match(ExprGrammar.LFLOOR)
                self.state = 585
                self.a_expr(0)
                self.state = 586
                self.match(ExprGrammar.RFLOOR)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 5)
                self.state = 588
                self.match(ExprGrammar.LCEIL)
                self.state = 589
                self.a_expr(0)
                self.state = 590
                self.match(ExprGrammar.RCEIL)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 6)
                self.state = 592
                self.match(ExprGrammar.LANGLE)
                self.state = 593
                self.a_expr(0)
                self.state = 594
                _la = self._input.LA(1)
                if not(_la==37 or _la==59):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 595
                self.a_expr(0)
                self.state = 596
                self.match(ExprGrammar.RANGLE)
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
            self.res = None
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
        self.enterRule(localctx, 52, self.RULE_combinatorial)
        self._la = 0 # Token type
        try:
            self.state = 624
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 600
                self.match(ExprGrammar.LBRACE)
                self.state = 601
                _la = self._input.LA(1)
                if not(_la==11 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 602
                localctx.n = self.a_expr(0)
                self.state = 603
                localctx.op = self.match(ExprGrammar.ID)
                self.state = 604
                if not ((None if localctx.op is None else localctx.op.text) in Ast.CombOpId):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "($op.text in Ast.CombOpId)")
                self.state = 605
                self.match(ExprGrammar.POW)
                self.state = 606
                localctx.k = self.a_expr(0)
                self.state = 607
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.combOpFromId(localctx, localctx.n.res, localctx.k.res, Ast.CombOpId((None if localctx.op is None else localctx.op.text)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 610
                self.match(ExprGrammar.LBRACE)
                self.state = 611
                localctx._ID = self.match(ExprGrammar.ID)
                self.state = 612
                if not (None if localctx._ID is None else localctx._ID.text) == 'D':
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$ID.text == 'D'")
                self.state = 613
                self.match(ExprGrammar.POW)
                self.state = 614
                localctx.n = self.a_expr(0)
                self.state = 615
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Derangements(localctx, localctx.n.res)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 618
                self.match(ExprGrammar.LBRACE)
                self.state = 619
                self.match(ExprGrammar.BANG)
                self.state = 620
                localctx.n = self.a_expr(0)
                self.state = 621
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
            self.res = None
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
        self.enterRule(localctx, 54, self.RULE_cmd_func)
        self._la = 0 # Token type
        try:
            self.state = 658
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 626
                self.match(ExprGrammar.FRAC)
                self.state = 627
                localctx.num = self.latex_cmd_arg()
                self.state = 628
                localctx.den = self.latex_cmd_arg()
                localctx.res = Ast.DivOp(localctx, localctx.num.res, localctx.den.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 631
                self.match(ExprGrammar.BINOM)
                self.state = 632
                localctx.n = self.latex_cmd_arg()
                self.state = 633
                localctx.k = self.latex_cmd_arg()
                localctx.res = Ast.Binom(localctx, localctx.n.res, localctx.k.res)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 636
                self.match(ExprGrammar.SQRT)
                self.state = 637
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Root(localctx, localctx._latex_cmd_arg.res, None) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 640
                self.match(ExprGrammar.SQRT)
                self.state = 645
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 641
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 642
                    localctx.root_index = self.a_expr(0)
                    self.state = 643
                    self.match(ExprGrammar.RBRACKET)


                self.state = 647
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Root(localctx, localctx._latex_cmd_arg.res, localctx.root_index.res)
                		
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 650
                self.match(ExprGrammar.CONJUGATE)
                self.state = 651
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Conjugate(localctx, localctx._latex_cmd_arg.res)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 654
                self.match(ExprGrammar.VEC_UNIT)
                self.state = 655
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
            self.res = None
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
        self.enterRule(localctx, 56, self.RULE_matrix_row)
        self._la = 0 # Token type
        try:
            self.state = 672
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63, 65, 67, 71]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1, 3, 6, 7, 20, 21, 22, 23, 24, 26, 28, 29, 30, 32, 33, 43, 45, 49, 53, 55, 57, 59, 60, 62, 64, 66, 73, 77, 78, 79]:
                self.enterOuterAlt(localctx, 2)
                self.state = 661
                localctx._a_expr = self.a_expr(0)
                localctx.res = [localctx._a_expr.res]
                self.state = 669
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==70:
                    self.state = 663
                    self.match(ExprGrammar.ENV_EL_SEP)
                    self.state = 664
                    localctx._a_expr = self.a_expr(0)
                    localctx.res.append(localctx._a_expr.res)
                    self.state = 671
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
            self.res = []
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
        self.enterRule(localctx, 58, self.RULE_matrix_body)
        self._la = 0 # Token type
        try:
            self.state = 692
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 675
                localctx._matrix_row = self.matrix_row()
                localctx.res = [localctx._matrix_row.res]
                self.state = 683
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 677
                        self.match(ExprGrammar.ENV_ROW_SEP)
                        self.state = 678
                        localctx._matrix_row = self.matrix_row()
                        localctx.res.append(localctx._matrix_row.res) 
                    self.state = 685
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

                self.state = 689
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==71:
                    self.state = 686
                    self.match(ExprGrammar.ENV_ROW_SEP)
                    self.state = 691
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
            self.res = None
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
        self.enterRule(localctx, 60, self.RULE_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 702
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
                self.state = 694
                localctx.beg = self.match(ExprGrammar.BEGIN_MATRIX)
                self.state = 695
                localctx._matrix_body = self.matrix_body()
                self.state = 696
                localctx.end = self.match(ExprGrammar.END_MATRIX)
                pass
            elif token in [66]:
                self.state = 698
                localctx.beg = self.match(ExprGrammar.BEGIN_ARRAY)
                self.state = 699
                localctx._matrix_body = self.matrix_body()
                self.state = 700
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
            self.res = None

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
        self.enterRule(localctx, 62, self.RULE_det_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(ExprGrammar.BEGIN_V_MATRIX)
            self.state = 707
            self.matrix_body()
            self.state = 708
            self.match(ExprGrammar.END_V_MATRIX)
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
        self._predicates[26] = self.combinatorial_sempred
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
                return self.precpred(self._ctx, 32)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 8)
         

    def combinatorial_sempred(self, localctx:CombinatorialContext, predIndex:int):
            if predIndex == 9:
                return ((None if localctx.op is None else localctx.op.text) in Ast.CombOpId)
         

            if predIndex == 10:
                return (None if localctx._ID is None else localctx._ID.text) == 'D'
         





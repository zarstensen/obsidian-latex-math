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
        4,1,89,810,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,83,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,93,8,2,1,3,1,3,1,3,
        1,3,1,3,1,3,5,3,101,8,3,10,3,12,3,104,9,3,1,3,5,3,107,8,3,10,3,12,
        3,110,9,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,4,5,123,8,
        5,11,5,12,5,124,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,135,8,6,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,149,8,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,161,8,8,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,3,9,186,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,3,9,202,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,3,9,215,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,
        228,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        3,9,244,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,268,8,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,3,9,280,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,3,9,290,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,334,
        8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,349,
        8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,364,
        8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,393,8,9,1,9,
        1,9,1,9,1,9,1,9,1,9,5,9,401,8,9,10,9,12,9,404,9,9,1,10,1,10,1,10,
        1,10,1,10,3,10,411,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        3,11,421,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,3,12,434,8,12,1,13,3,13,437,8,13,1,13,1,13,3,13,441,8,13,1,
        13,3,13,444,8,13,1,13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,3,15,460,8,15,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,3,16,471,8,16,1,16,1,16,1,16,1,16,3,16,477,8,16,
        1,16,1,16,1,16,4,16,482,8,16,11,16,12,16,483,1,16,1,16,3,16,488,
        8,16,1,16,1,16,1,16,3,16,493,8,16,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,508,8,17,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,520,8,18,1,19,4,19,523,8,
        19,11,19,12,19,524,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,3,20,539,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        3,21,561,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        5,22,573,8,22,10,22,12,22,576,9,22,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,604,8,23,1,24,1,24,1,24,
        1,24,3,24,610,8,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,
        1,26,3,26,622,8,26,1,27,1,27,3,27,626,8,27,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,5,27,635,8,27,10,27,12,27,638,9,27,3,27,640,8,27,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,654,
        8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,
        693,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,713,8,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,3,29,723,8,29,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,3,30,744,8,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,3,30,757,8,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,5,31,
        766,8,31,10,31,12,31,769,9,31,3,31,771,8,31,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,5,32,780,8,32,10,32,12,32,783,9,32,1,32,5,32,786,
        8,32,10,32,12,32,789,9,32,3,32,791,8,32,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,3,33,801,8,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,
        1,34,0,1,18,35,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,0,5,1,0,36,37,
        2,0,16,16,49,49,1,0,14,15,2,0,45,45,67,67,2,0,19,19,46,46,887,0,
        70,1,0,0,0,2,82,1,0,0,0,4,92,1,0,0,0,6,94,1,0,0,0,8,111,1,0,0,0,
        10,116,1,0,0,0,12,134,1,0,0,0,14,148,1,0,0,0,16,160,1,0,0,0,18,333,
        1,0,0,0,20,410,1,0,0,0,22,420,1,0,0,0,24,433,1,0,0,0,26,436,1,0,
        0,0,28,447,1,0,0,0,30,459,1,0,0,0,32,492,1,0,0,0,34,507,1,0,0,0,
        36,519,1,0,0,0,38,522,1,0,0,0,40,538,1,0,0,0,42,560,1,0,0,0,44,562,
        1,0,0,0,46,603,1,0,0,0,48,609,1,0,0,0,50,611,1,0,0,0,52,621,1,0,
        0,0,54,653,1,0,0,0,56,692,1,0,0,0,58,722,1,0,0,0,60,756,1,0,0,0,
        62,770,1,0,0,0,64,790,1,0,0,0,66,800,1,0,0,0,68,804,1,0,0,0,70,71,
        3,2,1,0,71,72,6,0,-1,0,72,1,1,0,0,0,73,74,3,18,9,0,74,75,6,1,-1,
        0,75,83,1,0,0,0,76,77,3,16,8,0,77,78,6,1,-1,0,78,83,1,0,0,0,79,80,
        3,12,6,0,80,81,6,1,-1,0,81,83,1,0,0,0,82,73,1,0,0,0,82,76,1,0,0,
        0,82,79,1,0,0,0,83,84,1,0,0,0,84,85,5,0,0,1,85,3,1,0,0,0,86,87,3,
        18,9,0,87,88,6,2,-1,0,88,93,1,0,0,0,89,90,3,16,8,0,90,91,6,2,-1,
        0,91,93,1,0,0,0,92,86,1,0,0,0,92,89,1,0,0,0,93,5,1,0,0,0,94,95,3,
        4,2,0,95,102,6,3,-1,0,96,97,5,79,0,0,97,98,3,4,2,0,98,99,6,3,-1,
        0,99,101,1,0,0,0,100,96,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,
        102,103,1,0,0,0,103,108,1,0,0,0,104,102,1,0,0,0,105,107,5,79,0,0,
        106,105,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,
        109,7,1,0,0,0,110,108,1,0,0,0,111,112,5,76,0,0,112,113,3,6,3,0,113,
        114,6,4,-1,0,114,115,5,77,0,0,115,9,1,0,0,0,116,117,3,4,2,0,117,
        122,6,5,-1,0,118,119,5,7,0,0,119,120,3,4,2,0,120,121,6,5,-1,0,121,
        123,1,0,0,0,122,118,1,0,0,0,123,124,1,0,0,0,124,122,1,0,0,0,124,
        125,1,0,0,0,125,126,1,0,0,0,126,127,6,5,-1,0,127,11,1,0,0,0,128,
        129,3,8,4,0,129,130,6,6,-1,0,130,135,1,0,0,0,131,132,3,10,5,0,132,
        133,6,6,-1,0,133,135,1,0,0,0,134,128,1,0,0,0,134,131,1,0,0,0,135,
        13,1,0,0,0,136,137,5,20,0,0,137,149,6,7,-1,0,138,139,5,21,0,0,139,
        149,6,7,-1,0,140,141,5,22,0,0,141,149,6,7,-1,0,142,143,5,23,0,0,
        143,149,6,7,-1,0,144,145,5,24,0,0,145,149,6,7,-1,0,146,147,5,25,
        0,0,147,149,6,7,-1,0,148,136,1,0,0,0,148,138,1,0,0,0,148,140,1,0,
        0,0,148,142,1,0,0,0,148,144,1,0,0,0,148,146,1,0,0,0,149,15,1,0,0,
        0,150,151,3,18,9,0,151,152,3,14,7,0,152,153,3,16,8,0,153,154,6,8,
        -1,0,154,161,1,0,0,0,155,156,3,18,9,0,156,157,3,14,7,0,157,158,3,
        18,9,0,158,159,6,8,-1,0,159,161,1,0,0,0,160,150,1,0,0,0,160,155,
        1,0,0,0,161,17,1,0,0,0,162,163,6,9,-1,0,163,164,5,34,0,0,164,165,
        3,34,17,0,165,166,5,28,0,0,166,167,5,51,0,0,167,168,5,35,0,0,168,
        169,3,18,9,0,169,170,5,52,0,0,170,171,3,22,11,0,171,172,6,9,-1,0,
        172,334,1,0,0,0,173,174,5,34,0,0,174,175,3,34,17,0,175,176,3,18,
        9,0,176,177,5,35,0,0,177,178,3,18,9,25,178,179,6,9,-1,0,179,334,
        1,0,0,0,180,185,5,37,0,0,181,182,5,57,0,0,182,183,3,18,9,0,183,184,
        5,58,0,0,184,186,1,0,0,0,185,181,1,0,0,0,185,186,1,0,0,0,186,187,
        1,0,0,0,187,188,3,22,11,0,188,189,5,51,0,0,189,190,3,18,9,0,190,
        191,5,52,0,0,191,192,5,51,0,0,192,193,3,18,9,0,193,194,5,52,0,0,
        194,195,6,9,-1,0,195,334,1,0,0,0,196,201,7,0,0,0,197,198,5,57,0,
        0,198,199,3,18,9,0,199,200,5,58,0,0,200,202,1,0,0,0,201,197,1,0,
        0,0,201,202,1,0,0,0,202,203,1,0,0,0,203,204,3,22,11,0,204,205,5,
        51,0,0,205,206,3,18,9,0,206,207,5,52,0,0,207,208,6,9,-1,0,208,334,
        1,0,0,0,209,214,7,0,0,0,210,211,5,57,0,0,211,212,3,18,9,0,212,213,
        5,58,0,0,213,215,1,0,0,0,214,210,1,0,0,0,214,215,1,0,0,0,215,216,
        1,0,0,0,216,217,3,22,11,0,217,218,3,18,9,21,218,219,6,9,-1,0,219,
        334,1,0,0,0,220,221,5,28,0,0,221,222,5,51,0,0,222,227,5,35,0,0,223,
        224,5,57,0,0,224,225,3,18,9,0,225,226,5,58,0,0,226,228,1,0,0,0,227,
        223,1,0,0,0,227,228,1,0,0,0,228,229,1,0,0,0,229,230,3,18,9,0,230,
        231,5,52,0,0,231,232,5,51,0,0,232,233,3,38,19,0,233,234,5,52,0,0,
        234,235,6,9,-1,0,235,334,1,0,0,0,236,237,5,28,0,0,237,238,5,51,0,
        0,238,243,5,35,0,0,239,240,5,57,0,0,240,241,3,18,9,0,241,242,5,58,
        0,0,242,244,1,0,0,0,243,239,1,0,0,0,243,244,1,0,0,0,244,245,1,0,
        0,0,245,246,5,52,0,0,246,247,5,51,0,0,247,248,3,38,19,0,248,249,
        5,52,0,0,249,250,3,18,9,19,250,251,6,9,-1,0,251,334,1,0,0,0,252,
        253,5,38,0,0,253,254,5,46,0,0,254,255,5,51,0,0,255,256,3,52,26,0,
        256,257,5,39,0,0,257,258,3,18,9,0,258,259,3,40,20,0,259,260,5,52,
        0,0,260,261,3,18,9,18,261,262,6,9,-1,0,262,334,1,0,0,0,263,264,5,
        40,0,0,264,268,6,9,-1,0,265,266,5,41,0,0,266,268,6,9,-1,0,267,263,
        1,0,0,0,267,265,1,0,0,0,268,269,1,0,0,0,269,270,3,42,21,0,270,271,
        5,53,0,0,271,272,3,18,9,0,272,273,5,54,0,0,273,274,6,9,-1,0,274,
        334,1,0,0,0,275,276,5,40,0,0,276,280,6,9,-1,0,277,278,5,41,0,0,278,
        280,6,9,-1,0,279,275,1,0,0,0,279,277,1,0,0,0,280,281,1,0,0,0,281,
        282,3,42,21,0,282,283,3,18,9,14,283,284,6,9,-1,0,284,334,1,0,0,0,
        285,286,5,14,0,0,286,290,6,9,-1,0,287,288,5,15,0,0,288,290,6,9,-1,
        0,289,285,1,0,0,0,289,287,1,0,0,0,290,291,1,0,0,0,291,292,3,18,9,
        12,292,293,6,9,-1,0,293,334,1,0,0,0,294,295,5,53,0,0,295,296,3,18,
        9,0,296,297,5,54,0,0,297,298,5,67,0,0,298,299,3,46,23,0,299,300,
        6,9,-1,0,300,334,1,0,0,0,301,302,5,3,0,0,302,303,3,18,9,0,303,304,
        5,67,0,0,304,305,3,46,23,0,305,306,6,9,-1,0,306,334,1,0,0,0,307,
        308,5,57,0,0,308,309,3,18,9,0,309,310,5,58,0,0,310,311,3,46,23,0,
        311,312,6,9,-1,0,312,334,1,0,0,0,313,314,3,58,29,0,314,315,6,9,-1,
        0,315,334,1,0,0,0,316,317,3,56,28,0,317,318,6,9,-1,0,318,334,1,0,
        0,0,319,320,3,60,30,0,320,321,6,9,-1,0,321,334,1,0,0,0,322,323,3,
        66,33,0,323,324,6,9,-1,0,324,334,1,0,0,0,325,326,3,68,34,0,326,327,
        6,9,-1,0,327,334,1,0,0,0,328,329,3,52,26,0,329,330,6,9,-1,0,330,
        334,1,0,0,0,331,332,5,81,0,0,332,334,6,9,-1,0,333,162,1,0,0,0,333,
        173,1,0,0,0,333,180,1,0,0,0,333,196,1,0,0,0,333,209,1,0,0,0,333,
        220,1,0,0,0,333,236,1,0,0,0,333,252,1,0,0,0,333,267,1,0,0,0,333,
        279,1,0,0,0,333,289,1,0,0,0,333,294,1,0,0,0,333,301,1,0,0,0,333,
        307,1,0,0,0,333,313,1,0,0,0,333,316,1,0,0,0,333,319,1,0,0,0,333,
        322,1,0,0,0,333,325,1,0,0,0,333,328,1,0,0,0,333,331,1,0,0,0,334,
        402,1,0,0,0,335,348,10,17,0,0,336,337,5,16,0,0,337,349,6,9,-1,0,
        338,339,5,27,0,0,339,349,6,9,-1,0,340,341,5,17,0,0,341,349,6,9,-1,
        0,342,343,5,33,0,0,343,349,6,9,-1,0,344,345,5,26,0,0,345,349,6,9,
        -1,0,346,347,5,18,0,0,347,349,6,9,-1,0,348,336,1,0,0,0,348,338,1,
        0,0,0,348,340,1,0,0,0,348,342,1,0,0,0,348,344,1,0,0,0,348,346,1,
        0,0,0,349,350,1,0,0,0,350,351,3,18,9,18,351,352,6,9,-1,0,352,401,
        1,0,0,0,353,354,10,16,0,0,354,355,4,9,2,0,355,356,3,18,9,17,356,
        357,6,9,-1,0,357,401,1,0,0,0,358,363,10,13,0,0,359,360,5,14,0,0,
        360,364,6,9,-1,0,361,362,5,15,0,0,362,364,6,9,-1,0,363,359,1,0,0,
        0,363,361,1,0,0,0,364,365,1,0,0,0,365,366,3,18,9,14,366,367,6,9,
        -1,0,367,401,1,0,0,0,368,369,10,29,0,0,369,370,5,19,0,0,370,371,
        3,24,12,0,371,372,5,46,0,0,372,373,3,32,16,0,373,374,6,9,-1,0,374,
        401,1,0,0,0,375,376,10,28,0,0,376,377,5,19,0,0,377,378,3,24,12,0,
        378,379,6,9,-1,0,379,401,1,0,0,0,380,381,10,27,0,0,381,382,5,46,
        0,0,382,383,3,32,16,0,383,384,6,9,-1,0,384,401,1,0,0,0,385,392,10,
        24,0,0,386,387,5,42,0,0,387,393,6,9,-1,0,388,389,5,43,0,0,389,393,
        6,9,-1,0,390,391,5,44,0,0,391,393,6,9,-1,0,392,386,1,0,0,0,392,388,
        1,0,0,0,392,390,1,0,0,0,393,394,1,0,0,0,394,401,6,9,-1,0,395,396,
        10,8,0,0,396,397,5,67,0,0,397,398,3,46,23,0,398,399,6,9,-1,0,399,
        401,1,0,0,0,400,335,1,0,0,0,400,353,1,0,0,0,400,358,1,0,0,0,400,
        368,1,0,0,0,400,375,1,0,0,0,400,380,1,0,0,0,400,385,1,0,0,0,400,
        395,1,0,0,0,401,404,1,0,0,0,402,400,1,0,0,0,402,403,1,0,0,0,403,
        19,1,0,0,0,404,402,1,0,0,0,405,406,3,48,24,0,406,407,6,10,-1,0,407,
        411,1,0,0,0,408,409,5,81,0,0,409,411,6,10,-1,0,410,405,1,0,0,0,410,
        408,1,0,0,0,411,21,1,0,0,0,412,413,3,20,10,0,413,414,6,11,-1,0,414,
        421,1,0,0,0,415,416,5,51,0,0,416,417,3,18,9,0,417,418,5,52,0,0,418,
        419,6,11,-1,0,419,421,1,0,0,0,420,412,1,0,0,0,420,415,1,0,0,0,421,
        23,1,0,0,0,422,423,3,20,10,0,423,424,6,12,-1,0,424,434,1,0,0,0,425,
        426,3,60,30,0,426,427,6,12,-1,0,427,434,1,0,0,0,428,429,5,51,0,0,
        429,430,3,18,9,0,430,431,5,52,0,0,431,432,6,12,-1,0,432,434,1,0,
        0,0,433,422,1,0,0,0,433,425,1,0,0,0,433,428,1,0,0,0,434,25,1,0,0,
        0,435,437,3,18,9,0,436,435,1,0,0,0,436,437,1,0,0,0,437,440,1,0,0,
        0,438,441,5,48,0,0,439,441,5,50,0,0,440,438,1,0,0,0,440,439,1,0,
        0,0,441,443,1,0,0,0,442,444,3,18,9,0,443,442,1,0,0,0,443,444,1,0,
        0,0,444,445,1,0,0,0,445,446,6,13,-1,0,446,27,1,0,0,0,447,448,7,1,
        0,0,448,29,1,0,0,0,449,450,3,18,9,0,450,451,6,15,-1,0,451,460,1,
        0,0,0,452,453,3,26,13,0,453,454,6,15,-1,0,454,460,1,0,0,0,455,456,
        3,28,14,0,456,457,6,15,-1,0,457,460,1,0,0,0,458,460,6,15,-1,0,459,
        449,1,0,0,0,459,452,1,0,0,0,459,455,1,0,0,0,459,458,1,0,0,0,460,
        31,1,0,0,0,461,462,3,20,10,0,462,463,6,16,-1,0,463,493,1,0,0,0,464,
        465,3,60,30,0,465,466,6,16,-1,0,466,493,1,0,0,0,467,470,5,51,0,0,
        468,471,5,57,0,0,469,471,5,53,0,0,470,468,1,0,0,0,470,469,1,0,0,
        0,470,471,1,0,0,0,471,472,1,0,0,0,472,473,3,30,15,0,473,481,6,16,
        -1,0,474,477,5,45,0,0,475,477,5,47,0,0,476,474,1,0,0,0,476,475,1,
        0,0,0,477,478,1,0,0,0,478,479,3,30,15,0,479,480,6,16,-1,0,480,482,
        1,0,0,0,481,476,1,0,0,0,482,483,1,0,0,0,483,481,1,0,0,0,483,484,
        1,0,0,0,484,487,1,0,0,0,485,488,5,57,0,0,486,488,5,53,0,0,487,485,
        1,0,0,0,487,486,1,0,0,0,487,488,1,0,0,0,488,489,1,0,0,0,489,490,
        5,52,0,0,490,491,6,16,-1,0,491,493,1,0,0,0,492,461,1,0,0,0,492,464,
        1,0,0,0,492,467,1,0,0,0,493,33,1,0,0,0,494,495,5,19,0,0,495,496,
        3,22,11,0,496,497,5,46,0,0,497,498,3,22,11,0,498,499,6,17,-1,0,499,
        508,1,0,0,0,500,501,5,46,0,0,501,502,3,22,11,0,502,503,5,19,0,0,
        503,504,3,22,11,0,504,505,6,17,-1,0,505,508,1,0,0,0,506,508,6,17,
        -1,0,507,494,1,0,0,0,507,500,1,0,0,0,507,506,1,0,0,0,508,35,1,0,
        0,0,509,510,5,35,0,0,510,511,3,18,9,0,511,512,5,19,0,0,512,513,3,
        22,11,0,513,514,6,18,-1,0,514,520,1,0,0,0,515,516,5,35,0,0,516,517,
        3,18,9,0,517,518,6,18,-1,0,518,520,1,0,0,0,519,509,1,0,0,0,519,515,
        1,0,0,0,520,37,1,0,0,0,521,523,3,36,18,0,522,521,1,0,0,0,523,524,
        1,0,0,0,524,522,1,0,0,0,524,525,1,0,0,0,525,39,1,0,0,0,526,539,6,
        20,-1,0,527,528,5,19,0,0,528,529,5,51,0,0,529,530,7,2,0,0,530,531,
        5,52,0,0,531,539,6,20,-1,0,532,533,5,19,0,0,533,534,5,14,0,0,534,
        539,6,20,-1,0,535,536,5,19,0,0,536,537,5,15,0,0,537,539,6,20,-1,
        0,538,526,1,0,0,0,538,527,1,0,0,0,538,532,1,0,0,0,538,535,1,0,0,
        0,539,41,1,0,0,0,540,541,5,46,0,0,541,542,5,51,0,0,542,543,3,18,
        9,0,543,544,5,20,0,0,544,545,3,18,9,0,545,546,5,52,0,0,546,547,5,
        19,0,0,547,548,3,24,12,0,548,549,6,21,-1,0,549,561,1,0,0,0,550,551,
        5,19,0,0,551,552,3,24,12,0,552,553,5,46,0,0,553,554,5,51,0,0,554,
        555,3,18,9,0,555,556,5,20,0,0,556,557,3,18,9,0,557,558,5,52,0,0,
        558,559,6,21,-1,0,559,561,1,0,0,0,560,540,1,0,0,0,560,550,1,0,0,
        0,561,43,1,0,0,0,562,563,3,18,9,0,563,564,5,20,0,0,564,565,3,18,
        9,0,565,574,6,22,-1,0,566,567,5,45,0,0,567,568,3,18,9,0,568,569,
        5,20,0,0,569,570,3,18,9,0,570,571,6,22,-1,0,571,573,1,0,0,0,572,
        566,1,0,0,0,573,576,1,0,0,0,574,572,1,0,0,0,574,575,1,0,0,0,575,
        45,1,0,0,0,576,574,1,0,0,0,577,578,5,46,0,0,578,579,5,51,0,0,579,
        580,3,44,22,0,580,581,5,52,0,0,581,582,6,23,-1,0,582,604,1,0,0,0,
        583,584,5,46,0,0,584,585,5,51,0,0,585,586,3,44,22,0,586,587,5,52,
        0,0,587,588,5,19,0,0,588,589,5,51,0,0,589,590,3,44,22,0,590,591,
        5,52,0,0,591,592,6,23,-1,0,592,604,1,0,0,0,593,594,5,19,0,0,594,
        595,5,51,0,0,595,596,3,44,22,0,596,597,5,52,0,0,597,598,5,46,0,0,
        598,599,5,51,0,0,599,600,3,44,22,0,600,601,5,52,0,0,601,602,6,23,
        -1,0,602,604,1,0,0,0,603,577,1,0,0,0,603,583,1,0,0,0,603,593,1,0,
        0,0,604,47,1,0,0,0,605,606,5,86,0,0,606,610,6,24,-1,0,607,608,5,
        87,0,0,608,610,6,24,-1,0,609,605,1,0,0,0,609,607,1,0,0,0,610,49,
        1,0,0,0,611,612,5,85,0,0,612,613,3,48,24,0,613,614,6,25,-1,0,614,
        51,1,0,0,0,615,616,3,48,24,0,616,617,6,26,-1,0,617,622,1,0,0,0,618,
        619,3,50,25,0,619,620,6,26,-1,0,620,622,1,0,0,0,621,615,1,0,0,0,
        621,618,1,0,0,0,622,53,1,0,0,0,623,626,5,1,0,0,624,626,5,2,0,0,625,
        623,1,0,0,0,625,624,1,0,0,0,626,627,1,0,0,0,627,639,5,53,0,0,628,
        629,3,18,9,0,629,636,6,27,-1,0,630,631,5,45,0,0,631,632,3,18,9,0,
        632,633,6,27,-1,0,633,635,1,0,0,0,634,630,1,0,0,0,635,638,1,0,0,
        0,636,634,1,0,0,0,636,637,1,0,0,0,637,640,1,0,0,0,638,636,1,0,0,
        0,639,628,1,0,0,0,639,640,1,0,0,0,640,641,1,0,0,0,641,642,5,54,0,
        0,642,654,6,27,-1,0,643,644,5,2,0,0,644,645,5,51,0,0,645,646,3,18,
        9,0,646,647,5,52,0,0,647,648,6,27,-1,0,648,654,1,0,0,0,649,650,5,
        2,0,0,650,651,3,18,9,0,651,652,6,27,-1,0,652,654,1,0,0,0,653,625,
        1,0,0,0,653,643,1,0,0,0,653,649,1,0,0,0,654,55,1,0,0,0,655,656,5,
        53,0,0,656,657,3,18,9,0,657,658,5,54,0,0,658,659,6,28,-1,0,659,693,
        1,0,0,0,660,661,5,57,0,0,661,662,3,18,9,0,662,663,5,58,0,0,663,664,
        6,28,-1,0,664,693,1,0,0,0,665,666,5,67,0,0,666,667,3,18,9,0,667,
        668,5,67,0,0,668,669,6,28,-1,0,669,693,1,0,0,0,670,671,5,68,0,0,
        671,672,3,18,9,0,672,673,5,68,0,0,673,674,6,28,-1,0,674,693,1,0,
        0,0,675,676,5,63,0,0,676,677,3,18,9,0,677,678,5,64,0,0,678,679,6,
        28,-1,0,679,693,1,0,0,0,680,681,5,61,0,0,681,682,3,18,9,0,682,683,
        5,62,0,0,683,684,6,28,-1,0,684,693,1,0,0,0,685,686,5,65,0,0,686,
        687,3,18,9,0,687,688,7,3,0,0,688,689,3,18,9,0,689,690,5,66,0,0,690,
        691,6,28,-1,0,691,693,1,0,0,0,692,655,1,0,0,0,692,660,1,0,0,0,692,
        665,1,0,0,0,692,670,1,0,0,0,692,675,1,0,0,0,692,680,1,0,0,0,692,
        685,1,0,0,0,693,57,1,0,0,0,694,695,5,51,0,0,695,696,7,4,0,0,696,
        697,3,18,9,0,697,698,5,86,0,0,698,699,4,29,9,1,699,700,4,29,10,1,
        700,701,5,19,0,0,701,702,3,18,9,0,702,703,5,52,0,0,703,704,6,29,
        -1,0,704,713,1,0,0,0,705,706,5,51,0,0,706,707,5,86,0,0,707,708,4,
        29,11,1,708,709,5,19,0,0,709,710,3,18,9,0,710,711,5,52,0,0,711,713,
        1,0,0,0,712,694,1,0,0,0,712,705,1,0,0,0,713,714,1,0,0,0,714,715,
        6,29,-1,0,715,723,1,0,0,0,716,717,5,51,0,0,717,718,5,42,0,0,718,
        719,3,18,9,0,719,720,5,52,0,0,720,721,6,29,-1,0,721,723,1,0,0,0,
        722,712,1,0,0,0,722,716,1,0,0,0,723,59,1,0,0,0,724,725,5,28,0,0,
        725,726,3,22,11,0,726,727,3,22,11,0,727,728,6,30,-1,0,728,757,1,
        0,0,0,729,730,5,29,0,0,730,731,3,22,11,0,731,732,3,22,11,0,732,733,
        6,30,-1,0,733,757,1,0,0,0,734,735,5,30,0,0,735,736,3,22,11,0,736,
        737,6,30,-1,0,737,757,1,0,0,0,738,743,5,30,0,0,739,740,5,57,0,0,
        740,741,3,18,9,0,741,742,5,58,0,0,742,744,1,0,0,0,743,739,1,0,0,
        0,743,744,1,0,0,0,744,745,1,0,0,0,745,746,3,22,11,0,746,747,6,30,
        -1,0,747,757,1,0,0,0,748,749,5,31,0,0,749,750,3,22,11,0,750,751,
        6,30,-1,0,751,757,1,0,0,0,752,753,5,32,0,0,753,754,3,22,11,0,754,
        755,6,30,-1,0,755,757,1,0,0,0,756,724,1,0,0,0,756,729,1,0,0,0,756,
        734,1,0,0,0,756,738,1,0,0,0,756,748,1,0,0,0,756,752,1,0,0,0,757,
        61,1,0,0,0,758,771,1,0,0,0,759,760,3,18,9,0,760,767,6,31,-1,0,761,
        762,5,78,0,0,762,763,3,18,9,0,763,764,6,31,-1,0,764,766,1,0,0,0,
        765,761,1,0,0,0,766,769,1,0,0,0,767,765,1,0,0,0,767,768,1,0,0,0,
        768,771,1,0,0,0,769,767,1,0,0,0,770,758,1,0,0,0,770,759,1,0,0,0,
        771,63,1,0,0,0,772,791,1,0,0,0,773,774,3,62,31,0,774,781,6,32,-1,
        0,775,776,5,79,0,0,776,777,3,62,31,0,777,778,6,32,-1,0,778,780,1,
        0,0,0,779,775,1,0,0,0,780,783,1,0,0,0,781,779,1,0,0,0,781,782,1,
        0,0,0,782,787,1,0,0,0,783,781,1,0,0,0,784,786,5,79,0,0,785,784,1,
        0,0,0,786,789,1,0,0,0,787,785,1,0,0,0,787,788,1,0,0,0,788,791,1,
        0,0,0,789,787,1,0,0,0,790,772,1,0,0,0,790,773,1,0,0,0,791,65,1,0,
        0,0,792,793,5,70,0,0,793,794,3,64,32,0,794,795,5,71,0,0,795,801,
        1,0,0,0,796,797,5,74,0,0,797,798,3,64,32,0,798,799,5,75,0,0,799,
        801,1,0,0,0,800,792,1,0,0,0,800,796,1,0,0,0,801,802,1,0,0,0,802,
        803,6,33,-1,0,803,67,1,0,0,0,804,805,5,72,0,0,805,806,3,64,32,0,
        806,807,5,73,0,0,807,808,6,34,-1,0,808,69,1,0,0,0,58,82,92,102,108,
        124,134,148,160,185,201,214,227,243,267,279,289,333,348,363,392,
        400,402,410,420,433,436,440,443,459,470,476,483,487,492,507,519,
        524,538,560,574,603,609,621,625,636,639,653,692,712,722,743,756,
        767,770,781,787,790,800
    ]

class ExprGrammar ( Parser ):

    grammarFileName = "ExprGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\not'", "'\\equiv'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'^'", "'='", "<INVALID>", 
                     "'<'", "<INVALID>", "'>'", "<INVALID>", "'\\times'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\sqrt'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\lim'", "<INVALID>", 
                     "'\\sum'", "'\\prod'", "'!'", "'\\%'", "'\\textperthousand'", 
                     "','", "'_'", "';'", "':'", "'\\star'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'&'", "'\\\\'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\Delta'" ]

    symbolicNames = [ "<INVALID>", "FUNC_ID", "FUNC_CMD", "LBLANK", "RBLANK", 
                      "IGNORE", "NAND", "AND", "NOR", "OR", "XOR", "XNOR", 
                      "NOT", "EQUIV", "PLUS", "MINUS", "MULT", "DIV", "XPROD", 
                      "POW", "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "TIMES", 
                      "DOT_PROD", "FRAC", "BINOM", "SQRT", "CONJUGATE", 
                      "VEC_UNIT", "MOD", "INT", "DIFFERENTIAL", "PHYS_DERIVATIVE", 
                      "PHYS_PARTIAL_DERIVATIVE", "LIMIT", "LIMIT_ARROW", 
                      "SUM", "PRODUCT", "BANG", "PERCENT", "PERMILLE", "COMMA", 
                      "UNDERSCORE", "SEMICOLON", "COLON", "STAR", "DOTS", 
                      "LBRACE", "RBRACE", "LPAREN", "RPAREN", "LBRACE_LITERAL", 
                      "RBRACE_LITERAL", "LBRACKET", "RBRACKET", "LBRACK_CMD", 
                      "RBRACK_CMD", "LCEIL", "RCEIL", "LFLOOR", "RFLOOR", 
                      "LANGLE", "RANGLE", "PIPE", "DOUBLE_PIPE", "DOT", 
                      "BEGIN_MATRIX", "END_MATRIX", "BEGIN_V_MATRIX", "END_V_MATRIX", 
                      "BEGIN_ARRAY", "END_ARRAY", "BEGIN_ENV", "END_ENV", 
                      "ENV_EL_SEP", "ENV_ROW_SEP", "ENV_SEP_SKIP", "NUMBER", 
                      "BIN_NUMBER", "OCT_NUMBER", "HEX_NUMBER", "DELTA", 
                      "ID", "COMMAND", "ARG_COMM", "ARG_WS" ]

    RULE_debug = 0
    RULE_alg_statement = 1
    RULE_system_el = 2
    RULE_system_body = 3
    RULE_system_env = 4
    RULE_system_and_chain = 5
    RULE_system = 6
    RULE_rel_op = 7
    RULE_relation = 8
    RULE_a_expr = 9
    RULE_atom = 10
    RULE_latex_cmd_arg = 11
    RULE_pow_arg = 12
    RULE_range_slot = 13
    RULE_all_slot = 14
    RULE_slot_entry = 15
    RULE_subscript_arg = 16
    RULE_int_bounds = 17
    RULE_diff_var = 18
    RULE_diff_vars = 19
    RULE_limit_dir = 20
    RULE_series_range_args = 21
    RULE_eval_at_sub_vars = 22
    RULE_eval_at_arg = 23
    RULE_primary_symbol = 24
    RULE_delta_symbol = 25
    RULE_symbol = 26
    RULE_function = 27
    RULE_delim_expr = 28
    RULE_combinatorial = 29
    RULE_cmd_func = 30
    RULE_matrix_row = 31
    RULE_matrix_body = 32
    RULE_matrix = 33
    RULE_det_matrix = 34

    ruleNames =  [ "debug", "alg_statement", "system_el", "system_body", 
                   "system_env", "system_and_chain", "system", "rel_op", 
                   "relation", "a_expr", "atom", "latex_cmd_arg", "pow_arg", 
                   "range_slot", "all_slot", "slot_entry", "subscript_arg", 
                   "int_bounds", "diff_var", "diff_vars", "limit_dir", "series_range_args", 
                   "eval_at_sub_vars", "eval_at_arg", "primary_symbol", 
                   "delta_symbol", "symbol", "function", "delim_expr", "combinatorial", 
                   "cmd_func", "matrix_row", "matrix_body", "matrix", "det_matrix" ]

    EOF = Token.EOF
    FUNC_ID=1
    FUNC_CMD=2
    LBLANK=3
    RBLANK=4
    IGNORE=5
    NAND=6
    AND=7
    NOR=8
    OR=9
    XOR=10
    XNOR=11
    NOT=12
    EQUIV=13
    PLUS=14
    MINUS=15
    MULT=16
    DIV=17
    XPROD=18
    POW=19
    EQ=20
    NEQ=21
    LT=22
    LTE=23
    GT=24
    GTE=25
    TIMES=26
    DOT_PROD=27
    FRAC=28
    BINOM=29
    SQRT=30
    CONJUGATE=31
    VEC_UNIT=32
    MOD=33
    INT=34
    DIFFERENTIAL=35
    PHYS_DERIVATIVE=36
    PHYS_PARTIAL_DERIVATIVE=37
    LIMIT=38
    LIMIT_ARROW=39
    SUM=40
    PRODUCT=41
    BANG=42
    PERCENT=43
    PERMILLE=44
    COMMA=45
    UNDERSCORE=46
    SEMICOLON=47
    COLON=48
    STAR=49
    DOTS=50
    LBRACE=51
    RBRACE=52
    LPAREN=53
    RPAREN=54
    LBRACE_LITERAL=55
    RBRACE_LITERAL=56
    LBRACKET=57
    RBRACKET=58
    LBRACK_CMD=59
    RBRACK_CMD=60
    LCEIL=61
    RCEIL=62
    LFLOOR=63
    RFLOOR=64
    LANGLE=65
    RANGLE=66
    PIPE=67
    DOUBLE_PIPE=68
    DOT=69
    BEGIN_MATRIX=70
    END_MATRIX=71
    BEGIN_V_MATRIX=72
    END_V_MATRIX=73
    BEGIN_ARRAY=74
    END_ARRAY=75
    BEGIN_ENV=76
    END_ENV=77
    ENV_EL_SEP=78
    ENV_ROW_SEP=79
    ENV_SEP_SKIP=80
    NUMBER=81
    BIN_NUMBER=82
    OCT_NUMBER=83
    HEX_NUMBER=84
    DELTA=85
    ID=86
    COMMAND=87
    ARG_COMM=88
    ARG_WS=89

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
            self.res = rule_t(Ast.AlgStmt)
            self._alg_statement = None # Alg_statementContext

        def alg_statement(self):
            return self.getTypedRuleContext(ExprGrammar.Alg_statementContext,0)


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
            self.state = 70
            localctx._alg_statement = self.alg_statement()
            localctx.res = localctx._alg_statement.res
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Alg_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AlgStmt)
            self._a_expr = None # A_exprContext
            self._relation = None # RelationContext
            self._system = None # SystemContext

        def EOF(self):
            return self.getToken(ExprGrammar.EOF, 0)

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def relation(self):
            return self.getTypedRuleContext(ExprGrammar.RelationContext,0)


        def system(self):
            return self.getTypedRuleContext(ExprGrammar.SystemContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_alg_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlg_statement" ):
                listener.enterAlg_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlg_statement" ):
                listener.exitAlg_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlg_statement" ):
                return visitor.visitAlg_statement(self)
            else:
                return visitor.visitChildren(self)




    def alg_statement(self):

        localctx = ExprGrammar.Alg_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_alg_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 73
                localctx._a_expr = self.a_expr(0)
                localctx.res = localctx._a_expr.res
                pass

            elif la_ == 2:
                self.state = 76
                localctx._relation = self.relation()
                localctx.res = localctx._relation.res
                pass

            elif la_ == 3:
                self.state = 79
                localctx._system = self.system()
                localctx.res = localctx._system.res
                pass


            self.state = 84
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
            self.res = rule_t(Ast.SystemEntry)
            self._a_expr = None # A_exprContext
            self._relation = None # RelationContext

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
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                localctx._a_expr = self.a_expr(0)
                localctx.res = Ast.AExprEntry(localctx, localctx._a_expr.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                localctx._relation = self.relation()
                localctx.res = Ast.RelEntry(localctx, localctx._relation.res)
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
            self.res = rule_t(list[Ast.SystemEntry], [])
            self._system_el = None # System_elContext

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
            self.state = 94
            localctx._system_el = self.system_el()
            localctx.res.append(localctx._system_el.res)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 96
                    self.match(ExprGrammar.ENV_ROW_SEP)
                    self.state = 97
                    localctx._system_el = self.system_el()
                    localctx.res.append(localctx._system_el.res) 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==79:
                self.state = 105
                self.match(ExprGrammar.ENV_ROW_SEP)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class System_envContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.SystemEnv)
            self._system_body = None # System_bodyContext

        def BEGIN_ENV(self):
            return self.getToken(ExprGrammar.BEGIN_ENV, 0)

        def system_body(self):
            return self.getTypedRuleContext(ExprGrammar.System_bodyContext,0)


        def END_ENV(self):
            return self.getToken(ExprGrammar.END_ENV, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_system_env

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSystem_env" ):
                listener.enterSystem_env(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSystem_env" ):
                listener.exitSystem_env(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSystem_env" ):
                return visitor.visitSystem_env(self)
            else:
                return visitor.visitChildren(self)




    def system_env(self):

        localctx = ExprGrammar.System_envContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_system_env)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(ExprGrammar.BEGIN_ENV)
            self.state = 112
            localctx._system_body = self.system_body()
            localctx.res = Ast.SystemEnv(localctx, localctx._system_body.res)
            self.state = 114
            self.match(ExprGrammar.END_ENV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class System_and_chainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.AndChain)
            self.elems = rule_t(list[Ast.SystemEntry], [])
            self._system_el = None # System_elContext

        def system_el(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.System_elContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.System_elContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.AND)
            else:
                return self.getToken(ExprGrammar.AND, i)

        def getRuleIndex(self):
            return ExprGrammar.RULE_system_and_chain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSystem_and_chain" ):
                listener.enterSystem_and_chain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSystem_and_chain" ):
                listener.exitSystem_and_chain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSystem_and_chain" ):
                return visitor.visitSystem_and_chain(self)
            else:
                return visitor.visitChildren(self)




    def system_and_chain(self):

        localctx = ExprGrammar.System_and_chainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_system_and_chain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            localctx._system_el = self.system_el()
            localctx.elems.append(localctx._system_el.res)
            self.state = 122 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 118
                self.match(ExprGrammar.AND)
                self.state = 119
                localctx._system_el = self.system_el()
                localctx.elems.append(localctx._system_el.res)
                self.state = 124 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

            localctx.res = Ast.AndChain(localctx, localctx.elems)
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
            self.res = rule_t(Ast.System)
            self._system_env = None # System_envContext
            self._system_and_chain = None # System_and_chainContext

        def system_env(self):
            return self.getTypedRuleContext(ExprGrammar.System_envContext,0)


        def system_and_chain(self):
            return self.getTypedRuleContext(ExprGrammar.System_and_chainContext,0)


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
        self.enterRule(localctx, 12, self.RULE_system)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [76]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                localctx._system_env = self.system_env()
                localctx.res = localctx._system_env.res
                pass
            elif token in [3, 14, 15, 28, 29, 30, 31, 32, 34, 36, 37, 38, 40, 41, 51, 53, 57, 61, 63, 65, 67, 68, 70, 72, 74, 81, 85, 86, 87]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                localctx._system_and_chain = self.system_and_chain()
                localctx.res = localctx._system_and_chain.res
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


    class Rel_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = rule_t(type)

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
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(ExprGrammar.EQ)
                localctx.op = Ast.Eq
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(ExprGrammar.NEQ)
                localctx.op = Ast.Neq
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.match(ExprGrammar.LT)
                localctx.op = Ast.Lt
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.match(ExprGrammar.LTE)
                localctx.op = Ast.Lte
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 144
                self.match(ExprGrammar.GT)
                localctx.op = Ast.Gt
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 6)
                self.state = 146
                self.match(ExprGrammar.GTE)
                localctx.op = Ast.Gte
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


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.Rel)
            self._a_expr = None # A_exprContext
            self._rel_op = None # Rel_opContext
            self._relation = None # RelationContext
            self.lhs = None # A_exprContext
            self.rhs = None # A_exprContext

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
        self.enterRule(localctx, 16, self.RULE_relation)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                localctx._a_expr = self.a_expr(0)
                self.state = 151
                localctx._rel_op = self.rel_op()
                self.state = 152
                localctx._relation = self.relation()
                localctx.res = localctx._rel_op.op (localctx, localctx._a_expr.res, localctx._relation.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                localctx.lhs = self.a_expr(0)
                self.state = 156
                localctx._rel_op = self.rel_op()
                self.state = 157
                localctx.rhs = self.a_expr(0)
                localctx.res = localctx._rel_op.op (localctx, localctx.lhs.res, localctx.rhs.res)
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
            self.subscript = None # Subscript_argContext

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

        def PIPE(self):
            return self.getToken(ExprGrammar.PIPE, 0)

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


        def subscript_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Subscript_argContext,0)


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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_a_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 163
                self.match(ExprGrammar.INT)
                self.state = 164
                localctx._int_bounds = self.int_bounds()
                self.state = 165
                self.match(ExprGrammar.FRAC)
                self.state = 166
                self.match(ExprGrammar.LBRACE)
                self.state = 167
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 168
                localctx.diff = localctx._a_expr = self.a_expr(0)
                self.state = 169
                self.match(ExprGrammar.RBRACE)
                self.state = 170
                localctx.recip_integrand = localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Integral(localctx, Ast.DivOp(localctx.recip_integrand, Ast.Number(localctx.recip_integrand, "1"), localctx.recip_integrand.res), localctx.diff.res, localctx._int_bounds.bounds)
                pass

            elif la_ == 2:
                self.state = 173
                self.match(ExprGrammar.INT)
                self.state = 174
                localctx._int_bounds = self.int_bounds()
                self.state = 175
                localctx.integrand = localctx._a_expr = self.a_expr(0)
                self.state = 176
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 177
                localctx.diff = localctx._a_expr = self.a_expr(25)
                localctx.res = Ast.Integral(localctx, localctx.integrand.res, localctx.diff.res, localctx._int_bounds.bounds)
                pass

            elif la_ == 3:
                self.state = 180
                self.match(ExprGrammar.PHYS_PARTIAL_DERIVATIVE)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==57:
                    self.state = 181
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 182
                    localctx._a_expr = self.a_expr(0)
                    self.state = 183
                    self.match(ExprGrammar.RBRACKET)


                self.state = 187
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 188
                self.match(ExprGrammar.LBRACE)
                self.state = 189
                localctx.diff_l = localctx._a_expr = self.a_expr(0)
                self.state = 190
                self.match(ExprGrammar.RBRACE)
                self.state = 191
                self.match(ExprGrammar.LBRACE)
                self.state = 192
                localctx.diff_r = localctx._a_expr = self.a_expr(0)
                self.state = 193
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._latex_cmd_arg.res, [(localctx.diff_l.res, None), (localctx.diff_r.res, None)])
                pass

            elif la_ == 4:
                self.state = 196
                _la = self._input.LA(1)
                if not(_la==36 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==57:
                    self.state = 197
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 198
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 199
                    self.match(ExprGrammar.RBRACKET)


                self.state = 203
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 204
                self.match(ExprGrammar.LBRACE)
                self.state = 205
                localctx._a_expr = self.a_expr(0)
                self.state = 206
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._latex_cmd_arg.res, [(localctx._a_expr.res, localctx.degree.res)])
                pass

            elif la_ == 5:
                self.state = 209
                _la = self._input.LA(1)
                if not(_la==36 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==57:
                    self.state = 210
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 211
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 212
                    self.match(ExprGrammar.RBRACKET)


                self.state = 216
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 217
                localctx.diffand_last = localctx._a_expr = self.a_expr(21)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, [(localctx._latex_cmd_arg.res, localctx.degree.res)])
                pass

            elif la_ == 6:
                self.state = 220
                self.match(ExprGrammar.FRAC)
                self.state = 221
                self.match(ExprGrammar.LBRACE)
                self.state = 222
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 227
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 223
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 224
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 225
                    self.match(ExprGrammar.RBRACKET)


                self.state = 229
                localctx._a_expr = self.a_expr(0)
                self.state = 230
                self.match(ExprGrammar.RBRACE)
                self.state = 231
                self.match(ExprGrammar.LBRACE)
                self.state = 232
                localctx._diff_vars = self.diff_vars()
                self.state = 233
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, localctx._diff_vars.res)
                pass

            elif la_ == 7:
                self.state = 236
                self.match(ExprGrammar.FRAC)
                self.state = 237
                self.match(ExprGrammar.LBRACE)
                self.state = 238
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==57:
                    self.state = 239
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 240
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 241
                    self.match(ExprGrammar.RBRACKET)


                self.state = 245
                self.match(ExprGrammar.RBRACE)
                self.state = 246
                self.match(ExprGrammar.LBRACE)
                self.state = 247
                localctx._diff_vars = self.diff_vars()
                self.state = 248
                self.match(ExprGrammar.RBRACE)
                self.state = 249
                localctx._a_expr = self.a_expr(19)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, localctx._diff_vars.res)
                pass

            elif la_ == 8:
                self.state = 252
                self.match(ExprGrammar.LIMIT)
                self.state = 253
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 254
                self.match(ExprGrammar.LBRACE)
                self.state = 255
                localctx.lim_var = localctx._symbol = self.symbol()
                self.state = 256
                self.match(ExprGrammar.LIMIT_ARROW)
                self.state = 257
                localctx.lim_poa = localctx._a_expr = self.a_expr(0)
                self.state = 258
                localctx._limit_dir = self.limit_dir()
                self.state = 259
                self.match(ExprGrammar.RBRACE)
                self.state = 260
                localctx._a_expr = self.a_expr(18)
                localctx.res = Ast.Limit(localctx, localctx._a_expr.res, localctx.lim_var.res, localctx.lim_poa.res, localctx._limit_dir.res)
                pass

            elif la_ == 9:
                self.state = 267
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [40]:
                    self.state = 263
                    self.match(ExprGrammar.SUM)
                    localctx.node_t = Ast.Sum
                    pass
                elif token in [41]:
                    self.state = 265
                    self.match(ExprGrammar.PRODUCT)
                    localctx.node_t = Ast.Product
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 269
                localctx._series_range_args = self.series_range_args()
                self.state = 270
                self.match(ExprGrammar.LPAREN)
                self.state = 271
                localctx._a_expr = self.a_expr(0)
                self.state = 272
                self.match(ExprGrammar.RPAREN)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res, localctx._series_range_args.symb, (localctx._series_range_args.start, localctx._series_range_args.end))
                pass

            elif la_ == 10:
                self.state = 279
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [40]:
                    self.state = 275
                    self.match(ExprGrammar.SUM)
                    localctx.node_t = Ast.Sum
                    pass
                elif token in [41]:
                    self.state = 277
                    self.match(ExprGrammar.PRODUCT)
                    localctx.node_t = Ast.Product
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 281
                localctx._series_range_args = self.series_range_args()
                self.state = 282
                localctx._a_expr = self.a_expr(14)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res, localctx._series_range_args.symb, (localctx._series_range_args.start, localctx._series_range_args.end))
                pass

            elif la_ == 11:
                self.state = 289
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14]:
                    self.state = 285
                    self.match(ExprGrammar.PLUS)
                    localctx.node_t = Ast.UPlusOp
                    pass
                elif token in [15]:
                    self.state = 287
                    self.match(ExprGrammar.MINUS)
                    localctx.node_t = Ast.UMinusOp
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 291
                localctx._a_expr = self.a_expr(12)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res)
                pass

            elif la_ == 12:
                self.state = 294
                self.match(ExprGrammar.LPAREN)
                self.state = 295
                localctx.expr = localctx._a_expr = self.a_expr(0)
                self.state = 296
                self.match(ExprGrammar.RPAREN)
                self.state = 297
                self.match(ExprGrammar.PIPE)
                self.state = 298
                localctx._eval_at_arg = self.eval_at_arg()
                localctx.res = Ast.EvalAt(localctx, localctx.expr.res, localctx._eval_at_arg.subs_start, localctx._eval_at_arg.subs_end)
                pass

            elif la_ == 13:
                self.state = 301
                self.match(ExprGrammar.LBLANK)
                self.state = 302
                localctx.expr = localctx._a_expr = self.a_expr(0)
                self.state = 303
                self.match(ExprGrammar.PIPE)
                self.state = 304
                localctx._eval_at_arg = self.eval_at_arg()
                localctx.res = Ast.EvalAt(localctx, localctx.expr.res, localctx._eval_at_arg.subs_start, localctx._eval_at_arg.subs_end)
                pass

            elif la_ == 14:
                self.state = 307
                self.match(ExprGrammar.LBRACKET)
                self.state = 308
                localctx.expr = localctx._a_expr = self.a_expr(0)
                self.state = 309
                self.match(ExprGrammar.RBRACKET)
                self.state = 310
                localctx._eval_at_arg = self.eval_at_arg()
                localctx.res = Ast.EvalAt(localctx, localctx.expr.res, localctx._eval_at_arg.subs_start, localctx._eval_at_arg.subs_end)
                pass

            elif la_ == 15:
                self.state = 313
                localctx._combinatorial = self.combinatorial()
                localctx.res = localctx._combinatorial.res
                pass

            elif la_ == 16:
                self.state = 316
                localctx._delim_expr = self.delim_expr()
                localctx.res = localctx._delim_expr.res
                pass

            elif la_ == 17:
                self.state = 319
                localctx._cmd_func = self.cmd_func()
                localctx.res = localctx._cmd_func.res
                pass

            elif la_ == 18:
                self.state = 322
                localctx._matrix = self.matrix()
                localctx.res = localctx._matrix.res 
                pass

            elif la_ == 19:
                self.state = 325
                localctx._det_matrix = self.det_matrix()
                localctx.res = localctx._det_matrix.res
                pass

            elif la_ == 20:
                self.state = 328
                localctx._symbol = self.symbol()
                localctx.res = localctx._symbol.res
                pass

            elif la_ == 21:
                self.state = 331
                localctx._NUMBER = self.match(ExprGrammar.NUMBER)
                localctx.res = Ast.Number(localctx, (None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 402
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 400
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 335
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 348
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [16]:
                            self.state = 336
                            self.match(ExprGrammar.MULT)
                            localctx.node_t = Ast.MultOp
                            pass
                        elif token in [27]:
                            self.state = 338
                            self.match(ExprGrammar.DOT_PROD)
                            localctx.node_t = Ast.MultOp
                            pass
                        elif token in [17]:
                            self.state = 340
                            self.match(ExprGrammar.DIV)
                            localctx.node_t = Ast.DivOp
                            pass
                        elif token in [33]:
                            self.state = 342
                            self.match(ExprGrammar.MOD)
                            localctx.node_t = Ast.ModOp
                            pass
                        elif token in [26]:
                            self.state = 344
                            self.match(ExprGrammar.TIMES)
                            localctx.node_t = Ast.XProdOp
                            pass
                        elif token in [18]:
                            self.state = 346
                            self.match(ExprGrammar.XPROD)
                            localctx.node_t = Ast.XProdOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 350
                        localctx.rhs = localctx._a_expr = self.a_expr(18)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 2:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 353
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 354
                        if not ((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS)):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS))")
                        self.state = 355
                        localctx.rhs = localctx._a_expr = self.a_expr(17)
                        localctx.res = Ast.MultOp(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 3:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 358
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 363
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [14]:
                            self.state = 359
                            self.match(ExprGrammar.PLUS)
                            localctx.node_t = Ast.AddOp
                            pass
                        elif token in [15]:
                            self.state = 361
                            self.match(ExprGrammar.MINUS)
                            localctx.node_t = Ast.SubOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 365
                        localctx.rhs = localctx._a_expr = self.a_expr(14)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 4:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 368
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 369
                        self.match(ExprGrammar.POW)
                        self.state = 370
                        localctx.exp = self.pow_arg()
                        self.state = 371
                        self.match(ExprGrammar.UNDERSCORE)
                        self.state = 372
                        localctx.subscript = self.subscript_arg()
                        localctx.res=Ast.ExpOp(localctx, Ast.SubscriptOp(localctx.base.res, localctx.subscript.res), localctx.exp.res)
                        pass

                    elif la_ == 5:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 375
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 376
                        self.match(ExprGrammar.POW)
                        self.state = 377
                        localctx.exp = self.pow_arg()
                        localctx.res=Ast.ExpOp(localctx, localctx.base.res, localctx.exp.res)
                        pass

                    elif la_ == 6:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 380
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 381
                        self.match(ExprGrammar.UNDERSCORE)
                        self.state = 382
                        localctx.subscript = self.subscript_arg()
                        localctx.res = Ast.SubscriptOp(localctx, localctx.base.res, localctx.subscript.res)
                        pass

                    elif la_ == 7:
                        localctx = ExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.op = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 385
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 392
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [42]:
                            self.state = 386
                            self.match(ExprGrammar.BANG)
                            localctx.node_t = Ast.Factorial
                            pass
                        elif token in [43]:
                            self.state = 388
                            self.match(ExprGrammar.PERCENT)
                            localctx.node_t = Ast.Percent
                            pass
                        elif token in [44]:
                            self.state = 390
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
                        self.state = 395
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 396
                        self.match(ExprGrammar.PIPE)
                        self.state = 397
                        localctx._eval_at_arg = self.eval_at_arg()
                        localctx.res = Ast.EvalAt(localctx, localctx.expr.res, localctx._eval_at_arg.subs_start, localctx._eval_at_arg.subs_end)
                        pass

             
                self.state = 404
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 20, self.RULE_atom)
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [86, 87]:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                localctx._primary_symbol = self.primary_symbol()
                localctx.res = localctx._primary_symbol.res
                pass
            elif token in [81]:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
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
        self.enterRule(localctx, 22, self.RULE_latex_cmd_arg)
        try:
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [81, 86, 87]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.match(ExprGrammar.LBRACE)
                self.state = 416
                localctx._a_expr = self.a_expr(0)
                self.state = 417
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
        self.enterRule(localctx, 24, self.RULE_pow_arg)
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [81, 86, 87]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass
            elif token in [28, 29, 30, 31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                localctx._cmd_func = self.cmd_func()
                localctx.res = localctx._cmd_func.res
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 3)
                self.state = 428
                self.match(ExprGrammar.LBRACE)
                self.state = 429
                localctx._a_expr = self.a_expr(0)
                self.state = 430
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


    class Range_slotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(tuple[Ast.AExpr | None, Ast.AExpr | None])
            self.beg = None # A_exprContext
            self.delim = None # Token
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
            return ExprGrammar.RULE_range_slot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_slot" ):
                listener.enterRange_slot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_slot" ):
                listener.exitRange_slot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_slot" ):
                return visitor.visitRange_slot(self)
            else:
                return visitor.visitChildren(self)




    def range_slot(self):

        localctx = ExprGrammar.Range_slotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_range_slot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -6762151035424161784) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 7406253) != 0):
                self.state = 435
                localctx.beg = self.a_expr(0)


            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 438
                localctx.delim = self.match(ExprGrammar.COLON)
                pass
            elif token in [50]:
                self.state = 439
                localctx.delim = self.match(ExprGrammar.DOTS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 442
                localctx.end = self.a_expr(0)


            localctx.res = (localctx.beg.res, localctx.end.res)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_slotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(ExprGrammar.MULT, 0)

        def STAR(self):
            return self.getToken(ExprGrammar.STAR, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_all_slot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_slot" ):
                listener.enterAll_slot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_slot" ):
                listener.exitAll_slot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_slot" ):
                return visitor.visitAll_slot(self)
            else:
                return visitor.visitChildren(self)




    def all_slot(self):

        localctx = ExprGrammar.All_slotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_all_slot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            _la = self._input.LA(1)
            if not(_la==16 or _la==49):
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


    class Slot_entryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.IndexEntry)
            self._a_expr = None # A_exprContext
            self._range_slot = None # Range_slotContext

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def range_slot(self):
            return self.getTypedRuleContext(ExprGrammar.Range_slotContext,0)


        def all_slot(self):
            return self.getTypedRuleContext(ExprGrammar.All_slotContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_slot_entry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSlot_entry" ):
                listener.enterSlot_entry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSlot_entry" ):
                listener.exitSlot_entry(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSlot_entry" ):
                return visitor.visitSlot_entry(self)
            else:
                return visitor.visitChildren(self)




    def slot_entry(self):

        localctx = ExprGrammar.Slot_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_slot_entry)
        try:
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                localctx._a_expr = self.a_expr(0)
                localctx.res = localctx._a_expr.res
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                localctx._range_slot = self.range_slot()
                localctx.res = localctx._range_slot.res
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 455
                self.all_slot()
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


    class Subscript_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(Ast.Subscript)
            self.slots = []
            self.seps = []
            self._atom = None # AtomContext
            self._cmd_func = None # Cmd_funcContext
            self.ldelim = None # Token
            self._slot_entry = None # Slot_entryContext
            self.sep = None # Token
            self.rdelim = None # Token

        def atom(self):
            return self.getTypedRuleContext(ExprGrammar.AtomContext,0)


        def cmd_func(self):
            return self.getTypedRuleContext(ExprGrammar.Cmd_funcContext,0)


        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)

        def slot_entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.Slot_entryContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.Slot_entryContext,i)


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
            return ExprGrammar.RULE_subscript_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscript_arg" ):
                listener.enterSubscript_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscript_arg" ):
                listener.exitSubscript_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubscript_arg" ):
                return visitor.visitSubscript_arg(self)
            else:
                return visitor.visitChildren(self)




    def subscript_arg(self):

        localctx = ExprGrammar.Subscript_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_subscript_arg)
        self._la = 0 # Token type
        try:
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [81, 86, 87]:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                localctx._atom = self.atom()
                localctx.res = Ast.Subscript((localctx._atom.res,), (), ())
                pass
            elif token in [28, 29, 30, 31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                localctx._cmd_func = self.cmd_func()
                localctx.res = Ast.Subscript((localctx._cmd_func.res,), (), ())
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 3)
                self.state = 467
                self.match(ExprGrammar.LBRACE)
                self.state = 470
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 468
                    localctx.ldelim = self.match(ExprGrammar.LBRACKET)

                elif la_ == 2:
                    self.state = 469
                    localctx.ldelim = self.match(ExprGrammar.LPAREN)


                self.state = 472
                localctx._slot_entry = self.slot_entry()
                localctx.slots.append(localctx._slot_entry.res)
                self.state = 481 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 476
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [45]:
                        self.state = 474
                        localctx.sep = self.match(ExprGrammar.COMMA)
                        pass
                    elif token in [47]:
                        self.state = 475
                        localctx.sep = self.match(ExprGrammar.SEMICOLON)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 478
                    localctx._slot_entry = self.slot_entry()

                    localctx.res.append(localctx._slot_entry.res)
                    localctx.seps.append((None if localctx.sep is None else localctx.sep.text))

                    self.state = 483 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==45 or _la==47):
                        break

                self.state = 487
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [57]:
                    self.state = 485
                    localctx.rdelim = self.match(ExprGrammar.LBRACKET)
                    pass
                elif token in [53]:
                    self.state = 486
                    localctx.rdelim = self.match(ExprGrammar.LPAREN)
                    pass
                elif token in [52]:
                    pass
                else:
                    pass
                self.state = 489
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Subscript(tuple(localctx.slots), tuple(localctx.seps), ((None if localctx.ldelim is None else localctx.ldelim.text), (None if localctx.rdelim is None else localctx.rdelim.text)))
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
        self.enterRule(localctx, 34, self.RULE_int_bounds)
        try:
            self.state = 507
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.match(ExprGrammar.POW)
                self.state = 495
                localctx.upper = self.latex_cmd_arg()
                self.state = 496
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 497
                localctx.lower = self.latex_cmd_arg()
                localctx.bounds = (localctx.lower.res, localctx.upper.res)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 501
                localctx.lower = self.latex_cmd_arg()
                self.state = 502
                self.match(ExprGrammar.POW)
                self.state = 503
                localctx.upper = self.latex_cmd_arg()
                localctx.bounds = (localctx.lower.res, localctx.upper.res)
                pass
            elif token in [3, 14, 15, 28, 29, 30, 31, 32, 34, 36, 37, 38, 40, 41, 51, 53, 57, 61, 63, 65, 67, 68, 70, 72, 74, 81, 85, 86, 87]:
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
        self.enterRule(localctx, 36, self.RULE_diff_var)
        try:
            self.state = 519
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 510
                localctx._a_expr = self.a_expr(0)
                self.state = 511
                self.match(ExprGrammar.POW)
                self.state = 512
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.getInvokingContext(19).res.append((localctx._a_expr.res, localctx._latex_cmd_arg.res))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 516
                localctx._a_expr = self.a_expr(0)
                self.getInvokingContext(19).res.append((localctx._a_expr.res, None))
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
        self.enterRule(localctx, 38, self.RULE_diff_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 521
                self.diff_var()
                self.state = 524 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==35):
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
        self.enterRule(localctx, 40, self.RULE_limit_dir)
        self._la = 0 # Token type
        try:
            self.state = 538
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                localctx.res = Ast.LimitDir.BOTH
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.match(ExprGrammar.POW)
                self.state = 528
                self.match(ExprGrammar.LBRACE)
                self.state = 529
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 530
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.LimitDir.BOTH
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 532
                self.match(ExprGrammar.POW)
                self.state = 533
                self.match(ExprGrammar.PLUS)
                localctx.res = Ast.LimitDir.POSITIVE
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 535
                self.match(ExprGrammar.POW)
                self.state = 536
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
        self.enterRule(localctx, 42, self.RULE_series_range_args)
        try:
            self.state = 560
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 541
                self.match(ExprGrammar.LBRACE)
                self.state = 542
                localctx.var = self.a_expr(0)
                self.state = 543
                self.match(ExprGrammar.EQ)
                self.state = 544
                localctx.s = self.a_expr(0)
                self.state = 545
                self.match(ExprGrammar.RBRACE)
                self.state = 546
                self.match(ExprGrammar.POW)
                self.state = 547
                localctx.e = self.pow_arg()

                localctx.symb = localctx.var.res
                localctx.start = localctx.s.res
                localctx.end = localctx.e.res

                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 550
                self.match(ExprGrammar.POW)
                self.state = 551
                localctx.e = self.pow_arg()
                self.state = 552
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 553
                self.match(ExprGrammar.LBRACE)
                self.state = 554
                localctx.var = self.a_expr(0)
                self.state = 555
                self.match(ExprGrammar.EQ)
                self.state = 556
                localctx.s = self.a_expr(0)
                self.state = 557
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
        self.enterRule(localctx, 44, self.RULE_eval_at_sub_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            localctx.var = self.a_expr(0)
            self.state = 563
            self.match(ExprGrammar.EQ)
            self.state = 564
            localctx.sub = self.a_expr(0)
            localctx.res.append((localctx.var.res, localctx.sub.res))
            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 566
                self.match(ExprGrammar.COMMA)
                self.state = 567
                localctx.var = self.a_expr(0)
                self.state = 568
                self.match(ExprGrammar.EQ)
                self.state = 569
                localctx.sub = self.a_expr(0)
                localctx.res.append((localctx.var.res, localctx.sub.res))
                self.state = 576
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
        self.enterRule(localctx, 46, self.RULE_eval_at_arg)
        try:
            self.state = 603
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 577
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 578
                self.match(ExprGrammar.LBRACE)
                self.state = 579
                localctx._eval_at_sub_vars = self.eval_at_sub_vars()
                self.state = 580
                self.match(ExprGrammar.RBRACE)
                localctx.subs_start = tuple(localctx._eval_at_sub_vars.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 583
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 584
                self.match(ExprGrammar.LBRACE)
                self.state = 585
                localctx.sstart = self.eval_at_sub_vars()
                self.state = 586
                self.match(ExprGrammar.RBRACE)
                self.state = 587
                self.match(ExprGrammar.POW)
                self.state = 588
                self.match(ExprGrammar.LBRACE)
                self.state = 589
                localctx.send = self.eval_at_sub_vars()
                self.state = 590
                self.match(ExprGrammar.RBRACE)

                localctx.subs_start = tuple(localctx.sstart.res)
                localctx.subs_end=tuple(localctx.send.res)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 593
                self.match(ExprGrammar.POW)
                self.state = 594
                self.match(ExprGrammar.LBRACE)
                self.state = 595
                localctx.send = self.eval_at_sub_vars()
                self.state = 596
                self.match(ExprGrammar.RBRACE)
                self.state = 597
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 598
                self.match(ExprGrammar.LBRACE)
                self.state = 599
                localctx.sstart = self.eval_at_sub_vars()
                self.state = 600
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
        self.enterRule(localctx, 48, self.RULE_primary_symbol)
        try:
            self.state = 609
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [86]:
                self.enterOuterAlt(localctx, 1)
                self.state = 605
                localctx._ID = self.match(ExprGrammar.ID)
                localctx.res = Ast.Symbol(localctx, (None if localctx._ID is None else localctx._ID.text))
                pass
            elif token in [87]:
                self.enterOuterAlt(localctx, 2)
                self.state = 607
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
        self.enterRule(localctx, 50, self.RULE_delta_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            localctx._DELTA = self.match(ExprGrammar.DELTA)
            self.state = 612
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
        self.enterRule(localctx, 52, self.RULE_symbol)
        try:
            self.state = 621
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [86, 87]:
                self.enterOuterAlt(localctx, 1)
                self.state = 615
                localctx._primary_symbol = self.primary_symbol()
                localctx.res = localctx._primary_symbol.res
                pass
            elif token in [85]:
                self.enterOuterAlt(localctx, 2)
                self.state = 618
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
        self.enterRule(localctx, 54, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.state = 653
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 625
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 623
                    localctx.func = self.match(ExprGrammar.FUNC_ID)
                    pass
                elif token in [2]:
                    self.state = 624
                    localctx.func = self.match(ExprGrammar.FUNC_CMD)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 627
                self.match(ExprGrammar.LPAREN)
                self.state = 639
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -6762151035424161784) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 7406253) != 0):
                    self.state = 628
                    localctx._a_expr = self.a_expr(0)
                    localctx.args.append(localctx._a_expr.res)
                    self.state = 636
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==45:
                        self.state = 630
                        self.match(ExprGrammar.COMMA)
                        self.state = 631
                        localctx._a_expr = self.a_expr(0)
                        localctx.args.append(localctx._a_expr.res)
                        self.state = 638
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 641
                self.match(ExprGrammar.RPAREN)
                localctx.res = Ast.ApplyFunc(localctx, Ast.Function((None if localctx.func is None else localctx.func.text)), tuple(localctx.args))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 643
                localctx._FUNC_CMD = self.match(ExprGrammar.FUNC_CMD)
                self.state = 644
                self.match(ExprGrammar.LBRACE)
                self.state = 645
                localctx._a_expr = self.a_expr(0)
                self.state = 646
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.ApplyFunc(localctx, Ast.Function((None if localctx._FUNC_CMD is None else localctx._FUNC_CMD.text)), (localctx._a_expr.res,))
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 649
                localctx._FUNC_CMD = self.match(ExprGrammar.FUNC_CMD)
                self.state = 650
                localctx._a_expr = self.a_expr(0)
                localctx.res = Ast.ApplyFunc(localctx, Ast.Function((None if localctx._FUNC_CMD is None else localctx._FUNC_CMD.text)), (localctx._a_expr.res,))
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

        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.PIPE)
            else:
                return self.getToken(ExprGrammar.PIPE, i)

        def DOUBLE_PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.DOUBLE_PIPE)
            else:
                return self.getToken(ExprGrammar.DOUBLE_PIPE, i)

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
        self.enterRule(localctx, 56, self.RULE_delim_expr)
        self._la = 0 # Token type
        try:
            self.state = 692
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 655
                self.match(ExprGrammar.LPAREN)
                self.state = 656
                localctx._a_expr = self.a_expr(0)
                self.state = 657
                self.match(ExprGrammar.RPAREN)
                localctx.res = localctx._a_expr.res.mut_ctx(localctx)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 660
                self.match(ExprGrammar.LBRACKET)
                self.state = 661
                localctx._a_expr = self.a_expr(0)
                self.state = 662
                self.match(ExprGrammar.RBRACKET)
                localctx.res = localctx._a_expr.res.mut_ctx(localctx)
                pass
            elif token in [67]:
                self.enterOuterAlt(localctx, 3)
                self.state = 665
                self.match(ExprGrammar.PIPE)
                self.state = 666
                localctx._a_expr = self.a_expr(0)
                self.state = 667
                self.match(ExprGrammar.PIPE)
                localctx.res = Ast.Abs(localctx, localctx._a_expr.res)
                pass
            elif token in [68]:
                self.enterOuterAlt(localctx, 4)
                self.state = 670
                self.match(ExprGrammar.DOUBLE_PIPE)
                self.state = 671
                localctx._a_expr = self.a_expr(0)
                self.state = 672
                self.match(ExprGrammar.DOUBLE_PIPE)
                localctx.res = Ast.Norm(localctx, localctx._a_expr.res)
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 5)
                self.state = 675
                self.match(ExprGrammar.LFLOOR)
                self.state = 676
                localctx._a_expr = self.a_expr(0)
                self.state = 677
                self.match(ExprGrammar.RFLOOR)
                localctx.res = Ast.Floor(localctx, localctx._a_expr.res)
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 6)
                self.state = 680
                self.match(ExprGrammar.LCEIL)
                self.state = 681
                localctx._a_expr = self.a_expr(0)
                self.state = 682
                self.match(ExprGrammar.RCEIL)
                localctx.res = Ast.Ceil(localctx, localctx._a_expr.res)
                pass
            elif token in [65]:
                self.enterOuterAlt(localctx, 7)
                self.state = 685
                self.match(ExprGrammar.LANGLE)
                self.state = 686
                localctx.lhs = self.a_expr(0)
                self.state = 687
                _la = self._input.LA(1)
                if not(_la==45 or _la==67):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 688
                localctx.rhs = self.a_expr(0)
                self.state = 689
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

        def ID(self):
            return self.getToken(ExprGrammar.ID, 0)

        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.A_exprContext,i)


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
        self.enterRule(localctx, 58, self.RULE_combinatorial)
        self._la = 0 # Token type
        try:
            self.state = 722
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 712
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                if la_ == 1:
                    self.state = 694
                    self.match(ExprGrammar.LBRACE)
                    self.state = 695
                    _la = self._input.LA(1)
                    if not(_la==19 or _la==46):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 696
                    localctx.n = self.a_expr(0)
                    self.state = 697
                    localctx.op = self.match(ExprGrammar.ID)
                    self.state = 698
                    if not (None if localctx._ID is None else localctx._ID.text) == 'C':
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$ID.text == 'C'")
                    self.state = 699
                    if not ((None if localctx.op is None else localctx.op.text) in Ast.CombOpId):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "($op.text in Ast.CombOpId)")
                    self.state = 700
                    self.match(ExprGrammar.POW)
                    self.state = 701
                    localctx.k = self.a_expr(0)
                    self.state = 702
                    self.match(ExprGrammar.RBRACE)
                    localctx.res = Ast.combOpFromId(localctx, localctx.n.res, localctx.k.res, Ast.CombOpId((None if localctx.op is None else localctx.op.text)))
                    pass

                elif la_ == 2:
                    self.state = 705
                    self.match(ExprGrammar.LBRACE)
                    self.state = 706
                    localctx._ID = self.match(ExprGrammar.ID)
                    self.state = 707
                    if not (None if localctx._ID is None else localctx._ID.text) == 'D':
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$ID.text == 'D'")
                    self.state = 708
                    self.match(ExprGrammar.POW)
                    self.state = 709
                    localctx.n = self.a_expr(0)
                    self.state = 710
                    self.match(ExprGrammar.RBRACE)
                    pass


                localctx.res = Ast.Derangements(localctx, localctx.n.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 716
                self.match(ExprGrammar.LBRACE)
                self.state = 717
                self.match(ExprGrammar.BANG)
                self.state = 718
                localctx.n = self.a_expr(0)
                self.state = 719
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
        self.enterRule(localctx, 60, self.RULE_cmd_func)
        self._la = 0 # Token type
        try:
            self.state = 756
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 724
                self.match(ExprGrammar.FRAC)
                self.state = 725
                localctx.num = self.latex_cmd_arg()
                self.state = 726
                localctx.den = self.latex_cmd_arg()
                localctx.res = Ast.DivOp(localctx, localctx.num.res, localctx.den.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 729
                self.match(ExprGrammar.BINOM)
                self.state = 730
                localctx.n = self.latex_cmd_arg()
                self.state = 731
                localctx.k = self.latex_cmd_arg()
                localctx.res = Ast.Binom(localctx, localctx.n.res, localctx.k.res)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 734
                self.match(ExprGrammar.SQRT)
                self.state = 735
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Root(localctx, localctx._latex_cmd_arg.res, None) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 738
                self.match(ExprGrammar.SQRT)
                self.state = 743
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==57:
                    self.state = 739
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 740
                    localctx.root_index = self.a_expr(0)
                    self.state = 741
                    self.match(ExprGrammar.RBRACKET)


                self.state = 745
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Root(localctx, localctx._latex_cmd_arg.res, localctx.root_index.res)
                        
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 748
                self.match(ExprGrammar.CONJUGATE)
                self.state = 749
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Conjugate(localctx, localctx._latex_cmd_arg.res)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 752
                self.match(ExprGrammar.VEC_UNIT)
                self.state = 753
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
        self.enterRule(localctx, 62, self.RULE_matrix_row)
        self._la = 0 # Token type
        try:
            self.state = 770
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [71, 73, 75, 79]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [3, 14, 15, 28, 29, 30, 31, 32, 34, 36, 37, 38, 40, 41, 51, 53, 57, 61, 63, 65, 67, 68, 70, 72, 74, 81, 85, 86, 87]:
                self.enterOuterAlt(localctx, 2)
                self.state = 759
                localctx._a_expr = self.a_expr(0)
                localctx.res = [localctx._a_expr.res]
                self.state = 767
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==78:
                    self.state = 761
                    self.match(ExprGrammar.ENV_EL_SEP)
                    self.state = 762
                    localctx._a_expr = self.a_expr(0)
                    localctx.res.append(localctx._a_expr.res)
                    self.state = 769
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
        self.enterRule(localctx, 64, self.RULE_matrix_body)
        self._la = 0 # Token type
        try:
            self.state = 790
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 773
                localctx._matrix_row = self.matrix_row()
                localctx.res = [localctx._matrix_row.res]
                self.state = 781
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 775
                        self.match(ExprGrammar.ENV_ROW_SEP)
                        self.state = 776
                        localctx._matrix_row = self.matrix_row()
                        localctx.res.append(localctx._matrix_row.res) 
                    self.state = 783
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

                self.state = 787
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==79:
                    self.state = 784
                    self.match(ExprGrammar.ENV_ROW_SEP)
                    self.state = 789
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
        self.enterRule(localctx, 66, self.RULE_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 800
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [70]:
                self.state = 792
                localctx.beg = self.match(ExprGrammar.BEGIN_MATRIX)
                self.state = 793
                localctx._matrix_body = self.matrix_body()
                self.state = 794
                localctx.end = self.match(ExprGrammar.END_MATRIX)
                pass
            elif token in [74]:
                self.state = 796
                localctx.beg = self.match(ExprGrammar.BEGIN_ARRAY)
                self.state = 797
                localctx._matrix_body = self.matrix_body()
                self.state = 798
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
        self.enterRule(localctx, 68, self.RULE_det_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 804
            self.match(ExprGrammar.BEGIN_V_MATRIX)
            self.state = 805
            localctx._matrix_body = self.matrix_body()
            self.state = 806
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
        self._predicates[9] = self.a_expr_sempred
        self._predicates[29] = self.combinatorial_sempred
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
                return (None if localctx._ID is None else localctx._ID.text) == 'C'
         

            if predIndex == 10:
                return ((None if localctx.op is None else localctx.op.text) in Ast.CombOpId)
         

            if predIndex == 11:
                return (None if localctx._ID is None else localctx._ID.text) == 'D'
         





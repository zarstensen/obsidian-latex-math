# Generated from AlgExprGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import lmat_cas_client.compiling.antlr.Ast as Ast
from typing import cast, Type, Callable

def rule_t[T](_t: Type[T], v: T | None = None) -> T:
	return cast(T, v)

def serializedATN():
    return [
        4,1,87,800,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,85,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,95,8,2,1,
        3,1,3,1,3,1,3,1,3,1,3,5,3,103,8,3,10,3,12,3,106,9,3,1,3,5,3,109,
        8,3,10,3,12,3,112,9,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,
        5,4,5,125,8,5,11,5,12,5,126,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,
        137,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,151,
        8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,163,8,8,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,3,9,188,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,3,9,204,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,217,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,3,9,230,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,3,9,246,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,270,8,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,282,8,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,292,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,3,9,336,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,354,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,369,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,389,8,9,10,9,12,9,392,9,
        9,1,10,1,10,1,10,1,10,1,10,3,10,399,8,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,3,11,409,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,3,12,422,8,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,3,13,444,8,13,1,14,1,14,1,14,1,14,1,14,1,14,5,14,452,8,14,10,
        14,12,14,455,9,14,1,15,3,15,458,8,15,1,15,1,15,3,15,462,8,15,1,15,
        3,15,465,8,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,3,17,481,8,17,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,3,18,492,8,18,1,18,1,18,1,18,1,18,3,18,498,8,18,1,
        18,1,18,1,18,5,18,503,8,18,10,18,12,18,506,9,18,1,18,1,18,3,18,510,
        8,18,1,18,1,18,1,18,3,18,515,8,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,530,8,19,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,542,8,20,1,21,4,21,545,8,
        21,11,21,12,21,546,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,3,22,561,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        3,23,583,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        5,24,595,8,24,10,24,12,24,598,9,24,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,626,8,25,1,26,1,26,1,26,
        1,26,3,26,632,8,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,
        1,28,3,28,644,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,3,29,683,8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,703,8,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,713,8,30,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,3,31,734,8,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,3,31,747,8,31,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,5,32,756,8,32,10,32,12,32,759,9,32,3,32,761,8,32,1,33,
        1,33,1,33,1,33,1,33,1,33,1,33,5,33,770,8,33,10,33,12,33,773,9,33,
        1,33,5,33,776,8,33,10,33,12,33,779,9,33,3,33,781,8,33,1,34,1,34,
        1,34,1,34,1,34,1,34,1,34,1,34,3,34,791,8,34,1,34,1,34,1,35,1,35,
        1,35,1,35,1,35,1,35,0,1,18,36,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,
        70,0,5,1,0,34,35,2,0,14,14,47,47,1,0,12,13,2,0,43,43,65,65,2,0,17,
        17,44,44,873,0,72,1,0,0,0,2,84,1,0,0,0,4,94,1,0,0,0,6,96,1,0,0,0,
        8,113,1,0,0,0,10,118,1,0,0,0,12,136,1,0,0,0,14,150,1,0,0,0,16,162,
        1,0,0,0,18,335,1,0,0,0,20,398,1,0,0,0,22,408,1,0,0,0,24,421,1,0,
        0,0,26,443,1,0,0,0,28,445,1,0,0,0,30,457,1,0,0,0,32,468,1,0,0,0,
        34,480,1,0,0,0,36,514,1,0,0,0,38,529,1,0,0,0,40,541,1,0,0,0,42,544,
        1,0,0,0,44,560,1,0,0,0,46,582,1,0,0,0,48,584,1,0,0,0,50,625,1,0,
        0,0,52,631,1,0,0,0,54,633,1,0,0,0,56,643,1,0,0,0,58,682,1,0,0,0,
        60,712,1,0,0,0,62,746,1,0,0,0,64,760,1,0,0,0,66,780,1,0,0,0,68,790,
        1,0,0,0,70,794,1,0,0,0,72,73,3,2,1,0,73,74,6,0,-1,0,74,1,1,0,0,0,
        75,76,3,18,9,0,76,77,6,1,-1,0,77,85,1,0,0,0,78,79,3,16,8,0,79,80,
        6,1,-1,0,80,85,1,0,0,0,81,82,3,12,6,0,82,83,6,1,-1,0,83,85,1,0,0,
        0,84,75,1,0,0,0,84,78,1,0,0,0,84,81,1,0,0,0,85,86,1,0,0,0,86,87,
        5,0,0,1,87,3,1,0,0,0,88,89,3,18,9,0,89,90,6,2,-1,0,90,95,1,0,0,0,
        91,92,3,16,8,0,92,93,6,2,-1,0,93,95,1,0,0,0,94,88,1,0,0,0,94,91,
        1,0,0,0,95,5,1,0,0,0,96,97,3,4,2,0,97,104,6,3,-1,0,98,99,5,77,0,
        0,99,100,3,4,2,0,100,101,6,3,-1,0,101,103,1,0,0,0,102,98,1,0,0,0,
        103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,110,1,0,0,0,
        106,104,1,0,0,0,107,109,5,77,0,0,108,107,1,0,0,0,109,112,1,0,0,0,
        110,108,1,0,0,0,110,111,1,0,0,0,111,7,1,0,0,0,112,110,1,0,0,0,113,
        114,5,74,0,0,114,115,3,6,3,0,115,116,6,4,-1,0,116,117,5,75,0,0,117,
        9,1,0,0,0,118,119,3,4,2,0,119,124,6,5,-1,0,120,121,5,5,0,0,121,122,
        3,4,2,0,122,123,6,5,-1,0,123,125,1,0,0,0,124,120,1,0,0,0,125,126,
        1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,129,
        6,5,-1,0,129,11,1,0,0,0,130,131,3,8,4,0,131,132,6,6,-1,0,132,137,
        1,0,0,0,133,134,3,10,5,0,134,135,6,6,-1,0,135,137,1,0,0,0,136,130,
        1,0,0,0,136,133,1,0,0,0,137,13,1,0,0,0,138,139,5,18,0,0,139,151,
        6,7,-1,0,140,141,5,19,0,0,141,151,6,7,-1,0,142,143,5,20,0,0,143,
        151,6,7,-1,0,144,145,5,21,0,0,145,151,6,7,-1,0,146,147,5,22,0,0,
        147,151,6,7,-1,0,148,149,5,23,0,0,149,151,6,7,-1,0,150,138,1,0,0,
        0,150,140,1,0,0,0,150,142,1,0,0,0,150,144,1,0,0,0,150,146,1,0,0,
        0,150,148,1,0,0,0,151,15,1,0,0,0,152,153,3,18,9,0,153,154,3,14,7,
        0,154,155,3,16,8,0,155,156,6,8,-1,0,156,163,1,0,0,0,157,158,3,18,
        9,0,158,159,3,14,7,0,159,160,3,18,9,0,160,161,6,8,-1,0,161,163,1,
        0,0,0,162,152,1,0,0,0,162,157,1,0,0,0,163,17,1,0,0,0,164,165,6,9,
        -1,0,165,166,5,32,0,0,166,167,3,38,19,0,167,168,5,26,0,0,168,169,
        5,49,0,0,169,170,5,33,0,0,170,171,3,18,9,0,171,172,5,50,0,0,172,
        173,3,22,11,0,173,174,6,9,-1,0,174,336,1,0,0,0,175,176,5,32,0,0,
        176,177,3,38,19,0,177,178,3,18,9,0,178,179,5,33,0,0,179,180,3,18,
        9,26,180,181,6,9,-1,0,181,336,1,0,0,0,182,187,5,35,0,0,183,184,5,
        55,0,0,184,185,3,18,9,0,185,186,5,56,0,0,186,188,1,0,0,0,187,183,
        1,0,0,0,187,188,1,0,0,0,188,189,1,0,0,0,189,190,3,22,11,0,190,191,
        5,49,0,0,191,192,3,18,9,0,192,193,5,50,0,0,193,194,5,49,0,0,194,
        195,3,18,9,0,195,196,5,50,0,0,196,197,6,9,-1,0,197,336,1,0,0,0,198,
        203,7,0,0,0,199,200,5,55,0,0,200,201,3,18,9,0,201,202,5,56,0,0,202,
        204,1,0,0,0,203,199,1,0,0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,
        206,3,22,11,0,206,207,5,49,0,0,207,208,3,18,9,0,208,209,5,50,0,0,
        209,210,6,9,-1,0,210,336,1,0,0,0,211,216,7,0,0,0,212,213,5,55,0,
        0,213,214,3,18,9,0,214,215,5,56,0,0,215,217,1,0,0,0,216,212,1,0,
        0,0,216,217,1,0,0,0,217,218,1,0,0,0,218,219,3,22,11,0,219,220,3,
        18,9,23,220,221,6,9,-1,0,221,336,1,0,0,0,222,223,5,26,0,0,223,224,
        5,49,0,0,224,229,5,33,0,0,225,226,5,55,0,0,226,227,3,18,9,0,227,
        228,5,56,0,0,228,230,1,0,0,0,229,225,1,0,0,0,229,230,1,0,0,0,230,
        231,1,0,0,0,231,232,3,18,9,0,232,233,5,50,0,0,233,234,5,49,0,0,234,
        235,3,42,21,0,235,236,5,50,0,0,236,237,6,9,-1,0,237,336,1,0,0,0,
        238,239,5,26,0,0,239,240,5,49,0,0,240,245,5,33,0,0,241,242,5,55,
        0,0,242,243,3,18,9,0,243,244,5,56,0,0,244,246,1,0,0,0,245,241,1,
        0,0,0,245,246,1,0,0,0,246,247,1,0,0,0,247,248,5,50,0,0,248,249,5,
        49,0,0,249,250,3,42,21,0,250,251,5,50,0,0,251,252,3,18,9,21,252,
        253,6,9,-1,0,253,336,1,0,0,0,254,255,5,36,0,0,255,256,5,44,0,0,256,
        257,5,49,0,0,257,258,3,56,28,0,258,259,5,37,0,0,259,260,3,18,9,0,
        260,261,3,44,22,0,261,262,5,50,0,0,262,263,3,18,9,16,263,264,6,9,
        -1,0,264,336,1,0,0,0,265,266,5,38,0,0,266,270,6,9,-1,0,267,268,5,
        39,0,0,268,270,6,9,-1,0,269,265,1,0,0,0,269,267,1,0,0,0,270,271,
        1,0,0,0,271,272,3,46,23,0,272,273,5,51,0,0,273,274,3,18,9,0,274,
        275,5,52,0,0,275,276,6,9,-1,0,276,336,1,0,0,0,277,278,5,38,0,0,278,
        282,6,9,-1,0,279,280,5,39,0,0,280,282,6,9,-1,0,281,277,1,0,0,0,281,
        279,1,0,0,0,282,283,1,0,0,0,283,284,3,46,23,0,284,285,3,18,9,14,
        285,286,6,9,-1,0,286,336,1,0,0,0,287,288,5,12,0,0,288,292,6,9,-1,
        0,289,290,5,13,0,0,290,292,6,9,-1,0,291,287,1,0,0,0,291,289,1,0,
        0,0,292,293,1,0,0,0,293,294,3,18,9,12,294,295,6,9,-1,0,295,336,1,
        0,0,0,296,297,5,51,0,0,297,298,3,18,9,0,298,299,5,52,0,0,299,300,
        5,65,0,0,300,301,3,50,25,0,301,302,6,9,-1,0,302,336,1,0,0,0,303,
        304,5,1,0,0,304,305,3,18,9,0,305,306,5,65,0,0,306,307,3,50,25,0,
        307,308,6,9,-1,0,308,336,1,0,0,0,309,310,5,55,0,0,310,311,3,18,9,
        0,311,312,5,56,0,0,312,313,3,50,25,0,313,314,6,9,-1,0,314,336,1,
        0,0,0,315,316,3,60,30,0,316,317,6,9,-1,0,317,336,1,0,0,0,318,319,
        3,58,29,0,319,320,6,9,-1,0,320,336,1,0,0,0,321,322,3,62,31,0,322,
        323,6,9,-1,0,323,336,1,0,0,0,324,325,3,68,34,0,325,326,6,9,-1,0,
        326,336,1,0,0,0,327,328,3,70,35,0,328,329,6,9,-1,0,329,336,1,0,0,
        0,330,331,3,56,28,0,331,332,6,9,-1,0,332,336,1,0,0,0,333,334,5,79,
        0,0,334,336,6,9,-1,0,335,164,1,0,0,0,335,175,1,0,0,0,335,182,1,0,
        0,0,335,198,1,0,0,0,335,211,1,0,0,0,335,222,1,0,0,0,335,238,1,0,
        0,0,335,254,1,0,0,0,335,269,1,0,0,0,335,281,1,0,0,0,335,291,1,0,
        0,0,335,296,1,0,0,0,335,303,1,0,0,0,335,309,1,0,0,0,335,315,1,0,
        0,0,335,318,1,0,0,0,335,321,1,0,0,0,335,324,1,0,0,0,335,327,1,0,
        0,0,335,330,1,0,0,0,335,333,1,0,0,0,336,390,1,0,0,0,337,338,10,19,
        0,0,338,339,5,15,0,0,339,340,3,18,9,20,340,341,6,9,-1,0,341,389,
        1,0,0,0,342,353,10,18,0,0,343,344,5,14,0,0,344,354,6,9,-1,0,345,
        346,5,25,0,0,346,354,6,9,-1,0,347,348,5,31,0,0,348,354,6,9,-1,0,
        349,350,5,24,0,0,350,354,6,9,-1,0,351,352,5,16,0,0,352,354,6,9,-1,
        0,353,343,1,0,0,0,353,345,1,0,0,0,353,347,1,0,0,0,353,349,1,0,0,
        0,353,351,1,0,0,0,354,355,1,0,0,0,355,356,3,18,9,19,356,357,6,9,
        -1,0,357,389,1,0,0,0,358,359,10,17,0,0,359,360,4,9,3,0,360,361,3,
        18,9,18,361,362,6,9,-1,0,362,389,1,0,0,0,363,368,10,13,0,0,364,365,
        5,12,0,0,365,369,6,9,-1,0,366,367,5,13,0,0,367,369,6,9,-1,0,368,
        364,1,0,0,0,368,366,1,0,0,0,369,370,1,0,0,0,370,371,3,18,9,14,371,
        372,6,9,-1,0,372,389,1,0,0,0,373,374,10,28,0,0,374,375,3,26,13,0,
        375,376,6,9,-1,0,376,389,1,0,0,0,377,378,10,20,0,0,378,379,5,51,
        0,0,379,380,3,28,14,0,380,381,5,52,0,0,381,382,6,9,-1,0,382,389,
        1,0,0,0,383,384,10,8,0,0,384,385,5,65,0,0,385,386,3,50,25,0,386,
        387,6,9,-1,0,387,389,1,0,0,0,388,337,1,0,0,0,388,342,1,0,0,0,388,
        358,1,0,0,0,388,363,1,0,0,0,388,373,1,0,0,0,388,377,1,0,0,0,388,
        383,1,0,0,0,389,392,1,0,0,0,390,388,1,0,0,0,390,391,1,0,0,0,391,
        19,1,0,0,0,392,390,1,0,0,0,393,394,3,52,26,0,394,395,6,10,-1,0,395,
        399,1,0,0,0,396,397,5,79,0,0,397,399,6,10,-1,0,398,393,1,0,0,0,398,
        396,1,0,0,0,399,21,1,0,0,0,400,401,3,20,10,0,401,402,6,11,-1,0,402,
        409,1,0,0,0,403,404,5,49,0,0,404,405,3,18,9,0,405,406,5,50,0,0,406,
        407,6,11,-1,0,407,409,1,0,0,0,408,400,1,0,0,0,408,403,1,0,0,0,409,
        23,1,0,0,0,410,411,3,20,10,0,411,412,6,12,-1,0,412,422,1,0,0,0,413,
        414,3,62,31,0,414,415,6,12,-1,0,415,422,1,0,0,0,416,417,5,49,0,0,
        417,418,3,18,9,0,418,419,5,50,0,0,419,420,6,12,-1,0,420,422,1,0,
        0,0,421,410,1,0,0,0,421,413,1,0,0,0,421,416,1,0,0,0,422,25,1,0,0,
        0,423,424,5,17,0,0,424,425,3,24,12,0,425,426,5,44,0,0,426,427,3,
        36,18,0,427,428,6,13,-1,0,428,444,1,0,0,0,429,430,5,17,0,0,430,431,
        3,24,12,0,431,432,6,13,-1,0,432,444,1,0,0,0,433,434,5,44,0,0,434,
        435,3,36,18,0,435,436,6,13,-1,0,436,444,1,0,0,0,437,438,5,40,0,0,
        438,444,6,13,-1,0,439,440,5,41,0,0,440,444,6,13,-1,0,441,442,5,42,
        0,0,442,444,6,13,-1,0,443,423,1,0,0,0,443,429,1,0,0,0,443,433,1,
        0,0,0,443,437,1,0,0,0,443,439,1,0,0,0,443,441,1,0,0,0,444,27,1,0,
        0,0,445,446,3,18,9,0,446,453,6,14,-1,0,447,448,5,43,0,0,448,449,
        3,18,9,0,449,450,6,14,-1,0,450,452,1,0,0,0,451,447,1,0,0,0,452,455,
        1,0,0,0,453,451,1,0,0,0,453,454,1,0,0,0,454,29,1,0,0,0,455,453,1,
        0,0,0,456,458,3,18,9,0,457,456,1,0,0,0,457,458,1,0,0,0,458,461,1,
        0,0,0,459,462,5,46,0,0,460,462,5,48,0,0,461,459,1,0,0,0,461,460,
        1,0,0,0,462,464,1,0,0,0,463,465,3,18,9,0,464,463,1,0,0,0,464,465,
        1,0,0,0,465,466,1,0,0,0,466,467,6,15,-1,0,467,31,1,0,0,0,468,469,
        7,1,0,0,469,33,1,0,0,0,470,471,3,18,9,0,471,472,6,17,-1,0,472,481,
        1,0,0,0,473,474,3,30,15,0,474,475,6,17,-1,0,475,481,1,0,0,0,476,
        477,3,32,16,0,477,478,6,17,-1,0,478,481,1,0,0,0,479,481,6,17,-1,
        0,480,470,1,0,0,0,480,473,1,0,0,0,480,476,1,0,0,0,480,479,1,0,0,
        0,481,35,1,0,0,0,482,483,3,20,10,0,483,484,6,18,-1,0,484,515,1,0,
        0,0,485,486,3,62,31,0,486,487,6,18,-1,0,487,515,1,0,0,0,488,491,
        5,49,0,0,489,492,5,55,0,0,490,492,5,51,0,0,491,489,1,0,0,0,491,490,
        1,0,0,0,491,492,1,0,0,0,492,493,1,0,0,0,493,494,3,18,9,0,494,504,
        6,18,-1,0,495,498,5,43,0,0,496,498,5,45,0,0,497,495,1,0,0,0,497,
        496,1,0,0,0,498,499,1,0,0,0,499,500,3,34,17,0,500,501,6,18,-1,0,
        501,503,1,0,0,0,502,497,1,0,0,0,503,506,1,0,0,0,504,502,1,0,0,0,
        504,505,1,0,0,0,505,509,1,0,0,0,506,504,1,0,0,0,507,510,5,55,0,0,
        508,510,5,51,0,0,509,507,1,0,0,0,509,508,1,0,0,0,509,510,1,0,0,0,
        510,511,1,0,0,0,511,512,5,50,0,0,512,513,6,18,-1,0,513,515,1,0,0,
        0,514,482,1,0,0,0,514,485,1,0,0,0,514,488,1,0,0,0,515,37,1,0,0,0,
        516,517,5,17,0,0,517,518,3,22,11,0,518,519,5,44,0,0,519,520,3,22,
        11,0,520,521,6,19,-1,0,521,530,1,0,0,0,522,523,5,44,0,0,523,524,
        3,22,11,0,524,525,5,17,0,0,525,526,3,22,11,0,526,527,6,19,-1,0,527,
        530,1,0,0,0,528,530,6,19,-1,0,529,516,1,0,0,0,529,522,1,0,0,0,529,
        528,1,0,0,0,530,39,1,0,0,0,531,532,5,33,0,0,532,533,3,18,9,0,533,
        534,5,17,0,0,534,535,3,22,11,0,535,536,6,20,-1,0,536,542,1,0,0,0,
        537,538,5,33,0,0,538,539,3,18,9,0,539,540,6,20,-1,0,540,542,1,0,
        0,0,541,531,1,0,0,0,541,537,1,0,0,0,542,41,1,0,0,0,543,545,3,40,
        20,0,544,543,1,0,0,0,545,546,1,0,0,0,546,544,1,0,0,0,546,547,1,0,
        0,0,547,43,1,0,0,0,548,561,6,22,-1,0,549,550,5,17,0,0,550,551,5,
        49,0,0,551,552,7,2,0,0,552,553,5,50,0,0,553,561,6,22,-1,0,554,555,
        5,17,0,0,555,556,5,12,0,0,556,561,6,22,-1,0,557,558,5,17,0,0,558,
        559,5,13,0,0,559,561,6,22,-1,0,560,548,1,0,0,0,560,549,1,0,0,0,560,
        554,1,0,0,0,560,557,1,0,0,0,561,45,1,0,0,0,562,563,5,44,0,0,563,
        564,5,49,0,0,564,565,3,18,9,0,565,566,5,18,0,0,566,567,3,18,9,0,
        567,568,5,50,0,0,568,569,5,17,0,0,569,570,3,24,12,0,570,571,6,23,
        -1,0,571,583,1,0,0,0,572,573,5,17,0,0,573,574,3,24,12,0,574,575,
        5,44,0,0,575,576,5,49,0,0,576,577,3,18,9,0,577,578,5,18,0,0,578,
        579,3,18,9,0,579,580,5,50,0,0,580,581,6,23,-1,0,581,583,1,0,0,0,
        582,562,1,0,0,0,582,572,1,0,0,0,583,47,1,0,0,0,584,585,3,18,9,0,
        585,586,5,18,0,0,586,587,3,18,9,0,587,596,6,24,-1,0,588,589,5,43,
        0,0,589,590,3,18,9,0,590,591,5,18,0,0,591,592,3,18,9,0,592,593,6,
        24,-1,0,593,595,1,0,0,0,594,588,1,0,0,0,595,598,1,0,0,0,596,594,
        1,0,0,0,596,597,1,0,0,0,597,49,1,0,0,0,598,596,1,0,0,0,599,600,5,
        44,0,0,600,601,5,49,0,0,601,602,3,48,24,0,602,603,5,50,0,0,603,604,
        6,25,-1,0,604,626,1,0,0,0,605,606,5,44,0,0,606,607,5,49,0,0,607,
        608,3,48,24,0,608,609,5,50,0,0,609,610,5,17,0,0,610,611,5,49,0,0,
        611,612,3,48,24,0,612,613,5,50,0,0,613,614,6,25,-1,0,614,626,1,0,
        0,0,615,616,5,17,0,0,616,617,5,49,0,0,617,618,3,48,24,0,618,619,
        5,50,0,0,619,620,5,44,0,0,620,621,5,49,0,0,621,622,3,48,24,0,622,
        623,5,50,0,0,623,624,6,25,-1,0,624,626,1,0,0,0,625,599,1,0,0,0,625,
        605,1,0,0,0,625,615,1,0,0,0,626,51,1,0,0,0,627,628,5,84,0,0,628,
        632,6,26,-1,0,629,630,5,85,0,0,630,632,6,26,-1,0,631,627,1,0,0,0,
        631,629,1,0,0,0,632,53,1,0,0,0,633,634,5,83,0,0,634,635,3,52,26,
        0,635,636,6,27,-1,0,636,55,1,0,0,0,637,638,3,52,26,0,638,639,6,28,
        -1,0,639,644,1,0,0,0,640,641,3,54,27,0,641,642,6,28,-1,0,642,644,
        1,0,0,0,643,637,1,0,0,0,643,640,1,0,0,0,644,57,1,0,0,0,645,646,5,
        51,0,0,646,647,3,18,9,0,647,648,5,52,0,0,648,649,6,29,-1,0,649,683,
        1,0,0,0,650,651,5,55,0,0,651,652,3,18,9,0,652,653,5,56,0,0,653,654,
        6,29,-1,0,654,683,1,0,0,0,655,656,5,65,0,0,656,657,3,18,9,0,657,
        658,5,65,0,0,658,659,6,29,-1,0,659,683,1,0,0,0,660,661,5,66,0,0,
        661,662,3,18,9,0,662,663,5,66,0,0,663,664,6,29,-1,0,664,683,1,0,
        0,0,665,666,5,61,0,0,666,667,3,18,9,0,667,668,5,62,0,0,668,669,6,
        29,-1,0,669,683,1,0,0,0,670,671,5,59,0,0,671,672,3,18,9,0,672,673,
        5,60,0,0,673,674,6,29,-1,0,674,683,1,0,0,0,675,676,5,63,0,0,676,
        677,3,18,9,0,677,678,7,3,0,0,678,679,3,18,9,0,679,680,5,64,0,0,680,
        681,6,29,-1,0,681,683,1,0,0,0,682,645,1,0,0,0,682,650,1,0,0,0,682,
        655,1,0,0,0,682,660,1,0,0,0,682,665,1,0,0,0,682,670,1,0,0,0,682,
        675,1,0,0,0,683,59,1,0,0,0,684,685,5,49,0,0,685,686,7,4,0,0,686,
        687,3,18,9,0,687,688,5,84,0,0,688,689,4,30,8,1,689,690,4,30,9,1,
        690,691,5,17,0,0,691,692,3,18,9,0,692,693,5,50,0,0,693,694,6,30,
        -1,0,694,703,1,0,0,0,695,696,5,49,0,0,696,697,5,84,0,0,697,698,4,
        30,10,1,698,699,5,17,0,0,699,700,3,18,9,0,700,701,5,50,0,0,701,703,
        1,0,0,0,702,684,1,0,0,0,702,695,1,0,0,0,703,704,1,0,0,0,704,705,
        6,30,-1,0,705,713,1,0,0,0,706,707,5,49,0,0,707,708,5,40,0,0,708,
        709,3,18,9,0,709,710,5,50,0,0,710,711,6,30,-1,0,711,713,1,0,0,0,
        712,702,1,0,0,0,712,706,1,0,0,0,713,61,1,0,0,0,714,715,5,26,0,0,
        715,716,3,22,11,0,716,717,3,22,11,0,717,718,6,31,-1,0,718,747,1,
        0,0,0,719,720,5,27,0,0,720,721,3,22,11,0,721,722,3,22,11,0,722,723,
        6,31,-1,0,723,747,1,0,0,0,724,725,5,28,0,0,725,726,3,22,11,0,726,
        727,6,31,-1,0,727,747,1,0,0,0,728,733,5,28,0,0,729,730,5,55,0,0,
        730,731,3,18,9,0,731,732,5,56,0,0,732,734,1,0,0,0,733,729,1,0,0,
        0,733,734,1,0,0,0,734,735,1,0,0,0,735,736,3,22,11,0,736,737,6,31,
        -1,0,737,747,1,0,0,0,738,739,5,29,0,0,739,740,3,22,11,0,740,741,
        6,31,-1,0,741,747,1,0,0,0,742,743,5,30,0,0,743,744,3,22,11,0,744,
        745,6,31,-1,0,745,747,1,0,0,0,746,714,1,0,0,0,746,719,1,0,0,0,746,
        724,1,0,0,0,746,728,1,0,0,0,746,738,1,0,0,0,746,742,1,0,0,0,747,
        63,1,0,0,0,748,761,1,0,0,0,749,750,3,18,9,0,750,757,6,32,-1,0,751,
        752,5,76,0,0,752,753,3,18,9,0,753,754,6,32,-1,0,754,756,1,0,0,0,
        755,751,1,0,0,0,756,759,1,0,0,0,757,755,1,0,0,0,757,758,1,0,0,0,
        758,761,1,0,0,0,759,757,1,0,0,0,760,748,1,0,0,0,760,749,1,0,0,0,
        761,65,1,0,0,0,762,781,1,0,0,0,763,764,3,64,32,0,764,771,6,33,-1,
        0,765,766,5,77,0,0,766,767,3,64,32,0,767,768,6,33,-1,0,768,770,1,
        0,0,0,769,765,1,0,0,0,770,773,1,0,0,0,771,769,1,0,0,0,771,772,1,
        0,0,0,772,777,1,0,0,0,773,771,1,0,0,0,774,776,5,77,0,0,775,774,1,
        0,0,0,776,779,1,0,0,0,777,775,1,0,0,0,777,778,1,0,0,0,778,781,1,
        0,0,0,779,777,1,0,0,0,780,762,1,0,0,0,780,763,1,0,0,0,781,67,1,0,
        0,0,782,783,5,68,0,0,783,784,3,66,33,0,784,785,5,69,0,0,785,791,
        1,0,0,0,786,787,5,72,0,0,787,788,3,66,33,0,788,789,5,73,0,0,789,
        791,1,0,0,0,790,782,1,0,0,0,790,786,1,0,0,0,791,792,1,0,0,0,792,
        793,6,34,-1,0,793,69,1,0,0,0,794,795,5,70,0,0,795,796,3,66,33,0,
        796,797,5,71,0,0,797,798,6,35,-1,0,798,71,1,0,0,0,55,84,94,104,110,
        126,136,150,162,187,203,216,229,245,269,281,291,335,353,368,388,
        390,398,408,421,443,453,457,461,464,480,491,497,504,509,514,529,
        541,546,560,582,596,625,631,643,682,702,712,733,746,757,760,771,
        777,780,790
    ]

class AlgExprGrammar ( Parser ):

    grammarFileName = "AlgExprGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\not'", "'\\equiv'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'^'", "'='", "<INVALID>", "'<'", "<INVALID>", "'>'", 
                     "<INVALID>", "'\\times'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\sqrt'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\lim'", "<INVALID>", "'\\sum'", "'\\prod'", 
                     "'!'", "'\\%'", "'\\textperthousand'", "','", "'_'", 
                     "';'", "':'", "'\\star'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'&'", "'\\\\'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\Delta'" ]

    symbolicNames = [ "<INVALID>", "LBLANK", "RBLANK", "IGNORE", "NAND", 
                      "AND", "NOR", "OR", "XOR", "XNOR", "NOT", "EQUIV", 
                      "PLUS", "MINUS", "MULT", "DIV", "XPROD", "POW", "EQ", 
                      "NEQ", "LT", "LTE", "GT", "GTE", "TIMES", "DOT_PROD", 
                      "FRAC", "BINOM", "SQRT", "CONJUGATE", "VEC_UNIT", 
                      "MOD", "INT", "DIFFERENTIAL", "PHYS_DERIVATIVE", "PHYS_PARTIAL_DERIVATIVE", 
                      "LIMIT", "LIMIT_ARROW", "SUM", "PRODUCT", "BANG", 
                      "PERCENT", "PERMILLE", "COMMA", "UNDERSCORE", "SEMICOLON", 
                      "COLON", "STAR", "DOTS", "LBRACE", "RBRACE", "LPAREN", 
                      "RPAREN", "LBRACE_LITERAL", "RBRACE_LITERAL", "LBRACKET", 
                      "RBRACKET", "LBRACK_CMD", "RBRACK_CMD", "LCEIL", "RCEIL", 
                      "LFLOOR", "RFLOOR", "LANGLE", "RANGLE", "PIPE", "DOUBLE_PIPE", 
                      "DOT", "BEGIN_MATRIX", "END_MATRIX", "BEGIN_V_MATRIX", 
                      "END_V_MATRIX", "BEGIN_ARRAY", "END_ARRAY", "BEGIN_ENV", 
                      "END_ENV", "ENV_EL_SEP", "ENV_ROW_SEP", "ENV_SEP_SKIP", 
                      "NUMBER", "BIN_NUMBER", "OCT_NUMBER", "HEX_NUMBER", 
                      "DELTA", "ID", "COMMAND", "ARG_COMM", "ARG_WS" ]

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
    RULE_postfix_op = 13
    RULE_func_args = 14
    RULE_range_slot = 15
    RULE_all_slot = 16
    RULE_slot_entry = 17
    RULE_subscript_arg = 18
    RULE_int_bounds = 19
    RULE_diff_var = 20
    RULE_diff_vars = 21
    RULE_limit_dir = 22
    RULE_series_range_args = 23
    RULE_eval_at_sub_vars = 24
    RULE_eval_at_arg = 25
    RULE_primary_symbol = 26
    RULE_delta_symbol = 27
    RULE_symbol = 28
    RULE_delim_expr = 29
    RULE_combinatorial = 30
    RULE_cmd_func = 31
    RULE_matrix_row = 32
    RULE_matrix_body = 33
    RULE_matrix = 34
    RULE_det_matrix = 35

    ruleNames =  [ "debug", "alg_statement", "system_el", "system_body", 
                   "system_env", "system_and_chain", "system", "rel_op", 
                   "relation", "a_expr", "atom", "latex_cmd_arg", "pow_arg", 
                   "postfix_op", "func_args", "range_slot", "all_slot", 
                   "slot_entry", "subscript_arg", "int_bounds", "diff_var", 
                   "diff_vars", "limit_dir", "series_range_args", "eval_at_sub_vars", 
                   "eval_at_arg", "primary_symbol", "delta_symbol", "symbol", 
                   "delim_expr", "combinatorial", "cmd_func", "matrix_row", 
                   "matrix_body", "matrix", "det_matrix" ]

    EOF = Token.EOF
    LBLANK=1
    RBLANK=2
    IGNORE=3
    NAND=4
    AND=5
    NOR=6
    OR=7
    XOR=8
    XNOR=9
    NOT=10
    EQUIV=11
    PLUS=12
    MINUS=13
    MULT=14
    DIV=15
    XPROD=16
    POW=17
    EQ=18
    NEQ=19
    LT=20
    LTE=21
    GT=22
    GTE=23
    TIMES=24
    DOT_PROD=25
    FRAC=26
    BINOM=27
    SQRT=28
    CONJUGATE=29
    VEC_UNIT=30
    MOD=31
    INT=32
    DIFFERENTIAL=33
    PHYS_DERIVATIVE=34
    PHYS_PARTIAL_DERIVATIVE=35
    LIMIT=36
    LIMIT_ARROW=37
    SUM=38
    PRODUCT=39
    BANG=40
    PERCENT=41
    PERMILLE=42
    COMMA=43
    UNDERSCORE=44
    SEMICOLON=45
    COLON=46
    STAR=47
    DOTS=48
    LBRACE=49
    RBRACE=50
    LPAREN=51
    RPAREN=52
    LBRACE_LITERAL=53
    RBRACE_LITERAL=54
    LBRACKET=55
    RBRACKET=56
    LBRACK_CMD=57
    RBRACK_CMD=58
    LCEIL=59
    RCEIL=60
    LFLOOR=61
    RFLOOR=62
    LANGLE=63
    RANGLE=64
    PIPE=65
    DOUBLE_PIPE=66
    DOT=67
    BEGIN_MATRIX=68
    END_MATRIX=69
    BEGIN_V_MATRIX=70
    END_V_MATRIX=71
    BEGIN_ARRAY=72
    END_ARRAY=73
    BEGIN_ENV=74
    END_ENV=75
    ENV_EL_SEP=76
    ENV_ROW_SEP=77
    ENV_SEP_SKIP=78
    NUMBER=79
    BIN_NUMBER=80
    OCT_NUMBER=81
    HEX_NUMBER=82
    DELTA=83
    ID=84
    COMMAND=85
    ARG_COMM=86
    ARG_WS=87

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
            return self.getTypedRuleContext(AlgExprGrammar.Alg_statementContext,0)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_debug

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

        localctx = AlgExprGrammar.DebugContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_debug)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
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
            return self.getToken(AlgExprGrammar.EOF, 0)

        def a_expr(self):
            return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,0)


        def relation(self):
            return self.getTypedRuleContext(AlgExprGrammar.RelationContext,0)


        def system(self):
            return self.getTypedRuleContext(AlgExprGrammar.SystemContext,0)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_alg_statement

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

        localctx = AlgExprGrammar.Alg_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_alg_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 75
                localctx._a_expr = self.a_expr(0)
                localctx.res = localctx._a_expr.res
                pass

            elif la_ == 2:
                self.state = 78
                localctx._relation = self.relation()
                localctx.res = localctx._relation.res
                pass

            elif la_ == 3:
                self.state = 81
                localctx._system = self.system()
                localctx.res = localctx._system.res
                pass


            self.state = 86
            self.match(AlgExprGrammar.EOF)
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
            return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,0)


        def relation(self):
            return self.getTypedRuleContext(AlgExprGrammar.RelationContext,0)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_system_el

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

        localctx = AlgExprGrammar.System_elContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_system_el)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                localctx._a_expr = self.a_expr(0)
                localctx.res = Ast.AExprEntry(localctx, localctx._a_expr.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
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
                return self.getTypedRuleContexts(AlgExprGrammar.System_elContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.System_elContext,i)


        def ENV_ROW_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.ENV_ROW_SEP)
            else:
                return self.getToken(AlgExprGrammar.ENV_ROW_SEP, i)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_system_body

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

        localctx = AlgExprGrammar.System_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_system_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            localctx._system_el = self.system_el()
            localctx.res.append(localctx._system_el.res)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 98
                    self.match(AlgExprGrammar.ENV_ROW_SEP)
                    self.state = 99
                    localctx._system_el = self.system_el()
                    localctx.res.append(localctx._system_el.res) 
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==77:
                self.state = 107
                self.match(AlgExprGrammar.ENV_ROW_SEP)
                self.state = 112
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
            return self.getToken(AlgExprGrammar.BEGIN_ENV, 0)

        def system_body(self):
            return self.getTypedRuleContext(AlgExprGrammar.System_bodyContext,0)


        def END_ENV(self):
            return self.getToken(AlgExprGrammar.END_ENV, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_system_env

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

        localctx = AlgExprGrammar.System_envContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_system_env)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(AlgExprGrammar.BEGIN_ENV)
            self.state = 114
            localctx._system_body = self.system_body()
            localctx.res = Ast.SystemEnv(localctx, localctx._system_body.res)
            self.state = 116
            self.match(AlgExprGrammar.END_ENV)
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
                return self.getTypedRuleContexts(AlgExprGrammar.System_elContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.System_elContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.AND)
            else:
                return self.getToken(AlgExprGrammar.AND, i)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_system_and_chain

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

        localctx = AlgExprGrammar.System_and_chainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_system_and_chain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            localctx._system_el = self.system_el()
            localctx.elems.append(localctx._system_el.res)
            self.state = 124 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 120
                self.match(AlgExprGrammar.AND)
                self.state = 121
                localctx._system_el = self.system_el()
                localctx.elems.append(localctx._system_el.res)
                self.state = 126 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5):
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
            return self.getTypedRuleContext(AlgExprGrammar.System_envContext,0)


        def system_and_chain(self):
            return self.getTypedRuleContext(AlgExprGrammar.System_and_chainContext,0)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_system

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

        localctx = AlgExprGrammar.SystemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_system)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [74]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                localctx._system_env = self.system_env()
                localctx.res = localctx._system_env.res
                pass
            elif token in [1, 12, 13, 26, 27, 28, 29, 30, 32, 34, 35, 36, 38, 39, 49, 51, 55, 59, 61, 63, 65, 66, 68, 70, 72, 79, 83, 84, 85]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
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
            return self.getToken(AlgExprGrammar.EQ, 0)

        def NEQ(self):
            return self.getToken(AlgExprGrammar.NEQ, 0)

        def LT(self):
            return self.getToken(AlgExprGrammar.LT, 0)

        def LTE(self):
            return self.getToken(AlgExprGrammar.LTE, 0)

        def GT(self):
            return self.getToken(AlgExprGrammar.GT, 0)

        def GTE(self):
            return self.getToken(AlgExprGrammar.GTE, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_rel_op

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

        localctx = AlgExprGrammar.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rel_op)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(AlgExprGrammar.EQ)
                localctx.op = Ast.Eq
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(AlgExprGrammar.NEQ)
                localctx.op = Ast.Neq
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.match(AlgExprGrammar.LT)
                localctx.op = Ast.Lt
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.match(AlgExprGrammar.LTE)
                localctx.op = Ast.Lte
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 5)
                self.state = 146
                self.match(AlgExprGrammar.GT)
                localctx.op = Ast.Gt
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 6)
                self.state = 148
                self.match(AlgExprGrammar.GTE)
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
                return self.getTypedRuleContexts(AlgExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,i)


        def rel_op(self):
            return self.getTypedRuleContext(AlgExprGrammar.Rel_opContext,0)


        def relation(self):
            return self.getTypedRuleContext(AlgExprGrammar.RelationContext,0)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_relation

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

        localctx = AlgExprGrammar.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_relation)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                localctx._a_expr = self.a_expr(0)
                self.state = 153
                localctx._rel_op = self.rel_op()
                self.state = 154
                localctx._relation = self.relation()
                localctx.res = localctx._rel_op.op (localctx, localctx._a_expr.res, localctx._relation.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                localctx.lhs = self.a_expr(0)
                self.state = 158
                localctx._rel_op = self.rel_op()
                self.state = 159
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
            self._postfix_op = None # Postfix_opContext
            self._func_args = None # Func_argsContext

        def INT(self):
            return self.getToken(AlgExprGrammar.INT, 0)

        def int_bounds(self):
            return self.getTypedRuleContext(AlgExprGrammar.Int_boundsContext,0)


        def FRAC(self):
            return self.getToken(AlgExprGrammar.FRAC, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.LBRACE)
            else:
                return self.getToken(AlgExprGrammar.LBRACE, i)

        def DIFFERENTIAL(self):
            return self.getToken(AlgExprGrammar.DIFFERENTIAL, 0)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.RBRACE)
            else:
                return self.getToken(AlgExprGrammar.RBRACE, i)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,i)


        def latex_cmd_arg(self):
            return self.getTypedRuleContext(AlgExprGrammar.Latex_cmd_argContext,0)


        def PHYS_PARTIAL_DERIVATIVE(self):
            return self.getToken(AlgExprGrammar.PHYS_PARTIAL_DERIVATIVE, 0)

        def LBRACKET(self):
            return self.getToken(AlgExprGrammar.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(AlgExprGrammar.RBRACKET, 0)

        def PHYS_DERIVATIVE(self):
            return self.getToken(AlgExprGrammar.PHYS_DERIVATIVE, 0)

        def diff_vars(self):
            return self.getTypedRuleContext(AlgExprGrammar.Diff_varsContext,0)


        def LIMIT(self):
            return self.getToken(AlgExprGrammar.LIMIT, 0)

        def UNDERSCORE(self):
            return self.getToken(AlgExprGrammar.UNDERSCORE, 0)

        def LIMIT_ARROW(self):
            return self.getToken(AlgExprGrammar.LIMIT_ARROW, 0)

        def limit_dir(self):
            return self.getTypedRuleContext(AlgExprGrammar.Limit_dirContext,0)


        def symbol(self):
            return self.getTypedRuleContext(AlgExprGrammar.SymbolContext,0)


        def series_range_args(self):
            return self.getTypedRuleContext(AlgExprGrammar.Series_range_argsContext,0)


        def LPAREN(self):
            return self.getToken(AlgExprGrammar.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AlgExprGrammar.RPAREN, 0)

        def SUM(self):
            return self.getToken(AlgExprGrammar.SUM, 0)

        def PRODUCT(self):
            return self.getToken(AlgExprGrammar.PRODUCT, 0)

        def PLUS(self):
            return self.getToken(AlgExprGrammar.PLUS, 0)

        def MINUS(self):
            return self.getToken(AlgExprGrammar.MINUS, 0)

        def PIPE(self):
            return self.getToken(AlgExprGrammar.PIPE, 0)

        def eval_at_arg(self):
            return self.getTypedRuleContext(AlgExprGrammar.Eval_at_argContext,0)


        def LBLANK(self):
            return self.getToken(AlgExprGrammar.LBLANK, 0)

        def combinatorial(self):
            return self.getTypedRuleContext(AlgExprGrammar.CombinatorialContext,0)


        def delim_expr(self):
            return self.getTypedRuleContext(AlgExprGrammar.Delim_exprContext,0)


        def cmd_func(self):
            return self.getTypedRuleContext(AlgExprGrammar.Cmd_funcContext,0)


        def matrix(self):
            return self.getTypedRuleContext(AlgExprGrammar.MatrixContext,0)


        def det_matrix(self):
            return self.getTypedRuleContext(AlgExprGrammar.Det_matrixContext,0)


        def NUMBER(self):
            return self.getToken(AlgExprGrammar.NUMBER, 0)

        def DIV(self):
            return self.getToken(AlgExprGrammar.DIV, 0)

        def MULT(self):
            return self.getToken(AlgExprGrammar.MULT, 0)

        def DOT_PROD(self):
            return self.getToken(AlgExprGrammar.DOT_PROD, 0)

        def MOD(self):
            return self.getToken(AlgExprGrammar.MOD, 0)

        def TIMES(self):
            return self.getToken(AlgExprGrammar.TIMES, 0)

        def XPROD(self):
            return self.getToken(AlgExprGrammar.XPROD, 0)

        def postfix_op(self):
            return self.getTypedRuleContext(AlgExprGrammar.Postfix_opContext,0)


        def func_args(self):
            return self.getTypedRuleContext(AlgExprGrammar.Func_argsContext,0)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_a_expr

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
        localctx = AlgExprGrammar.A_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_a_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 165
                self.match(AlgExprGrammar.INT)
                self.state = 166
                localctx._int_bounds = self.int_bounds()
                self.state = 167
                self.match(AlgExprGrammar.FRAC)
                self.state = 168
                self.match(AlgExprGrammar.LBRACE)
                self.state = 169
                self.match(AlgExprGrammar.DIFFERENTIAL)
                self.state = 170
                localctx.diff = localctx._a_expr = self.a_expr(0)
                self.state = 171
                self.match(AlgExprGrammar.RBRACE)
                self.state = 172
                localctx.recip_integrand = localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Integral(localctx, Ast.DivOp(localctx.recip_integrand, Ast.Number(localctx.recip_integrand, "1"), localctx.recip_integrand.res), localctx.diff.res, localctx._int_bounds.bounds)
                pass

            elif la_ == 2:
                self.state = 175
                self.match(AlgExprGrammar.INT)
                self.state = 176
                localctx._int_bounds = self.int_bounds()
                self.state = 177
                localctx.integrand = localctx._a_expr = self.a_expr(0)
                self.state = 178
                self.match(AlgExprGrammar.DIFFERENTIAL)
                self.state = 179
                localctx.diff = localctx._a_expr = self.a_expr(26)
                localctx.res = Ast.Integral(localctx, localctx.integrand.res, localctx.diff.res, localctx._int_bounds.bounds)
                pass

            elif la_ == 3:
                self.state = 182
                self.match(AlgExprGrammar.PHYS_PARTIAL_DERIVATIVE)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==55:
                    self.state = 183
                    self.match(AlgExprGrammar.LBRACKET)
                    self.state = 184
                    localctx._a_expr = self.a_expr(0)
                    self.state = 185
                    self.match(AlgExprGrammar.RBRACKET)


                self.state = 189
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 190
                self.match(AlgExprGrammar.LBRACE)
                self.state = 191
                localctx.diff_l = localctx._a_expr = self.a_expr(0)
                self.state = 192
                self.match(AlgExprGrammar.RBRACE)
                self.state = 193
                self.match(AlgExprGrammar.LBRACE)
                self.state = 194
                localctx.diff_r = localctx._a_expr = self.a_expr(0)
                self.state = 195
                self.match(AlgExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._latex_cmd_arg.res, [(localctx.diff_l.res, None), (localctx.diff_r.res, None)])
                pass

            elif la_ == 4:
                self.state = 198
                _la = self._input.LA(1)
                if not(_la==34 or _la==35):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==55:
                    self.state = 199
                    self.match(AlgExprGrammar.LBRACKET)
                    self.state = 200
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 201
                    self.match(AlgExprGrammar.RBRACKET)


                self.state = 205
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 206
                self.match(AlgExprGrammar.LBRACE)
                self.state = 207
                localctx._a_expr = self.a_expr(0)
                self.state = 208
                self.match(AlgExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._latex_cmd_arg.res, [(localctx._a_expr.res, localctx.degree.res)])
                pass

            elif la_ == 5:
                self.state = 211
                _la = self._input.LA(1)
                if not(_la==34 or _la==35):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==55:
                    self.state = 212
                    self.match(AlgExprGrammar.LBRACKET)
                    self.state = 213
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 214
                    self.match(AlgExprGrammar.RBRACKET)


                self.state = 218
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 219
                localctx.diffand_last = localctx._a_expr = self.a_expr(23)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, [(localctx._latex_cmd_arg.res, localctx.degree.res)])
                pass

            elif la_ == 6:
                self.state = 222
                self.match(AlgExprGrammar.FRAC)
                self.state = 223
                self.match(AlgExprGrammar.LBRACE)
                self.state = 224
                self.match(AlgExprGrammar.DIFFERENTIAL)
                self.state = 229
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 225
                    self.match(AlgExprGrammar.LBRACKET)
                    self.state = 226
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 227
                    self.match(AlgExprGrammar.RBRACKET)


                self.state = 231
                localctx._a_expr = self.a_expr(0)
                self.state = 232
                self.match(AlgExprGrammar.RBRACE)
                self.state = 233
                self.match(AlgExprGrammar.LBRACE)
                self.state = 234
                localctx._diff_vars = self.diff_vars()
                self.state = 235
                self.match(AlgExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, localctx._diff_vars.res)
                pass

            elif la_ == 7:
                self.state = 238
                self.match(AlgExprGrammar.FRAC)
                self.state = 239
                self.match(AlgExprGrammar.LBRACE)
                self.state = 240
                self.match(AlgExprGrammar.DIFFERENTIAL)
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==55:
                    self.state = 241
                    self.match(AlgExprGrammar.LBRACKET)
                    self.state = 242
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 243
                    self.match(AlgExprGrammar.RBRACKET)


                self.state = 247
                self.match(AlgExprGrammar.RBRACE)
                self.state = 248
                self.match(AlgExprGrammar.LBRACE)
                self.state = 249
                localctx._diff_vars = self.diff_vars()
                self.state = 250
                self.match(AlgExprGrammar.RBRACE)
                self.state = 251
                localctx._a_expr = self.a_expr(21)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, localctx._diff_vars.res)
                pass

            elif la_ == 8:
                self.state = 254
                self.match(AlgExprGrammar.LIMIT)
                self.state = 255
                self.match(AlgExprGrammar.UNDERSCORE)
                self.state = 256
                self.match(AlgExprGrammar.LBRACE)
                self.state = 257
                localctx.lim_var = localctx._symbol = self.symbol()
                self.state = 258
                self.match(AlgExprGrammar.LIMIT_ARROW)
                self.state = 259
                localctx.lim_poa = localctx._a_expr = self.a_expr(0)
                self.state = 260
                localctx._limit_dir = self.limit_dir()
                self.state = 261
                self.match(AlgExprGrammar.RBRACE)
                self.state = 262
                localctx._a_expr = self.a_expr(16)
                localctx.res = Ast.Limit(localctx, localctx._a_expr.res, localctx.lim_var.res, localctx.lim_poa.res, localctx._limit_dir.res)
                pass

            elif la_ == 9:
                self.state = 269
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [38]:
                    self.state = 265
                    self.match(AlgExprGrammar.SUM)
                    localctx.node_t = Ast.Sum
                    pass
                elif token in [39]:
                    self.state = 267
                    self.match(AlgExprGrammar.PRODUCT)
                    localctx.node_t = Ast.Product
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 271
                localctx._series_range_args = self.series_range_args()
                self.state = 272
                self.match(AlgExprGrammar.LPAREN)
                self.state = 273
                localctx._a_expr = self.a_expr(0)
                self.state = 274
                self.match(AlgExprGrammar.RPAREN)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res, localctx._series_range_args.symb, (localctx._series_range_args.start, localctx._series_range_args.end))
                pass

            elif la_ == 10:
                self.state = 281
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [38]:
                    self.state = 277
                    self.match(AlgExprGrammar.SUM)
                    localctx.node_t = Ast.Sum
                    pass
                elif token in [39]:
                    self.state = 279
                    self.match(AlgExprGrammar.PRODUCT)
                    localctx.node_t = Ast.Product
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 283
                localctx._series_range_args = self.series_range_args()
                self.state = 284
                localctx._a_expr = self.a_expr(14)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res, localctx._series_range_args.symb, (localctx._series_range_args.start, localctx._series_range_args.end))
                pass

            elif la_ == 11:
                self.state = 291
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 287
                    self.match(AlgExprGrammar.PLUS)
                    localctx.node_t = Ast.UPlusOp
                    pass
                elif token in [13]:
                    self.state = 289
                    self.match(AlgExprGrammar.MINUS)
                    localctx.node_t = Ast.UMinusOp
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 293
                localctx._a_expr = self.a_expr(12)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res)
                pass

            elif la_ == 12:
                self.state = 296
                self.match(AlgExprGrammar.LPAREN)
                self.state = 297
                localctx.expr = localctx._a_expr = self.a_expr(0)
                self.state = 298
                self.match(AlgExprGrammar.RPAREN)
                self.state = 299
                self.match(AlgExprGrammar.PIPE)
                self.state = 300
                localctx._eval_at_arg = self.eval_at_arg()
                localctx.res = Ast.EvalAt(localctx, localctx.expr.res, localctx._eval_at_arg.subs_start, localctx._eval_at_arg.subs_end)
                pass

            elif la_ == 13:
                self.state = 303
                self.match(AlgExprGrammar.LBLANK)
                self.state = 304
                localctx.expr = localctx._a_expr = self.a_expr(0)
                self.state = 305
                self.match(AlgExprGrammar.PIPE)
                self.state = 306
                localctx._eval_at_arg = self.eval_at_arg()
                localctx.res = Ast.EvalAt(localctx, localctx.expr.res, localctx._eval_at_arg.subs_start, localctx._eval_at_arg.subs_end)
                pass

            elif la_ == 14:
                self.state = 309
                self.match(AlgExprGrammar.LBRACKET)
                self.state = 310
                localctx.expr = localctx._a_expr = self.a_expr(0)
                self.state = 311
                self.match(AlgExprGrammar.RBRACKET)
                self.state = 312
                localctx._eval_at_arg = self.eval_at_arg()
                localctx.res = Ast.EvalAt(localctx, localctx.expr.res, localctx._eval_at_arg.subs_start, localctx._eval_at_arg.subs_end)
                pass

            elif la_ == 15:
                self.state = 315
                localctx._combinatorial = self.combinatorial()
                localctx.res = localctx._combinatorial.res
                pass

            elif la_ == 16:
                self.state = 318
                localctx._delim_expr = self.delim_expr()
                localctx.res = localctx._delim_expr.res
                pass

            elif la_ == 17:
                self.state = 321
                localctx._cmd_func = self.cmd_func()
                localctx.res = localctx._cmd_func.res
                pass

            elif la_ == 18:
                self.state = 324
                localctx._matrix = self.matrix()
                localctx.res = localctx._matrix.res 
                pass

            elif la_ == 19:
                self.state = 327
                localctx._det_matrix = self.det_matrix()
                localctx.res = localctx._det_matrix.res
                pass

            elif la_ == 20:
                self.state = 330
                localctx._symbol = self.symbol()
                localctx.res = localctx._symbol.res
                pass

            elif la_ == 21:
                self.state = 333
                localctx._NUMBER = self.match(AlgExprGrammar.NUMBER)
                localctx.res = Ast.Number(localctx, (None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 388
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = AlgExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 337
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 338
                        self.match(AlgExprGrammar.DIV)
                        self.state = 339
                        localctx.rhs = localctx._a_expr = self.a_expr(20)
                        localctx.res = Ast.DivOp(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 2:
                        localctx = AlgExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 342
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 353
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [14]:
                            self.state = 343
                            self.match(AlgExprGrammar.MULT)
                            localctx.node_t = Ast.MultOp
                            pass
                        elif token in [25]:
                            self.state = 345
                            self.match(AlgExprGrammar.DOT_PROD)
                            localctx.node_t = Ast.MultOp
                            pass
                        elif token in [31]:
                            self.state = 347
                            self.match(AlgExprGrammar.MOD)
                            localctx.node_t = Ast.ModOp
                            pass
                        elif token in [24]:
                            self.state = 349
                            self.match(AlgExprGrammar.TIMES)
                            localctx.node_t = Ast.XProdOp
                            pass
                        elif token in [16]:
                            self.state = 351
                            self.match(AlgExprGrammar.XPROD)
                            localctx.node_t = Ast.XProdOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 355
                        localctx.rhs = localctx._a_expr = self.a_expr(19)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 3:
                        localctx = AlgExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 358
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 359
                        if not ((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS, self.LPAREN)):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS, self.LPAREN))")
                        self.state = 360
                        localctx.rhs = localctx._a_expr = self.a_expr(18)
                        localctx.res = Ast.MultOp(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 4:
                        localctx = AlgExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 363
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 368
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [12]:
                            self.state = 364
                            self.match(AlgExprGrammar.PLUS)
                            localctx.node_t = Ast.AddOp
                            pass
                        elif token in [13]:
                            self.state = 366
                            self.match(AlgExprGrammar.MINUS)
                            localctx.node_t = Ast.SubOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 370
                        localctx.rhs = localctx._a_expr = self.a_expr(14)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 5:
                        localctx = AlgExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 373
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 374
                        localctx._postfix_op = self.postfix_op()
                        localctx.res = localctx._postfix_op.op (localctx, localctx.base.res)
                        pass

                    elif la_ == 6:
                        localctx = AlgExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 377
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 378
                        self.match(AlgExprGrammar.LPAREN)
                        self.state = 379
                        localctx._func_args = self.func_args()
                        self.state = 380
                        self.match(AlgExprGrammar.RPAREN)
                        localctx.res = Ast.AmbigApplyFunc(localctx, Ast.ApplyFunc(localctx, localctx.lhs.res, localctx._func_args.res))
                        pass

                    elif la_ == 7:
                        localctx = AlgExprGrammar.A_exprContext(self, _parentctx, _parentState)
                        localctx.expr = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 383
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 384
                        self.match(AlgExprGrammar.PIPE)
                        self.state = 385
                        localctx._eval_at_arg = self.eval_at_arg()
                        localctx.res = Ast.EvalAt(localctx, localctx.expr.res, localctx._eval_at_arg.subs_start, localctx._eval_at_arg.subs_end)
                        pass

             
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            return self.getTypedRuleContext(AlgExprGrammar.Primary_symbolContext,0)


        def NUMBER(self):
            return self.getToken(AlgExprGrammar.NUMBER, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_atom

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

        localctx = AlgExprGrammar.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atom)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [84, 85]:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                localctx._primary_symbol = self.primary_symbol()
                localctx.res = localctx._primary_symbol.res
                pass
            elif token in [79]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                localctx._NUMBER = self.match(AlgExprGrammar.NUMBER)
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
            return self.getTypedRuleContext(AlgExprGrammar.AtomContext,0)


        def LBRACE(self):
            return self.getToken(AlgExprGrammar.LBRACE, 0)

        def a_expr(self):
            return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,0)


        def RBRACE(self):
            return self.getToken(AlgExprGrammar.RBRACE, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_latex_cmd_arg

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

        localctx = AlgExprGrammar.Latex_cmd_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_latex_cmd_arg)
        try:
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [79, 84, 85]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.match(AlgExprGrammar.LBRACE)
                self.state = 404
                localctx._a_expr = self.a_expr(0)
                self.state = 405
                self.match(AlgExprGrammar.RBRACE)
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
            return self.getTypedRuleContext(AlgExprGrammar.AtomContext,0)


        def cmd_func(self):
            return self.getTypedRuleContext(AlgExprGrammar.Cmd_funcContext,0)


        def LBRACE(self):
            return self.getToken(AlgExprGrammar.LBRACE, 0)

        def a_expr(self):
            return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,0)


        def RBRACE(self):
            return self.getToken(AlgExprGrammar.RBRACE, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_pow_arg

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

        localctx = AlgExprGrammar.Pow_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_pow_arg)
        try:
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [79, 84, 85]:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass
            elif token in [26, 27, 28, 29, 30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                localctx._cmd_func = self.cmd_func()
                localctx.res = localctx._cmd_func.res
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 3)
                self.state = 416
                self.match(AlgExprGrammar.LBRACE)
                self.state = 417
                localctx._a_expr = self.a_expr(0)
                self.state = 418
                self.match(AlgExprGrammar.RBRACE)
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


    class Postfix_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = rule_t(Callable[[ParserRuleContext, Ast.AExpr], Ast.PostfixOp])
            self.exp = None # Pow_argContext
            self.subscript = None # Subscript_argContext

        def POW(self):
            return self.getToken(AlgExprGrammar.POW, 0)

        def UNDERSCORE(self):
            return self.getToken(AlgExprGrammar.UNDERSCORE, 0)

        def pow_arg(self):
            return self.getTypedRuleContext(AlgExprGrammar.Pow_argContext,0)


        def subscript_arg(self):
            return self.getTypedRuleContext(AlgExprGrammar.Subscript_argContext,0)


        def BANG(self):
            return self.getToken(AlgExprGrammar.BANG, 0)

        def PERCENT(self):
            return self.getToken(AlgExprGrammar.PERCENT, 0)

        def PERMILLE(self):
            return self.getToken(AlgExprGrammar.PERMILLE, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_postfix_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix_op" ):
                listener.enterPostfix_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix_op" ):
                listener.exitPostfix_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix_op" ):
                return visitor.visitPostfix_op(self)
            else:
                return visitor.visitChildren(self)




    def postfix_op(self):

        localctx = AlgExprGrammar.Postfix_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_postfix_op)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(AlgExprGrammar.POW)
                self.state = 424
                localctx.exp = self.pow_arg()
                self.state = 425
                self.match(AlgExprGrammar.UNDERSCORE)
                self.state = 426
                localctx.subscript = self.subscript_arg()
                localctx.op=lambda ctx, base: Ast.ExpOp(ctx, Ast.SubscriptOp(ctx, base, localctx.subscript.res), localctx.exp.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.match(AlgExprGrammar.POW)
                self.state = 430
                localctx.exp = self.pow_arg()
                localctx.op=lambda ctx, base: Ast.ExpOp(ctx, base, localctx.exp.res)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 433
                self.match(AlgExprGrammar.UNDERSCORE)
                self.state = 434
                localctx.subscript = self.subscript_arg()
                localctx.op = lambda ctx, target: Ast.SubscriptOp(ctx, target, localctx.subscript.res)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 437
                self.match(AlgExprGrammar.BANG)
                localctx.op = lambda ctx, target: Ast.Factorial(ctx, target)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 439
                self.match(AlgExprGrammar.PERCENT)
                localctx.op = lambda ctx, target: Ast.Percent(ctx, target)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 441
                self.match(AlgExprGrammar.PERMILLE)
                localctx.op = lambda ctx, target: Ast.Permille(ctx, target)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = rule_t(list[Ast.AExpr], [])
            self._a_expr = None # A_exprContext

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.COMMA)
            else:
                return self.getToken(AlgExprGrammar.COMMA, i)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_func_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_args" ):
                listener.enterFunc_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_args" ):
                listener.exitFunc_args(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_args" ):
                return visitor.visitFunc_args(self)
            else:
                return visitor.visitChildren(self)




    def func_args(self):

        localctx = AlgExprGrammar.Func_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            localctx._a_expr = self.a_expr(0)
            localctx.res.append(localctx._a_expr.res)
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 447
                self.match(AlgExprGrammar.COMMA)
                self.state = 448
                localctx._a_expr = self.a_expr(0)
                localctx.res.append(localctx._a_expr.res)
                self.state = 455
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getToken(AlgExprGrammar.COLON, 0)

        def DOTS(self):
            return self.getToken(AlgExprGrammar.DOTS, 0)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,i)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_range_slot

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

        localctx = AlgExprGrammar.Range_slotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_range_slot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -6302223777283428350) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 1851563) != 0):
                self.state = 456
                localctx.beg = self.a_expr(0)


            self.state = 461
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.state = 459
                localctx.delim = self.match(AlgExprGrammar.COLON)
                pass
            elif token in [48]:
                self.state = 460
                localctx.delim = self.match(AlgExprGrammar.DOTS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 463
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
            return self.getToken(AlgExprGrammar.MULT, 0)

        def STAR(self):
            return self.getToken(AlgExprGrammar.STAR, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_all_slot

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

        localctx = AlgExprGrammar.All_slotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_all_slot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            _la = self._input.LA(1)
            if not(_la==14 or _la==47):
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
            return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,0)


        def range_slot(self):
            return self.getTypedRuleContext(AlgExprGrammar.Range_slotContext,0)


        def all_slot(self):
            return self.getTypedRuleContext(AlgExprGrammar.All_slotContext,0)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_slot_entry

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

        localctx = AlgExprGrammar.Slot_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_slot_entry)
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                localctx._a_expr = self.a_expr(0)
                localctx.res = localctx._a_expr.res
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                localctx._range_slot = self.range_slot()
                localctx.res = localctx._range_slot.res
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 476
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
            self._a_expr = None # A_exprContext
            self.sep = None # Token
            self._slot_entry = None # Slot_entryContext
            self.rdelim = None # Token

        def atom(self):
            return self.getTypedRuleContext(AlgExprGrammar.AtomContext,0)


        def cmd_func(self):
            return self.getTypedRuleContext(AlgExprGrammar.Cmd_funcContext,0)


        def LBRACE(self):
            return self.getToken(AlgExprGrammar.LBRACE, 0)

        def a_expr(self):
            return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,0)


        def RBRACE(self):
            return self.getToken(AlgExprGrammar.RBRACE, 0)

        def slot_entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgExprGrammar.Slot_entryContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.Slot_entryContext,i)


        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.LBRACKET)
            else:
                return self.getToken(AlgExprGrammar.LBRACKET, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.LPAREN)
            else:
                return self.getToken(AlgExprGrammar.LPAREN, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.COMMA)
            else:
                return self.getToken(AlgExprGrammar.COMMA, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.SEMICOLON)
            else:
                return self.getToken(AlgExprGrammar.SEMICOLON, i)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_subscript_arg

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

        localctx = AlgExprGrammar.Subscript_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_subscript_arg)
        self._la = 0 # Token type
        try:
            self.state = 514
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [79, 84, 85]:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                localctx._atom = self.atom()
                localctx.res = Ast.Subscript(localctx, (localctx._atom.res,), Ast.SubscriptForm((None, None), ()))
                pass
            elif token in [26, 27, 28, 29, 30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                localctx._cmd_func = self.cmd_func()
                localctx.res = Ast.Subscript(localctx, (localctx._cmd_func.res,), Ast.SubscriptForm((None, None), ()))
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 3)
                self.state = 488
                self.match(AlgExprGrammar.LBRACE)
                self.state = 491
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 489
                    localctx.ldelim = self.match(AlgExprGrammar.LBRACKET)

                elif la_ == 2:
                    self.state = 490
                    localctx.ldelim = self.match(AlgExprGrammar.LPAREN)


                self.state = 493
                localctx._a_expr = self.a_expr(0)
                localctx.slots.append(localctx._a_expr.res)
                self.state = 504
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==43 or _la==45:
                    self.state = 497
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [43]:
                        self.state = 495
                        localctx.sep = self.match(AlgExprGrammar.COMMA)
                        pass
                    elif token in [45]:
                        self.state = 496
                        localctx.sep = self.match(AlgExprGrammar.SEMICOLON)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 499
                    localctx._slot_entry = self.slot_entry()

                    localctx.res.append(localctx._slot_entry.res)
                    localctx.seps.append((None if localctx.sep is None else localctx.sep.text))

                    self.state = 506
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 509
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [55]:
                    self.state = 507
                    localctx.rdelim = self.match(AlgExprGrammar.LBRACKET)
                    pass
                elif token in [51]:
                    self.state = 508
                    localctx.rdelim = self.match(AlgExprGrammar.LPAREN)
                    pass
                elif token in [50]:
                    pass
                else:
                    pass
                self.state = 511
                self.match(AlgExprGrammar.RBRACE)
                localctx.res = Ast.Subscript(localctx, tuple(localctx.slots), Ast.SubscriptForm(((None if localctx.ldelim is None else localctx.ldelim.text), (None if localctx.rdelim is None else localctx.rdelim.text)), tuple(localctx.seps)))
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
            return self.getToken(AlgExprGrammar.POW, 0)

        def UNDERSCORE(self):
            return self.getToken(AlgExprGrammar.UNDERSCORE, 0)

        def latex_cmd_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgExprGrammar.Latex_cmd_argContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.Latex_cmd_argContext,i)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_int_bounds

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

        localctx = AlgExprGrammar.Int_boundsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_int_bounds)
        try:
            self.state = 529
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.match(AlgExprGrammar.POW)
                self.state = 517
                localctx.upper = self.latex_cmd_arg()
                self.state = 518
                self.match(AlgExprGrammar.UNDERSCORE)
                self.state = 519
                localctx.lower = self.latex_cmd_arg()
                localctx.bounds = (localctx.lower.res, localctx.upper.res)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.match(AlgExprGrammar.UNDERSCORE)
                self.state = 523
                localctx.lower = self.latex_cmd_arg()
                self.state = 524
                self.match(AlgExprGrammar.POW)
                self.state = 525
                localctx.upper = self.latex_cmd_arg()
                localctx.bounds = (localctx.lower.res, localctx.upper.res)
                pass
            elif token in [1, 12, 13, 26, 27, 28, 29, 30, 32, 34, 35, 36, 38, 39, 49, 51, 55, 59, 61, 63, 65, 66, 68, 70, 72, 79, 83, 84, 85]:
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
            return self.getToken(AlgExprGrammar.DIFFERENTIAL, 0)

        def a_expr(self):
            return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,0)


        def POW(self):
            return self.getToken(AlgExprGrammar.POW, 0)

        def latex_cmd_arg(self):
            return self.getTypedRuleContext(AlgExprGrammar.Latex_cmd_argContext,0)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_diff_var

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

        localctx = AlgExprGrammar.Diff_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_diff_var)
        try:
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.match(AlgExprGrammar.DIFFERENTIAL)
                self.state = 532
                localctx._a_expr = self.a_expr(0)
                self.state = 533
                self.match(AlgExprGrammar.POW)
                self.state = 534
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.getInvokingContext(21).res.append((localctx._a_expr.res, localctx._latex_cmd_arg.res))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 537
                self.match(AlgExprGrammar.DIFFERENTIAL)
                self.state = 538
                localctx._a_expr = self.a_expr(0)
                self.getInvokingContext(21).res.append((localctx._a_expr.res, None))
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
                return self.getTypedRuleContexts(AlgExprGrammar.Diff_varContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.Diff_varContext,i)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_diff_vars

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

        localctx = AlgExprGrammar.Diff_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_diff_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 543
                self.diff_var()
                self.state = 546 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==33):
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
            return self.getToken(AlgExprGrammar.POW, 0)

        def LBRACE(self):
            return self.getToken(AlgExprGrammar.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AlgExprGrammar.RBRACE, 0)

        def PLUS(self):
            return self.getToken(AlgExprGrammar.PLUS, 0)

        def MINUS(self):
            return self.getToken(AlgExprGrammar.MINUS, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_limit_dir

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

        localctx = AlgExprGrammar.Limit_dirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_limit_dir)
        self._la = 0 # Token type
        try:
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                localctx.res = Ast.LimitDir.BOTH
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
                self.match(AlgExprGrammar.POW)
                self.state = 550
                self.match(AlgExprGrammar.LBRACE)
                self.state = 551
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 552
                self.match(AlgExprGrammar.RBRACE)
                localctx.res = Ast.LimitDir.BOTH
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 554
                self.match(AlgExprGrammar.POW)
                self.state = 555
                self.match(AlgExprGrammar.PLUS)
                localctx.res = Ast.LimitDir.POSITIVE
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 557
                self.match(AlgExprGrammar.POW)
                self.state = 558
                self.match(AlgExprGrammar.MINUS)
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
            return self.getToken(AlgExprGrammar.UNDERSCORE, 0)

        def LBRACE(self):
            return self.getToken(AlgExprGrammar.LBRACE, 0)

        def EQ(self):
            return self.getToken(AlgExprGrammar.EQ, 0)

        def RBRACE(self):
            return self.getToken(AlgExprGrammar.RBRACE, 0)

        def POW(self):
            return self.getToken(AlgExprGrammar.POW, 0)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,i)


        def pow_arg(self):
            return self.getTypedRuleContext(AlgExprGrammar.Pow_argContext,0)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_series_range_args

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

        localctx = AlgExprGrammar.Series_range_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_series_range_args)
        try:
            self.state = 582
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 562
                self.match(AlgExprGrammar.UNDERSCORE)
                self.state = 563
                self.match(AlgExprGrammar.LBRACE)
                self.state = 564
                localctx.var = self.a_expr(0)
                self.state = 565
                self.match(AlgExprGrammar.EQ)
                self.state = 566
                localctx.s = self.a_expr(0)
                self.state = 567
                self.match(AlgExprGrammar.RBRACE)
                self.state = 568
                self.match(AlgExprGrammar.POW)
                self.state = 569
                localctx.e = self.pow_arg()

                localctx.symb = localctx.var.res
                localctx.start = localctx.s.res
                localctx.end = localctx.e.res

                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 572
                self.match(AlgExprGrammar.POW)
                self.state = 573
                localctx.e = self.pow_arg()
                self.state = 574
                self.match(AlgExprGrammar.UNDERSCORE)
                self.state = 575
                self.match(AlgExprGrammar.LBRACE)
                self.state = 576
                localctx.var = self.a_expr(0)
                self.state = 577
                self.match(AlgExprGrammar.EQ)
                self.state = 578
                localctx.s = self.a_expr(0)
                self.state = 579
                self.match(AlgExprGrammar.RBRACE)

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
                return self.getTokens(AlgExprGrammar.EQ)
            else:
                return self.getToken(AlgExprGrammar.EQ, i)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.COMMA)
            else:
                return self.getToken(AlgExprGrammar.COMMA, i)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_eval_at_sub_vars

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

        localctx = AlgExprGrammar.Eval_at_sub_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_eval_at_sub_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            localctx.var = self.a_expr(0)
            self.state = 585
            self.match(AlgExprGrammar.EQ)
            self.state = 586
            localctx.sub = self.a_expr(0)
            localctx.res.append((localctx.var.res, localctx.sub.res))
            self.state = 596
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 588
                self.match(AlgExprGrammar.COMMA)
                self.state = 589
                localctx.var = self.a_expr(0)
                self.state = 590
                self.match(AlgExprGrammar.EQ)
                self.state = 591
                localctx.sub = self.a_expr(0)
                localctx.res.append((localctx.var.res, localctx.sub.res))
                self.state = 598
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
            return self.getToken(AlgExprGrammar.UNDERSCORE, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.LBRACE)
            else:
                return self.getToken(AlgExprGrammar.LBRACE, i)

        def eval_at_sub_vars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgExprGrammar.Eval_at_sub_varsContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.Eval_at_sub_varsContext,i)


        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.RBRACE)
            else:
                return self.getToken(AlgExprGrammar.RBRACE, i)

        def POW(self):
            return self.getToken(AlgExprGrammar.POW, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_eval_at_arg

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

        localctx = AlgExprGrammar.Eval_at_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_eval_at_arg)
        try:
            self.state = 625
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 599
                self.match(AlgExprGrammar.UNDERSCORE)
                self.state = 600
                self.match(AlgExprGrammar.LBRACE)
                self.state = 601
                localctx._eval_at_sub_vars = self.eval_at_sub_vars()
                self.state = 602
                self.match(AlgExprGrammar.RBRACE)
                localctx.subs_start = tuple(localctx._eval_at_sub_vars.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 605
                self.match(AlgExprGrammar.UNDERSCORE)
                self.state = 606
                self.match(AlgExprGrammar.LBRACE)
                self.state = 607
                localctx.sstart = self.eval_at_sub_vars()
                self.state = 608
                self.match(AlgExprGrammar.RBRACE)
                self.state = 609
                self.match(AlgExprGrammar.POW)
                self.state = 610
                self.match(AlgExprGrammar.LBRACE)
                self.state = 611
                localctx.send = self.eval_at_sub_vars()
                self.state = 612
                self.match(AlgExprGrammar.RBRACE)

                localctx.subs_start = tuple(localctx.sstart.res)
                localctx.subs_end=tuple(localctx.send.res)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 615
                self.match(AlgExprGrammar.POW)
                self.state = 616
                self.match(AlgExprGrammar.LBRACE)
                self.state = 617
                localctx.send = self.eval_at_sub_vars()
                self.state = 618
                self.match(AlgExprGrammar.RBRACE)
                self.state = 619
                self.match(AlgExprGrammar.UNDERSCORE)
                self.state = 620
                self.match(AlgExprGrammar.LBRACE)
                self.state = 621
                localctx.sstart = self.eval_at_sub_vars()
                self.state = 622
                self.match(AlgExprGrammar.RBRACE)

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
            return self.getToken(AlgExprGrammar.ID, 0)

        def COMMAND(self):
            return self.getToken(AlgExprGrammar.COMMAND, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_primary_symbol

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

        localctx = AlgExprGrammar.Primary_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_primary_symbol)
        try:
            self.state = 631
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [84]:
                self.enterOuterAlt(localctx, 1)
                self.state = 627
                localctx._ID = self.match(AlgExprGrammar.ID)
                localctx.res = Ast.Symbol(localctx, (None if localctx._ID is None else localctx._ID.text))
                pass
            elif token in [85]:
                self.enterOuterAlt(localctx, 2)
                self.state = 629
                localctx._COMMAND = self.match(AlgExprGrammar.COMMAND)
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
            return self.getToken(AlgExprGrammar.DELTA, 0)

        def primary_symbol(self):
            return self.getTypedRuleContext(AlgExprGrammar.Primary_symbolContext,0)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_delta_symbol

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

        localctx = AlgExprGrammar.Delta_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_delta_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            localctx._DELTA = self.match(AlgExprGrammar.DELTA)
            self.state = 634
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
            return self.getTypedRuleContext(AlgExprGrammar.Primary_symbolContext,0)


        def delta_symbol(self):
            return self.getTypedRuleContext(AlgExprGrammar.Delta_symbolContext,0)


        def getRuleIndex(self):
            return AlgExprGrammar.RULE_symbol

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

        localctx = AlgExprGrammar.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_symbol)
        try:
            self.state = 643
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [84, 85]:
                self.enterOuterAlt(localctx, 1)
                self.state = 637
                localctx._primary_symbol = self.primary_symbol()
                localctx.res = localctx._primary_symbol.res
                pass
            elif token in [83]:
                self.enterOuterAlt(localctx, 2)
                self.state = 640
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
            self.res = rule_t(Ast.AExpr)
            self._a_expr = None # A_exprContext
            self.lhs = None # A_exprContext
            self.rhs = None # A_exprContext

        def LPAREN(self):
            return self.getToken(AlgExprGrammar.LPAREN, 0)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,i)


        def RPAREN(self):
            return self.getToken(AlgExprGrammar.RPAREN, 0)

        def LBRACKET(self):
            return self.getToken(AlgExprGrammar.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(AlgExprGrammar.RBRACKET, 0)

        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.PIPE)
            else:
                return self.getToken(AlgExprGrammar.PIPE, i)

        def DOUBLE_PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.DOUBLE_PIPE)
            else:
                return self.getToken(AlgExprGrammar.DOUBLE_PIPE, i)

        def LFLOOR(self):
            return self.getToken(AlgExprGrammar.LFLOOR, 0)

        def RFLOOR(self):
            return self.getToken(AlgExprGrammar.RFLOOR, 0)

        def LCEIL(self):
            return self.getToken(AlgExprGrammar.LCEIL, 0)

        def RCEIL(self):
            return self.getToken(AlgExprGrammar.RCEIL, 0)

        def LANGLE(self):
            return self.getToken(AlgExprGrammar.LANGLE, 0)

        def RANGLE(self):
            return self.getToken(AlgExprGrammar.RANGLE, 0)

        def COMMA(self):
            return self.getToken(AlgExprGrammar.COMMA, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_delim_expr

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

        localctx = AlgExprGrammar.Delim_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_delim_expr)
        self._la = 0 # Token type
        try:
            self.state = 682
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 645
                self.match(AlgExprGrammar.LPAREN)
                self.state = 646
                localctx._a_expr = self.a_expr(0)
                self.state = 647
                self.match(AlgExprGrammar.RPAREN)
                localctx.res = Ast.Parens(localctx, localctx._a_expr.res)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 650
                self.match(AlgExprGrammar.LBRACKET)
                self.state = 651
                localctx._a_expr = self.a_expr(0)
                self.state = 652
                self.match(AlgExprGrammar.RBRACKET)
                localctx.res = Ast.Parens(localctx, localctx._a_expr.res)
                pass
            elif token in [65]:
                self.enterOuterAlt(localctx, 3)
                self.state = 655
                self.match(AlgExprGrammar.PIPE)
                self.state = 656
                localctx._a_expr = self.a_expr(0)
                self.state = 657
                self.match(AlgExprGrammar.PIPE)
                localctx.res = Ast.Abs(localctx, localctx._a_expr.res)
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 4)
                self.state = 660
                self.match(AlgExprGrammar.DOUBLE_PIPE)
                self.state = 661
                localctx._a_expr = self.a_expr(0)
                self.state = 662
                self.match(AlgExprGrammar.DOUBLE_PIPE)
                localctx.res = Ast.Norm(localctx, localctx._a_expr.res)
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 5)
                self.state = 665
                self.match(AlgExprGrammar.LFLOOR)
                self.state = 666
                localctx._a_expr = self.a_expr(0)
                self.state = 667
                self.match(AlgExprGrammar.RFLOOR)
                localctx.res = Ast.Floor(localctx, localctx._a_expr.res)
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 6)
                self.state = 670
                self.match(AlgExprGrammar.LCEIL)
                self.state = 671
                localctx._a_expr = self.a_expr(0)
                self.state = 672
                self.match(AlgExprGrammar.RCEIL)
                localctx.res = Ast.Ceil(localctx, localctx._a_expr.res)
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 7)
                self.state = 675
                self.match(AlgExprGrammar.LANGLE)
                self.state = 676
                localctx.lhs = self.a_expr(0)
                self.state = 677
                _la = self._input.LA(1)
                if not(_la==43 or _la==65):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 678
                localctx.rhs = self.a_expr(0)
                self.state = 679
                self.match(AlgExprGrammar.RANGLE)
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
            return self.getToken(AlgExprGrammar.LBRACE, 0)

        def POW(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.POW)
            else:
                return self.getToken(AlgExprGrammar.POW, i)

        def RBRACE(self):
            return self.getToken(AlgExprGrammar.RBRACE, 0)

        def ID(self):
            return self.getToken(AlgExprGrammar.ID, 0)

        def UNDERSCORE(self):
            return self.getToken(AlgExprGrammar.UNDERSCORE, 0)

        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,i)


        def BANG(self):
            return self.getToken(AlgExprGrammar.BANG, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_combinatorial

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

        localctx = AlgExprGrammar.CombinatorialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_combinatorial)
        self._la = 0 # Token type
        try:
            self.state = 712
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 702
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                if la_ == 1:
                    self.state = 684
                    self.match(AlgExprGrammar.LBRACE)
                    self.state = 685
                    _la = self._input.LA(1)
                    if not(_la==17 or _la==44):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 686
                    localctx.n = self.a_expr(0)
                    self.state = 687
                    localctx.op = self.match(AlgExprGrammar.ID)
                    self.state = 688
                    if not (None if localctx._ID is None else localctx._ID.text) == 'C':
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$ID.text == 'C'")
                    self.state = 689
                    if not ((None if localctx.op is None else localctx.op.text) in Ast.CombOpId):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "($op.text in Ast.CombOpId)")
                    self.state = 690
                    self.match(AlgExprGrammar.POW)
                    self.state = 691
                    localctx.k = self.a_expr(0)
                    self.state = 692
                    self.match(AlgExprGrammar.RBRACE)
                    localctx.res = Ast.combOpFromId(localctx, localctx.n.res, localctx.k.res, Ast.CombOpId((None if localctx.op is None else localctx.op.text)))
                    pass

                elif la_ == 2:
                    self.state = 695
                    self.match(AlgExprGrammar.LBRACE)
                    self.state = 696
                    localctx._ID = self.match(AlgExprGrammar.ID)
                    self.state = 697
                    if not (None if localctx._ID is None else localctx._ID.text) == 'D':
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$ID.text == 'D'")
                    self.state = 698
                    self.match(AlgExprGrammar.POW)
                    self.state = 699
                    localctx.n = self.a_expr(0)
                    self.state = 700
                    self.match(AlgExprGrammar.RBRACE)
                    pass


                localctx.res = Ast.Derangements(localctx, localctx.n.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 706
                self.match(AlgExprGrammar.LBRACE)
                self.state = 707
                self.match(AlgExprGrammar.BANG)
                self.state = 708
                localctx.n = self.a_expr(0)
                self.state = 709
                self.match(AlgExprGrammar.RBRACE)
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
            return self.getToken(AlgExprGrammar.FRAC, 0)

        def latex_cmd_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgExprGrammar.Latex_cmd_argContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.Latex_cmd_argContext,i)


        def BINOM(self):
            return self.getToken(AlgExprGrammar.BINOM, 0)

        def SQRT(self):
            return self.getToken(AlgExprGrammar.SQRT, 0)

        def LBRACKET(self):
            return self.getToken(AlgExprGrammar.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(AlgExprGrammar.RBRACKET, 0)

        def a_expr(self):
            return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,0)


        def CONJUGATE(self):
            return self.getToken(AlgExprGrammar.CONJUGATE, 0)

        def VEC_UNIT(self):
            return self.getToken(AlgExprGrammar.VEC_UNIT, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_cmd_func

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

        localctx = AlgExprGrammar.Cmd_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_cmd_func)
        self._la = 0 # Token type
        try:
            self.state = 746
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 714
                self.match(AlgExprGrammar.FRAC)
                self.state = 715
                localctx.num = self.latex_cmd_arg()
                self.state = 716
                localctx.den = self.latex_cmd_arg()
                localctx.res = Ast.DivOp(localctx, localctx.num.res, localctx.den.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 719
                self.match(AlgExprGrammar.BINOM)
                self.state = 720
                localctx.n = self.latex_cmd_arg()
                self.state = 721
                localctx.k = self.latex_cmd_arg()
                localctx.res = Ast.Binom(localctx, localctx.n.res, localctx.k.res)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 724
                self.match(AlgExprGrammar.SQRT)
                self.state = 725
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Root(localctx, localctx._latex_cmd_arg.res, None) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 728
                self.match(AlgExprGrammar.SQRT)
                self.state = 733
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==55:
                    self.state = 729
                    self.match(AlgExprGrammar.LBRACKET)
                    self.state = 730
                    localctx.root_index = self.a_expr(0)
                    self.state = 731
                    self.match(AlgExprGrammar.RBRACKET)


                self.state = 735
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Root(localctx, localctx._latex_cmd_arg.res, localctx.root_index.res)
                        
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 738
                self.match(AlgExprGrammar.CONJUGATE)
                self.state = 739
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Conjugate(localctx, localctx._latex_cmd_arg.res)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 742
                self.match(AlgExprGrammar.VEC_UNIT)
                self.state = 743
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
                return self.getTypedRuleContexts(AlgExprGrammar.A_exprContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.A_exprContext,i)


        def ENV_EL_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.ENV_EL_SEP)
            else:
                return self.getToken(AlgExprGrammar.ENV_EL_SEP, i)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_matrix_row

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

        localctx = AlgExprGrammar.Matrix_rowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_matrix_row)
        self._la = 0 # Token type
        try:
            self.state = 760
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [69, 71, 73, 77]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1, 12, 13, 26, 27, 28, 29, 30, 32, 34, 35, 36, 38, 39, 49, 51, 55, 59, 61, 63, 65, 66, 68, 70, 72, 79, 83, 84, 85]:
                self.enterOuterAlt(localctx, 2)
                self.state = 749
                localctx._a_expr = self.a_expr(0)
                localctx.res = [localctx._a_expr.res]
                self.state = 757
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==76:
                    self.state = 751
                    self.match(AlgExprGrammar.ENV_EL_SEP)
                    self.state = 752
                    localctx._a_expr = self.a_expr(0)
                    localctx.res.append(localctx._a_expr.res)
                    self.state = 759
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
                return self.getTypedRuleContexts(AlgExprGrammar.Matrix_rowContext)
            else:
                return self.getTypedRuleContext(AlgExprGrammar.Matrix_rowContext,i)


        def ENV_ROW_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(AlgExprGrammar.ENV_ROW_SEP)
            else:
                return self.getToken(AlgExprGrammar.ENV_ROW_SEP, i)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_matrix_body

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

        localctx = AlgExprGrammar.Matrix_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_matrix_body)
        self._la = 0 # Token type
        try:
            self.state = 780
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 763
                localctx._matrix_row = self.matrix_row()
                localctx.res = [localctx._matrix_row.res]
                self.state = 771
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 765
                        self.match(AlgExprGrammar.ENV_ROW_SEP)
                        self.state = 766
                        localctx._matrix_row = self.matrix_row()
                        localctx.res.append(localctx._matrix_row.res) 
                    self.state = 773
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

                self.state = 777
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==77:
                    self.state = 774
                    self.match(AlgExprGrammar.ENV_ROW_SEP)
                    self.state = 779
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
            return self.getTypedRuleContext(AlgExprGrammar.Matrix_bodyContext,0)


        def BEGIN_MATRIX(self):
            return self.getToken(AlgExprGrammar.BEGIN_MATRIX, 0)

        def END_MATRIX(self):
            return self.getToken(AlgExprGrammar.END_MATRIX, 0)

        def BEGIN_ARRAY(self):
            return self.getToken(AlgExprGrammar.BEGIN_ARRAY, 0)

        def END_ARRAY(self):
            return self.getToken(AlgExprGrammar.END_ARRAY, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_matrix

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

        localctx = AlgExprGrammar.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 790
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [68]:
                self.state = 782
                localctx.beg = self.match(AlgExprGrammar.BEGIN_MATRIX)
                self.state = 783
                localctx._matrix_body = self.matrix_body()
                self.state = 784
                localctx.end = self.match(AlgExprGrammar.END_MATRIX)
                pass
            elif token in [72]:
                self.state = 786
                localctx.beg = self.match(AlgExprGrammar.BEGIN_ARRAY)
                self.state = 787
                localctx._matrix_body = self.matrix_body()
                self.state = 788
                localctx.end = self.match(AlgExprGrammar.END_ARRAY)
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
            return self.getToken(AlgExprGrammar.BEGIN_V_MATRIX, 0)

        def matrix_body(self):
            return self.getTypedRuleContext(AlgExprGrammar.Matrix_bodyContext,0)


        def END_V_MATRIX(self):
            return self.getToken(AlgExprGrammar.END_V_MATRIX, 0)

        def getRuleIndex(self):
            return AlgExprGrammar.RULE_det_matrix

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

        localctx = AlgExprGrammar.Det_matrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_det_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 794
            self.match(AlgExprGrammar.BEGIN_V_MATRIX)
            self.state = 795
            localctx._matrix_body = self.matrix_body()
            self.state = 796
            self.match(AlgExprGrammar.END_V_MATRIX)
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
        self._predicates[30] = self.combinatorial_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def a_expr_sempred(self, localctx:A_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 3:
                return ((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS, self.LPAREN))
         

            if predIndex == 4:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 8)
         

    def combinatorial_sempred(self, localctx:CombinatorialContext, predIndex:int):
            if predIndex == 8:
                return (None if localctx._ID is None else localctx._ID.text) == 'C'
         

            if predIndex == 9:
                return ((None if localctx.op is None else localctx.op.text) in Ast.CombOpId)
         

            if predIndex == 10:
                return (None if localctx._ID is None else localctx._ID.text) == 'D'
         





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
from typing import cast

def serializedATN():
    return [
        4,1,78,615,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,0,1,0,1,0,1,0,3,0,65,8,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,3,1,74,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,99,8,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,115,
        8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,128,8,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,141,8,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,157,8,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,171,8,2,10,2,12,2,174,
        9,2,3,2,176,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,201,8,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,213,8,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,223,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,245,8,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,254,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,269,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,296,8,2,1,2,5,2,299,8,2,10,2,12,2,302,9,2,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,3,4,311,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,321,8,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,334,8,6,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,349,8,7,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,361,8,8,1,9,4,9,364,8,9,11,
        9,12,9,365,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,3,10,380,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,402,
        8,11,1,12,1,12,1,12,1,12,3,12,408,8,12,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,1,14,1,14,3,14,420,8,14,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,3,15,445,8,15,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,3,16,471,8,16,1,17,1,17,1,18,3,18,
        476,8,18,1,18,1,18,3,18,480,8,18,1,19,1,19,1,20,1,20,1,20,1,20,3,
        20,488,8,20,1,21,1,21,3,21,492,8,21,1,21,1,21,1,21,4,21,497,8,21,
        11,21,12,21,498,1,21,3,21,502,8,21,1,21,1,21,1,21,1,21,3,21,508,
        8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,529,8,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,542,8,22,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,5,23,551,8,23,10,23,12,23,554,9,23,3,23,
        556,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,5,24,565,8,24,10,24,
        12,24,568,9,24,1,24,5,24,571,8,24,10,24,12,24,574,9,24,3,24,576,
        8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,586,8,25,1,25,
        1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,5,27,597,8,27,10,27,12,27,
        600,9,27,1,27,5,27,603,8,27,10,27,12,27,606,9,27,3,27,608,8,27,1,
        28,1,28,1,28,1,28,1,28,1,28,0,1,4,29,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,0,9,1,0,26,
        27,1,0,9,14,1,0,4,5,2,0,35,35,56,56,2,0,8,8,36,36,2,0,39,39,78,78,
        2,0,6,6,38,38,2,0,42,42,46,46,2,0,35,35,37,37,673,0,64,1,0,0,0,2,
        73,1,0,0,0,4,244,1,0,0,0,6,303,1,0,0,0,8,310,1,0,0,0,10,320,1,0,
        0,0,12,333,1,0,0,0,14,348,1,0,0,0,16,360,1,0,0,0,18,363,1,0,0,0,
        20,379,1,0,0,0,22,401,1,0,0,0,24,407,1,0,0,0,26,409,1,0,0,0,28,419,
        1,0,0,0,30,444,1,0,0,0,32,470,1,0,0,0,34,472,1,0,0,0,36,475,1,0,
        0,0,38,481,1,0,0,0,40,487,1,0,0,0,42,507,1,0,0,0,44,541,1,0,0,0,
        46,555,1,0,0,0,48,575,1,0,0,0,50,585,1,0,0,0,52,589,1,0,0,0,54,607,
        1,0,0,0,56,609,1,0,0,0,58,59,3,56,28,0,59,60,6,0,-1,0,60,65,1,0,
        0,0,61,62,3,4,2,0,62,63,6,0,-1,0,63,65,1,0,0,0,64,58,1,0,0,0,64,
        61,1,0,0,0,65,66,1,0,0,0,66,67,5,0,0,1,67,1,1,0,0,0,68,69,3,4,2,
        0,69,70,3,6,3,0,70,71,3,2,1,0,71,74,1,0,0,0,72,74,3,4,2,0,73,68,
        1,0,0,0,73,72,1,0,0,0,74,3,1,0,0,0,75,76,6,2,-1,0,76,77,5,24,0,0,
        77,78,3,14,7,0,78,79,5,18,0,0,79,80,5,40,0,0,80,81,5,25,0,0,81,82,
        3,4,2,0,82,83,5,41,0,0,83,84,3,10,5,0,84,85,6,2,-1,0,85,245,1,0,
        0,0,86,87,5,24,0,0,87,88,3,14,7,0,88,89,3,4,2,0,89,90,5,25,0,0,90,
        91,3,4,2,23,91,92,6,2,-1,0,92,245,1,0,0,0,93,98,5,27,0,0,94,95,5,
        46,0,0,95,96,3,4,2,0,96,97,5,47,0,0,97,99,1,0,0,0,98,94,1,0,0,0,
        98,99,1,0,0,0,99,100,1,0,0,0,100,101,3,10,5,0,101,102,5,40,0,0,102,
        103,3,4,2,0,103,104,5,41,0,0,104,105,5,40,0,0,105,106,3,4,2,0,106,
        107,5,41,0,0,107,108,6,2,-1,0,108,245,1,0,0,0,109,114,7,0,0,0,110,
        111,5,46,0,0,111,112,3,4,2,0,112,113,5,47,0,0,113,115,1,0,0,0,114,
        110,1,0,0,0,114,115,1,0,0,0,115,116,1,0,0,0,116,117,3,10,5,0,117,
        118,5,40,0,0,118,119,3,4,2,0,119,120,5,41,0,0,120,121,6,2,-1,0,121,
        245,1,0,0,0,122,127,7,0,0,0,123,124,5,46,0,0,124,125,3,4,2,0,125,
        126,5,47,0,0,126,128,1,0,0,0,127,123,1,0,0,0,127,128,1,0,0,0,128,
        129,1,0,0,0,129,130,3,10,5,0,130,131,3,4,2,19,131,132,6,2,-1,0,132,
        245,1,0,0,0,133,134,5,18,0,0,134,135,5,40,0,0,135,140,5,25,0,0,136,
        137,5,46,0,0,137,138,3,4,2,0,138,139,5,47,0,0,139,141,1,0,0,0,140,
        136,1,0,0,0,140,141,1,0,0,0,141,142,1,0,0,0,142,143,3,4,2,0,143,
        144,5,41,0,0,144,145,5,40,0,0,145,146,3,18,9,0,146,147,5,41,0,0,
        147,148,6,2,-1,0,148,245,1,0,0,0,149,150,5,18,0,0,150,151,5,40,0,
        0,151,156,5,25,0,0,152,153,5,46,0,0,153,154,3,4,2,0,154,155,5,47,
        0,0,155,157,1,0,0,0,156,152,1,0,0,0,156,157,1,0,0,0,157,158,1,0,
        0,0,158,159,5,41,0,0,159,160,5,40,0,0,160,161,3,18,9,0,161,162,5,
        41,0,0,162,163,3,4,2,17,163,164,6,2,-1,0,164,245,1,0,0,0,165,166,
        5,1,0,0,166,175,5,42,0,0,167,172,3,4,2,0,168,169,5,35,0,0,169,171,
        3,4,2,0,170,168,1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,172,173,
        1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,0,175,167,1,0,0,0,175,176,
        1,0,0,0,176,177,1,0,0,0,177,245,5,43,0,0,178,179,5,1,0,0,179,180,
        5,40,0,0,180,181,3,4,2,0,181,182,5,41,0,0,182,245,1,0,0,0,183,184,
        5,1,0,0,184,245,3,4,2,14,185,186,5,28,0,0,186,187,5,36,0,0,187,188,
        5,40,0,0,188,189,3,28,14,0,189,190,5,29,0,0,190,191,3,4,2,0,191,
        192,3,20,10,0,192,193,5,41,0,0,193,194,3,4,2,13,194,195,6,2,-1,0,
        195,245,1,0,0,0,196,197,5,30,0,0,197,201,6,2,-1,0,198,199,5,31,0,
        0,199,201,6,2,-1,0,200,196,1,0,0,0,200,198,1,0,0,0,201,202,1,0,0,
        0,202,203,3,22,11,0,203,204,5,42,0,0,204,205,3,4,2,0,205,206,5,43,
        0,0,206,207,6,2,-1,0,207,245,1,0,0,0,208,209,5,30,0,0,209,213,6,
        2,-1,0,210,211,5,31,0,0,211,213,6,2,-1,0,212,208,1,0,0,0,212,210,
        1,0,0,0,213,214,1,0,0,0,214,215,3,22,11,0,215,216,3,4,2,9,216,217,
        6,2,-1,0,217,245,1,0,0,0,218,219,5,4,0,0,219,223,6,2,-1,0,220,221,
        5,5,0,0,221,223,6,2,-1,0,222,218,1,0,0,0,222,220,1,0,0,0,223,224,
        1,0,0,0,224,225,3,4,2,7,225,226,6,2,-1,0,226,245,1,0,0,0,227,228,
        3,32,16,0,228,229,6,2,-1,0,229,245,1,0,0,0,230,231,3,30,15,0,231,
        232,6,2,-1,0,232,245,1,0,0,0,233,234,3,44,22,0,234,235,6,2,-1,0,
        235,245,1,0,0,0,236,237,3,50,25,0,237,238,6,2,-1,0,238,245,1,0,0,
        0,239,240,3,28,14,0,240,241,6,2,-1,0,241,245,1,0,0,0,242,243,5,69,
        0,0,243,245,6,2,-1,0,244,75,1,0,0,0,244,86,1,0,0,0,244,93,1,0,0,
        0,244,109,1,0,0,0,244,122,1,0,0,0,244,133,1,0,0,0,244,149,1,0,0,
        0,244,165,1,0,0,0,244,178,1,0,0,0,244,183,1,0,0,0,244,185,1,0,0,
        0,244,200,1,0,0,0,244,212,1,0,0,0,244,222,1,0,0,0,244,227,1,0,0,
        0,244,230,1,0,0,0,244,233,1,0,0,0,244,236,1,0,0,0,244,239,1,0,0,
        0,244,242,1,0,0,0,245,300,1,0,0,0,246,253,10,12,0,0,247,248,5,6,
        0,0,248,254,6,2,-1,0,249,250,5,7,0,0,250,254,6,2,-1,0,251,252,5,
        23,0,0,252,254,6,2,-1,0,253,247,1,0,0,0,253,249,1,0,0,0,253,251,
        1,0,0,0,254,255,1,0,0,0,255,256,3,4,2,13,256,257,6,2,-1,0,257,299,
        1,0,0,0,258,259,10,11,0,0,259,260,4,2,2,0,260,261,3,4,2,12,261,262,
        6,2,-1,0,262,299,1,0,0,0,263,268,10,8,0,0,264,265,5,4,0,0,265,269,
        6,2,-1,0,266,267,5,5,0,0,267,269,6,2,-1,0,268,264,1,0,0,0,268,266,
        1,0,0,0,269,270,1,0,0,0,270,271,3,4,2,9,271,272,6,2,-1,0,272,299,
        1,0,0,0,273,274,10,27,0,0,274,275,5,8,0,0,275,276,3,12,6,0,276,277,
        5,36,0,0,277,278,3,42,21,0,278,279,6,2,-1,0,279,299,1,0,0,0,280,
        281,10,26,0,0,281,282,5,8,0,0,282,283,3,12,6,0,283,284,6,2,-1,0,
        284,299,1,0,0,0,285,286,10,25,0,0,286,287,5,36,0,0,287,299,3,42,
        21,0,288,295,10,22,0,0,289,290,5,32,0,0,290,296,6,2,-1,0,291,292,
        5,33,0,0,292,296,6,2,-1,0,293,294,5,34,0,0,294,296,6,2,-1,0,295,
        289,1,0,0,0,295,291,1,0,0,0,295,293,1,0,0,0,296,297,1,0,0,0,297,
        299,6,2,-1,0,298,246,1,0,0,0,298,258,1,0,0,0,298,263,1,0,0,0,298,
        273,1,0,0,0,298,280,1,0,0,0,298,285,1,0,0,0,298,288,1,0,0,0,299,
        302,1,0,0,0,300,298,1,0,0,0,300,301,1,0,0,0,301,5,1,0,0,0,302,300,
        1,0,0,0,303,304,7,1,0,0,304,7,1,0,0,0,305,306,3,24,12,0,306,307,
        6,4,-1,0,307,311,1,0,0,0,308,309,5,69,0,0,309,311,6,4,-1,0,310,305,
        1,0,0,0,310,308,1,0,0,0,311,9,1,0,0,0,312,313,3,8,4,0,313,314,6,
        5,-1,0,314,321,1,0,0,0,315,316,5,40,0,0,316,317,3,4,2,0,317,318,
        5,41,0,0,318,319,6,5,-1,0,319,321,1,0,0,0,320,312,1,0,0,0,320,315,
        1,0,0,0,321,11,1,0,0,0,322,323,3,8,4,0,323,324,6,6,-1,0,324,334,
        1,0,0,0,325,326,3,44,22,0,326,327,6,6,-1,0,327,334,1,0,0,0,328,329,
        5,40,0,0,329,330,3,4,2,0,330,331,5,41,0,0,331,332,6,6,-1,0,332,334,
        1,0,0,0,333,322,1,0,0,0,333,325,1,0,0,0,333,328,1,0,0,0,334,13,1,
        0,0,0,335,336,5,8,0,0,336,337,3,10,5,0,337,338,5,36,0,0,338,339,
        3,10,5,0,339,340,6,7,-1,0,340,349,1,0,0,0,341,342,5,36,0,0,342,343,
        3,10,5,0,343,344,5,8,0,0,344,345,3,10,5,0,345,346,6,7,-1,0,346,349,
        1,0,0,0,347,349,6,7,-1,0,348,335,1,0,0,0,348,341,1,0,0,0,348,347,
        1,0,0,0,349,15,1,0,0,0,350,351,5,25,0,0,351,352,3,4,2,0,352,353,
        5,8,0,0,353,354,3,10,5,0,354,355,6,8,-1,0,355,361,1,0,0,0,356,357,
        5,25,0,0,357,358,3,4,2,0,358,359,6,8,-1,0,359,361,1,0,0,0,360,350,
        1,0,0,0,360,356,1,0,0,0,361,17,1,0,0,0,362,364,3,16,8,0,363,362,
        1,0,0,0,364,365,1,0,0,0,365,363,1,0,0,0,365,366,1,0,0,0,366,19,1,
        0,0,0,367,380,6,10,-1,0,368,369,5,8,0,0,369,370,5,40,0,0,370,371,
        7,2,0,0,371,372,5,41,0,0,372,380,6,10,-1,0,373,374,5,8,0,0,374,375,
        5,4,0,0,375,380,6,10,-1,0,376,377,5,8,0,0,377,378,5,5,0,0,378,380,
        6,10,-1,0,379,367,1,0,0,0,379,368,1,0,0,0,379,373,1,0,0,0,379,376,
        1,0,0,0,380,21,1,0,0,0,381,382,5,36,0,0,382,383,5,40,0,0,383,384,
        3,4,2,0,384,385,5,9,0,0,385,386,3,4,2,0,386,387,5,41,0,0,387,388,
        5,8,0,0,388,389,3,12,6,0,389,390,6,11,-1,0,390,402,1,0,0,0,391,392,
        5,8,0,0,392,393,3,12,6,0,393,394,5,36,0,0,394,395,5,40,0,0,395,396,
        3,4,2,0,396,397,5,9,0,0,397,398,3,4,2,0,398,399,5,41,0,0,399,400,
        6,11,-1,0,400,402,1,0,0,0,401,381,1,0,0,0,401,391,1,0,0,0,402,23,
        1,0,0,0,403,404,5,74,0,0,404,408,6,12,-1,0,405,406,5,75,0,0,406,
        408,6,12,-1,0,407,403,1,0,0,0,407,405,1,0,0,0,408,25,1,0,0,0,409,
        410,5,73,0,0,410,411,3,24,12,0,411,412,6,13,-1,0,412,27,1,0,0,0,
        413,414,3,24,12,0,414,415,6,14,-1,0,415,420,1,0,0,0,416,417,3,26,
        13,0,417,418,6,14,-1,0,418,420,1,0,0,0,419,413,1,0,0,0,419,416,1,
        0,0,0,420,29,1,0,0,0,421,422,5,42,0,0,422,423,3,4,2,0,423,424,5,
        43,0,0,424,425,6,15,-1,0,425,445,1,0,0,0,426,427,5,56,0,0,427,428,
        3,4,2,0,428,429,5,56,0,0,429,445,1,0,0,0,430,431,5,52,0,0,431,432,
        3,4,2,0,432,433,5,53,0,0,433,445,1,0,0,0,434,435,5,50,0,0,435,436,
        3,4,2,0,436,437,5,51,0,0,437,445,1,0,0,0,438,439,5,54,0,0,439,440,
        3,4,2,0,440,441,7,3,0,0,441,442,3,4,2,0,442,443,5,55,0,0,443,445,
        1,0,0,0,444,421,1,0,0,0,444,426,1,0,0,0,444,430,1,0,0,0,444,434,
        1,0,0,0,444,438,1,0,0,0,445,31,1,0,0,0,446,447,5,40,0,0,447,448,
        7,4,0,0,448,449,3,4,2,0,449,450,5,74,0,0,450,451,4,16,8,1,451,452,
        5,8,0,0,452,453,3,4,2,0,453,454,5,41,0,0,454,455,6,16,-1,0,455,471,
        1,0,0,0,456,457,5,40,0,0,457,458,5,74,0,0,458,459,4,16,9,1,459,460,
        5,8,0,0,460,461,3,4,2,0,461,462,5,41,0,0,462,463,6,16,-1,0,463,471,
        1,0,0,0,464,465,5,40,0,0,465,466,5,32,0,0,466,467,3,4,2,0,467,468,
        5,41,0,0,468,469,6,16,-1,0,469,471,1,0,0,0,470,446,1,0,0,0,470,456,
        1,0,0,0,470,464,1,0,0,0,471,33,1,0,0,0,472,473,3,4,2,0,473,35,1,
        0,0,0,474,476,3,4,2,0,475,474,1,0,0,0,475,476,1,0,0,0,476,477,1,
        0,0,0,477,479,7,5,0,0,478,480,3,4,2,0,479,478,1,0,0,0,479,480,1,
        0,0,0,480,37,1,0,0,0,481,482,7,6,0,0,482,39,1,0,0,0,483,488,3,34,
        17,0,484,488,3,36,18,0,485,488,3,38,19,0,486,488,1,0,0,0,487,483,
        1,0,0,0,487,484,1,0,0,0,487,485,1,0,0,0,487,486,1,0,0,0,488,41,1,
        0,0,0,489,491,5,40,0,0,490,492,7,7,0,0,491,490,1,0,0,0,491,492,1,
        0,0,0,492,493,1,0,0,0,493,496,3,40,20,0,494,495,7,8,0,0,495,497,
        3,40,20,0,496,494,1,0,0,0,497,498,1,0,0,0,498,496,1,0,0,0,498,499,
        1,0,0,0,499,501,1,0,0,0,500,502,7,7,0,0,501,500,1,0,0,0,501,502,
        1,0,0,0,502,503,1,0,0,0,503,504,5,41,0,0,504,508,1,0,0,0,505,508,
        3,8,4,0,506,508,3,44,22,0,507,489,1,0,0,0,507,505,1,0,0,0,507,506,
        1,0,0,0,508,43,1,0,0,0,509,510,5,18,0,0,510,511,3,10,5,0,511,512,
        3,10,5,0,512,513,6,22,-1,0,513,542,1,0,0,0,514,515,5,19,0,0,515,
        516,3,10,5,0,516,517,3,10,5,0,517,518,6,22,-1,0,518,542,1,0,0,0,
        519,520,5,20,0,0,520,521,3,10,5,0,521,522,6,22,-1,0,522,542,1,0,
        0,0,523,528,5,20,0,0,524,525,5,46,0,0,525,526,3,4,2,0,526,527,5,
        47,0,0,527,529,1,0,0,0,528,524,1,0,0,0,528,529,1,0,0,0,529,530,1,
        0,0,0,530,531,3,10,5,0,531,532,6,22,-1,0,532,542,1,0,0,0,533,534,
        5,21,0,0,534,535,3,10,5,0,535,536,6,22,-1,0,536,542,1,0,0,0,537,
        538,5,22,0,0,538,539,3,10,5,0,539,540,6,22,-1,0,540,542,1,0,0,0,
        541,509,1,0,0,0,541,514,1,0,0,0,541,519,1,0,0,0,541,523,1,0,0,0,
        541,533,1,0,0,0,541,537,1,0,0,0,542,45,1,0,0,0,543,556,1,0,0,0,544,
        545,3,4,2,0,545,552,6,23,-1,0,546,547,5,66,0,0,547,548,3,4,2,0,548,
        549,6,23,-1,0,549,551,1,0,0,0,550,546,1,0,0,0,551,554,1,0,0,0,552,
        550,1,0,0,0,552,553,1,0,0,0,553,556,1,0,0,0,554,552,1,0,0,0,555,
        543,1,0,0,0,555,544,1,0,0,0,556,47,1,0,0,0,557,576,1,0,0,0,558,559,
        3,46,23,0,559,566,6,24,-1,0,560,561,5,67,0,0,561,562,3,46,23,0,562,
        563,6,24,-1,0,563,565,1,0,0,0,564,560,1,0,0,0,565,568,1,0,0,0,566,
        564,1,0,0,0,566,567,1,0,0,0,567,572,1,0,0,0,568,566,1,0,0,0,569,
        571,5,67,0,0,570,569,1,0,0,0,571,574,1,0,0,0,572,570,1,0,0,0,572,
        573,1,0,0,0,573,576,1,0,0,0,574,572,1,0,0,0,575,557,1,0,0,0,575,
        558,1,0,0,0,576,49,1,0,0,0,577,578,5,58,0,0,578,579,3,48,24,0,579,
        580,5,59,0,0,580,586,1,0,0,0,581,582,5,62,0,0,582,583,3,48,24,0,
        583,584,5,63,0,0,584,586,1,0,0,0,585,577,1,0,0,0,585,581,1,0,0,0,
        586,587,1,0,0,0,587,588,6,25,-1,0,588,51,1,0,0,0,589,590,3,4,2,0,
        590,591,6,26,-1,0,591,53,1,0,0,0,592,608,1,0,0,0,593,598,3,52,26,
        0,594,595,5,67,0,0,595,597,3,52,26,0,596,594,1,0,0,0,597,600,1,0,
        0,0,598,596,1,0,0,0,598,599,1,0,0,0,599,604,1,0,0,0,600,598,1,0,
        0,0,601,603,5,67,0,0,602,601,1,0,0,0,603,606,1,0,0,0,604,602,1,0,
        0,0,604,605,1,0,0,0,605,608,1,0,0,0,606,604,1,0,0,0,607,592,1,0,
        0,0,607,593,1,0,0,0,608,55,1,0,0,0,609,610,5,64,0,0,610,611,3,54,
        27,0,611,612,5,65,0,0,612,613,6,28,-1,0,613,57,1,0,0,0,48,64,73,
        98,114,127,140,156,172,175,200,212,222,244,253,268,295,298,300,310,
        320,333,348,360,365,379,401,407,419,444,470,475,479,487,491,498,
        501,507,528,541,552,555,566,572,575,585,598,604,607
    ]

class ExprGrammar ( Parser ):

    grammarFileName = "ExprGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'^'", "'='", "<INVALID>", "'<'", "<INVALID>", "'>'", 
                     "<INVALID>", "'\\times'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\sqrt'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\lim'", "<INVALID>", "'\\sum'", 
                     "'\\prod'", "'!'", "'\\%'", "'\\textperthousand'", 
                     "','", "'_'", "';'", "'\\star'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\{'", "'\\}'", 
                     "'['", "']'", "'\\lbrack'", "'\\rbrack'", "'\\lceil'", 
                     "'\\rceil'", "'\\lfloor'", "'\\rfloor'", "'\\langle'", 
                     "'\\rangle'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'&'", "'\\\\'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\Delta'" ]

    symbolicNames = [ "<INVALID>", "FUNCTION", "CMD_FUNCTION", "IGNORE", 
                      "PLUS", "MINUS", "MULT", "DIV", "POW", "EQ", "NEQ", 
                      "LT", "LTE", "GT", "GTE", "TIMES", "CROSS_PROD", "DOT_PROD", 
                      "FRAC", "BINOM", "SQRT", "CONJUGATE", "VEC_UNIT", 
                      "MOD", "INT", "DIFFERENTIAL", "PHYS_DERIVATIVE", "PHYS_PARTIAL_DERIVATIVE", 
                      "LIMIT", "LIMIT_ARROW", "SUM", "PRODUCT", "BANG", 
                      "PERCENT", "PERMILLE", "COMMA", "UNDERSCORE", "SEMICOLON", 
                      "STAR", "DOTS", "LBRACE", "RBRACE", "LPAREN", "RPAREN", 
                      "LBRACE_LITERAL", "RBRACE_LITERAL", "LBRACKET", "RBRACKET", 
                      "LBRACK_CMD", "RBRACK_CMD", "LCEIL", "RCEIL", "LFLOOR", 
                      "RFLOOR", "LANGLE", "RANGLE", "BAR", "DOUBLE_BAR", 
                      "BEGIN_MATRIX", "END_MATRIX", "BEGIN_V_MATRIX", "END_V_MATRIX", 
                      "BEGIN_ARRAY", "END_ARRAY", "BEGIN_ENV", "END_ENV", 
                      "ENV_EL_SEP", "ENV_ROW_SEP", "ENV_SEP_SKIP", "NUMBER", 
                      "BIN_NUMBER", "OCT_NUMBER", "HEX_NUMBER", "DELTA", 
                      "ID", "COMMAND", "ARG_COMM", "ARG_WS", "COLON" ]

    RULE_debug = 0
    RULE_relation = 1
    RULE_a_expr = 2
    RULE_rel_op = 3
    RULE_atom = 4
    RULE_latex_cmd_arg = 5
    RULE_pow_arg = 6
    RULE_int_bounds = 7
    RULE_diff_var = 8
    RULE_diff_vars = 9
    RULE_limit_dir = 10
    RULE_series_range_args = 11
    RULE_primary_symbol = 12
    RULE_delta_symbol = 13
    RULE_symbol = 14
    RULE_delim_expr = 15
    RULE_combinatorial = 16
    RULE_singular_index = 17
    RULE_range_index = 18
    RULE_all_index = 19
    RULE_index_entry = 20
    RULE_index_arg = 21
    RULE_builtin_func = 22
    RULE_matrix_row = 23
    RULE_matrix_body = 24
    RULE_matrix = 25
    RULE_expr_system_expr = 26
    RULE_expr_system_body = 27
    RULE_expr_system = 28

    ruleNames =  [ "debug", "relation", "a_expr", "rel_op", "atom", "latex_cmd_arg", 
                   "pow_arg", "int_bounds", "diff_var", "diff_vars", "limit_dir", 
                   "series_range_args", "primary_symbol", "delta_symbol", 
                   "symbol", "delim_expr", "combinatorial", "singular_index", 
                   "range_index", "all_index", "index_entry", "index_arg", 
                   "builtin_func", "matrix_row", "matrix_body", "matrix", 
                   "expr_system_expr", "expr_system_body", "expr_system" ]

    EOF = Token.EOF
    FUNCTION=1
    CMD_FUNCTION=2
    IGNORE=3
    PLUS=4
    MINUS=5
    MULT=6
    DIV=7
    POW=8
    EQ=9
    NEQ=10
    LT=11
    LTE=12
    GT=13
    GTE=14
    TIMES=15
    CROSS_PROD=16
    DOT_PROD=17
    FRAC=18
    BINOM=19
    SQRT=20
    CONJUGATE=21
    VEC_UNIT=22
    MOD=23
    INT=24
    DIFFERENTIAL=25
    PHYS_DERIVATIVE=26
    PHYS_PARTIAL_DERIVATIVE=27
    LIMIT=28
    LIMIT_ARROW=29
    SUM=30
    PRODUCT=31
    BANG=32
    PERCENT=33
    PERMILLE=34
    COMMA=35
    UNDERSCORE=36
    SEMICOLON=37
    STAR=38
    DOTS=39
    LBRACE=40
    RBRACE=41
    LPAREN=42
    RPAREN=43
    LBRACE_LITERAL=44
    RBRACE_LITERAL=45
    LBRACKET=46
    RBRACKET=47
    LBRACK_CMD=48
    RBRACK_CMD=49
    LCEIL=50
    RCEIL=51
    LFLOOR=52
    RFLOOR=53
    LANGLE=54
    RANGLE=55
    BAR=56
    DOUBLE_BAR=57
    BEGIN_MATRIX=58
    END_MATRIX=59
    BEGIN_V_MATRIX=60
    END_V_MATRIX=61
    BEGIN_ARRAY=62
    END_ARRAY=63
    BEGIN_ENV=64
    END_ENV=65
    ENV_EL_SEP=66
    ENV_ROW_SEP=67
    ENV_SEP_SKIP=68
    NUMBER=69
    BIN_NUMBER=70
    OCT_NUMBER=71
    HEX_NUMBER=72
    DELTA=73
    ID=74
    COMMAND=75
    ARG_COMM=76
    ARG_WS=77
    COLON=78

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
            self.res = cast(Ast.Expr, None)
            self._expr_system = None # Expr_systemContext
            self._a_expr = None # A_exprContext

        def EOF(self):
            return self.getToken(ExprGrammar.EOF, 0)

        def expr_system(self):
            return self.getTypedRuleContext(ExprGrammar.Expr_systemContext,0)


        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


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
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 58
                localctx._expr_system = self.expr_system()
                localctx.res = localctx._expr_system.res
                pass
            elif token in [1, 4, 5, 18, 19, 20, 21, 22, 24, 26, 27, 28, 30, 31, 40, 42, 50, 52, 54, 56, 58, 62, 69, 73, 74, 75]:
                self.state = 61
                localctx._a_expr = self.a_expr(0)
                localctx.res = localctx._a_expr.res
                pass
            else:
                raise NoViableAltException(self)

            self.state = 66
            self.match(ExprGrammar.EOF)
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

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


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
        self.enterRule(localctx, 2, self.RULE_relation)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.a_expr(0)
                self.state = 69
                self.rel_op()
                self.state = 70
                self.relation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
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
            self.res = cast(Ast.Expr, None)
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
            self._builtin_func = None # Builtin_funcContext
            self._matrix = None # MatrixContext
            self._symbol = None # SymbolContext
            self._NUMBER = None # Token
            self.copyFrom(ctx)

        def builtin_func(self):
            return self.getTypedRuleContext(ExprGrammar.Builtin_funcContext,0)

        def matrix(self):
            return self.getTypedRuleContext(ExprGrammar.MatrixContext,0)

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
            self.index = None # Index_argContext
            self.copyFrom(ctx)

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)

        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_a_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = ExprGrammar.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 76
                self.match(ExprGrammar.INT)
                self.state = 77
                localctx._int_bounds = self.int_bounds()
                self.state = 78
                self.match(ExprGrammar.FRAC)
                self.state = 79
                self.match(ExprGrammar.LBRACE)
                self.state = 80
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 81
                localctx.diff = localctx._a_expr = self.a_expr(0)
                self.state = 82
                self.match(ExprGrammar.RBRACE)
                self.state = 83
                localctx.recip_integrand = localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Integral(localctx, Ast.DivOp(localctx.recip_integrand, Ast.Number(localctx.recip_integrand, "1"), localctx.recip_integrand.res), localctx.diff.res, localctx._int_bounds.bounds)
                pass

            elif la_ == 2:
                localctx = ExprGrammar.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 86
                self.match(ExprGrammar.INT)
                self.state = 87
                localctx._int_bounds = self.int_bounds()
                self.state = 88
                localctx.integrand = localctx._a_expr = self.a_expr(0)
                self.state = 89
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 90
                localctx.diff = localctx._a_expr = self.a_expr(23)
                localctx.res = Ast.Integral(localctx, localctx.integrand.res, localctx.diff.res, localctx._int_bounds.bounds)
                pass

            elif la_ == 3:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 93
                self.match(ExprGrammar.PHYS_PARTIAL_DERIVATIVE)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 94
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 95
                    localctx._a_expr = self.a_expr(0)
                    self.state = 96
                    self.match(ExprGrammar.RBRACKET)


                self.state = 100
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 101
                self.match(ExprGrammar.LBRACE)
                self.state = 102
                localctx.diff_l = localctx._a_expr = self.a_expr(0)
                self.state = 103
                self.match(ExprGrammar.RBRACE)
                self.state = 104
                self.match(ExprGrammar.LBRACE)
                self.state = 105
                localctx.diff_r = localctx._a_expr = self.a_expr(0)
                self.state = 106
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._latex_cmd_arg.res, [(localctx.diff_l.res, None), (localctx.diff_r.res, None)])
                pass

            elif la_ == 4:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 110
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 111
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 112
                    self.match(ExprGrammar.RBRACKET)


                self.state = 116
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 117
                self.match(ExprGrammar.LBRACE)
                self.state = 118
                localctx._a_expr = self.a_expr(0)
                self.state = 119
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._latex_cmd_arg.res, [(localctx._a_expr.res, localctx.degree.res)])
                pass

            elif la_ == 5:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 123
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 124
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 125
                    self.match(ExprGrammar.RBRACKET)


                self.state = 129
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 130
                localctx.diffand_last = localctx._a_expr = self.a_expr(19)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, [(localctx._latex_cmd_arg.res, localctx.degree.res)])
                pass

            elif la_ == 6:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                self.match(ExprGrammar.FRAC)
                self.state = 134
                self.match(ExprGrammar.LBRACE)
                self.state = 135
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 136
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 137
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 138
                    self.match(ExprGrammar.RBRACKET)


                self.state = 142
                localctx._a_expr = self.a_expr(0)
                self.state = 143
                self.match(ExprGrammar.RBRACE)
                self.state = 144
                self.match(ExprGrammar.LBRACE)
                self.state = 145
                localctx._diff_vars = self.diff_vars()
                self.state = 146
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, localctx._diff_vars.res)
                pass

            elif la_ == 7:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                self.match(ExprGrammar.FRAC)
                self.state = 150
                self.match(ExprGrammar.LBRACE)
                self.state = 151
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 152
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 153
                    localctx.degree = localctx._a_expr = self.a_expr(0)
                    self.state = 154
                    self.match(ExprGrammar.RBRACKET)


                self.state = 158
                self.match(ExprGrammar.RBRACE)
                self.state = 159
                self.match(ExprGrammar.LBRACE)
                self.state = 160
                localctx._diff_vars = self.diff_vars()
                self.state = 161
                self.match(ExprGrammar.RBRACE)
                self.state = 162
                localctx._a_expr = self.a_expr(17)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, localctx._diff_vars.res)
                pass

            elif la_ == 8:
                localctx = ExprGrammar.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 165
                self.match(ExprGrammar.FUNCTION)
                self.state = 166
                self.match(ExprGrammar.LPAREN)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4995623387934752818) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 113) != 0):
                    self.state = 167
                    localctx._a_expr = self.a_expr(0)
                    self.state = 172
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==35:
                        self.state = 168
                        self.match(ExprGrammar.COMMA)
                        self.state = 169
                        localctx._a_expr = self.a_expr(0)
                        self.state = 174
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 177
                self.match(ExprGrammar.RPAREN)
                pass

            elif la_ == 9:
                localctx = ExprGrammar.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 178
                self.match(ExprGrammar.FUNCTION)
                self.state = 179
                self.match(ExprGrammar.LBRACE)
                self.state = 180
                localctx._a_expr = self.a_expr(0)
                self.state = 181
                self.match(ExprGrammar.RBRACE)
                pass

            elif la_ == 10:
                localctx = ExprGrammar.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 183
                self.match(ExprGrammar.FUNCTION)
                self.state = 184
                localctx._a_expr = self.a_expr(14)
                pass

            elif la_ == 11:
                localctx = ExprGrammar.LimitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 185
                self.match(ExprGrammar.LIMIT)
                self.state = 186
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 187
                self.match(ExprGrammar.LBRACE)
                self.state = 188
                localctx.lim_var = localctx._symbol = self.symbol()
                self.state = 189
                self.match(ExprGrammar.LIMIT_ARROW)
                self.state = 190
                localctx.lim_poa = localctx._a_expr = self.a_expr(0)
                self.state = 191
                localctx._limit_dir = self.limit_dir()
                self.state = 192
                self.match(ExprGrammar.RBRACE)
                self.state = 193
                localctx._a_expr = self.a_expr(13)
                localctx.res = Ast.Limit(localctx._a_expr.res, localctx.lim_var.res, localctx.lim_poa.res, localctx._limit_dir.res)
                pass

            elif la_ == 12:
                localctx = ExprGrammar.SeriesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 200
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [30]:
                    self.state = 196
                    self.match(ExprGrammar.SUM)
                    localctx.node_t = Ast.Sum
                    pass
                elif token in [31]:
                    self.state = 198
                    self.match(ExprGrammar.PRODUCT)
                    localctx.node_t = Ast.Product
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 202
                localctx._series_range_args = self.series_range_args()
                self.state = 203
                self.match(ExprGrammar.LPAREN)
                self.state = 204
                localctx._a_expr = self.a_expr(0)
                self.state = 205
                self.match(ExprGrammar.RPAREN)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res, localctx._series_range_args.symb, (localctx._series_range_args.start, localctx._series_range_args.end))
                pass

            elif la_ == 13:
                localctx = ExprGrammar.SeriesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 212
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [30]:
                    self.state = 208
                    self.match(ExprGrammar.SUM)
                    localctx.node_t = Ast.Sum
                    pass
                elif token in [31]:
                    self.state = 210
                    self.match(ExprGrammar.PRODUCT)
                    localctx.node_t = Ast.Product
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 214
                localctx._series_range_args = self.series_range_args()
                self.state = 215
                localctx._a_expr = self.a_expr(9)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res, localctx._series_range_args.symb, (localctx._series_range_args.start, localctx._series_range_args.end))
                pass

            elif la_ == 14:
                localctx = ExprGrammar.UAdditiveOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 222
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 218
                    self.match(ExprGrammar.PLUS)
                    localctx.node_t = Ast.UPlusOp
                    pass
                elif token in [5]:
                    self.state = 220
                    self.match(ExprGrammar.MINUS)
                    localctx.node_t = Ast.UMinusOp
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 224
                localctx._a_expr = self.a_expr(7)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res)
                pass

            elif la_ == 15:
                localctx = ExprGrammar.CombContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 227
                localctx._combinatorial = self.combinatorial()
                localctx.res = localctx._combinatorial.res
                pass

            elif la_ == 16:
                localctx = ExprGrammar.DelimitedExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 230
                localctx._delim_expr = self.delim_expr()
                localctx.res = localctx._delim_expr.res
                pass

            elif la_ == 17:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 233
                localctx._builtin_func = self.builtin_func()
                localctx.res = localctx._builtin_func.res
                pass

            elif la_ == 18:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 236
                localctx._matrix = self.matrix()
                localctx.res = localctx._matrix.res 
                pass

            elif la_ == 19:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 239
                localctx._symbol = self.symbol()
                localctx.res = localctx._symbol.res
                pass

            elif la_ == 20:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 242
                localctx._NUMBER = self.match(ExprGrammar.NUMBER)
                localctx.res = Ast.Number(localctx, (None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 300
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 298
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = ExprGrammar.MultiplicativeOpContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 246
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 253
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [6]:
                            self.state = 247
                            self.match(ExprGrammar.MULT)
                            localctx.node_t = Ast.MultOp
                            pass
                        elif token in [7]:
                            self.state = 249
                            self.match(ExprGrammar.DIV)
                            localctx.node_t = Ast.DivOp
                            pass
                        elif token in [23]:
                            self.state = 251
                            self.match(ExprGrammar.MOD)
                            localctx.node_t = Ast.ModOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 255
                        localctx.rhs = localctx._a_expr = self.a_expr(13)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 2:
                        localctx = ExprGrammar.MultiplicativeOpContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 258
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 259
                        if not ((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS)):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS))")
                        self.state = 260
                        localctx.rhs = localctx._a_expr = self.a_expr(12)
                        localctx.res = Ast.MultOp(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 3:
                        localctx = ExprGrammar.AdditiveOpContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 263
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 268
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [4]:
                            self.state = 264
                            self.match(ExprGrammar.PLUS)
                            localctx.node_t = Ast.AddOp
                            pass
                        elif token in [5]:
                            self.state = 266
                            self.match(ExprGrammar.MINUS)
                            localctx.node_t = Ast.SubOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 270
                        localctx.rhs = localctx._a_expr = self.a_expr(9)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 4:
                        localctx = ExprGrammar.IndexPowContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 273
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 274
                        self.match(ExprGrammar.POW)
                        self.state = 275
                        localctx.exp = self.pow_arg()
                        self.state = 276
                        self.match(ExprGrammar.UNDERSCORE)
                        self.state = 277
                        localctx.index = self.index_arg()
                        localctx.res=Ast.ExpOp(localctx, localctx.base.res, localctx.exp.res)
                        pass

                    elif la_ == 5:
                        localctx = ExprGrammar.PowContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 280
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 281
                        self.match(ExprGrammar.POW)
                        self.state = 282
                        localctx.exp = self.pow_arg()
                        localctx.res=Ast.ExpOp(localctx, localctx.base.res, localctx.exp.res)
                        pass

                    elif la_ == 6:
                        localctx = ExprGrammar.IndexContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 285
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 286
                        self.match(ExprGrammar.UNDERSCORE)
                        self.state = 287
                        localctx.index = self.index_arg()
                        pass

                    elif la_ == 7:
                        localctx = ExprGrammar.PrefixContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.op = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 288
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 295
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [32]:
                            self.state = 289
                            self.match(ExprGrammar.BANG)
                            localctx.node_t = Ast.Factorial
                            pass
                        elif token in [33]:
                            self.state = 291
                            self.match(ExprGrammar.PERCENT)
                            localctx.node_t = Ast.Percent
                            pass
                        elif token in [34]:
                            self.state = 293
                            self.match(ExprGrammar.PERMILLE)
                            localctx.node_t = Ast.Permille
                            pass
                        else:
                            raise NoViableAltException(self)

                        localctx.res = localctx.node_t(localctx, localctx.op.res)
                        pass

             
                self.state = 302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
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
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [74, 75]:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                localctx._primary_symbol = self.primary_symbol()
                localctx.res = localctx._primary_symbol.res
                pass
            elif token in [69]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
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
        self.enterRule(localctx, 10, self.RULE_latex_cmd_arg)
        try:
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [69, 74, 75]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.match(ExprGrammar.LBRACE)
                self.state = 316
                localctx._a_expr = self.a_expr(0)
                self.state = 317
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
            self._builtin_func = None # Builtin_funcContext
            self._a_expr = None # A_exprContext

        def atom(self):
            return self.getTypedRuleContext(ExprGrammar.AtomContext,0)


        def builtin_func(self):
            return self.getTypedRuleContext(ExprGrammar.Builtin_funcContext,0)


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
        self.enterRule(localctx, 12, self.RULE_pow_arg)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [69, 74, 75]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass
            elif token in [18, 19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                localctx._builtin_func = self.builtin_func()
                localctx.res = localctx._builtin_func.res
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 328
                self.match(ExprGrammar.LBRACE)
                self.state = 329
                localctx._a_expr = self.a_expr(0)
                self.state = 330
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
        self.enterRule(localctx, 14, self.RULE_int_bounds)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.match(ExprGrammar.POW)
                self.state = 336
                localctx.upper = self.latex_cmd_arg()
                self.state = 337
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 338
                localctx.lower = self.latex_cmd_arg()
                localctx.bounds = (localctx.lower.res, localctx.upper.res)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 342
                localctx.lower = self.latex_cmd_arg()
                self.state = 343
                self.match(ExprGrammar.POW)
                self.state = 344
                localctx.upper = self.latex_cmd_arg()
                localctx.bounds = (localctx.lower.res, localctx.upper.res)
                pass
            elif token in [1, 4, 5, 18, 19, 20, 21, 22, 24, 26, 27, 28, 30, 31, 40, 42, 50, 52, 54, 56, 58, 62, 69, 73, 74, 75]:
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
        self.enterRule(localctx, 16, self.RULE_diff_var)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 351
                localctx._a_expr = self.a_expr(0)
                self.state = 352
                self.match(ExprGrammar.POW)
                self.state = 353
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.getInvokingContext(9).res.append((localctx._a_expr.res, localctx._latex_cmd_arg.res))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 357
                localctx._a_expr = self.a_expr(0)
                self.getInvokingContext(9).res.append((localctx._a_expr.res, None))
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
        self.enterRule(localctx, 18, self.RULE_diff_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 362
                self.diff_var()
                self.state = 365 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
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
        self.enterRule(localctx, 20, self.RULE_limit_dir)
        self._la = 0 # Token type
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                localctx.res = Ast.LimitDir.BOTH
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.match(ExprGrammar.POW)
                self.state = 369
                self.match(ExprGrammar.LBRACE)
                self.state = 370
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 371
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.LimitDir.BOTH
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 373
                self.match(ExprGrammar.POW)
                self.state = 374
                self.match(ExprGrammar.PLUS)
                localctx.res = Ast.LimitDir.POSITIVE
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 376
                self.match(ExprGrammar.POW)
                self.state = 377
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
        self.enterRule(localctx, 22, self.RULE_series_range_args)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 382
                self.match(ExprGrammar.LBRACE)
                self.state = 383
                localctx.var = self.a_expr(0)
                self.state = 384
                self.match(ExprGrammar.EQ)
                self.state = 385
                localctx.s = self.a_expr(0)
                self.state = 386
                self.match(ExprGrammar.RBRACE)
                self.state = 387
                self.match(ExprGrammar.POW)
                self.state = 388
                localctx.e = self.pow_arg()

                localctx.symb = localctx.var.res
                localctx.start = localctx.s.res
                localctx.end = localctx.e.res

                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.match(ExprGrammar.POW)
                self.state = 392
                localctx.e = self.pow_arg()
                self.state = 393
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 394
                self.match(ExprGrammar.LBRACE)
                self.state = 395
                localctx.var = self.a_expr(0)
                self.state = 396
                self.match(ExprGrammar.EQ)
                self.state = 397
                localctx.s = self.a_expr(0)
                self.state = 398
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
        self.enterRule(localctx, 24, self.RULE_primary_symbol)
        try:
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [74]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                localctx._ID = self.match(ExprGrammar.ID)
                localctx.res = Ast.Symbol(localctx, (None if localctx._ID is None else localctx._ID.text))
                pass
            elif token in [75]:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
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
        self.enterRule(localctx, 26, self.RULE_delta_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            localctx._DELTA = self.match(ExprGrammar.DELTA)
            self.state = 410
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
        self.enterRule(localctx, 28, self.RULE_symbol)
        try:
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [74, 75]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                localctx._primary_symbol = self.primary_symbol()
                localctx.res = localctx._primary_symbol.res
                pass
            elif token in [73]:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
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
        self.enterRule(localctx, 30, self.RULE_delim_expr)
        self._la = 0 # Token type
        try:
            self.state = 444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.match(ExprGrammar.LPAREN)
                self.state = 422
                localctx._a_expr = self.a_expr(0)
                self.state = 423
                self.match(ExprGrammar.RPAREN)
                localctx.res = localctx._a_expr.res.mut_ctx(localctx)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.match(ExprGrammar.BAR)
                self.state = 427
                self.a_expr(0)
                self.state = 428
                self.match(ExprGrammar.BAR)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 430
                self.match(ExprGrammar.LFLOOR)
                self.state = 431
                self.a_expr(0)
                self.state = 432
                self.match(ExprGrammar.RFLOOR)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 4)
                self.state = 434
                self.match(ExprGrammar.LCEIL)
                self.state = 435
                self.a_expr(0)
                self.state = 436
                self.match(ExprGrammar.RCEIL)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 5)
                self.state = 438
                self.match(ExprGrammar.LANGLE)
                self.state = 439
                self.a_expr(0)
                self.state = 440
                _la = self._input.LA(1)
                if not(_la==35 or _la==56):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 441
                self.a_expr(0)
                self.state = 442
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
        self.enterRule(localctx, 32, self.RULE_combinatorial)
        self._la = 0 # Token type
        try:
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(ExprGrammar.LBRACE)
                self.state = 447
                _la = self._input.LA(1)
                if not(_la==8 or _la==36):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 448
                localctx.n = self.a_expr(0)
                self.state = 449
                localctx.op = self.match(ExprGrammar.ID)
                self.state = 450
                if not ((None if localctx.op is None else localctx.op.text) in Ast.CombOpId):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "($op.text in Ast.CombOpId)")
                self.state = 451
                self.match(ExprGrammar.POW)
                self.state = 452
                localctx.k = self.a_expr(0)
                self.state = 453
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.combOpFromId(localctx, localctx.n.res, localctx.k.res, Ast.CombOpId((None if localctx.op is None else localctx.op.text)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.match(ExprGrammar.LBRACE)
                self.state = 457
                localctx._ID = self.match(ExprGrammar.ID)
                self.state = 458
                if not (None if localctx._ID is None else localctx._ID.text) == 'D':
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$ID.text == 'D'")
                self.state = 459
                self.match(ExprGrammar.POW)
                self.state = 460
                localctx.n = self.a_expr(0)
                self.state = 461
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Derangements(localctx, localctx.n.res)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
                self.match(ExprGrammar.LBRACE)
                self.state = 465
                self.match(ExprGrammar.BANG)
                self.state = 466
                localctx.n = self.a_expr(0)
                self.state = 467
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


    class Singular_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_singular_index

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingular_index" ):
                listener.enterSingular_index(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingular_index" ):
                listener.exitSingular_index(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingular_index" ):
                return visitor.visitSingular_index(self)
            else:
                return visitor.visitChildren(self)




    def singular_index(self):

        localctx = ExprGrammar.Singular_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_singular_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.a_expr(0)
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
            self.from_ = None # A_exprContext
            self.to = None # A_exprContext

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
        self.enterRule(localctx, 36, self.RULE_range_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4995623387934752818) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 113) != 0):
                self.state = 474
                localctx.from_ = self.a_expr(0)


            self.state = 477
            _la = self._input.LA(1)
            if not(_la==39 or _la==78):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 478
                localctx.to = self.a_expr(0)


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
        self.enterRule(localctx, 38, self.RULE_all_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            _la = self._input.LA(1)
            if not(_la==6 or _la==38):
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

        def singular_index(self):
            return self.getTypedRuleContext(ExprGrammar.Singular_indexContext,0)


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
        self.enterRule(localctx, 40, self.RULE_index_entry)
        try:
            self.state = 487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 483
                self.singular_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
                self.range_index()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 485
                self.all_index()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

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

        def atom(self):
            return self.getTypedRuleContext(ExprGrammar.AtomContext,0)


        def builtin_func(self):
            return self.getTypedRuleContext(ExprGrammar.Builtin_funcContext,0)


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
        self.enterRule(localctx, 42, self.RULE_index_arg)
        self._la = 0 # Token type
        try:
            self.state = 507
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.match(ExprGrammar.LBRACE)
                self.state = 491
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 490
                    _la = self._input.LA(1)
                    if not(_la==42 or _la==46):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 493
                self.index_entry()
                self.state = 496 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 494
                    _la = self._input.LA(1)
                    if not(_la==35 or _la==37):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 495
                    self.index_entry()
                    self.state = 498 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==35 or _la==37):
                        break

                self.state = 501
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42 or _la==46:
                    self.state = 500
                    _la = self._input.LA(1)
                    if not(_la==42 or _la==46):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 503
                self.match(ExprGrammar.RBRACE)
                pass
            elif token in [69, 74, 75]:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
                self.atom()
                pass
            elif token in [18, 19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 506
                self.builtin_func()
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


    class Builtin_funcContext(ParserRuleContext):
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
            return ExprGrammar.RULE_builtin_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuiltin_func" ):
                listener.enterBuiltin_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuiltin_func" ):
                listener.exitBuiltin_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuiltin_func" ):
                return visitor.visitBuiltin_func(self)
            else:
                return visitor.visitChildren(self)




    def builtin_func(self):

        localctx = ExprGrammar.Builtin_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_builtin_func)
        self._la = 0 # Token type
        try:
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.match(ExprGrammar.FRAC)
                self.state = 510
                localctx.num = self.latex_cmd_arg()
                self.state = 511
                localctx.den = self.latex_cmd_arg()
                localctx.res = Ast.DivOp(localctx, localctx.num.res, localctx.den.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 514
                self.match(ExprGrammar.BINOM)
                self.state = 515
                localctx.n = self.latex_cmd_arg()
                self.state = 516
                localctx.k = self.latex_cmd_arg()
                localctx.res = Ast.Binom(localctx, localctx.n.res, localctx.k.res)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 519
                self.match(ExprGrammar.SQRT)
                self.state = 520
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Root(localctx, localctx._latex_cmd_arg.res, None) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 523
                self.match(ExprGrammar.SQRT)
                self.state = 528
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 524
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 525
                    localctx.root_index = self.a_expr(0)
                    self.state = 526
                    self.match(ExprGrammar.RBRACKET)


                self.state = 530
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Root(localctx, localctx._latex_cmd_arg.res, localctx.root_index.res)
                		
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 533
                self.match(ExprGrammar.CONJUGATE)
                self.state = 534
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Conjugate(localctx, localctx._latex_cmd_arg.res)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 537
                self.match(ExprGrammar.VEC_UNIT)
                self.state = 538
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
        self.enterRule(localctx, 46, self.RULE_matrix_row)
        self._la = 0 # Token type
        try:
            self.state = 555
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59, 63, 67]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1, 4, 5, 18, 19, 20, 21, 22, 24, 26, 27, 28, 30, 31, 40, 42, 50, 52, 54, 56, 58, 62, 69, 73, 74, 75]:
                self.enterOuterAlt(localctx, 2)
                self.state = 544
                localctx._a_expr = self.a_expr(0)
                localctx.res = [localctx._a_expr.res]
                self.state = 552
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==66:
                    self.state = 546
                    self.match(ExprGrammar.ENV_EL_SEP)
                    self.state = 547
                    localctx._a_expr = self.a_expr(0)
                    localctx.res.append(localctx._a_expr.res)
                    self.state = 554
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
        self.enterRule(localctx, 48, self.RULE_matrix_body)
        self._la = 0 # Token type
        try:
            self.state = 575
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 558
                localctx._matrix_row = self.matrix_row()
                localctx.res = [localctx._matrix_row.res]
                self.state = 566
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 560
                        self.match(ExprGrammar.ENV_ROW_SEP)
                        self.state = 561
                        localctx._matrix_row = self.matrix_row()
                        localctx.res.append(localctx._matrix_row.res) 
                    self.state = 568
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

                self.state = 572
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==67:
                    self.state = 569
                    self.match(ExprGrammar.ENV_ROW_SEP)
                    self.state = 574
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
        self.enterRule(localctx, 50, self.RULE_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [58]:
                self.state = 577
                localctx.beg = self.match(ExprGrammar.BEGIN_MATRIX)
                self.state = 578
                localctx._matrix_body = self.matrix_body()
                self.state = 579
                localctx.end = self.match(ExprGrammar.END_MATRIX)
                pass
            elif token in [62]:
                self.state = 581
                localctx.beg = self.match(ExprGrammar.BEGIN_ARRAY)
                self.state = 582
                localctx._matrix_body = self.matrix_body()
                self.state = 583
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


    class Expr_system_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._a_expr = None # A_exprContext

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_expr_system_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_system_expr" ):
                listener.enterExpr_system_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_system_expr" ):
                listener.exitExpr_system_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_system_expr" ):
                return visitor.visitExpr_system_expr(self)
            else:
                return visitor.visitChildren(self)




    def expr_system_expr(self):

        localctx = ExprGrammar.Expr_system_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr_system_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            localctx._a_expr = self.a_expr(0)
            self.getInvokingContext(27).res.append(localctx._a_expr.res)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_system_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = []

        def expr_system_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.Expr_system_exprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.Expr_system_exprContext,i)


        def ENV_ROW_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.ENV_ROW_SEP)
            else:
                return self.getToken(ExprGrammar.ENV_ROW_SEP, i)

        def getRuleIndex(self):
            return ExprGrammar.RULE_expr_system_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_system_body" ):
                listener.enterExpr_system_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_system_body" ):
                listener.exitExpr_system_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_system_body" ):
                return visitor.visitExpr_system_body(self)
            else:
                return visitor.visitChildren(self)




    def expr_system_body(self):

        localctx = ExprGrammar.Expr_system_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr_system_body)
        self._la = 0 # Token type
        try:
            self.state = 607
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1, 4, 5, 18, 19, 20, 21, 22, 24, 26, 27, 28, 30, 31, 40, 42, 50, 52, 54, 56, 58, 62, 69, 73, 74, 75]:
                self.enterOuterAlt(localctx, 2)
                self.state = 593
                self.expr_system_expr()
                self.state = 598
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 594
                        self.match(ExprGrammar.ENV_ROW_SEP)
                        self.state = 595
                        self.expr_system_expr() 
                    self.state = 600
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

                self.state = 604
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==67:
                    self.state = 601
                    self.match(ExprGrammar.ENV_ROW_SEP)
                    self.state = 606
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


    class Expr_systemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.body = None # Expr_system_bodyContext

        def BEGIN_ENV(self):
            return self.getToken(ExprGrammar.BEGIN_ENV, 0)

        def END_ENV(self):
            return self.getToken(ExprGrammar.END_ENV, 0)

        def expr_system_body(self):
            return self.getTypedRuleContext(ExprGrammar.Expr_system_bodyContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_expr_system

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_system" ):
                listener.enterExpr_system(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_system" ):
                listener.exitExpr_system(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_system" ):
                return visitor.visitExpr_system(self)
            else:
                return visitor.visitChildren(self)




    def expr_system(self):

        localctx = ExprGrammar.Expr_systemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr_system)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.match(ExprGrammar.BEGIN_ENV)
            self.state = 610
            localctx.body = self.expr_system_body()
            self.state = 611
            self.match(ExprGrammar.END_ENV)
            localctx.res = Ast.ExprSystem(localctx, localctx.body.res)
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
        self._predicates[2] = self.a_expr_sempred
        self._predicates[16] = self.combinatorial_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def a_expr_sempred(self, localctx:A_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return ((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS))
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 22)
         

    def combinatorial_sempred(self, localctx:CombinatorialContext, predIndex:int):
            if predIndex == 8:
                return ((None if localctx.op is None else localctx.op.text) in Ast.CombOpId)
         

            if predIndex == 9:
                return (None if localctx._ID is None else localctx._ID.text) == 'D'
         





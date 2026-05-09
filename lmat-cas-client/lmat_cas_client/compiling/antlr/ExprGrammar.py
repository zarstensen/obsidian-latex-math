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

def serializedATN():
    return [
        4,1,71,527,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,1,0,1,0,1,0,3,0,53,8,0,1,0,
        1,0,1,1,1,1,1,2,1,2,1,2,1,2,5,2,63,8,2,10,2,12,2,66,9,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,78,8,3,1,4,4,4,81,8,4,11,4,12,
        4,82,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,98,
        8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,123,8,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,139,8,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,152,8,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,165,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,181,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,5,6,195,8,6,10,6,12,6,198,9,6,3,6,200,8,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,225,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,3,6,237,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,247,
        8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,284,8,6,1,6,1,6,1,6,1,6,1,6,3,6,291,8,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,306,8,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,323,
        8,6,1,6,5,6,326,8,6,10,6,12,6,329,9,6,1,7,1,7,1,7,1,7,1,7,3,7,336,
        8,7,1,8,1,8,1,8,1,8,3,8,342,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,5,9,357,8,9,10,9,12,9,360,9,9,1,9,1,9,3,9,364,
        8,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,3,11,379,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,3,12,392,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,3,13,406,8,13,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,3,14,428,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,449,8,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,462,
        8,15,1,16,1,16,1,16,1,17,1,17,1,17,1,17,5,17,471,8,17,10,17,12,17,
        474,9,17,1,17,1,17,3,17,478,8,17,1,18,1,18,1,18,1,18,5,18,484,8,
        18,10,18,12,18,487,9,18,1,18,5,18,490,8,18,10,18,12,18,493,9,18,
        3,18,495,8,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,
        1,21,1,21,5,21,509,8,21,10,21,12,21,512,9,21,1,21,5,21,515,8,21,
        10,21,12,21,518,9,21,3,21,520,8,21,1,22,1,22,1,22,1,22,1,22,1,22,
        0,1,12,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,0,4,1,0,9,14,1,0,26,27,2,0,8,8,42,42,1,0,4,5,574,0,52,1,
        0,0,0,2,56,1,0,0,0,4,58,1,0,0,0,6,77,1,0,0,0,8,80,1,0,0,0,10,97,
        1,0,0,0,12,283,1,0,0,0,14,335,1,0,0,0,16,341,1,0,0,0,18,363,1,0,
        0,0,20,365,1,0,0,0,22,378,1,0,0,0,24,391,1,0,0,0,26,405,1,0,0,0,
        28,427,1,0,0,0,30,461,1,0,0,0,32,463,1,0,0,0,34,477,1,0,0,0,36,494,
        1,0,0,0,38,496,1,0,0,0,40,501,1,0,0,0,42,519,1,0,0,0,44,521,1,0,
        0,0,46,47,3,44,22,0,47,48,6,0,-1,0,48,53,1,0,0,0,49,50,3,12,6,0,
        50,51,6,0,-1,0,51,53,1,0,0,0,52,46,1,0,0,0,52,49,1,0,0,0,53,54,1,
        0,0,0,54,55,5,0,0,1,55,1,1,0,0,0,56,57,7,0,0,0,57,3,1,0,0,0,58,64,
        3,12,6,0,59,60,3,2,1,0,60,61,3,12,6,0,61,63,1,0,0,0,62,59,1,0,0,
        0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,5,1,0,0,0,66,64,1,
        0,0,0,67,68,5,25,0,0,68,69,3,12,6,0,69,70,5,8,0,0,70,71,3,22,11,
        0,71,72,6,3,-1,0,72,78,1,0,0,0,73,74,5,25,0,0,74,75,3,12,6,0,75,
        76,6,3,-1,0,76,78,1,0,0,0,77,67,1,0,0,0,77,73,1,0,0,0,78,7,1,0,0,
        0,79,81,3,6,3,0,80,79,1,0,0,0,81,82,1,0,0,0,82,80,1,0,0,0,82,83,
        1,0,0,0,83,9,1,0,0,0,84,85,5,8,0,0,85,86,3,22,11,0,86,87,5,42,0,
        0,87,88,3,22,11,0,88,89,6,5,-1,0,89,98,1,0,0,0,90,91,5,42,0,0,91,
        92,3,22,11,0,92,93,5,8,0,0,93,94,3,22,11,0,94,95,6,5,-1,0,95,98,
        1,0,0,0,96,98,6,5,-1,0,97,84,1,0,0,0,97,90,1,0,0,0,97,96,1,0,0,0,
        98,11,1,0,0,0,99,100,6,6,-1,0,100,101,5,24,0,0,101,102,3,10,5,0,
        102,103,5,18,0,0,103,104,5,43,0,0,104,105,5,25,0,0,105,106,3,12,
        6,0,106,107,5,44,0,0,107,108,3,22,11,0,108,109,6,6,-1,0,109,284,
        1,0,0,0,110,111,5,24,0,0,111,112,3,10,5,0,112,113,3,12,6,0,113,114,
        5,25,0,0,114,115,3,12,6,24,115,116,6,6,-1,0,116,284,1,0,0,0,117,
        122,5,27,0,0,118,119,5,49,0,0,119,120,3,12,6,0,120,121,5,50,0,0,
        121,123,1,0,0,0,122,118,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,
        124,125,3,22,11,0,125,126,5,43,0,0,126,127,3,12,6,0,127,128,5,44,
        0,0,128,129,5,43,0,0,129,130,3,12,6,0,130,131,5,44,0,0,131,132,6,
        6,-1,0,132,284,1,0,0,0,133,138,7,1,0,0,134,135,5,49,0,0,135,136,
        3,12,6,0,136,137,5,50,0,0,137,139,1,0,0,0,138,134,1,0,0,0,138,139,
        1,0,0,0,139,140,1,0,0,0,140,141,3,22,11,0,141,142,5,43,0,0,142,143,
        3,12,6,0,143,144,5,44,0,0,144,145,6,6,-1,0,145,284,1,0,0,0,146,151,
        7,1,0,0,147,148,5,49,0,0,148,149,3,12,6,0,149,150,5,50,0,0,150,152,
        1,0,0,0,151,147,1,0,0,0,151,152,1,0,0,0,152,153,1,0,0,0,153,154,
        3,22,11,0,154,155,3,12,6,20,155,156,6,6,-1,0,156,284,1,0,0,0,157,
        158,5,18,0,0,158,159,5,43,0,0,159,164,5,25,0,0,160,161,5,49,0,0,
        161,162,3,12,6,0,162,163,5,50,0,0,163,165,1,0,0,0,164,160,1,0,0,
        0,164,165,1,0,0,0,165,166,1,0,0,0,166,167,3,12,6,0,167,168,5,44,
        0,0,168,169,5,43,0,0,169,170,3,8,4,0,170,171,5,44,0,0,171,172,6,
        6,-1,0,172,284,1,0,0,0,173,174,5,18,0,0,174,175,5,43,0,0,175,180,
        5,25,0,0,176,177,5,49,0,0,177,178,3,12,6,0,178,179,5,50,0,0,179,
        181,1,0,0,0,180,176,1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,
        183,5,44,0,0,183,184,5,43,0,0,184,185,3,8,4,0,185,186,5,44,0,0,186,
        187,3,12,6,18,187,188,6,6,-1,0,188,284,1,0,0,0,189,190,5,1,0,0,190,
        199,5,45,0,0,191,196,3,12,6,0,192,193,5,41,0,0,193,195,3,12,6,0,
        194,192,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,
        197,200,1,0,0,0,198,196,1,0,0,0,199,191,1,0,0,0,199,200,1,0,0,0,
        200,201,1,0,0,0,201,284,5,46,0,0,202,203,5,1,0,0,203,204,5,43,0,
        0,204,205,3,12,6,0,205,206,5,44,0,0,206,284,1,0,0,0,207,208,5,1,
        0,0,208,284,3,12,6,15,209,210,5,28,0,0,210,211,5,42,0,0,211,212,
        5,43,0,0,212,213,3,16,8,0,213,214,5,29,0,0,214,215,3,12,6,0,215,
        216,3,26,13,0,216,217,5,44,0,0,217,218,3,12,6,14,218,219,6,6,-1,
        0,219,284,1,0,0,0,220,221,5,30,0,0,221,225,6,6,-1,0,222,223,5,31,
        0,0,223,225,6,6,-1,0,224,220,1,0,0,0,224,222,1,0,0,0,225,226,1,0,
        0,0,226,227,3,28,14,0,227,228,5,45,0,0,228,229,3,12,6,0,229,230,
        5,46,0,0,230,231,6,6,-1,0,231,284,1,0,0,0,232,233,5,30,0,0,233,237,
        6,6,-1,0,234,235,5,31,0,0,235,237,6,6,-1,0,236,232,1,0,0,0,236,234,
        1,0,0,0,237,238,1,0,0,0,238,239,3,28,14,0,239,240,3,12,6,10,240,
        241,6,6,-1,0,241,284,1,0,0,0,242,243,5,4,0,0,243,247,6,6,-1,0,244,
        245,5,5,0,0,245,247,6,6,-1,0,246,242,1,0,0,0,246,244,1,0,0,0,247,
        248,1,0,0,0,248,249,3,12,6,8,249,250,6,6,-1,0,250,284,1,0,0,0,251,
        252,5,43,0,0,252,253,7,2,0,0,253,254,3,12,6,0,254,255,3,16,8,0,255,
        256,5,8,0,0,256,257,3,12,6,0,257,258,5,44,0,0,258,259,6,6,-1,0,259,
        260,6,6,-1,0,260,284,1,0,0,0,261,262,5,45,0,0,262,263,3,12,6,0,263,
        264,5,46,0,0,264,265,6,6,-1,0,265,284,1,0,0,0,266,267,5,57,0,0,267,
        268,3,12,6,0,268,269,5,57,0,0,269,270,6,6,-1,0,270,284,1,0,0,0,271,
        272,3,30,15,0,272,273,6,6,-1,0,273,284,1,0,0,0,274,275,3,38,19,0,
        275,276,6,6,-1,0,276,284,1,0,0,0,277,278,3,20,10,0,278,279,6,6,-1,
        0,279,284,1,0,0,0,280,281,3,14,7,0,281,282,6,6,-1,0,282,284,1,0,
        0,0,283,99,1,0,0,0,283,110,1,0,0,0,283,117,1,0,0,0,283,133,1,0,0,
        0,283,146,1,0,0,0,283,157,1,0,0,0,283,173,1,0,0,0,283,189,1,0,0,
        0,283,202,1,0,0,0,283,207,1,0,0,0,283,209,1,0,0,0,283,224,1,0,0,
        0,283,236,1,0,0,0,283,246,1,0,0,0,283,251,1,0,0,0,283,261,1,0,0,
        0,283,266,1,0,0,0,283,271,1,0,0,0,283,274,1,0,0,0,283,277,1,0,0,
        0,283,280,1,0,0,0,284,327,1,0,0,0,285,290,10,13,0,0,286,287,5,6,
        0,0,287,291,6,6,-1,0,288,289,5,7,0,0,289,291,6,6,-1,0,290,286,1,
        0,0,0,290,288,1,0,0,0,291,292,1,0,0,0,292,293,3,12,6,14,293,294,
        6,6,-1,0,294,326,1,0,0,0,295,296,10,12,0,0,296,297,4,6,2,0,297,298,
        3,12,6,13,298,299,6,6,-1,0,299,326,1,0,0,0,300,305,10,9,0,0,301,
        302,5,4,0,0,302,306,6,6,-1,0,303,304,5,5,0,0,304,306,6,6,-1,0,305,
        301,1,0,0,0,305,303,1,0,0,0,306,307,1,0,0,0,307,308,3,12,6,10,308,
        309,6,6,-1,0,309,326,1,0,0,0,310,311,10,26,0,0,311,312,5,8,0,0,312,
        313,3,24,12,0,313,314,6,6,-1,0,314,326,1,0,0,0,315,322,10,23,0,0,
        316,317,5,32,0,0,317,323,6,6,-1,0,318,319,5,33,0,0,319,323,6,6,-1,
        0,320,321,5,34,0,0,321,323,6,6,-1,0,322,316,1,0,0,0,322,318,1,0,
        0,0,322,320,1,0,0,0,323,324,1,0,0,0,324,326,6,6,-1,0,325,285,1,0,
        0,0,325,295,1,0,0,0,325,300,1,0,0,0,325,310,1,0,0,0,325,315,1,0,
        0,0,326,329,1,0,0,0,327,325,1,0,0,0,327,328,1,0,0,0,328,13,1,0,0,
        0,329,327,1,0,0,0,330,331,3,16,8,0,331,332,6,7,-1,0,332,336,1,0,
        0,0,333,334,5,37,0,0,334,336,6,7,-1,0,335,330,1,0,0,0,335,333,1,
        0,0,0,336,15,1,0,0,0,337,338,5,35,0,0,338,342,6,8,-1,0,339,340,5,
        36,0,0,340,342,6,8,-1,0,341,337,1,0,0,0,341,339,1,0,0,0,342,17,1,
        0,0,0,343,344,3,14,7,0,344,345,6,9,-1,0,345,364,1,0,0,0,346,347,
        3,30,15,0,347,348,6,9,-1,0,348,364,1,0,0,0,349,350,5,43,0,0,350,
        351,3,12,6,0,351,358,6,9,-1,0,352,353,5,41,0,0,353,354,3,12,6,0,
        354,355,6,9,-1,0,355,357,1,0,0,0,356,352,1,0,0,0,357,360,1,0,0,0,
        358,356,1,0,0,0,358,359,1,0,0,0,359,361,1,0,0,0,360,358,1,0,0,0,
        361,362,5,44,0,0,362,364,1,0,0,0,363,343,1,0,0,0,363,346,1,0,0,0,
        363,349,1,0,0,0,364,19,1,0,0,0,365,366,3,16,8,0,366,367,5,42,0,0,
        367,368,3,18,9,0,368,369,6,10,-1,0,369,21,1,0,0,0,370,371,3,14,7,
        0,371,372,6,11,-1,0,372,379,1,0,0,0,373,374,5,43,0,0,374,375,3,12,
        6,0,375,376,5,44,0,0,376,377,6,11,-1,0,377,379,1,0,0,0,378,370,1,
        0,0,0,378,373,1,0,0,0,379,23,1,0,0,0,380,381,3,14,7,0,381,382,6,
        12,-1,0,382,392,1,0,0,0,383,384,3,30,15,0,384,385,6,12,-1,0,385,
        392,1,0,0,0,386,387,5,43,0,0,387,388,3,12,6,0,388,389,5,44,0,0,389,
        390,6,12,-1,0,390,392,1,0,0,0,391,380,1,0,0,0,391,383,1,0,0,0,391,
        386,1,0,0,0,392,25,1,0,0,0,393,406,6,13,-1,0,394,395,5,8,0,0,395,
        396,5,43,0,0,396,397,7,3,0,0,397,398,5,44,0,0,398,406,6,13,-1,0,
        399,400,5,8,0,0,400,401,5,4,0,0,401,406,6,13,-1,0,402,403,5,8,0,
        0,403,404,5,5,0,0,404,406,6,13,-1,0,405,393,1,0,0,0,405,394,1,0,
        0,0,405,399,1,0,0,0,405,402,1,0,0,0,406,27,1,0,0,0,407,408,5,42,
        0,0,408,409,5,43,0,0,409,410,3,16,8,0,410,411,5,9,0,0,411,412,3,
        12,6,0,412,413,5,44,0,0,413,414,5,8,0,0,414,415,3,22,11,0,415,416,
        6,14,-1,0,416,428,1,0,0,0,417,418,5,8,0,0,418,419,3,22,11,0,419,
        420,5,42,0,0,420,421,5,43,0,0,421,422,3,16,8,0,422,423,5,9,0,0,423,
        424,3,12,6,0,424,425,5,44,0,0,425,426,6,14,-1,0,426,428,1,0,0,0,
        427,407,1,0,0,0,427,417,1,0,0,0,428,29,1,0,0,0,429,430,5,18,0,0,
        430,431,3,22,11,0,431,432,3,22,11,0,432,433,6,15,-1,0,433,462,1,
        0,0,0,434,435,5,19,0,0,435,436,3,22,11,0,436,437,3,22,11,0,437,438,
        6,15,-1,0,438,462,1,0,0,0,439,440,5,20,0,0,440,441,3,22,11,0,441,
        442,6,15,-1,0,442,462,1,0,0,0,443,448,5,20,0,0,444,445,5,49,0,0,
        445,446,3,12,6,0,446,447,5,50,0,0,447,449,1,0,0,0,448,444,1,0,0,
        0,448,449,1,0,0,0,449,450,1,0,0,0,450,451,3,22,11,0,451,452,6,15,
        -1,0,452,462,1,0,0,0,453,454,5,21,0,0,454,455,3,22,11,0,455,456,
        6,15,-1,0,456,462,1,0,0,0,457,458,5,22,0,0,458,459,3,22,11,0,459,
        460,6,15,-1,0,460,462,1,0,0,0,461,429,1,0,0,0,461,434,1,0,0,0,461,
        439,1,0,0,0,461,443,1,0,0,0,461,453,1,0,0,0,461,457,1,0,0,0,462,
        31,1,0,0,0,463,464,3,12,6,0,464,465,6,16,-1,0,465,33,1,0,0,0,466,
        478,1,0,0,0,467,472,3,32,16,0,468,469,5,67,0,0,469,471,3,32,16,0,
        470,468,1,0,0,0,471,474,1,0,0,0,472,470,1,0,0,0,472,473,1,0,0,0,
        473,475,1,0,0,0,474,472,1,0,0,0,475,476,6,17,-1,0,476,478,1,0,0,
        0,477,466,1,0,0,0,477,467,1,0,0,0,478,35,1,0,0,0,479,495,1,0,0,0,
        480,485,3,34,17,0,481,482,5,68,0,0,482,484,3,34,17,0,483,481,1,0,
        0,0,484,487,1,0,0,0,485,483,1,0,0,0,485,486,1,0,0,0,486,491,1,0,
        0,0,487,485,1,0,0,0,488,490,5,68,0,0,489,488,1,0,0,0,490,493,1,0,
        0,0,491,489,1,0,0,0,491,492,1,0,0,0,492,495,1,0,0,0,493,491,1,0,
        0,0,494,479,1,0,0,0,494,480,1,0,0,0,495,37,1,0,0,0,496,497,5,59,
        0,0,497,498,3,36,18,0,498,499,5,60,0,0,499,500,6,19,-1,0,500,39,
        1,0,0,0,501,502,3,12,6,0,502,503,6,20,-1,0,503,41,1,0,0,0,504,520,
        1,0,0,0,505,510,3,40,20,0,506,507,5,68,0,0,507,509,3,40,20,0,508,
        506,1,0,0,0,509,512,1,0,0,0,510,508,1,0,0,0,510,511,1,0,0,0,511,
        516,1,0,0,0,512,510,1,0,0,0,513,515,5,68,0,0,514,513,1,0,0,0,515,
        518,1,0,0,0,516,514,1,0,0,0,516,517,1,0,0,0,517,520,1,0,0,0,518,
        516,1,0,0,0,519,504,1,0,0,0,519,505,1,0,0,0,520,43,1,0,0,0,521,522,
        5,65,0,0,522,523,3,42,21,0,523,524,5,66,0,0,524,525,6,22,-1,0,525,
        45,1,0,0,0,39,52,64,77,82,97,122,138,151,164,180,196,199,224,236,
        246,283,290,305,322,325,327,335,341,358,363,378,391,405,427,448,
        461,472,477,485,491,494,510,516,519
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','", "'_'", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'\\{'", "'\\}'", "'['", 
                     "']'", "'\\lceil'", "'\\rceil'", "'\\lfloor'", "'\\rfloor'", 
                     "'\\langle'", "'\\rangle'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'&'", "'\\\\'" ]

    symbolicNames = [ "<INVALID>", "FUNCTION", "CMD_FUNCTION", "IGNORE", 
                      "PLUS", "MINUS", "MULT", "DIV", "POW", "EQ", "NEQ", 
                      "LT", "LTE", "GT", "GTE", "TIMES", "CROSS_PROD", "DOT_PROD", 
                      "FRAC", "BINOM", "SQRT", "CONJUGATE", "VEC_UNIT", 
                      "MOD", "INT", "DIFFERENTIAL", "PHYS_DERIVATIVE", "PHYS_PARTIAL_DERIVATIVE", 
                      "LIMIT", "LIMIT_ARROW", "SUM", "PRODUCT", "BANG", 
                      "PERCENT", "PERMILLE", "ID", "COMMAND", "NUMBER", 
                      "BIN_NUMBER", "OCT_NUMBER", "HEX_NUMBER", "COMMA", 
                      "UNDERSCORE", "LBRACE", "RBRACE", "LPAREN", "RPAREN", 
                      "LBRACE_LITERAL", "RBRACE_LITERAL", "LBRACKET", "RBRACKET", 
                      "LCEIL", "RCEIL", "LFLOOR", "RFLOOR", "LANGLE", "RANGLE", 
                      "BAR", "DOUBLE_BAR", "BEGIN_MATRIX", "END_MATRIX", 
                      "BEGIN_V_MATRIX", "END_V_MATRIX", "BEGIN_ARRAY", "END_ARRAY", 
                      "BEGIN_ENV", "END_ENV", "ENV_EL_SEP", "ENV_ROW_SEP", 
                      "ENV_SEP_SKIP", "ARG_COMM", "ARG_WS" ]

    RULE_debug = 0
    RULE_rel_op = 1
    RULE_relation = 2
    RULE_deriv_arg = 3
    RULE_deriv_args = 4
    RULE_int_bounds = 5
    RULE_a_expr = 6
    RULE_atom = 7
    RULE_symbol = 8
    RULE_subscript_arg = 9
    RULE_subscript_symbol = 10
    RULE_latex_cmd_arg = 11
    RULE_pow_arg = 12
    RULE_limit_dir = 13
    RULE_series_range_args = 14
    RULE_builtin_func = 15
    RULE_matrix_el = 16
    RULE_matrix_row = 17
    RULE_matrix_body = 18
    RULE_matrix = 19
    RULE_expr_system_expr = 20
    RULE_expr_system_body = 21
    RULE_expr_system = 22

    ruleNames =  [ "debug", "rel_op", "relation", "deriv_arg", "deriv_args", 
                   "int_bounds", "a_expr", "atom", "symbol", "subscript_arg", 
                   "subscript_symbol", "latex_cmd_arg", "pow_arg", "limit_dir", 
                   "series_range_args", "builtin_func", "matrix_el", "matrix_row", 
                   "matrix_body", "matrix", "expr_system_expr", "expr_system_body", 
                   "expr_system" ]

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
    ID=35
    COMMAND=36
    NUMBER=37
    BIN_NUMBER=38
    OCT_NUMBER=39
    HEX_NUMBER=40
    COMMA=41
    UNDERSCORE=42
    LBRACE=43
    RBRACE=44
    LPAREN=45
    RPAREN=46
    LBRACE_LITERAL=47
    RBRACE_LITERAL=48
    LBRACKET=49
    RBRACKET=50
    LCEIL=51
    RCEIL=52
    LFLOOR=53
    RFLOOR=54
    LANGLE=55
    RANGLE=56
    BAR=57
    DOUBLE_BAR=58
    BEGIN_MATRIX=59
    END_MATRIX=60
    BEGIN_V_MATRIX=61
    END_V_MATRIX=62
    BEGIN_ARRAY=63
    END_ARRAY=64
    BEGIN_ENV=65
    END_ENV=66
    ENV_EL_SEP=67
    ENV_ROW_SEP=68
    ENV_SEP_SKIP=69
    ARG_COMM=70
    ARG_WS=71

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
            self.res = None
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
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 46
                localctx._expr_system = self.expr_system()
                localctx.res = localctx._expr_system.res
                pass
            elif token in [1, 4, 5, 18, 19, 20, 21, 22, 24, 26, 27, 28, 30, 31, 35, 36, 37, 43, 45, 57, 59]:
                self.state = 49
                localctx._a_expr = self.a_expr(0)
                localctx.res = localctx._a_expr.res
                pass
            else:
                raise NoViableAltException(self)

            self.state = 54
            self.match(ExprGrammar.EOF)
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
        self.enterRule(localctx, 2, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
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


        def rel_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.Rel_opContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.Rel_opContext,i)


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
        self.enterRule(localctx, 4, self.RULE_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.a_expr(0)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0):
                self.state = 59
                self.rel_op()
                self.state = 60
                self.a_expr(0)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Deriv_argContext(ParserRuleContext):
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
            return ExprGrammar.RULE_deriv_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeriv_arg" ):
                listener.enterDeriv_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeriv_arg" ):
                listener.exitDeriv_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeriv_arg" ):
                return visitor.visitDeriv_arg(self)
            else:
                return visitor.visitChildren(self)




    def deriv_arg(self):

        localctx = ExprGrammar.Deriv_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_deriv_arg)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 68
                localctx._a_expr = self.a_expr(0)
                self.state = 69
                self.match(ExprGrammar.POW)
                self.state = 70
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.getInvokingContext(4).res.append((localctx._a_expr.res, localctx._latex_cmd_arg.res))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 74
                localctx._a_expr = self.a_expr(0)
                self.getInvokingContext(4).res.append((localctx._a_expr.res, None))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Deriv_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = []

        def deriv_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.Deriv_argContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.Deriv_argContext,i)


        def getRuleIndex(self):
            return ExprGrammar.RULE_deriv_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeriv_args" ):
                listener.enterDeriv_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeriv_args" ):
                listener.exitDeriv_args(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeriv_args" ):
                return visitor.visitDeriv_args(self)
            else:
                return visitor.visitChildren(self)




    def deriv_args(self):

        localctx = ExprGrammar.Deriv_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_deriv_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 79
                self.deriv_arg()
                self.state = 82 
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
        self.enterRule(localctx, 10, self.RULE_int_bounds)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(ExprGrammar.POW)
                self.state = 85
                localctx.upper = self.latex_cmd_arg()
                self.state = 86
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 87
                localctx.lower = self.latex_cmd_arg()
                localctx.bounds = (localctx.lower.res, localctx.upper.res)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 91
                localctx.lower = self.latex_cmd_arg()
                self.state = 92
                self.match(ExprGrammar.POW)
                self.state = 93
                localctx.upper = self.latex_cmd_arg()
                localctx.bounds = (localctx.lower.res, localctx.upper.res)
                pass
            elif token in [1, 4, 5, 18, 19, 20, 21, 22, 24, 26, 27, 28, 30, 31, 35, 36, 37, 43, 45, 57, 59]:
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


    class A_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
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
            self.lhs = None # A_exprContext
            self._a_expr = None # A_exprContext
            self.op = None # SymbolContext
            self.rhs = None # A_exprContext
            self.copyFrom(ctx)

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

        def symbol(self):
            return self.getTypedRuleContext(ExprGrammar.SymbolContext,0)


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


    class StubContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self._a_expr = None # A_exprContext
            self._builtin_func = None # Builtin_funcContext
            self._matrix = None # MatrixContext
            self._subscript_symbol = None # Subscript_symbolContext
            self._atom = None # AtomContext
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ExprGrammar.LPAREN, 0)
        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)

        def RPAREN(self):
            return self.getToken(ExprGrammar.RPAREN, 0)
        def builtin_func(self):
            return self.getTypedRuleContext(ExprGrammar.Builtin_funcContext,0)

        def matrix(self):
            return self.getTypedRuleContext(ExprGrammar.MatrixContext,0)

        def subscript_symbol(self):
            return self.getTypedRuleContext(ExprGrammar.Subscript_symbolContext,0)

        def atom(self):
            return self.getTypedRuleContext(ExprGrammar.AtomContext,0)


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


    class ExponentialOpContext(A_exprContext):

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
            if hasattr( listener, "enterExponentialOp" ):
                listener.enterExponentialOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponentialOp" ):
                listener.exitExponentialOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponentialOp" ):
                return visitor.visitExponentialOp(self)
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
            self.deg = None # A_exprContext
            self.diffand_last = None # A_exprContext
            self.diff = None # A_exprContext
            self._deriv_args = None # Deriv_argsContext
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
        def deriv_args(self):
            return self.getTypedRuleContext(ExprGrammar.Deriv_argsContext,0)


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


    class AbsContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self._a_expr = None # A_exprContext
            self.copyFrom(ctx)

        def BAR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.BAR)
            else:
                return self.getToken(ExprGrammar.BAR, i)
        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbs" ):
                listener.enterAbs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbs" ):
                listener.exitAbs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbs" ):
                return visitor.visitAbs(self)
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


    class LimitContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.A_exprContext
            super().__init__(parser)
            self.lim_var = None # SymbolContext
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
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = ExprGrammar.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 100
                self.match(ExprGrammar.INT)
                self.state = 101
                localctx._int_bounds = self.int_bounds()
                self.state = 102
                self.match(ExprGrammar.FRAC)
                self.state = 103
                self.match(ExprGrammar.LBRACE)
                self.state = 104
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 105
                localctx.diff = localctx._a_expr = self.a_expr(0)
                self.state = 106
                self.match(ExprGrammar.RBRACE)
                self.state = 107
                localctx.recip_integrand = localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Integral(localctx, Ast.DivOp(localctx.recip_integrand, Ast.Number(localctx.recip_integrand, "1"), localctx.recip_integrand.res), localctx.diff.res, localctx._int_bounds.bounds)
                pass

            elif la_ == 2:
                localctx = ExprGrammar.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(ExprGrammar.INT)
                self.state = 111
                localctx._int_bounds = self.int_bounds()
                self.state = 112
                localctx.integrand = localctx._a_expr = self.a_expr(0)
                self.state = 113
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 114
                localctx.diff = localctx._a_expr = self.a_expr(24)
                localctx.res = Ast.Integral(localctx, localctx.integrand.res, localctx.diff.res, localctx._int_bounds.bounds)
                pass

            elif la_ == 3:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 117
                self.match(ExprGrammar.PHYS_PARTIAL_DERIVATIVE)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 118
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 119
                    localctx._a_expr = self.a_expr(0)
                    self.state = 120
                    self.match(ExprGrammar.RBRACKET)


                self.state = 124
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 125
                self.match(ExprGrammar.LBRACE)
                self.state = 126
                localctx.diff_l = localctx._a_expr = self.a_expr(0)
                self.state = 127
                self.match(ExprGrammar.RBRACE)
                self.state = 128
                self.match(ExprGrammar.LBRACE)
                self.state = 129
                localctx.diff_r = localctx._a_expr = self.a_expr(0)
                self.state = 130
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._latex_cmd_arg.res, [(localctx.diff_l.res, None), (localctx.diff_r.res, None)])
                pass

            elif la_ == 4:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 134
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 135
                    localctx.deg = localctx._a_expr = self.a_expr(0)
                    self.state = 136
                    self.match(ExprGrammar.RBRACKET)


                self.state = 140
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 141
                self.match(ExprGrammar.LBRACE)
                self.state = 142
                localctx._a_expr = self.a_expr(0)
                self.state = 143
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._latex_cmd_arg.res, [(localctx._a_expr.res, localctx.deg.res)])
                pass

            elif la_ == 5:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 147
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 148
                    localctx.deg = localctx._a_expr = self.a_expr(0)
                    self.state = 149
                    self.match(ExprGrammar.RBRACKET)


                self.state = 153
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 154
                localctx.diffand_last = localctx._a_expr = self.a_expr(20)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, [(localctx._latex_cmd_arg.res, localctx.deg.res)])
                pass

            elif la_ == 6:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 157
                self.match(ExprGrammar.FRAC)
                self.state = 158
                self.match(ExprGrammar.LBRACE)
                self.state = 159
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 160
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 161
                    localctx.diff = localctx._a_expr = self.a_expr(0)
                    self.state = 162
                    self.match(ExprGrammar.RBRACKET)


                self.state = 166
                localctx._a_expr = self.a_expr(0)
                self.state = 167
                self.match(ExprGrammar.RBRACE)
                self.state = 168
                self.match(ExprGrammar.LBRACE)
                self.state = 169
                localctx._deriv_args = self.deriv_args()
                self.state = 170
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, localctx._deriv_args.res)
                pass

            elif la_ == 7:
                localctx = ExprGrammar.DerivContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 173
                self.match(ExprGrammar.FRAC)
                self.state = 174
                self.match(ExprGrammar.LBRACE)
                self.state = 175
                self.match(ExprGrammar.DIFFERENTIAL)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 176
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 177
                    localctx.diff = localctx._a_expr = self.a_expr(0)
                    self.state = 178
                    self.match(ExprGrammar.RBRACKET)


                self.state = 182
                self.match(ExprGrammar.RBRACE)
                self.state = 183
                self.match(ExprGrammar.LBRACE)
                self.state = 184
                localctx._deriv_args = self.deriv_args()
                self.state = 185
                self.match(ExprGrammar.RBRACE)
                self.state = 186
                localctx._a_expr = self.a_expr(18)
                localctx.res = Ast.Differential(localctx, localctx._a_expr.res, localctx._deriv_args.res)
                pass

            elif la_ == 8:
                localctx = ExprGrammar.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 189
                self.match(ExprGrammar.FUNCTION)
                self.state = 190
                self.match(ExprGrammar.LPAREN)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 720620165078450226) != 0):
                    self.state = 191
                    localctx._a_expr = self.a_expr(0)
                    self.state = 196
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==41:
                        self.state = 192
                        self.match(ExprGrammar.COMMA)
                        self.state = 193
                        localctx._a_expr = self.a_expr(0)
                        self.state = 198
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 201
                self.match(ExprGrammar.RPAREN)
                pass

            elif la_ == 9:
                localctx = ExprGrammar.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 202
                self.match(ExprGrammar.FUNCTION)
                self.state = 203
                self.match(ExprGrammar.LBRACE)
                self.state = 204
                localctx._a_expr = self.a_expr(0)
                self.state = 205
                self.match(ExprGrammar.RBRACE)
                pass

            elif la_ == 10:
                localctx = ExprGrammar.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 207
                self.match(ExprGrammar.FUNCTION)
                self.state = 208
                localctx._a_expr = self.a_expr(15)
                pass

            elif la_ == 11:
                localctx = ExprGrammar.LimitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 209
                self.match(ExprGrammar.LIMIT)
                self.state = 210
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 211
                self.match(ExprGrammar.LBRACE)
                self.state = 212
                localctx.lim_var = self.symbol()
                self.state = 213
                self.match(ExprGrammar.LIMIT_ARROW)
                self.state = 214
                localctx.lim_poa = localctx._a_expr = self.a_expr(0)
                self.state = 215
                localctx._limit_dir = self.limit_dir()
                self.state = 216
                self.match(ExprGrammar.RBRACE)
                self.state = 217
                localctx._a_expr = self.a_expr(14)
                localctx.res = Ast.Limit(localctx._a_expr.res, localctx.lim_var.res, localctx.lim_poa.res, localctx._limit_dir.res)
                pass

            elif la_ == 12:
                localctx = ExprGrammar.SeriesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 224
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [30]:
                    self.state = 220
                    self.match(ExprGrammar.SUM)
                    localctx.node_t = Ast.Sum
                    pass
                elif token in [31]:
                    self.state = 222
                    self.match(ExprGrammar.PRODUCT)
                    localctx.node_t = Ast.Product
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 226
                localctx._series_range_args = self.series_range_args()
                self.state = 227
                self.match(ExprGrammar.LPAREN)
                self.state = 228
                localctx._a_expr = self.a_expr(0)
                self.state = 229
                self.match(ExprGrammar.RPAREN)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res, localctx._series_range_args.symb, (localctx._series_range_args.start, localctx._series_range_args.end))
                pass

            elif la_ == 13:
                localctx = ExprGrammar.SeriesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 236
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [30]:
                    self.state = 232
                    self.match(ExprGrammar.SUM)
                    localctx.node_t = Ast.Sum
                    pass
                elif token in [31]:
                    self.state = 234
                    self.match(ExprGrammar.PRODUCT)
                    localctx.node_t = Ast.Product
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 238
                localctx._series_range_args = self.series_range_args()
                self.state = 239
                localctx._a_expr = self.a_expr(10)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res, localctx._series_range_args.symb, (localctx._series_range_args.start, localctx._series_range_args.end))
                pass

            elif la_ == 14:
                localctx = ExprGrammar.UAdditiveOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 246
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 242
                    self.match(ExprGrammar.PLUS)
                    localctx.node_t = Ast.UPlusOp
                    pass
                elif token in [5]:
                    self.state = 244
                    self.match(ExprGrammar.MINUS)
                    localctx.node_t = Ast.UMinusOp
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 248
                localctx._a_expr = self.a_expr(8)
                localctx.res = localctx.node_t(localctx, localctx._a_expr.res)
                pass

            elif la_ == 15:
                localctx = ExprGrammar.CombContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 251
                self.match(ExprGrammar.LBRACE)
                self.state = 252
                _la = self._input.LA(1)
                if not(_la==8 or _la==42):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 253
                localctx.lhs = localctx._a_expr = self.a_expr(0)
                self.state = 254
                localctx.op = self.symbol()
                self.state = 255
                self.match(ExprGrammar.POW)
                self.state = 256
                localctx.rhs = localctx._a_expr = self.a_expr(0)
                self.state = 257
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.Number(localctx, '1')

                #localctx.res = Ast.tryMakeComb(localctx.lhs.res, localctx.rhs.res, localctx.op.res)

                pass

            elif la_ == 16:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 261
                self.match(ExprGrammar.LPAREN)
                self.state = 262
                localctx._a_expr = self.a_expr(0)
                self.state = 263
                self.match(ExprGrammar.RPAREN)
                localctx.res = localctx._a_expr.res.mut_ctx(localctx)
                pass

            elif la_ == 17:
                localctx = ExprGrammar.AbsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 266
                self.match(ExprGrammar.BAR)
                self.state = 267
                localctx._a_expr = self.a_expr(0)
                self.state = 268
                self.match(ExprGrammar.BAR)
                localctx.res = Ast.Abs(localctx, localctx._a_expr.res)
                pass

            elif la_ == 18:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 271
                localctx._builtin_func = self.builtin_func()
                localctx.res = localctx._builtin_func.res
                pass

            elif la_ == 19:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 274
                localctx._matrix = self.matrix()
                localctx.res = localctx._matrix.res 
                pass

            elif la_ == 20:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 277
                localctx._subscript_symbol = self.subscript_symbol()
                localctx.res = localctx._subscript_symbol.res
                pass

            elif la_ == 21:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 280
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 325
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = ExprGrammar.MultiplicativeOpContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 285
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 290
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [6]:
                            self.state = 286
                            self.match(ExprGrammar.MULT)
                            localctx.node_t = Ast.MultOp
                            pass
                        elif token in [7]:
                            self.state = 288
                            self.match(ExprGrammar.DIV)
                            localctx.node_t = Ast.DivOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 292
                        localctx.rhs = localctx._a_expr = self.a_expr(14)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 2:
                        localctx = ExprGrammar.MultiplicativeOpContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 295
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 296
                        if not ((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS)):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS))")
                        self.state = 297
                        localctx.rhs = localctx._a_expr = self.a_expr(13)
                        localctx.res = Ast.MultOp(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 3:
                        localctx = ExprGrammar.AdditiveOpContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 300
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 305
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [4]:
                            self.state = 301
                            self.match(ExprGrammar.PLUS)
                            localctx.node_t = Ast.AddOp
                            pass
                        elif token in [5]:
                            self.state = 303
                            self.match(ExprGrammar.MINUS)
                            localctx.node_t = Ast.SubOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 307
                        localctx.rhs = localctx._a_expr = self.a_expr(10)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 4:
                        localctx = ExprGrammar.ExponentialOpContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 310
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 311
                        self.match(ExprGrammar.POW)
                        self.state = 312
                        localctx.exp = self.pow_arg()
                        localctx.res=Ast.ExpOp(localctx, localctx.base.res, localctx.exp.res)
                        pass

                    elif la_ == 5:
                        localctx = ExprGrammar.PrefixContext(self, ExprGrammar.A_exprContext(self, _parentctx, _parentState))
                        localctx.op = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_a_expr)
                        self.state = 315
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 322
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [32]:
                            self.state = 316
                            self.match(ExprGrammar.BANG)
                            localctx.node_t = Ast.Factorial
                            pass
                        elif token in [33]:
                            self.state = 318
                            self.match(ExprGrammar.PERCENT)
                            localctx.node_t = Ast.Percent
                            pass
                        elif token in [34]:
                            self.state = 320
                            self.match(ExprGrammar.PERMILLE)
                            localctx.node_t = Ast.Permille
                            pass
                        else:
                            raise NoViableAltException(self)

                        localctx.res = localctx.node_t(localctx, localctx.op.res)
                        pass

             
                self.state = 329
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
            self.res = None
            self._symbol = None # SymbolContext
            self._NUMBER = None # Token

        def symbol(self):
            return self.getTypedRuleContext(ExprGrammar.SymbolContext,0)


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
        self.enterRule(localctx, 14, self.RULE_atom)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35, 36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                localctx._symbol = self.symbol()
                localctx.res = localctx._symbol.res
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
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


    class SymbolContext(ParserRuleContext):
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
        self.enterRule(localctx, 16, self.RULE_symbol)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                localctx._ID = self.match(ExprGrammar.ID)
                localctx.res = Ast.Symbol(localctx, (None if localctx._ID is None else localctx._ID.text))
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
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


    class Subscript_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = []
            self._atom = None # AtomContext
            self._builtin_func = None # Builtin_funcContext
            self.first = None # A_exprContext
            self._a_expr = None # A_exprContext
            self.rem = None # A_exprContext

        def atom(self):
            return self.getTypedRuleContext(ExprGrammar.AtomContext,0)


        def builtin_func(self):
            return self.getTypedRuleContext(ExprGrammar.Builtin_funcContext,0)


        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

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
        self.enterRule(localctx, 18, self.RULE_subscript_arg)
        self._la = 0 # Token type
        try:
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35, 36, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                localctx._atom = self.atom()
                localctx.res = [localctx._atom.res]
                pass
            elif token in [18, 19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                localctx._builtin_func = self.builtin_func()
                localctx.res = [localctx._builtin_func.res]
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 349
                self.match(ExprGrammar.LBRACE)
                self.state = 350
                localctx.first = localctx._a_expr = self.a_expr(0)
                localctx.res = [localctx._a_expr.res]
                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==41:
                    self.state = 352
                    self.match(ExprGrammar.COMMA)
                    self.state = 353
                    localctx.rem = localctx._a_expr = self.a_expr(0)
                    localctx.res.append(localctx.rem.res)
                    self.state = 360
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 361
                self.match(ExprGrammar.RBRACE)
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


    class Subscript_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self._symbol = None # SymbolContext
            self._subscript_arg = None # Subscript_argContext

        def symbol(self):
            return self.getTypedRuleContext(ExprGrammar.SymbolContext,0)


        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)

        def subscript_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Subscript_argContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_subscript_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscript_symbol" ):
                listener.enterSubscript_symbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscript_symbol" ):
                listener.exitSubscript_symbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubscript_symbol" ):
                return visitor.visitSubscript_symbol(self)
            else:
                return visitor.visitChildren(self)




    def subscript_symbol(self):

        localctx = ExprGrammar.Subscript_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_subscript_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            localctx._symbol = self.symbol()
            self.state = 366
            self.match(ExprGrammar.UNDERSCORE)
            self.state = 367
            localctx._subscript_arg = self.subscript_arg()
            localctx.res = Ast.SubscriptSymbol(localctx, localctx._symbol.res, localctx._subscript_arg.res)
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
        self.enterRule(localctx, 22, self.RULE_latex_cmd_arg)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35, 36, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.match(ExprGrammar.LBRACE)
                self.state = 374
                localctx._a_expr = self.a_expr(0)
                self.state = 375
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
        self.enterRule(localctx, 24, self.RULE_pow_arg)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35, 36, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass
            elif token in [18, 19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                localctx._builtin_func = self.builtin_func()
                localctx.res = localctx._builtin_func.res
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.match(ExprGrammar.LBRACE)
                self.state = 387
                localctx._a_expr = self.a_expr(0)
                self.state = 388
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
        self.enterRule(localctx, 26, self.RULE_limit_dir)
        self._la = 0 # Token type
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                localctx.res = Ast.LimitDir.BOTH
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.match(ExprGrammar.POW)
                self.state = 395
                self.match(ExprGrammar.LBRACE)
                self.state = 396
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 397
                self.match(ExprGrammar.RBRACE)
                localctx.res = Ast.LimitDir.BOTH
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self.match(ExprGrammar.POW)
                self.state = 400
                self.match(ExprGrammar.PLUS)
                localctx.res = Ast.LimitDir.POSITIVE
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 402
                self.match(ExprGrammar.POW)
                self.state = 403
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
            self._symbol = None # SymbolContext
            self._a_expr = None # A_exprContext
            self._latex_cmd_arg = None # Latex_cmd_argContext

        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)

        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)

        def symbol(self):
            return self.getTypedRuleContext(ExprGrammar.SymbolContext,0)


        def EQ(self):
            return self.getToken(ExprGrammar.EQ, 0)

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

        def POW(self):
            return self.getToken(ExprGrammar.POW, 0)

        def latex_cmd_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Latex_cmd_argContext,0)


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
        self.enterRule(localctx, 28, self.RULE_series_range_args)
        try:
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 408
                self.match(ExprGrammar.LBRACE)
                self.state = 409
                localctx._symbol = self.symbol()
                self.state = 410
                self.match(ExprGrammar.EQ)
                self.state = 411
                localctx._a_expr = self.a_expr(0)
                self.state = 412
                self.match(ExprGrammar.RBRACE)
                self.state = 413
                self.match(ExprGrammar.POW)
                self.state = 414
                localctx._latex_cmd_arg = self.latex_cmd_arg()

                localctx.symb = localctx._symbol.res
                localctx.start = localctx._a_expr.res
                localctx.end = localctx._latex_cmd_arg.res

                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.match(ExprGrammar.POW)
                self.state = 418
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 419
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 420
                self.match(ExprGrammar.LBRACE)
                self.state = 421
                localctx._symbol = self.symbol()
                self.state = 422
                self.match(ExprGrammar.EQ)
                self.state = 423
                localctx._a_expr = self.a_expr(0)
                self.state = 424
                self.match(ExprGrammar.RBRACE)

                localctx.symb = localctx._symbol.res
                localctx.start = localctx._a_expr.res
                localctx.end = localctx._latex_cmd_arg.res

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
            self.index = None # A_exprContext

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
        self.enterRule(localctx, 30, self.RULE_builtin_func)
        self._la = 0 # Token type
        try:
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(ExprGrammar.FRAC)
                self.state = 430
                localctx.num = self.latex_cmd_arg()
                self.state = 431
                localctx.den = self.latex_cmd_arg()
                localctx.res = Ast.DivOp(localctx, localctx.num.res, localctx.den.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.match(ExprGrammar.BINOM)
                self.state = 435
                localctx.n = self.latex_cmd_arg()
                self.state = 436
                localctx.k = self.latex_cmd_arg()
                localctx.res = Ast.Binom(localctx, localctx.n.res, localctx.k.res)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 439
                self.match(ExprGrammar.SQRT)
                self.state = 440
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Root(localctx, localctx._latex_cmd_arg.res, None) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 443
                self.match(ExprGrammar.SQRT)
                self.state = 448
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 444
                    self.match(ExprGrammar.LBRACKET)
                    self.state = 445
                    localctx.index = self.a_expr(0)
                    self.state = 446
                    self.match(ExprGrammar.RBRACKET)


                self.state = 450
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Root(localctx, localctx._latex_cmd_arg.res, localctx.index.res)
                		
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 453
                self.match(ExprGrammar.CONJUGATE)
                self.state = 454
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                localctx.res = Ast.Conjugate(localctx, localctx._latex_cmd_arg.res)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 457
                self.match(ExprGrammar.VEC_UNIT)
                self.state = 458
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


    class Matrix_elContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._a_expr = None # A_exprContext

        def a_expr(self):
            return self.getTypedRuleContext(ExprGrammar.A_exprContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_matrix_el

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix_el" ):
                listener.enterMatrix_el(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix_el" ):
                listener.exitMatrix_el(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix_el" ):
                return visitor.visitMatrix_el(self)
            else:
                return visitor.visitChildren(self)




    def matrix_el(self):

        localctx = ExprGrammar.Matrix_elContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_matrix_el)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            localctx._a_expr = self.a_expr(0)
            self.getInvokingContext(17).res.append(localctx._a_expr.res) 
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
            self.res = []

        def matrix_el(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.Matrix_elContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.Matrix_elContext,i)


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
        self.enterRule(localctx, 34, self.RULE_matrix_row)
        self._la = 0 # Token type
        try:
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [60, 68]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1, 4, 5, 18, 19, 20, 21, 22, 24, 26, 27, 28, 30, 31, 35, 36, 37, 43, 45, 57, 59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
                self.matrix_el()
                self.state = 472
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==67:
                    self.state = 468
                    self.match(ExprGrammar.ENV_EL_SEP)
                    self.state = 469
                    self.matrix_el()
                    self.state = 474
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.getInvokingContext(18).res.append(localctx.res)
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
        self.enterRule(localctx, 36, self.RULE_matrix_body)
        self._la = 0 # Token type
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
                self.matrix_row()
                self.state = 485
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 481
                        self.match(ExprGrammar.ENV_ROW_SEP)
                        self.state = 482
                        self.matrix_row() 
                    self.state = 487
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

                self.state = 491
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==68:
                    self.state = 488
                    self.match(ExprGrammar.ENV_ROW_SEP)
                    self.state = 493
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
            self._BEGIN_MATRIX = None # Token
            self._matrix_body = None # Matrix_bodyContext
            self._END_MATRIX = None # Token

        def BEGIN_MATRIX(self):
            return self.getToken(ExprGrammar.BEGIN_MATRIX, 0)

        def matrix_body(self):
            return self.getTypedRuleContext(ExprGrammar.Matrix_bodyContext,0)


        def END_MATRIX(self):
            return self.getToken(ExprGrammar.END_MATRIX, 0)

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
        self.enterRule(localctx, 38, self.RULE_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            localctx._BEGIN_MATRIX = self.match(ExprGrammar.BEGIN_MATRIX)
            self.state = 497
            localctx._matrix_body = self.matrix_body()
            self.state = 498
            localctx._END_MATRIX = self.match(ExprGrammar.END_MATRIX)
            localctx.res = Ast.Matrix(localctx, localctx._matrix_body.res, (None if localctx._BEGIN_MATRIX is None else localctx._BEGIN_MATRIX.text), (None if localctx._END_MATRIX is None else localctx._END_MATRIX.text))
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
        self.enterRule(localctx, 40, self.RULE_expr_system_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            localctx._a_expr = self.a_expr(0)
            self.getInvokingContext(21).res.append(localctx._a_expr.res)
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
        self.enterRule(localctx, 42, self.RULE_expr_system_body)
        self._la = 0 # Token type
        try:
            self.state = 519
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1, 4, 5, 18, 19, 20, 21, 22, 24, 26, 27, 28, 30, 31, 35, 36, 37, 43, 45, 57, 59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
                self.expr_system_expr()
                self.state = 510
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 506
                        self.match(ExprGrammar.ENV_ROW_SEP)
                        self.state = 507
                        self.expr_system_expr() 
                    self.state = 512
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

                self.state = 516
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==68:
                    self.state = 513
                    self.match(ExprGrammar.ENV_ROW_SEP)
                    self.state = 518
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
        self.enterRule(localctx, 44, self.RULE_expr_system)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(ExprGrammar.BEGIN_ENV)
            self.state = 522
            localctx.body = self.expr_system_body()
            self.state = 523
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
        self._predicates[6] = self.a_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def a_expr_sempred(self, localctx:A_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return ((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS))
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 23)
         





import re
import sys
sys.path.append("..")
from modules import PAMFinder

def generateGRNAPairs(template):
    complement = PAMFinder.complementary(template)
    templateLocations , complementLocations = PAMFinder.get_PAM(template.upper())
    regex = "\(([0-9]*)\, ([0-9]*)\)"
    tempGRNAs = []
    compGRNAs = []

    for tempLoc in templateLocations:
        for compLoc in complementLocations:
            match1 = re.match(regex,str(tempLoc))
            match2 = re.match(regex,str(compLoc))
            if((int(match2.groups()[0]) - int(match1.groups()[1]) <= 20 and int(match2.groups()[0]) - int(match1.groups()[1]) >= 0)):
                tempGRNAs.append(toGRNA(template,int(match1.groups()[1]), int(match2.groups()[0]) - int(match1.groups()[1])))
                compGRNAs.append(toGRNA(complement,int(match2.groups()[0]), int(match2.groups()[0]) - int(match1.groups()[1]),False))
    
    return tempGRNAs,compGRNAs

def toGRNA(strand, loc, spaces, isTemplate = True):
    comp_dict = {'A':'T','T':'A','C':'G','G':'C','Y':'R','R':'Y','W':'W','S':'S','K':'M','M':'K','N':'N'}
    grna = ''
    if(isTemplate):
        for i in range(loc-2,loc+spaces+1):
            grna = grna + comp_dict[strand[i]]
        grna = grna[::-1]
    else:
        for i in range(loc-spaces,loc+3):
            grna = grna + comp_dict[strand[i]]
    print(spaces)
    print(grna)
    return grna
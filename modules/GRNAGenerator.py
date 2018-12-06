import re
import sys
sys.path.append("..")
from modules import PAMFinder

def get_PAM(seq):
  pam = re.compile("[ACTG]GG")
  matches = pam.finditer(seq)
  pam_loc = []
  for match in matches:
    if(match.span()[0] >=20):
      pam_loc.append(match.span())
  comp_pam = re.compile("GG[ACTG]")
  matches = comp_pam.finditer(complementary(seq))
  comp_loc = []
  for match in matches:
    if(len(seq) - match.span()[1] >= 20):
      comp_loc.append(match.span())
  return pam_loc, comp_loc

#Input: sequence, Output: complementary sequence
def complementary(seq):
  comp_dict = {'A':'T','T':'A','C':'G','G':'C','Y':'R','R':'Y','W':'W','S':'S','K':'M','M':'K','N':'N'}
  comp_seq = ""
  for char in seq:
    comp_seq += comp_dict[char]
  return comp_seq

seq = "CCTGATAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGATAGG"


def generateGRNAPairs(template):
    complement = complementary(template)
    templateLocations , complementLocations = get_PAM(template.upper())
    tempGRNAs = []
    compGRNAs = []

    for tempLoc in templateLocations:
        for compLoc in complementLocations:
            print(tempLoc, compLoc)
            difference = tempLoc[0] - compLoc[1]
            if(difference > 20 and difference <= 40):
                tempGRNAs.append(template[(tempLoc[0] - 20):tempLoc[0]])
                compGRNAs.append(complement[compLoc[1]:(compLoc[1]+20)])
    
    return tempGRNAs,compGRNAs
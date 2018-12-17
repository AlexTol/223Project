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
            #print(tempLoc, compLoc)
            difference = tempLoc[0] - compLoc[1]
            if(difference > 20 and difference <= 30):
                tempGRNAs.append(template[(tempLoc[0] - 20):tempLoc[0]])
                compGRNAs.append(complement[compLoc[1]:(compLoc[1]+20)])

    return tempGRNAs[:30],compGRNAs[:30]

def similarityScore(string1, string2):
    tot = len(string1)
    score = 0

    for i in range(0,len(string1)):
        if(string1[i] == string2[i]):
            score += 1

    return score/len(string1)

def getOffTargetScore(gRNA, msuper):
    cap = int(len(msuper)/20)
    score = 1
    msuper = msuper.replace('\n','')

    comp_dict = {'A':'T','T':'A','C':'G','G':'C','Y':'R','R':'Y','W':'W','S':'S','K':'M','M':'K','N':'N'}
    sense = ''
    for i in range(0,len(gRNA)):
        sense = sense + comp_dict[gRNA[i]]

    for i in range(0,cap):
        frame = msuper[(i*20):(i*20)+20]

        if(len(frame) < len(sense)):
            continue
        if(similarityScore(sense,frame) >= .9):
          score -= 1

    return score

def chooseBestFive(mdict):
  sortedDict = sorted(mdict.items(), key=lambda kv: kv[1])
      
  best = []
  for i in range(0,5):
    best.append(sortedDict[i][0])

  return best

def on_target_score(seq): #make sure to pass in string only
  score = 100
  if(seq[0] == 'G' or seq[-1] == 'G'):
    score -= 50
  GC_amount = seq.count('G') + seq.count('C')
  score -= (10 - GC_amount) * 5
  return score

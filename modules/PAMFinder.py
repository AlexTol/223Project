import re

#Input: Genomic sequence
#Output: A list of PAM site locations

def get_PAM(seq):
 pam = re.compile("[ACTG]GG")
 matches = pam.finditer(seq)
 pam_loc = []
 for match in matches:
   pam_loc.append(match.span())
 comp_pam = re.compile("[ACTG]GG")
 matches = comp_pam.finditer(complementary(seq))
 comp_loc = []
 for match in matches:
   comp_loc.append(match.span())
 return pam_loc, comp_loc

#Input: sequence, Output: complementary sequence
def complementary(seq):
 comp_dict = {'A':'T','T':'A','C':'G','G':'C','Y':'R','R':'Y','W':'W','S':'S','K':'M','M':'K','N':'N'}
 comp_seq = ""
 for char in seq:
   comp_seq += comp_dict[char]
 return comp_seq

seq = "ACGGCATGGCTAGCTAGCTACGAGCTAGCTAAAGAGGGGAGTTTCTCC"
a, b = get_PAM(seq)

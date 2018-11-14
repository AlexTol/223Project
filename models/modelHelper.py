import json
import os
from ChromosomeRegion import ChromosomeRegion

def OstreococcusTauri():
    path = 'Genomes/Ostreococcus Tauri'
    os.mkdir(path)
    
    cr1 = ChromosomeRegion()
    cr2 = ChromosomeRegion()
    cr3 = ChromosomeRegion()
    cr1.assignVals('1', 'NC_014426.2', {'pl' : '1092397,1094430' ,'risp' : '1078419,1079394' })
    cr2.assignVals('2', 'NC_014427.2', { 'nsd' : '1072391,1073596' , 'mfsd' : '1058207,1061056'})
    cr3.assignVals('3', 'NC_014428.2', {'derlin' : '986536,987282'  , 'rpS13' : '958157,959171'})

    jS1 = cr1.toJSON()
    jS2 = cr2.toJSON()
    jS3 = cr3.toJSON()

    filename = str(cr1.region) + '.txt' 
    with open(os.path.join(path,filename), 'w') as out:
        out.write(jS1)

    filename = str(cr2.region) + '.txt' 
    with open(os.path.join(path,filename), 'w') as out:
        out.write(jS2)

    filename = str(cr3.region) + '.txt' 
    with open(os.path.join(path,filename), 'w') as out:
        out.write(jS3)


#cr = ChromosomeRegion()
#cr.assignVals('2R', 'AT5678.1',{'gcc':'100000,200000', 'gpp': '300000,400000'})

#jString = cr.toJSON()

#print(jString)

#ncr = ChromosomeRegion()
#ncr.fromJSON(json.loads(jString))
OstreococcusTauri()
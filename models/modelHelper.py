import json
from ChromosomeRegion import ChromosomeRegion

cr = ChromosomeRegion()
cr.assignVals('2R', 'AT5678.1',{'gcc':'100000,200000', 'gpp': '300000,400000'})

jString = cr.toJSON()

print(jString)

ncr = ChromosomeRegion()
ncr.fromJSON(json.loads(jString))
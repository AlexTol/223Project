import json
class ChromosomeRegion(object):

    def __init__(self):
        self.region = '' #for example
        self.id = ''  #for example
        self.genes = {}

    def assignVals(self, r = '',i = '', g = ''):
        self.region = r
        self.id = i
        self.genes = g

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def fromJSON(self,j):
        for item,val in j.items():
            if(item == 'id'):
                self.id = val
            if(item == 'region'):
                self.region = val
            if(item == 'genes'):
                for gene, region in val.items():
                    self.genes[gene] = region
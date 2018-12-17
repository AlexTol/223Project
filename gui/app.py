from appJar import gui

import requests
import json
import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.
#the file system now starts from the directory above
from modules import PAMFinder
from modules import GRNAGenerator
from models.ChromosomeRegion import ChromosomeRegion


def holder(btn):
    print('nothing much')

def getGRNA():
    templateGRNAs, complementGRNAs = GRNAGenerator.generateGRNAPairs(app.getTextArea('t2').upper())
    
    templString = ''
    for item in templateGRNAs:
        templString = templString + str(item) + ' '
    complString = ''
    for item in complementGRNAs:
        complString = complString + str(item) + ' '

    app.setLabel('l22', templString)
    app.setLabel('l24', complString)

    try:
        app.showLabel('l21')
    except:
        print('widget already shown')
    try:
        app.showLabel('l22')
    except:
        print('widget already shown')
    try:
        app.showLabel('l23')
    except:
        print('widget already shown')
    try:
        app.showLabel('l24')
    except:
        print('widget already shown')

def findPAMSites():
    strand = app.getTextArea('t1')
    templateLocations , complementLocations = PAMFinder.get_PAM(strand.upper())
    templString = ''
    for item in templateLocations:
        templString = templString + str(item) + ' '
    complString = ''
    for item in complementLocations:
        complString = complString + str(item) + ' '

    app.setLabel('l12', templString)
    app.setLabel('l14', complString)

    try:
        app.showLabel('l11')
    except:
        print('widget already shown')
    try:
        app.showLabel('l12')
    except:
        print('widget already shown')
    try:
        app.showLabel('l13')
    except:
        print('widget already shown')
    try:
        app.showLabel('l14')
    except:
        print('widget already shown')

def hideRegion1():
    try:
        app.removeTextArea('t1')
    except:
        print('text area already hidden')
    
    try:    
        app.removeButton('Find Pam Sites')
    except:
        print('widget already hidden')
    
    try:    
        app.removeLabel('l11')
    except:
        print('widget already hidden')

    try:    
        app.removeLabel('l12')
    except:
        print('widget already hidden')

    try:    
        app.removeLabel('l13')
    except:
        print('widget already hidden')

    try:    
        app.removeLabel('l14')
    except:
        print('widget already hidden')

def showRegion1():
    app.addScrolledTextArea('t1',4)
    app.addButton('Find Pam Sites',findPAMSites,5)
    app.addLabel('l11','Template Strand Pam Sites:',6)
    app.addLabel('l12','',7)
    app.addLabel('l13','Sense Strand Pam Sites:',8)
    app.addLabel('l14','',9)
    app.hideLabel('l11')
    app.hideLabel('l12')
    app.hideLabel('l13')
    app.hideLabel('l14')

def hideRegion2():
    try:
        app.removeOptionBox('Species')
    except:
        print('widget already hidden')
    try:
        app.removeOptionBox('Chromosome')
    except:
        print('widget already hidden')
    try:
        app.removeOptionBox('Gene')
    except:
        print('widget already hidden')
    try:
        app.removeButton('Get GRNA for Gene')
    except:
        print('widget already hidden')
    try:
        app.removeLabel('l31')
    except:
        print('widget already hidden')
    try:
        app.removeLabel('l32')
    except:
        print('widget already hidden')
    try:
        app.removeLabel('l33')
    except:
        print('widget already hidden')
    try:
        app.removeLabel('l34')
    except:
        print('widget already hidden')

    os.chdir(returnPath)

def showRegion2():
    os.chdir(returnPath)
    #app.addButton('tba1',holder,4)
    app.addOptionBox("Species", [], 4,0, callFunction=True)
    app.setOptionBoxChangeFunction('Species', speciesPick)
    app.addOptionBox("Chromosome", [], 5,0)
    app.hideOptionBox('Chromosome')
    app.setOptionBoxChangeFunction('Chromosome', chromosomePick)
    app.addOptionBox("Gene", [], 6,0)
    app.hideOptionBox('Gene')
    app.addButton('Get GRNA for Gene',getGRNAForGene,7)
    app.addLabel('l31','Template Strands',8)
    app.hideLabel('l31')
    app.addLabel('l32','',9)
    app.hideLabel('l32')
    app.addLabel('l33','Sense Strands',10)
    app.hideLabel('l33')
    app.addLabel('l34','',11)
    app.hideLabel('l34')
    
    
    os.chdir('..')
    os.chdir('models/genomes')
    genomes = []
    genomes.append(' ')
    for dirname, dirnames, filenames in os.walk('.'):
        if(dirname != '.'):
            genomes.append(dirname.strip('.\\'))

    app.changeOptionBox("Species",genomes)    


def hideRegion3():
    try:
        app.removeOptionBox('Species1')
    except:
        print('widgey already hidden')

    try:
        app.removeOptionBox('Chromosome1')
    except:
        print('widgey already hidden')

    try:
        app.removeLabel('l41')
    except:
        print('widget already hidden')
    
    try:
        app.removeLabel('l42')
    except:
        print('widget already hidden')

    try:
        app.removeLabel('l43')
    except:
        print('widget already hidden')

    try:
        app.removeLabel('l44')
    except:
        print('widget already hidden')

    try:
        app.removeButton('Get GRNAs for Chr')
    except:
        print('widget already hidden')

    try:
        app.removeLabel('l45')
    except:
        print('widget already hidden')

    try:
        app.removeLabel('l46')
    except:
        print('widget already hidden')

    try:
        app.removeEntry('E41')
    except:
        print('widget already hidden')

    try:
        app.removeEntry('E42')
    except:
        print('widget already hidden')

def showRegion3():
    app.addOptionBox("Species1", [], 4,0, callFunction=True)
    app.setOptionBoxChangeFunction('Species1', speciesPick1)
    app.addOptionBox("Chromosome1", [], 5,0)
    app.hideOptionBox('Chromosome1')
    app.setOptionBoxChangeFunction('Chromosome1', chromosomePick1)
    app.addLabel('l45','Start',6,0)
    app.addEntry('E41',7,0)
    app.addLabel('l46','End',8,0)
    app.addEntry('E42',9,0)
    app.addLabel('l41','Template Strands',10)
    app.hideLabel('l41')
    app.addLabel('l42','',11)
    app.hideLabel('l42')
    app.addLabel('l43','Sense Strands',12)
    app.hideLabel('l43')
    app.addLabel('l44','',13)
    app.hideLabel('l44')
    app.addButton('Get GRNAs for Chr',getGRNAForChromosome,14)
    app.hideButton('Get GRNAs for Chr')

    os.chdir('..')
    os.chdir('models/genomes')
    genomes = []
    genomes.append(' ')
    for dirname, dirnames, filenames in os.walk('.'):
        if(dirname != '.'):
            genomes.append(dirname.strip('.\\'))

    app.changeOptionBox("Species1",genomes) 

def showRegion4():
    app.addScrolledTextArea('t2',4)
    app.addButton('Get GRNAs',getGRNA,5)
    app.addLabel('l21','Template Strand Pam Sites:',6)
    app.addLabel('l22','',7)
    app.addLabel('l23','Sense Strand Pam Sites:',8)
    app.addLabel('l24','',9)
    app.hideLabel('l21')
    app.hideLabel('l22')
    app.hideLabel('l23')
    app.hideLabel('l24')

def hideRegion4():
    try:
        app.removeTextArea('t2')
    except:
        print('text area already hidden')
    
    try:    
        app.removeButton('Get GRNAs')
    except:
        print('widget already hidden')

    try:    
        app.removeLabel('l21')
    except:
        print('widget already hidden')

    try:    
        app.removeLabel('l22')
    except:
        print('widget already hidden')

    try:    
        app.removeLabel('l23')
    except:
        print('widget already hidden')

    try:    
        app.removeLabel('l24')
    except:
        print('widget already hidden')

def changeFunc(rb):
    returnPath = os.getcwd()
    if(app.getRadioButton("option") == "Find all potential PAM sequences"):
        hideRegion2()
        hideRegion3()
        hideRegion4()
        showRegion1()
    elif(app.getRadioButton("option") == "Get Best GRNA for gene"):
        hideRegion1()
        hideRegion3()
        hideRegion4()
        showRegion2()
    elif(app.getRadioButton("option") == "Get Best GRNA for chromosome region"):
        hideRegion1()
        hideRegion2()
        hideRegion4()
        showRegion3()
    elif(app.getRadioButton("option") == "Get Best GRNA for strand"):
        hideRegion1()
        hideRegion2()
        hideRegion3()
        showRegion4()
    
def speciesPick():
    os.chdir(returnPath)
    os.chdir('..')
    os.chdir('models/genomes')
    
    species = app.getOptionBox('Species')
    os.chdir(species)

    chromosomes = []
    chromosomes.append(' ')
    for dirname, dirnames, filenames in os.walk('.'):
        for mfile in filenames:
            chromosomes.append(mfile.strip('\.txt'))
    app.changeOptionBox("Chromosome",chromosomes) 

    app.showOptionBox('Chromosome')

def speciesPick1():
    os.chdir(returnPath)
    os.chdir('..')
    os.chdir('models/genomes')
    
    species = app.getOptionBox('Species1')
    os.chdir(species)

    chromosomes = []
    chromosomes.append(' ')
    for dirname, dirnames, filenames in os.walk('.'):
        for mfile in filenames:
            chromosomes.append(mfile.strip('\.txt'))
    app.changeOptionBox("Chromosome1",chromosomes) 

    app.showOptionBox('Chromosome1')


def chromosomePick():
    chromosome = app.getOptionBox('Chromosome')
    string = ''
    with open(chromosome + '.txt') as f:
        for line in f:
            string = string + line
    
    global ncr
    ncr = ChromosomeRegion()
    ncr.fromJSON(json.loads(string))


    genes = []
    genes.append('')
    for gene, region in ncr.genes.items():
        genes.append(gene)

    app.changeOptionBox("Gene",genes)
    app.showOptionBox('Gene')

def chromosomePick1():
    chromosome = app.getOptionBox('Chromosome1')
    string = ''
    with open(chromosome + '.txt') as f:
        for line in f:
            string = string + line
    
    global ncr
    ncr = ChromosomeRegion()
    ncr.fromJSON(json.loads(string))

    app.showButton('Get GRNAs for Chr')

def getGRNAForGene():
    site = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    params = {}
    params['db'] = 'nucleotide'
    params['id'] = str(ncr.id)
    params['rettype'] = 'fasta'

    gene = app.getOptionBox('Gene')
    token = ncr.genes[gene].split(',')
    params['from'] = token[0]
    params['to'] = token[1]

    r = requests.get(site, params = params)
    
    print('here')
    dna = r.text[130:]
    dna = dna.strip()
    dna = dna.replace('\n', '')
    templateGRNAs, complementGRNAs = GRNAGenerator.generateGRNAPairs(dna)

    tempScores = []
    tempDict = {}
    compScores = []
    compDict = {}
    for grna in templateGRNAs:
        tempScores.append(GRNAGenerator.getOffTargetScore(grna,dna) + GRNAGenerator.on_target_score(grna))
    for i in range(0,len(templateGRNAs)):
        tempDict[templateGRNAs[i]] = tempScores[i]

    for grna in complementGRNAs:
        compScores.append(GRNAGenerator.getOffTargetScore(grna,dna) + GRNAGenerator.on_target_score(grna))
    for i in range(0,len(complementGRNAs)):
        compDict[ complementGRNAs[i]] = compScores[i]

    finalTemplateGRNAs = GRNAGenerator.chooseBestFive(tempDict)
    finalComplementGRNAs = GRNAGenerator.chooseBestFive(compDict)

    finalTempString = ''
    for i in range(0,5):
        finalTempString += str(i + 1) + ' :   ' + finalTemplateGRNAs[i] + '       '
    
    finalCompString = ''
    for i in range(0,5):
        finalCompString += str(i + 1) + ' :   ' + finalComplementGRNAs[i] + '      '

    app.setLabel('l32',finalTempString)
    app.setLabel('l34',finalCompString)
    app.showLabel('l31')
    app.showLabel('l32')
    app.showLabel('l33')
    app.showLabel('l34')

def getGRNAForChromosome():
    site = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    params = {}
    params['db'] = 'nucleotide'
    params['id'] = str(ncr.id)
    params['from'] = app.getEntry('E41')
    params['to'] = app.getEntry('E42')
    params['rettype'] = 'fasta'

    r = requests.get(site, params = params)

    dna = r.text[130:]
    dna = dna.strip()
    dna = dna.replace('\n', '')
    templateGRNAs, complementGRNAs = GRNAGenerator.generateGRNAPairs(dna)
    
    tempScores = []
    tempDict = {}
    compScores = []
    compDict = {}
    for grna in templateGRNAs:
        tempScores.append(GRNAGenerator.getOffTargetScore(grna,dna[:100000]) + GRNAGenerator.on_target_score(grna))
    for i in range(0,len(templateGRNAs)):
        tempDict[templateGRNAs[i]] = tempScores[i]

    for grna in complementGRNAs:
        compScores.append(GRNAGenerator.getOffTargetScore(grna,dna[:100000]) + GRNAGenerator.on_target_score(grna))
    for i in range(0,len(complementGRNAs)):
        compDict[ complementGRNAs[i]] = compScores[i]

    finalTemplateGRNAs = GRNAGenerator.chooseBestFive(tempDict)
    finalComplementGRNAs = GRNAGenerator.chooseBestFive(compDict)

    finalTempString = ''
    for i in range(0,5):
        finalTempString += str(i + 1) + ' :   ' + finalTemplateGRNAs[i] + '       '
    
    finalCompString = ''
    for i in range(0,5):
        finalCompString += str(i + 1) + ' :   ' + finalComplementGRNAs[i] + '      '

    app.setLabel('l42',finalTempString)
    app.setLabel('l44',finalCompString)
    app.showLabel('l41')
    app.showLabel('l42')
    app.showLabel('l43')
    app.showLabel('l44')


app = gui("CRISPR TOOL","1500x500")

app.addRadioButton("option", "Find all potential PAM sequences",0)
app.addRadioButton("option", "Get Best GRNA for strand",1)
app.addRadioButton("option", "Get Best GRNA for gene",2)
app.addRadioButton("option", "Get Best GRNA for chromosome region",3)
app.setRadioButtonChangeFunction("option", changeFunc)

app.addScrolledTextArea('t1',4)
app.addButton('Find Pam Sites',findPAMSites,5)
app.addLabel('l11','Template Strand Pam Sites:',6)
app.addLabel('l12','',7)
app.addLabel('l13','Sense Strand Pam Sites:',8)
app.addLabel('l14','',9)
app.hideLabel('l11')
app.hideLabel('l12')
app.hideLabel('l13')
app.hideLabel('l14')

global returnPath
returnPath = os.getcwd()

app.go()
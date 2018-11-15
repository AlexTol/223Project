from appJar import gui

import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.
#the file system now starts from the directory above
from modules import PAMFinder
from modules import GRNAGenerator


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

    os.chdir(returnPath)

def showRegion2():
    #app.addButton('tba1',holder,4)
    global returnPath
    returnPath = os.getcwd()
    app.addOptionBox("Species", [], 4,1, callFunction=True)
    app.setOptionBoxChangeFunction('Species', speciesPick)
    app.addOptionBox("Chromosome", [], 5,1)
    app.addOptionBox("Gene", [], 6,1)
    
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
        app.removeButton('tba2')
    except:
        print('widget already hidden')

def showRegion3():
    app.addButton('tba2',holder,4)

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
    elif(app.getRadioButton("option") == "Get Best GRNA for chromosome"):
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
    print('hi')

app = gui("CRISPR TOOL","400x400")

app.addRadioButton("option", "Find all potential PAM sequences",0)
app.addRadioButton("option", "Get Best GRNA for strand",1)
app.addRadioButton("option", "Get Best GRNA for gene",2)
app.addRadioButton("option", "Get Best GRNA for chromosome",3)
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

app.go()
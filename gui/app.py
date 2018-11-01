from appJar import gui

import sys
sys.path.append("..") # Adds higher directory to python modules path.
#the file system now starts from the directory above
from modules import PAMFinder


def holder(btn):
    print('nothing much')

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
    app.addScrolledTextArea('t1',3)
    app.addButton('Find Pam Sites',findPAMSites,4)
    app.addLabel('l11','Template Strand Pam Sites:',5)
    app.addLabel('l12','',6)
    app.addLabel('l13','Sense Strand Pam Sites:',7)
    app.addLabel('l14','',8)
    app.hideLabel('l11')
    app.hideLabel('l12')
    app.hideLabel('l13')
    app.hideLabel('l14')

def hideRegion2():
    try:
        app.removeButton('tba1')
    except:
        print('widget already hidden')

def showRegion2():
    app.addButton('tba1',holder,3)

def hideRegion3():
    try:
        app.removeButton('tba2')
    except:
        print('widget already hidden')

def showRegion3():
    app.addButton('tba2',holder,3)

def changeFunc(rb):
    if(app.getRadioButton("option") == "Find all potential PAM sequences"):
        hideRegion2()
        hideRegion3()
        showRegion1()
    elif(app.getRadioButton("option") == "Get Best GRNA for gene"):
        hideRegion1()
        hideRegion3()
        showRegion2()
    elif(app.getRadioButton("option") == "Get Best GRNA for region"):
        hideRegion1()
        hideRegion2()
        showRegion3()
        

app = gui("CRISPR TOOL","400x400")

app.addRadioButton("option", "Find all potential PAM sequences",0,0)
app.addRadioButton("option", "Get Best GRNA for gene",1)
app.addRadioButton("option", "Get Best GRNA for region",2)
app.setRadioButtonChangeFunction("option", changeFunc)

app.addScrolledTextArea('t1',3)
app.addButton('Find Pam Sites',findPAMSites,4)
app.addLabel('l11','Template Strand Pam Sites:',5)
app.addLabel('l12','',6)
app.addLabel('l13','Sense Strand Pam Sites:',7)
app.addLabel('l14','',8)
app.hideLabel('l11')
app.hideLabel('l12')
app.hideLabel('l13')
app.hideLabel('l14')

app.go()
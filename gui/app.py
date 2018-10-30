from appJar import gui
def holder(btn):
    print('nothing much')

def hideRegion1():
    try:
        app.removeTextArea('t1')
    except:
        print('text area already hidden')
    
    try:    
        app.removeButton('Find Pam Sites')
    except:
        print('widget already hidden')

def showRegion1():
    app.addScrolledTextArea('t1',3)
    app.addButton('Find Pam Sites',holder,4)

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
app.addButton('Find Pam Sites',holder,4)

app.go()
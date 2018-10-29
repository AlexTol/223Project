from appJar import gui
def holder(btn):
    print('nothing much')

def hideRegion1():
    app.hideTextArea('t1')
    app.hideButton('Find Pam Sites')
def showRegion1():
    app.showTextArea('t1')
    app.showButton('Find Pam Sites')

def hideRegion2():
    app.hideButton('tba1')
def showRegion2():
    app.showButton('tba1')

def hideRegion3():
    app.hideButton('tba2')
def showRegion3():
    app.showButton('tba2')

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

app.addRadioButton("option", "Find all potential PAM sequences")
app.addRadioButton("option", "Get Best GRNA for gene")
app.addRadioButton("option", "Get Best GRNA for region")
app.setRadioButtonChangeFunction("option", changeFunc)

app.addScrolledTextArea('t1')
app.addButton('Find Pam Sites',holder)

app.addButton('tba1',holder)
app.hideButton('tba1')

app.addButton('tba2',holder)
app.hideButton('tba2')

app.add
app.go()
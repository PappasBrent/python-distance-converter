# Imports all from tkinter
from tkinter import *

# Defines calculation function for later use
def calculate(*args):
    try:
        inputUnit=inputUnitName.get()
        outputUnit=outputUnitName.get()

        value=float(inputDistTextVar.get())

        # First converts input to feet...
        if inputUnit=='inches':
            value*=(1/12)
        elif inputUnit=='feet':
            value*=1
        elif inputUnit=='yards':
            value*=3
        elif inputUnit=='miles':
            value*=5280
        elif inputUnit=='millimeters':
            value*=(1/304.8)
        elif inputUnit=='centimeters':
            value*=(1/30.48)
        elif inputUnit=='meters':
            value*=3.28084
        elif inputUnit=='kilometers':
            value*=3280.84

        # ...then to the appropriate output value
        if outputUnit=='inches':
            result=value*12
        elif outputUnit=='feet':
            result=value
        elif outputUnit=='yards':
            result=value*(1/3)
        elif outputUnit=='miles':
            result=value*(1/5280)
        elif outputUnit=='millimeters':
            result=value*304.8
        elif outputUnit=='centimeters':
            result=value*30.48
        elif outputUnit=='meters':
            result=value*(1/3.28084)
        elif outputUnit=='kilometers':
            result=value*(1/3280.84)
        
        if value==0:
            result=0
        
        outputDistTextVar.set(result)
        inputDistEntry.config(width=len(inputDistTextVar.get())+1)
        outputDistEntry.config(width=len(outputDistTextVar.get()))

    except ValueError:
        outputDistTextVar.set('?')
        
    checkPlural()
    #print(inputUnitName.get(), 'to', outputUnitName.get())

# Defines the checkPlural function for later use
def checkPlural(*args):
    try:
        if inputDistTextVar.get() == '1':
            pass
        else:
            pass
    except ValueError:
        pass
    
# Creates the master root object and stylizes it
root=Tk()
root.title('Distance Converter')
root.config(background='lightgray')

# Creates the frame widget to which all the other widgets are slaves
mainframe=Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.config(padx=5, pady=10, background='lightgray')
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Creates the StringVars storing the values of the input and output
inputDistTextVar=StringVar()
outputDistTextVar=StringVar()

# Entry widget for the input units
inputDistEntry=Entry(mainframe, width=5, textvariable=inputDistTextVar)
inputDistEntry.grid(column=1, row=1, sticky=(W, E))

# = sign label
Label(mainframe, text='=').grid(column=2, row=1, sticky=(W, E))

# Entry widget for the input units; is readonly
outputDistEntry=Entry(mainframe, width=5, textvariable=outputDistTextVar, state='readonly')
outputDistEntry.grid(column=3, row=1, sticky=(W, E))

# Arrays storing the names of the various units
unitNamesPlural=['inches', 'feet', 'yards', 'miles', 'millimeters', 'centimeters', 'meters', 'kilometers']
unitNamesSingular=['inch', 'foot', 'yard', 'mile', 'millimeter', 'centimeter', 'meter', 'kilometer']

# String var storing the input unit name
inputUnitName=StringVar(root)
inputUnitName.set('inches')

# OptionMenu widget for selecting the input unit name
inputUnitList=OptionMenu(mainframe, inputUnitName, *unitNamesPlural, command=calculate)
inputUnitList.config(border='2', highlightthickness='0')
inputUnitList.grid(column=1, row=3, sticky=(N,W,S,E))

# String var storing the output unit name
outputUnitName=StringVar(root)
outputUnitName.set('meters')

# OptionMenu widget for selecting the output unit name
outputUnitList=OptionMenu(mainframe, outputUnitName, *unitNamesPlural, command=calculate)
outputUnitList.config(border='2', highlightthickness='0')
outputUnitList.grid(column=3, row=3, sticky=(N,W,S,E))

# Stylizes every widget
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
    child.config(background='lightgray')
    child.config(border='2')
    child.config(font=('Helvecta', 12))

# Stylizes specific widgets
inputDistEntry.config(bg='white')
outputDistEntry.config(bg='white')

# Begins the program with focus on the inputDistEntry widget
inputDistEntry.focus()

# Assigns keybinds to specific widgets
inputDistEntry.bind('<KeyRelease>', calculate)


root.mainloop()

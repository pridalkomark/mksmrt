from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox
import tkinter.simpledialog
import math

#Mark 'o Soft(ware): Mark 'o Soft Math Related Tools (C) 2024

#0 - 9 test and plecehold
#10 option edit allow
#11 say license on start
#12 does canvas exist (obsolete)
#13 can -1st option open console & debug? + dev mode in help
#14 is output simple (if true then no explanation)
optionTable = [True, 1, "hello", None, 2, None, None, None, None, None, True, False, False, False, False]

a = 0
b = 0
c = 0
d = 0
ma = 0
mb = 0
mc = 0
md = 0
e = 0
f = 0
r = 0

unitConverts = ["...Farenheiht to Celcius.", "...Celcius to Farenheiht."]

def unitConvertWindow():
    if optionTable[13] == True:
        pass
    else:
        tkinter.messagebox.showerror(title="Mark 'o Soft Math Related Tools", message="Unfinished.\nChange options to access.\nNote: this is locked for a reason!!")
        return 1
    unitConvertWind = Toplevel()
    unitConvertWind.maxsize(300, 250)
#    unitConvertWind.minsize(300, 250)
    conWin = ttk.Frame(unitConvertWind, padding=15)
    conWin.grid()
    ttk.Label(conWin, text="Convert units!", image=imgSmile, compound= LEFT, padding=0).grid(column=1, row=0)
    ttk.Label(conWin, text="                          ", compound= LEFT, padding=0).grid(column=0, row=0)
    ttk.Label(conWin, text="                Convert...", compound= LEFT, padding=0).grid(column=0, row=1)
    ttk.Label(conWin, text="                          ", compound= LEFT, padding=0).grid(column=0, row=2)
    ttk.Label(conWin, text="                          ", compound= LEFT, padding=0).grid(column=0, row=3)

    anumbox = Spinbox(conWin, from_=-999999999, to=999999999)
    anumbox.grid(column=1, row=1)
    
    convertbox = ttk.Combobox(conWin, values = unitConverts)
    convertbox.set("...pick a unit pair.")
    convertbox.grid(column=1, row=2)
    
    ttk.Button(conWin, text="Calculate...", image=imgCalcEdit, compound= LEFT, command= lambda: unitConvert(anumbox.get(), convertbox.get())).grid(column=1, row=3)
    
    ttk.Label(conWin, text="                          ", compound= LEFT, padding=0).grid(column=2, row=0)
    ttk.Label(conWin, text="                          ", compound= LEFT, padding=0).grid(column=2, row=1)
    ttk.Label(conWin, text="                          ", compound= LEFT, padding=0).grid(column=2, row=2)
    ttk.Label(conWin, text="                          ", compound= LEFT, padding=0).grid(column=2, row=3)
    unitConvertWind.title("Mark 'o Soft Math Related Tools: Unit conversion")
    unitConvertWind.mainloop()
    pass


def unitConvert(anum, convert):
#    if convert == "...Farenheiht to Celcius.":
#        
    print(anum)
    print(convert)
    pass


def area2DSquare():
    if optionTable[14] == True:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DSquare", message="Square:\nArea=" + str(a*a) + "\nParemeter=" + str(2*a) + "\n")
    else:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DSquare", message="Square:\na=" + str(a) + "\nArea=a*a\nArea=" + str(a) + "*" + str(a) + "\nArea=" + str(a*a) + "\nParemeter=2*a\nParemeter=2*" + str(a) + "\nParemeter=" + str(2*a) + "\n")

def area2DRectangle():
    if optionTable[14] == True:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DRectangle", message="Rectangle:\nArea=" + str(a*b) + "\nParemeter=" + str(2*(a+b)) + "\n")
    else:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DRectangle", message="Rectangle:\na=" + str(a) + "\nb=" + str(b) + "\nArea=a*b\nArea=" + str(a) + "*" + str(b) + "\nArea=" + str(a*b) + "\nParemeter=2*(a+b)\nParemeter=2*(" + str(a) + "+" + str(b) + ")\nParemeter=" + str(2*(a+b)) + "\n")

def area2DTrapez():
    if optionTable[14] == True:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DTrapez", message="Trapez:\nArea=" + str(((a+c)/2)*ma) + "\nParemeter=" + str(a+b+c+d) + "\n")
    else:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DTrapez", message="Trapez:\na=" + str(a) + "\nb=" + str(b) + "\nc=" + str(c) + "\nd=" + str(d) + "\nma=" + str(ma) + "\nArea=(a+c/2)*ma\nArea=(" + str(a) + "+" + str(c) + "/2)*" + str(ma) + "\nArea=" + str(((a+c)/2)*ma) + "\nParemeter=a+b+c+d\nParemeter=" + str(a) + "+" + str(b) + "+" + str(c) + "+" + str(d) + "\nParemeter=" + str(a+b+c+d) + "\n")

def area2DTriangle():
    if optionTable[14] == True:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DTriangle", message="Triangle:\nArea=" + str((a*ma)/2) + "\nParemeter=" + str(a+b+c) + "\n")
    else:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DTriangle", message="Triangle:\na=" + str(a) + "\nb=" + str(b) + "\nc=" + str(c) + "\nma=" + str(ma) + "\nArea=(a*ma)/2\nArea=(" + str(a) + "*" + str(ma) + ")/2\nArea=" + str((a*ma)/2) + "\nParemeter=a+b+c\nParemeter=" + str(a) + "+" + str(b) + "+" + str(c) + "\nParemeter=" + str(a+b+c) + "\n")

def area2DParalellogram():
    if optionTable[14] == True:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DParalellogram", message="Paralellogram:\nArea=" + str(a*ma) + "\nParemeter=" + str(2*(a+b)) + "\n")
    else:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DParalellogram", message="Paralellogram:\na=" + str(a) + "\nb=" + str(b) + "\nma=" + str(ma) + "\nArea=a*ma\nArea=" + str(a) + "*" + str(ma) + "\nArea=" + str(a*ma) + "\nParemeter=2*(a+b)\nParemeter=2*(" + str(a) + "+" + str(b) + ")\nParemeter=" + str(2*(a+b)) + "\n")

def area2DDeltoid():
    if optionTable[14] == True:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DDeltoid", message="Deltoid:\nArea=" + str((e*f)/2) + "\nParemeter=" + str(2*(a+b)) + "\n")
    else:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DDeltoid", message="Deltoid:\na=" + str(a) + "\nb=" + str(b) + "\ne=" + str(e) + "\nf=" + str(f) + "\nArea=(e*f)/2\nArea=(" + str(e) + "*" + str(f) + ")/2\nArea=" + str(a*ma) + "\nParemeter=2*(a+b)\nParemeter=2*(" + str(a) + "+" + str(b) + ")\nParemeter=" + str(2*(a+b)) + "\n")

def area2Rhombus():
    if optionTable[14] == True:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2Rhombus", message="Rhombus:\nArea=" + str(4*a) + "\nParemeter=" + str(a*ma) + "\n")
    else:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2Rhombus", message="Rhombus:\na=" + str(a) + "\nma=" + str(ma) + "\nArea=(a*ma)/2\nArea=(" + str(a) + "*" + str(ma) + "\nArea=" + str(a*ma) + "\nParemeter=4*a\nParemeter=4*" + str(a) + "\nParemeter=" + str(4*a) + "\n")

def area2DCircle():
    if optionTable[14] == True:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DCircle", message="Circle:\nArea=" + str(r*r*math.pi) + "\nParemeter=" + str(2*r*math.pi) + "\n")
    else:
        tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: Output of area2DCircle", message="Circle:\na=" + str(a) + "\nπ=" + str(math.pi) + "\nArea=(r*r*π)/2\nArea=(" + str(r) + "*" + str(r) + "*" + str(math.pi) + "\nArea=" + str(r*r*math.pi) + "\nParemeter=2*r*π\nParemeter=r*" + str(r) + "*" + str(math.pi) + "\nParemeter=" + str(2*r*math.pi) + "\n")

def aSideSet():
    global a
    a = tkinter.simpledialog.askfloat("Mark 'o Soft Math Related Tools: Input a side", "Input value for a side.\nSyntax: 3.14; 43.0\nNote: no unit support or conversion!")

def bSideSet():
    global b
    b = tkinter.simpledialog.askfloat("Mark 'o Soft Math Related Tools: Input b side", "Input value for b side.\nSyntax: 3.14; 43.0\nNote: no unit support or conversion!")

def cSideSet():
    global c
    c = tkinter.simpledialog.askfloat("Mark 'o Soft Math Related Tools: Input c side", "Input value for c side.\nSyntax: 3.14; 43.0\nNote: no unit support or conversion!")

def dSideSet():
    global d
    d = tkinter.simpledialog.askfloat("Mark 'o Soft Math Related Tools: Input d side", "Input value for d side.\nSyntax: 3.14; 43.0\nNote: no unit support or conversion!")

def maHeightSet():
    global ma
    ma = tkinter.simpledialog.askfloat("Mark 'o Soft Math Related Tools: Input ma height", "Input value for ma height.\nSyntax: 3.14; 43.0\nNote: no unit support or conversion!")

def mbHeightSet():
    global mb
    mb = tkinter.simpledialog.askfloat("Mark 'o Soft Math Related Tools: Input mb height", "Input value for mb height.\nSyntax: 3.14; 43.0\nNote: no unit support or conversion!")

def mcHeightSet():
    global mc
    mc = tkinter.simpledialog.askfloat("Mark 'o Soft Math Related Tools: Input mc height", "Input value for mc height.\nSyntax: 3.14; 43.0\nNote: no unit support or conversion!")

def mdHeightSet():
    global md
    md = tkinter.simpledialog.askfloat("Mark 'o Soft Math Related Tools: Input md height", "Input value for md height.\nSyntax: 3.14; 43.0\nNote: no unit support or conversion!")

def eSet():
    global e
    e = tkinter.simpledialog.askfloat("Mark 'o Soft Math Related Tools: Input e", "Input value for e.\nSyntax: 3.14; 43.0\nNote: no unit support or conversion!")

def fSet():
    global f
    f = tkinter.simpledialog.askfloat("Mark 'o Soft Math Related Tools: Input f", "Input value for f.\nSyntax: 3.14; 43.0\nNote: no unit support or conversion!")

def rRadiusSet():
    global r
    r = tkinter.simpledialog.askfloat("Mark 'o Soft Math Related Tools: Input r radius", "Input value for r radius.\nSyntax: 3.14; 43.0\nNote: no unit support or conversion!")
    
def helloWorld():
    tkinter.messagebox.showinfo(title="hello world", message="hello there!!")

def openConsole():
    if optionTable[13] == True:
        exec(tkinter.simpledialog.askstring("CONSOLE & DEBUG!! DO NOT FOOL AROUND!!", "THIS DEFS SOLE PURPOSE IS TO DEBUG,\nUSE ONLY IF YOU KNOW WHAT YOU ARE DOING!!"))
    else:
        tkinter.messagebox.showerror(title="Who do you think you are??", message="This place is not for maggots like you! You aren't a dev, are you?!")
    
def editOptionTable():
    if optionTable[10] == True:
        pass
    else:
        tkinter.messagebox.showerror(title="", message="The options are locked. Change the\noptionsTable in the program to\nallow on-fly setup.")
        return
    editOptionTableInputIndex = tkinter.simpledialog.askinteger("", "Input option table index. Maximal value: " + str(len(optionTable) - 1))
    if editOptionTableInputIndex == -1 and optionTable[13] == True:
        openConsole()
        return
    if type(optionTable[editOptionTableInputIndex]) == bool:
        optionTable[editOptionTableInputIndex] = tkinter.messagebox.askyesno(title="", message="Current value of " + str(editOptionTableInputIndex) + " is " + str(optionTable[editOptionTableInputIndex]) + ".\nPress YES to set to true, NO to set to false.\nTo not change the value, set it to the current state.")
    if type(optionTable[editOptionTableInputIndex]) == int:
        optionTable[editOptionTableInputIndex] = tkinter.simpledialog.askinteger("", "Current value of " + str(editOptionTableInputIndex) + " is " + str(optionTable[editOptionTableInputIndex]) + ".\nType the new value then press OK or key ENTER.\nTo not change the value, set it to the current state.")
    if type(optionTable[editOptionTableInputIndex]) == str:
        optionTable[editOptionTableInputIndex] = tkinter.simpledialog.askstring("", "Current value of " + str(editOptionTableInputIndex) + " is " + str(optionTable[editOptionTableInputIndex]) + ".\nType the new value then press OK or key ENTER.\nTo not change the value, set it to the current state.")
    else:
        #tkinter.messagebox.showerror(title="", message="Current value of " + str(editOptionTableInputIndex) + " is " + str(optionTable[editOptionTableInputIndex]) + ", its type is " + str(type(optionTable[editOptionTableInputIndex])) + ".\nThis entry can be NoneType because it is a placeholder and can't be changed\nor you messed something up. In this case\nrestart the program now!")
        pass

if optionTable[11] == True:
    f = open("gpl-3.0.txt")
    print(f.read())
    tkinter.messagebox.showwarning(title="Mark 'o Soft Math Related Tools: Legal", message="IMPORTANT STUFF IN CONSOLE!!\nPlease read the license provided in the console. This program\noperates under the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007.\n\nIF YOU CONTINUE THE EXECUTION OF THIS\nPROGRAM, YOU ACCEPT THESE TERMS.")
    f.close()
else:
    pass

def stopProg():
    root.destroy()

def helpAbout():
    tkinter.messagebox.showinfo(title="Mark 'o Soft Math Related Tools: About", message="Mark 'o Soft Math Related Tools.\nVersion 1." + str(optionTable[4]) + "\n\nMark 'o Soft Math Related Tools.\nCopyright (C) 2024  Mark 'o Soft(ware)\nIcons: Copyright (C) Mark James http://www.famfamfam.com/lab/icons/silk/\n\nYou should have received a copy of the GNU General Public License along with this program.\nIf not, see <https://www.gnu.org/licenses/>.\n\nIcons: This work is licensed under a\nCreative Commons Attribution 2.5 License.\n[ http://creativecommons.org/licenses/by/2.5/ ]")
    if tkinter.messagebox.askyesno(title="Mark 'o Soft Math Related Tools: Legal", message="Do you want to see the GPL license?") == True:
        f = open("gpl-3.0.txt")
        print(f.read())
        tkinter.messagebox.showwarning(title="Mark 'o Soft Math Related Tools: Legal", message="IMPORTANT STUFF IN CONSOLE!!\nPlease read the license provided in the console. This program\noperates under the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007.\n\nIF YOU CONTINUE THE EXECUTION OF THIS\nPROGRAM, YOU ACCEPT THESE TERMS.")
        f.close()
    else:
        pass
    if optionTable[13] == True:
        tkinter.messagebox.showinfo(title="devstuff: optionTable list", message="devstuff: optionTable list\n0 - 9 test and plecehold\n10 option edit allow\n11 say license on start\n12 does canvas exist (obsolete)\n13 can -1st option open console & debug? + dev mode in help\n14 is output simple (if true then no explanation)")
        tkinter.messagebox.showinfo(title="devstuff: console", message="devstuff: console\njust a shortcut to execute functions\ntest with the helloWorld() func")
    else:
        pass

root = Tk()




iconCog = Image.open('res/cog.png')
imgCog = ImageTk.PhotoImage(iconCog)

iconStop = Image.open('res/stop.png')
imgStop = ImageTk.PhotoImage(iconStop)

iconTennisBall = Image.open('res/sport_tennis.png')
imgTennisBall = ImageTk.PhotoImage(iconTennisBall)

iconSquare = Image.open('shape/square.png')
imgSquare = ImageTk.PhotoImage(iconSquare)

iconTriangle = Image.open('shape/triangle.png')
imgTriangle = ImageTk.PhotoImage(iconTriangle)

iconTrapezium = Image.open('shape/trapezium.png')
imgTrapezium = ImageTk.PhotoImage(iconTrapezium)

iconRectangle = Image.open('shape/rectangle.png')
imgRectangle = ImageTk.PhotoImage(iconRectangle)

iconParalelogram = Image.open('shape/paralelogram.png')
imgParalelogram = ImageTk.PhotoImage(iconParalelogram)

iconDeltoid = Image.open('shape/deltoid.png')
imgDeltoid = ImageTk.PhotoImage(iconDeltoid)

iconCircle = Image.open('shape/circle.png')
imgCircle = ImageTk.PhotoImage(iconCircle)

iconCalcEdit= Image.open('res/calculator_edit.png')
imgCalcEdit = ImageTk.PhotoImage(iconCalcEdit)

iconBugWarn= Image.open('res/bug_error.png')
imgBugWarn = ImageTk.PhotoImage(iconBugWarn)

iconSmile= Image.open('res/emoticon_smile.png')
imgSmile = ImageTk.PhotoImage(iconSmile)

iconBook= Image.open('res/book.png')
imgBook = ImageTk.PhotoImage(iconBook)


menubar = Menu(root)
progmenu = Menu(menubar, tearoff=0)
progmenu.add_command(label="About...", image=imgTennisBall, compound= LEFT, command=helpAbout)
progmenu.add_command(label="Program options...", image=imgCog, compound= LEFT, command=editOptionTable)
progmenu.add_command(label="Debug Console™ (option 13 only)...", image=imgBugWarn, compound=RIGHT, command=openConsole)
progmenu.add_separator()
progmenu.add_command(label="Exit", image=imgStop, compound= LEFT, command=stopProg)
menubar.add_cascade(label="Program", menu=progmenu)

vartools = Menu(menubar, tearoff=0)
vartools.add_command(label="...a side...", image=imgCalcEdit, compound= LEFT, command=aSideSet)
vartools.add_command(label="...b side...", image=imgCalcEdit, compound= LEFT, command=bSideSet)
vartools.add_command(label="...c side...", image=imgCalcEdit, compound= LEFT, command=cSideSet)
vartools.add_command(label="...d side...", image=imgCalcEdit, compound= LEFT, command=dSideSet)
vartools.add_separator()
vartools.add_command(label="...ma height...", image=imgCalcEdit, compound= LEFT, command=maHeightSet)
vartools.add_command(label="...mb height...", image=imgCalcEdit, compound= LEFT, command=mbHeightSet)
vartools.add_command(label="...mc height...", image=imgCalcEdit, compound= LEFT, command=mcHeightSet)
vartools.add_command(label="...md height...", image=imgCalcEdit, compound= LEFT, command=mdHeightSet)
vartools.add_separator()
vartools.add_command(label="...e...", image=imgCalcEdit, compound= LEFT, command=eSet)
vartools.add_command(label="...f...", image=imgCalcEdit, compound= LEFT, command=fSet)
vartools.add_separator()
vartools.add_command(label="...r radius...", image=imgCalcEdit, compound= LEFT, command=rRadiusSet)
menubar.add_cascade(label="Set value for...", menu=vartools)

flatgeotoolsmenu = Menu(menubar, tearoff=0)
flatgeotoolsmenuarea = Menu(flatgeotoolsmenu, tearoff=0)
flatgeotoolsmenuarea.add_command(label="...square...", image=imgSquare, compound= LEFT, command=area2DSquare)
flatgeotoolsmenuarea.add_command(label="...rectangle...", image=imgRectangle, compound= LEFT, command=area2DRectangle)
flatgeotoolsmenuarea.add_separator()
flatgeotoolsmenuarea.add_command(label="...trapezium...", image=imgTrapezium, compound= LEFT, command=area2DTrapez)
flatgeotoolsmenuarea.add_command(label="...triangle...", image=imgTriangle, compound= LEFT, command=area2DTriangle)
flatgeotoolsmenuarea.add_command(label="...parallelogram...", image=imgParalelogram, compound= LEFT, command=area2DParalellogram)
flatgeotoolsmenuarea.add_command(label="...deltoid...", image=imgDeltoid, compound= LEFT, command=area2DDeltoid)
flatgeotoolsmenuarea.add_command(label="...rhombus...", image=imgDeltoid, compound= LEFT, command=area2Rhombus)
flatgeotoolsmenuarea.add_separator()
flatgeotoolsmenuarea.add_command(label="...circle...", image=imgCircle, compound= LEFT, command=area2DCircle)
flatgeotoolsmenu.add_cascade(label="Calculate area and paremeter for...", menu=flatgeotoolsmenuarea)
menubar.add_cascade(label="2D Geometry Tools", menu=flatgeotoolsmenu)

unitconvertmenu = Menu(menubar, tearoff=0)
unitconvertmenu.add_command(label="Unit conversion", image=imgBook, compound= LEFT, command=unitConvertWindow)
menubar.add_cascade(label="Unit conversion", menu=unitconvertmenu)

root.config(menu=menubar)

mainWin = ttk.Frame(root, padding=15)
mainWin.grid()
'''
ttk.Button(mainWin, text="Move forward...", image=imgArrowRight, compound= LEFT, command=moveForw).grid(column=0, row=0)
ttk.Button(mainWin, text="Move backward...", image=imgArrowLeft, compound= LEFT, command=moveBackw).grid(column=1, row=0)
ttk.Button(mainWin, text="Rotate left...", image=imgArrowRotLeft, compound= LEFT, command=rotLeft).grid(column=0, row=1)
ttk.Button(mainWin, text="Rotate right...", image=imgArrowRotRight, compound= LEFT, command=rotRight).grid(column=1, row=1)
ttk.Button(mainWin, text="Make ring...", image=imgCompactDisk, compound= LEFT, command=makeRing).grid(column=0, row=2)
ttk.Button(mainWin, text="Go to...", image=imgCar, compound= LEFT, command=goTo).grid(column=0, row=3)
ttk.Button(mainWin, text="Get position", image=imgEye, compound= LEFT, command=getPos).grid(column=1, row=3)
ttk.Button(mainWin, text="Go home", image=imgHouseGo, compound= LEFT, command=goHome).grid(column=2, row=3)
ttk.Button(mainWin, text="Clear canvas...", image=imgProgDel, compound= LEFT, command=clScreen).grid(column=0, row=4)
ttk.Button(mainWin, text="Open .COD script...", image=imgFolderPage, compound= LEFT, command=openFile).grid(column=0, row=5)
ttk.Button(mainWin, text="Pencil sharpness...", image=imgPencilDel, compound= LEFT, command=penSharp).grid(column=0, row=6)
ttk.Button(mainWin, text="Pencil color...", image=imgPalette, compound= LEFT, command=penColor).grid(column=1, row=6)
'''
ttk.Label(mainWin, text="Hello there! Tools are in the menubar!", image=imgSmile, compound= LEFT, padding=15).grid(column=1, row=6)
ttk.Button(mainWin, text="Options...", image=imgCog, compound= LEFT, command=editOptionTable).grid(column=0, row=7)
ttk.Button(mainWin, text="Exit", image=imgStop, compound= LEFT, command=stopProg).grid(column=1, row=7)
ttk.Button(mainWin, text="Help & about...", image=imgTennisBall, compound= LEFT, command=helpAbout).grid(column=2, row=7)
root.title("Mark 'o Soft Math Related Tools: Toolbox")
root.mainloop()

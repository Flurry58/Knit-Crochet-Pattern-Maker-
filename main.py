from tkinter import *
import tkinter as tk
import csv
global rows
global columns
global table_M

global count
count = 0
rows = 10
columns = 5
global buttons
rowg = rows * 100
colg = columns * 100
win = tk.Tk()
import backend as bk
#Define the size of the window
geo = str(rowg) + "x" + str(colg)
win.geometry(geo)
usname = "flurry58"
passw = "Lcp35177"
#Name the title of the window
win.title("Pattern Maker")
#SET TABLE_M FIRST
table_M = bk.PatternMatrix(usname, passw)

buttons = []  #button list
stitch = ["k1"]  #temporary until I add stitch selector GUI
oframe = Frame(win)


def graphic1():
  menu.grid(row=0, column=columns + 8)
  loadboard.grid(row=4, column=0)
  olab.pack(side="top")
  Sframe.grid(row=5, column=0)
  xins.pack()
  yins.pack()
  subxybut.pack()
  #show login and options to either load or create new with reshape.


def graphic2():
  #add a check to see if grid is visable. If it is don't run the function.
  print(bool(eframe.winfo_ismapped()))
  if not bool(eframe.winfo_ismapped()):
    oframe.grid(column=1, row=0)
    canvas.grid(row=0, column=columns + 2)
    canvas1.grid(row=0, column=0)
    eframe.grid(column=0, row=0)
    knit.grid(row=2, column=0)
    purl.grid(row=3, column=0)
    k1b.grid(row=4, column=0)
    kb.grid(row=5, column=0)
    saveboard.grid(row=3, column=0)
    clearspace.grid(row=0, column=0)
    clearboard.grid(row=2, column=0)
  #reveal oframe and eframe


def setpatassign(p, stType):

  #change to make self into username and passsword variables. Make it so it accesses the file, counts rows and initializes self.gmatrix and cmatrix
  fgname = password + username + "g.csv"
  with open(fgname, newline='') as file:
    reader = csv.reader(file, delimiter=',')
    output = []
    for row in reader:
      output.append(row[:])
    file.close()
    output.pop(0)
  print(output)
  rows = len(output)
  print(rows)

  cols = len(output[0])
  print(cols)
  buttons[x][y].config(image=bk.knitpats[stType])

  #stType = selected stitch from stitch selector
  table_M.setpat(stType, x, y)


#reconfigure board dimensions
def subxy():
  graphic2()
  tempbut = []
  xin = int(xins.get(1.0, "end-1c"))
  yin = int(yins.get(1.0, "end-1c"))
  xins.delete(1.0, "end-1c")
  yins.delete(1.0, "end-1c")
  xins.insert(1.0, "X")
  yins.insert(1.0, "Y")
  table_M.reshape(xin, yin)
  for widgets in oframe.winfo_children():
    widgets.destroy()
  for i in range(xin):
    cols = []
    for j in range(yin):
      e = Button(oframe,
                 text=" ",
                 command=lambda p=[j, i]: setpatassign(p, stitch[0]))
      e.grid(row=i + 1, column=j + 2)
      cols.append(e)
    tempbut.append(cols)
  buttons = tempbut


def setStitch(st):
  stitch[0] = st


def saveb(uspass):
  table_M.export_matrix(uspass[0], uspass[1])


def loadb(uspass):
  graphic2()
  table_M = bk.PatternMatrix(uspass[0], uspass[1])
  table_M.import_matrix(uspass[0], uspass[1])
  gmat = table_M.retmatg()
  columns = len(gmat[0])
  print(columns)
  rows = len(gmat)
  print(rows)

  for i in range(rows):
    for j in range(columns):
      print(buttons[i][j])
      print("text")
      try:
        buttons[i][j].config(image=gmat[i][j])
        print(buttons[i][j])
      except tk.TclError:
        pass
  bk.dismat(gmat)


def clearall(p):
  for i in range(rows):
    for j in range(columns):
      table_M.setpat("c", i, j)
      try:
        buttons[i][j].config(image='')
      except tk.TclError:
        pass
  cmat = table_M.retmatc()
  gmat = table_M.retmatg()
  bk.dismat(gmat)
  bk.dismat(cmat)


#make sitch set to if stitch selector is on or off. Make a string that contains the value of the button that is on and assign the next grid press to that stitch.
username = "flurry58"
password = "Lcp35177"
eframe = Frame(win)

knit = Button(eframe,
              text="",
              image=bk.knitpats["k1"],
              command=lambda p="k1": setStitch(p))

purl = Button(eframe,
              text="",
              image=bk.knitpats["p1"],
              command=lambda p="p1": setStitch(p))

k1b = Button(eframe,
             text="",
             image=bk.knitpats["k1-b"],
             command=lambda p="k1-b": setStitch(p))

kb = Button(eframe,
            text="",
            image=bk.knitpats["kb"],
            command=lambda p="kb": setStitch(p))

#make delete pattern spo
clearspace = Button(eframe, text="", command=lambda p=0.0: setStitch(p))
count = 0
for i in range(rows):
  cols = []
  for j in range(columns):
    e = Button(oframe,
               text=" ",
               command=lambda p=[j, i]: setpatassign(p, stitch[0]))
    e.grid(row=i + 1, column=j + 2)
    cols.append(e)
  buttons.append(cols)

canvas = tk.Canvas(oframe, width=20, height=0)
canvas1 = tk.Canvas(oframe, width=20, height=0)

menu = Frame(win)

clearboard = Button(menu, text="Clear", command=lambda p="0": clearall(p))

saveboard = Button(menu,
                   text="Save",
                   command=lambda p=[username, password]: saveb(p))
loadboard = Button(menu,
                   text="Load",
                   command=lambda p=[username, password]: loadb(p))

Sframe = Frame(menu)

olab = Label(Sframe, text="ReShape:")

xins = Text(Sframe, height=1, width=10)
xins.insert(1.0, "X")
yins = Text(Sframe, height=1, width=10)
yins.insert(1.0, "Y")
subxybut = Button(Sframe, text="Submit", command=subxy)

#inuser = input("Username: ")
#inpass = input("Password: ")

#username must be email
#table_M.export_matrix("flurry58", "Lcp35177")
graphic1()

win.mainloop()

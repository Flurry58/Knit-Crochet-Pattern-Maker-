from tkinter import *
import tkinter as tk
import csv
import numpy as np
from PIL import ImageTk, Image
import pyautogui as pg
global columns
global rows
rows = 0
columns = 0
global table_M
win = tk.Tk()
import backend as bk
#Define the size of the window
table_M = bk.PatternMatrix(5, 10, "Test", "temp")
table_M.storebut([])
buttons = table_M.buttons
geo = "500x1000"
win.geometry(geo)

#Name the title of the window
win.title("Pattern Maker")
#SET TABLE_M FIRST

#right here make it so you can enter username with text input

username = "flurry58"
password = "Lcp35177"


def setclass():
  fgname = password + username + "g.csv"
  try:
    with open(fgname, newline='') as file:
      reader = csv.reader(file, delimiter=',')
      output = []
      for row in reader:
        output.append(row[:])
      file.close()
  except FileNotFoundError:
    bk.exportblank(username, password)
    with open(fgname, newline='') as file:
      reader = csv.reader(file, delimiter=',')
      output = []
      for row in reader:
        output.append(row[:])
      file.close()
  output.pop(0)
  gmx = bk.csv_to_list(output)
  columns = len(gmx)
  rows = len(gmx[0])

  table_M = bk.PatternMatrix(rows, columns, username, password)


stitch = ["k1"]  #temporary until I add stitch selector GUI
oframe = Frame(win)


def graphic1():
  table_M.import_matrix(username, password)
  gmat = table_M.retmatg()
  rows = len(gmat)
  columns = len(gmat[0])
  buttons = []
  setclass()
  for i in range(rows):
    cols = []
    for j in range(columns):
      e = Button(oframe,
                 text=" ",
                 command=lambda p=[j, i]: setpatassign(p, stitch[0]))
      e.grid(row=i + 1, column=j + 2)
      cols.append(e)
    buttons.append(cols)

  table_M.storebut(buttons)
  menu.grid(row=0, column=columns + 8)
  loadboard.grid(row=4, column=0)
  olab.pack(side="top")
  Sframe.grid(row=5, column=0)
  xins.pack()
  yins.pack()
  subxybut.pack()
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
  #show login and options to either load or create new with reshape.


def graphic2():
  #add a check to see if grid is visable. If it is don't run the function.
  #print(bool(eframe.winfo_ismapped()))
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


#reconfigure board dimensions
def subxy():
  graphic2()
  fgname = password + username + "g.csv"
  try:
    with open(fgname, newline='') as file:
      reader = csv.reader(file, delimiter=',')
      output = []
      for row in reader:
        output.append(row[:])
      file.close()
  except FileNotFoundError:
    bk.exportblank(username, password)
    with open(fgname, newline='') as file:
      reader = csv.reader(file, delimiter=',')
      output = []
      for row in reader:
        output.append(row[:])
      file.close()
  output.pop(0)
  gmx = bk.csv_to_list(output)
  columns = len(gmx)
  rows = len(gmx[0])
  tempbut = []
  yin = int(xins.get(1.0, "end-1c"))
  xin = int(yins.get(1.0, "end-1c"))
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
  table_M.storebut(tempbut)


def setpatassign(p, stType):
  buttons = table_M.buttons
  #print(p) #prints coordinents
  y = p[0]
  x = p[1]
  #print(buttons[x][y])
  #print(stType)
  buttons[x][y].config(image=bk.knitpats[stType])
  #print(buttons[x][y].cget("image"))
  #stType = selected stitch from stitch selector
  table_M.setpat(stType, x, y)
  cmat = table_M.retmatc()
  gmat = table_M.retmatg()


#reconfigure board dimensions
#reconfigure board dimensions


def setStitch(st):
  stitch[0] = st


def saveb(uspass):
  table_M.export_matrix(uspass[0], uspass[1])


def loadb(uspass):
  #graphic2()
  table_M.import_matrix(uspass[0], uspass[1])
  buttons = table_M.buttons
  gmat = table_M.retmatg()

  tempbut = []
  for i in range(len(gmat)):
    cols = []
    for j in range(len(gmat[0])):
      cols.append(1)
    tempbut.append(cols)
  tempbut = np.array(tempbut)
  butn = np.array(table_M.buttons)
  if tempbut.shape != butn.shape:
    for i in range(len(gmat)):
      cols = []
      for j in range(len(gmat[0])):
        e = Button(oframe,
                   text=" ",
                   command=lambda p=[j, i]: setpatassign(p, stitch[0]))
        e.grid(row=i + 1, column=j + 2)
  buttons = table_M.buttons
  if not buttons:
    table_M.storebut(tempbut)
    buttons = table_M.buttons
  #print(buttons)
  for i in range(len(gmat)):
    for j in range(len(gmat[0])):
      try:
        buttons[i][j].config(image=bk.knitpats[gmat[i][j]])
        print(bk.knitpats[gmat[i][j]])
      except tk.TclError:
        pass
  table_M.storebut(buttons)
  #bk.dismat(gmat)


def clearall(p):
  buttons = table_M.buttons
  gmat = table_M.retmatg()
  for i in range(len(gmat)):
    for j in range(len(gmat[0])):
      table_M.setpat("c", i, j)
      try:
        buttons[i][j].config(image='')

      except tk.TclError:
        pass
  table_M.storebut(buttons)
  cmat = table_M.retmatc()
  gmat = table_M.retmatg()
  #bk.dismat(gmat)
  #bk.dismat(cmat)


#make sitch set to if stitch selector is on or off. Make a string that contains the value of the button that is on and assign the next grid press to that stitch.
buttons = table_M.buttons
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

#make it so graphics1 is run when username and password form is filled out
graphic1()

win.mainloop()

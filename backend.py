import math
import pandas as pd
import base64
from numpy import asarray
from numpy import savetxt
import numpy as np
from tkinter.ttk import *
from tkinter import *
import os
import csv


def getkeyval(dic, val):
  key_list = list(dic.keys())
  val_list = list(dic.values())

  position = val_list.index(val)
  value = key_list[position]
  return value


def listToString(s):

  # initialize an empty string
  str1 = " "

  # return string
  return (str1.join(s))


def dismat(matrix):
  for i in range(len(matrix)):
    print(matrix[i])


#how it displays knit pattern options in the matrix
knitpats = {
  #name: image
  "k1": PhotoImage(file=r"1.gif"),
  "k1-b": PhotoImage(file=r"86.gif"),
  "k1 tbl": PhotoImage(file=r"89.gif"),
  "kb": PhotoImage(file=r"535.gif"),
  "p1": PhotoImage(file=r"2.gif"),
  "0": '',  #clear board
  0.0: '',
  "0.0": '',
  0: ''
}

knitpatname = {
  #name: image
  "k1": "k1",
  "k1-b": "k1-b",
  "k1 tbl": "k1 tbl",
  "kb": "kb",
  "p1": "p1"
}


def csv_to_list(contents):
  for row_num, rows in enumerate(contents):
    contents[row_num].pop(0)
  for i in range(len(contents)):
    for j in range(len(contents[i])):
      if "[" in contents[i][j]:
        temp = contents[i][j]
        temp = temp.replace("[", '')
        temp = temp.replace("]", '')
        temp = temp.replace("'", '')
        temp = temp.replace(" ", '')
        temp = str(temp)
        contents[i][j] = temp.split(",")
        for o in range(2):
          try:
            contents[i][j][o] = float(contents[i][j][o])
          except ValueError:
            contents[i][j][o] = str(contents[i][j][o])
      elif isinstance(contents[i][j], str):
        try:
          contents[i][j] = float(contents[i][j])
        except ValueError:
          contents[i][j] = str(contents[i][j])
  return contents


class PatternMatrix:

  def __init__(self, username, password):
    self.username = username
    self.gmatrix = []
    self.cmatrix = []
    self.password = password

  def setmatrix(self, xsize, ysize):
    self.xsize = xsize
    self.ysize = ysize
    self.gmatrix = np.zeros((xsize, ysize)).tolist()  #set board
    self.cmatrix = np.zeros((xsize, ysize, 2)).tolist()

  def setpat(self, pat_type, x, y):  #set pattern in matrix
    self.gmatrix[x][y] = pat_type

    for i in range(len(self.cmatrix)):
      for j in range(len(self.cmatrix[i])):
        if pat_type == "c":
          if self.cmatrix[i][j][0] != 0.0:
            self.cmatrix[i][j][0] = 0
          self.gmatrix[i][j] = 0.0
          self.cmatrix[i][j][0] = 0.0
          self.cmatrix[i][j][1] = 0.0
        elif self.gmatrix[i][j] != 0.0:
          try:
            vst = getkeyval(knitpatname, self.gmatrix[i][j])
            self.cmatrix[i][j - 1][1] = vst
          except:
            pass
          try:
            vst = getkeyval(knitpatname, self.gmatrix[i][j])
            self.cmatrix[i][j + 1][0] = vst
          except:
            pass

  def export_matrix(self, username, password):  #you can only save one pattern
    self.password = password
    self.username = username
    pass1 = password + username + "g.csv"
    self.fgname = pass1
    pass2 = password + username + "c.csv"
    self.fcname = pass2

    DF = pd.DataFrame(self.gmatrix)
    DF.to_csv(self.fgname)
    DF = pd.DataFrame(self.cmatrix)
    DF.to_csv(self.fcname)

  def import_matrix(self, username, password):
    try:
      temp = self.fname
    except AttributeError:
      pass1 = password + username + "g.csv"
      self.fgname = pass1
      pass2 = password + username + "c.csv"
      self.fcname = pass2
    try:
      with open(self.fgname, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        output = []
        for row in reader:
          output.append(row[:])
        file.close()
      output.pop(0)
      
      with open(self.fcname, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        output = []
        for row in reader:
          output.append(row[:])
        file.close()
      output.pop(0)
      
      self.gmatrix = csv_to_list(output)
      self.cmatrix = csv_to_list(output)
      print("GMATRIX:----------------------")
      dismat(self.gmatrix)

    except FileNotFoundError:
      #self.export_matrix(username, password)
      pass

    dismat(self.cmatrix)
    #dismat(self.gmatrix)

  def retmatc(self):
    return self.cmatrix

  def retmatg(self):
    return self.gmatrix

  def reshape(self, newx, newy):
    self.xsize = newx
    self.ysize = newy
    self.gmatrix = np.zeros((newx, newy)).tolist()
    self.cmatrix = np.zeros((newx, newy, 2)).tolist()
    try:
      if (os.path.exists(self.fgname) and os.path.isfile(self.fgname)):
        os.remove(self.fgname)
      if (os.path.exists(self.fcname) and os.path.isfile(self.fcname)):
        os.remove(self.fcname)
    except AttributeError:
      self.export_matrix(self.username, self.password)
      if (os.path.exists(self.fgname) and os.path.isfile(self.fgname)):
        os.remove(self.fgname)
      if (os.path.exists(self.fcname) and os.path.isfile(self.fcname)):
        os.remove(self.fcname)

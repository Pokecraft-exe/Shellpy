# Shellpy is a interactive shell with net download,
# Shellpy is opensource on github and new version will avaliable above 1/month
# Shellpy is a pseudo-linux emulator

import zipfile
import os

def bashrc_read():
  bashrc = open(".bashrc", 'r')
  lines = bashrc.readlines()
  for line in bashrc.readlines():
    testvar = 1
  #if findchar(lines[0], "P") and findchar(lines[0], "S") and findchar(lines[0], "1") and findchar(lines[0], "="):
  rootstr = input("$ ") #getstr(lines[0], 5))
  #else:
  #  rootstr = "ERROR ROOT"
  #  print("DEBUG: .bashrc line (1):{}".format(lines[1]))
  path(rootstr)

def path(command):
  PATH="COMMAND"
  autosh()

def findchar(list, char):
  find = False
  for i in range(len(list)):
    if list[i - 1] == char:
      find = True
    else:
      if find == True:
        find = True
      else:
        find = False

  return find

def findstr(list, char): # if you have the code tell me in coms
  find = findchar(list, char)
  for i in range(len(list) - 1):
    for t in range(len(char) - 1):
      if findchar(list[i], char[t]): #implicitly if findchar(list[loop], char[t]) == True:
          find = True
      else:
        #if find == True:
        #  find = True
        #else:
        find = False
  return find

def getchar(list, char):
  return list[char - 1]

def getstr(list, char):
  if len(list) >= char:
    strr = getchar(list, char)
    loop = 1
  
    while loop != (len(list) - 1):
      try:
        strr = strr + getchar(list, loop + char)
        loop = loop + 1
      except:
        return strr
  else:
    return 'out of range: {}, try: {} to get "{}"'.format(char, len(list), getchar(list, len(list)))

print(result())
  

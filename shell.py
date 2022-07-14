import sys
import os
from datetime import datetime
import time
import socket
import random
from pynput.keyboard import Key, Controller

"""
Shellpy is a interactive shell with net download,
Shellpy is opensource on github
"""

def shell():
  instr = command(input("$ "))
  if instr[0] == "bruteforce":
    if len(instr) >= 2:
      try:
        int(instr[1])
        keyboard = Controller()
        alphabet = "0123456789-ABCEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz"
        alphabetpassfinal = ""
        print("brutefroce will start in 10 seconds!")
        time.sleep(10)
        for j in range(int(instr[1])):
          for i in range(random.randint(3, 10)):
            alphabetpass = alphabet[random.randint(0, (len(alphabet) - 1))]
            alphabetpassfinal = alphabetpassfinal + alphabetpass
          print(alphabetpassfinal)
          keyboard.type(alphabetpassfinal)
          time.sleep(0.06)
          keyboard.press(Key.enter)
          keyboard.release(Key.enter)
          keyboard.press(Key.ctrl)
          keyboard.press("a")
          keyboard.release(Key.ctrl)
          keyboard.release("a")
          keyboard.press(Key.delete)
          keyboard.release(Key.delete)
          alphabetpassfinal = ""
      except ValueError:
        print("Error: the argument `time' must be integer, not", type(instr[1]))
    else:
        print("Error: `bruteforce' need 1 positional argument `time'")
  elif instr[0] == "ddos":
    try:
      print("under construction")
    except:
      print("Error: `ddos' need 1 positional argument `time'")
  elif instr[0] == "truc":
    print("")
  elif instr[0] == "help":
    print("bruteforce - used to bruteforce some passwords:")
    print("  time")
    print("ddos - used to ddos some servers:")
    print("  time")
  else:
    print("Error: command `{}' not found.".format(instr[0]))

def command(string, point = ' '):
  args = [""]
  alist = 0
  for i in range(len(string)):
    if string[i] == point:
      args.append("")
      alist = alist + 1
    else:
      args[alist] = args[alist] + string[i]
  return args

while(1):
  shell()

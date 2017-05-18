# The idea and motivation came from my good friend Kyle Pullen. The code and execution was written by Alex Nagel.
import os
import string
import ConfigParser
import io
import sys
import time
import math

def headers(rounders, big, breaker):
  os.system("clear")
  flag = 1
  small = math.floor(big / 2)
  flag = rounders % breaker
  if flag == 0:
    print "Break Round: %d  Last Blind: %d  Next Blind: %d" % (rounders, small, big)
    big = big / 2
  else:
    print "Round: %d  Big Blind: %d  Small Blind: %d" % (rounders, big, small)
  return flag

def countdown(timer):
  for min in xrange(timer,-1,-1):
    sec = 59
    while sec > 0:
      sys.stdout.write("                    \r")
      sys.stdout.write("Timer: %d:%02d" % (min, sec))
      sys.stdout.flush()
      sys.stdout.write("                    \r")
      sec -= 1
      try:
        time.sleep(1)
      except KeyboardInterrupt:
        sys.stdout.write("                                                                                            \r")
        # Press ctrl+c to pause originally
        sys.stdout.write("*PAUSED* Timer: %d:%02d. Press enter to continue, [s]kip, [p]revious, [e]xit" % (min, sec))
        sys.stdout.flush()
        sys.stdout.write("                                                                                              \r")
        inp = raw_input()
        if inp == '':
          headers(rounders, big, breaker)
          continue
        if inp == 'p':
          return True
        elif inp == 's':
          return False
        elif inp == 'e':
          print
          exit()
    sys.stdout.write("Timer: %d:00" % (min))
    sys.stdout.flush()
    sys.stdout.write("                    \r")
    time.sleep(1)
  return False

# grab settings
settings = ConfigParser.ConfigParser()
settings.read('settings.ini')
settings.sections()

rounders = 1
timer = int(settings.get('General', 'timer'))
big = int(settings.get('General', 'starting_big'))
breaker = int(settings.get('General', 'break_every'))

# Enter Clock
while True:
  flag = headers(rounders, big, breaker)
  if flag == 0:
    big = big / 2
    print "Do you want to skip the break: (y/n)"
    que = raw_input()
    if que == 'y':
      rounders += 1
      big = big * 2
      continue
  sys.stdout.write("                    \r")
  sys.stdout.write("Timer: %d:00" % (timer))
  sys.stdout.flush()
  sys.stdout.write("                    \r")
  time.sleep(1)
  previous = countdown(timer-1)
  if previous == True:
    rounders -= 1
    big /= 2
    continue
  rounders += 1
  # todo code blind structure algo in python for now just double blinds
  big = big * 2

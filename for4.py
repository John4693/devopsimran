#!/usr/bin/python

for i in range(10):
  print "Value of i is %d " % i
  if i == 5:
    print "We are at 5"
    break
  print "How is it going?"



for i in range(10):
  print "Value of i is %d " % i
  if i == 5:
    print "We are at 5"
    continue
  print "How is it going?"

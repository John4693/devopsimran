#!/usr/bin/python

for Planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus", "Pluto"]:
  print "We are going over Planet %s " % Planet
  if Planet == "Saturn":
    print "We are Landing now on %s " % Planet
    break

print "Out of the LOOP"

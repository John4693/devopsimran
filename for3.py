#!/usr/bin/python

for Planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus", "Pluto"]:
  print "###########################################"  
  print "###########################################"  
  if Planet == "Saturn":
    print "We are not Landing on %s " % Planet
    continue
  
  print "%s is safe for Landing" % Planet
  print "We are Landing on Planet %s " % Planet
  

print "Out of the LOOP"

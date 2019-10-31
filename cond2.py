#!/usr/bin/python

PLANET = raw_input("Enter the Planet name: ")
num = input("Enter a number:")

print type(PLANET)
print type(num)

if PLANET == "mercury":
   print "We are on planet %s " % (PLANET)
elif PLANET == "Earth":
   print "We are on planet %s " % (PLANET)
else:
  print "%s planet is good to land." % (PLANET)


# Testing pull


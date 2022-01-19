import sys
import re

f = sys.argv[1]
find = sys.argv[2]
replace = sys.argv[3]
with open (f, "r") as myfile:
     s=myfile.read()
ret = re.sub(find,replace, s)   # <<< This is where the magic happens
print ret
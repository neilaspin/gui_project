import re
import glob, os

os.chdir("/Users/neilaspin/Downloads/aichallenge")
cwd = os.getcwd()
# for file in os.listdir:
for file in glob.glob("*.py"):
    if len(file) <= 7:
        print(file)
    else:
        print(file + " this is a longer file")

m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))
n = re.search(r'(?<=-)\w+', 'spam-egg')
print(n.group(0))

print("Current working directory:", cwd)

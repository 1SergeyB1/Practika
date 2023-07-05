import os
import re

def getfiles(dir = os.getcwd()):
    filelist = []
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if re.findall('\.php$',filename):
                filelist.append(os.path.join(dirpath, filename))
    return filelist

text = ''
data = getfiles('Z:\практика\\abitcab2022')
for i in data:
        with open(i, 'r', encoding = "ISO-8859-1") as file:
            line = file.readline()
            while line:
                if line.count('require_once'):
                    print(line)
                line = file.readline()
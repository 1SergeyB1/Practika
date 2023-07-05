import os


def getfiles(dir = os.getcwd()):
    filelist = []
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            filelist.append(os.path.join(dirpath, filename).split('\\')[-1])
    return filelist

data = getfiles('Z:\практика\studcab')
output = {}

for i in data:
    if i.count('.'):
        output['.'+(i.split('.')[-1])] = True
    else:
        output[i] = True

output = list(output.keys())
text = ''

for i in output:
    text = text  + i + '\n'

with open('studcab-formats.txt','w') as file:
    file.write(text)
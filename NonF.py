import os


def getfiles(dir = os.getcwd()):
    filelist = []
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            filelist.append(os.path.join(dirpath, filename).split('\\')[-1])
    return filelist

data = getfiles('Z:\практика\\abitcab2022')
output = {}

for i in data:
    if i.count('.') == 0:
        output[i] = True

output = list(output.keys())
text = ''

for i in output:
    text = text + '.' + i + '\n'

with open('abitcab2022-NONf.txt','w') as file:
    file.write(text)
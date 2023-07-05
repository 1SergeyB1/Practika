import os


def getfiles(dir = os.getcwd()):
    filelist = []
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if filename.count('.') == 0:
                filelist.append(os.path.join(dirpath, filename))
    return filelist

data = getfiles('Z:\практика\\abitcab2022')
for i in data:
        with open(i, 'r', encoding = "ISO-8859-1") as file:
            text = str(file.read())
            with open('./decode/' + i.split('\\')[-1] + '.txt', 'w', encoding="utf-8") as txt:
                txt.write(text)

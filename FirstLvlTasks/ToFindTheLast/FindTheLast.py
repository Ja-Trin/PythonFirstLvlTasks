import os
import json
from os.path import getmtime, join
from time import ctime

resource = 'config.json'
pathToResource = '\\ToFindTheLast'

os.chdir(f'{os.getcwd()}{pathToResource}')

with open(resource, 'r') as config:
    text = json.load(config)

pathToFiles = f'{os.getcwd()}{text["path"]}'
print(pathToFiles)
extentionOfFiles = text['extention']
timespan = text['timespanInSec']

files = [join(pathToFiles, file) for file in os.listdir(pathToFiles)]
neededFormatFiles = []

for file in files:
    if file.endswith(extentionOfFiles):
        neededFormatFiles.append(file)
        
if neededFormatFiles:
    aroundLastCreation = []

    for file in neededFormatFiles:
        thisFile = max(neededFormatFiles, key=getmtime)
        difference = float(getmtime(thisFile)) - float(getmtime(file))
        if difference <= timespan and difference > 0:
            aroundLastCreation.append(file)

    print(f'The last created file in a directory is\n{thisFile}\n{ctime(getmtime(thisFile))}\n')

    if aroundLastCreation:
        for file in aroundLastCreation:
            print(f'Нere are the files created in the {timespan} seconds before it:\n{file} - {ctime(getmtime(thisFile))}')
else:
    print(f'There are no {extentionOfFiles}\'s!')
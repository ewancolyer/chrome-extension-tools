#!/usr/bin/env python3

import json
import csv
from modules import jsonActions
from modules import miscTools


# Generates the file used below


def csvLoader():
    """
    loads csv and returs it
    """

    csvBigList = ""
    jsonArray = []

    with open("input/chrome_extensions_installed.csv") as csvFile:
        csvFile2 = csv.reader(csvFile, dialect="excel")

        for item in csvFile2:

            csvBigList = ",".join([csvBigList, item[1]])

    csvBigList = miscTools.remove_prefix(csvBigList, ",")
    csvBigList = miscTools.remove_suffix(csvBigList, ",")

    for item in csvBigList.split(','):
        jsonArray.append(item)

    with open('result/extensionsListWithDuplicates.json', 'w') as file:
        json.dump(jsonArray, file)

    return csvBigList


csvLoader()

with open("result/extensionsListWithDuplicates.json") as file:
    extensionsList = json.load(file)
with open("config/extensionsMapper.json") as file:
    extensionsMapper = json.load(file)

extensionsDir = []
extensionsUnknown = []

for item in extensionsList:

    # check if ID is in extensionsDir
    dirResult = jsonActions.checkDir(extensionsDir, item)
    unkResult = jsonActions.checkUnk(extensionsUnknown, item)

    # if not in there, check if ID is in extensions mapper
    mapperResult = jsonActions.checkMapping(extensionsMapper, item)
    if(dirResult is None and unkResult is None):

        if(mapperResult is not None):
            # if in extensions mapper, add to extensionsDir
            jsonData = {
                "id": item,
                "extensionName": mapperResult["extensionName"],
                "publisher": mapperResult["publisher"],
                "count": 1
            }
            extensionsDir = jsonActions.add(jsonData, extensionsDir)
            print("Adding extension to Known extensions")
        else:
            # if not in extensions mapper, add to unknown json array
            jsonData = {
                "id": item,
                "count": 1
            }
            extensionsUnknown = jsonActions.add(jsonData, extensionsUnknown)
            print("Adding extension to unknown extensions")

    else:
        if(dirResult is not None):
            # change stuff in the directory json
            print("Extension already exists, adding 1 to count")
            for item2 in extensionsDir:
                if(item2["id"] == item):
                    item2["count"] += 1
        elif(unkResult is not None):
            print("Extension already exists, adding 1 to count")
            # change stuff in the unknown json
            for item2 in extensionsUnknown:
                if(item2["id"] == item):
                    item2["count"] += 1

with open('result/extensionsUnknown.json', 'w') as outfile:
    json.dump(extensionsUnknown, outfile)

with open('result/extensionsKnown.json', 'w') as outfile:
    json.dump(extensionsDir, outfile)

print("and with that, im done")

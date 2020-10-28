#!/usr/bin/env python3

def checkDir(jsonArray, ID):
    """
    Checks whether the id exists in the unknow file
    """
    if(jsonArray != []):
        for item in jsonArray:
            if(item["id"] == ID):
                return item


def checkUnk(jsonArray, ID):
    """
    Checks whether the id exists in the unknow file
    """
    if(jsonArray != []):
        for item in jsonArray:
            if(item["id"] == ID):

                return item


def checkMapping(jsonArray, ID):
    """
    Checks whether the id exists in the jsonMapper file
    """
    if(jsonArray == []):

        return
    else:
        for item in jsonArray:
            if(item["id"] == ID):
                return item


def add(newJsonArray, oldJsonArray):
    """
    Appends a json array to the end of a current one
    """

    oldJsonArray.append(newJsonArray)

    return oldJsonArray

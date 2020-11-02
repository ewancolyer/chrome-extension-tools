#!/usr/bin/env python3

def check_dir(json_array, ID):
    """
    Checks whether the id exists in the unknow file
    """
    if(json_array != []):
        for item in json_array:
            if(item["id"] == ID):
                return item


def check_unk(json_array, ID):
    """
    Checks whether the id exists in the unknow file
    """
    if(json_array != []):
        for item in json_array:
            if(item["id"] == ID):

                return item


def check_mapping(json_array, ID):
    """
    Checks whether the id exists in the json_mapper file
    """
    if(json_array == []):

        return
    else:
        for item in json_array:
            if(item["id"] == ID):
                return item


def add(new_json_array, old_json_array):
    """
    Appends a json array to the end of a current one
    """

    old_json_array.append(new_json_array)

    return old_json_array

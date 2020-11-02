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

    csv_big_list = ""
    json_array = []

    with open("input/chrome_extensions_installed.csv") as csv_file:
        csv_file_2 = csv.reader(csv_file, dialect="excel")

        for item in csv_file_2:

            csv_big_list = ",".join([csv_big_list, item[1]])

    csv_big_list = miscTools.remove_prefix(csv_big_list, ",")
    csv_big_list = miscTools.remove_suffix(csv_big_list, ",")

    for item in csv_big_list.split(','):
        json_array.append(item)

    with open('result/extensions_list_with_duplicates.json', 'w') as file:
        json.dump(json_array, file)

    return csv_big_list


csvLoader()

with open("result/extensions_list_with_duplicates.json") as file:
    extensions_list = json.load(file)
with open("config/extensions_mapper.json") as file:
    extensions_mapper = json.load(file)

extensions_known = []
extensions_unknown = []

for item in extensions_list:

    # check if ID is in extensions_known
    dir_result = jsonActions.check_dir(extensions_known, item)
    unk_result = jsonActions.check_unk(extensions_unknown, item)

    # if not in there, check if ID is in extensions mapper
    mapper_result = jsonActions.check_mapping(extensions_mapper, item)
    if(dir_result is None and unk_result is None):

        if(mapper_result is not None):
            # if in extensions mapper, add to extensions_known
            json_data = {
                "id": item,
                "extension_name": mapper_result["extension_name"],
                "publisher": mapper_result["publisher"],
                "count": 1
            }
            extensions_known = jsonActions.add(json_data, extensions_known)
            print("Adding extension to Known extensions")
        else:
            # if not in extensions mapper, add to unknown json array
            json_data = {
                "id": item,
                "count": 1
            }
            extensions_unknown = jsonActions.add(json_data, extensions_unknown)
            print("Adding extension to unknown extensions")

    else:
        if(dir_result is not None):
            # change stuff in the directory json
            print("Extension already exists, adding 1 to count")
            for item_2 in extensions_known:
                if(item_2["id"] == item):
                    item_2["count"] += 1
        elif(unk_result is not None):
            print("Extension already exists, adding 1 to count")
            # change stuff in the unknown json
            for item_2 in extensions_unknown:
                if(item_2["id"] == item):
                    item_2["count"] += 1

with open('result/extensions_unknown.json', 'w') as outfile:
    json.dump(extensions_unknown, outfile)

with open('result/extensions_known.json', 'w') as outfile:
    json.dump(extensions_known, outfile)

print("and with that, im done")

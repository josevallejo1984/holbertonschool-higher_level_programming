#!/usr/bin/python3
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except:
    my_list = []
finally:
    for idx in range(1, len(sys.argv)):
        my_list.append(sys.argv[idx])
    save_to_json_file(my_list, filename)

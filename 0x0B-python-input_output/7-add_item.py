#!/usr/bin/python3
"""Creates an Object from a “JSON file”"""

import argparse
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

my_list = []
parser = argparse.ArgumentParser(description='parse arguments')
parser.add_argument('args', metavar='N', type=str, nargs='+',
                    help='an integer for the accumulator')
args = parser.parse_args()

for arg in args:
    my_list.append(arg)

try:
    my_list = load('add_item.json')
except FileNotFoundError:
    pass

save(my_list + args.args, 'add_item.json')

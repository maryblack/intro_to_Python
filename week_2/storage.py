import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="key of element in dict")
parser.add_argument("--value", help="value of element in dict")
args = parser.parse_args()
data = dict()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


if args.value == None:
    try:
        with open(storage_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(None)
    else:
        if args.key in [*data]:
            print(', '.join(data.get(args.key)))
        else:
            print(None)
else:
    try:
        with open(storage_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    with open(storage_path, 'w') as f:
        new_value = []
        if args.key in [*data]:
            for el in data[args.key]:
                new_value.append(el)
            new_value.append(args.value)
        else:
            new_value.append(args.value)
        data[args.key] = new_value
        json.dump(data, f)


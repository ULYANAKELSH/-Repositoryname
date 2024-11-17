import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as file:
        readr = csv.DictReader(file)
        d = [OrderedDict(row) for row in readr]
    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(d, file, indent=4)



if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
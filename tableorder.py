# Imports

import argparse
import re

# Globals

PATTERNS = ["appendixtable", "table", "appendixfigure", "figure"]

# Parser

parser = argparse.ArgumentParser(description="Get order that tables appear in text")

parser.add_argument(
    "file",
    type=str,
    help="file to parse"
)

args = parser.parse_args()

# Functions

def open_file(file):
    with open(file) as f:
        txt = f.read()

    txt = txt.lower()
    txt = re.sub(r"(\s|\u180B|\u200B|\u200C|\u200D|\u2060|\uFEFF)+", "", txt)

    return txt

def initialize_patterns(patterns):
    patterns_dict = {}
    for pattern in patterns:
        patterns_dict[pattern] = re.compile(fr"{pattern}\\ref{{.*?}}")

    return patterns_dict

def get_content_between_braces(string):
    return string[string.find("{") + 1:string.find("}")]

def dedupe_with_order(lst):
    return list(dict.fromkeys(lst))

def get_results(patterns_dict, txt):
    res_dict = {}
    for pattern in patterns_dict:
        raw_results = dedupe_with_order(re.findall(patterns_dict[pattern], txt))
        res = [get_content_between_braces(raw_res) for raw_res in raw_results]
        res_dict[pattern] = res
        
        for entry in raw_results:
            txt = txt.replace(entry, "")
    
    return res_dict

def write_results(results):
    with open("__temp__.txt", "w") as f:
        for pattern in results:
            f.write(f"{pattern}:\n")

            for res in results[pattern]:
                f.write(f"\t{res}\n")

            f.write("\n")

def main(file=args.file, patterns=PATTERNS):
    txt = open_file(file)
    patterns_dict = initialize_patterns(patterns)
    res_dict = get_results(patterns_dict, txt)
    write_results(res_dict)

if __name__ == "__main__":
    main()

"""
Add example from rules and merged
python3 python/example_from_rules.py project
"""

import csv
import sys
import symbols_set

def main():
    """
    Main
    """

    args = sys.argv
    project = args[1]
    rules_file_path = project + "/rules.csv"
    original_file_path = project + "/git_merged.csv"

    with open(rules_file_path, "r") as rules_file:
        rules = csv.DictReader(rules_file, fieldnames=["lhs","rhs","support","confidence","lift","count"])

        with open(original_file_path, "r") as original_file:
            originals = list(csv.DictReader(original_file))
        # 空読み
        rules.__next__()
        unfixables = originals
        ori_len = len(unfixables)
        for rule in rules:
            # 先頭と末尾の{}と_plusは取り除く
            lhs = rule["lhs"][1:-1]
            rhs = rule["rhs"][1:-1]
            if lhs:
                unfixables = [ori
                for ori in unfixables
                    if not (ori[lhs]=="1" and ori[rhs]=="1")]
        print("%d / %d" % (ori_len - len(unfixables), ori_len))

def str_to_percent(ori_str):
    """
    "0.01" to "1%"
    """
    return round(float(ori_str) * 100, 2)

if __name__ == '__main__':
    main()

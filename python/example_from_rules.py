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
    symbols = symbols_set.SYMBOLS

    args = sys.argv
    project = args[1]
    rules_file_path = project + "/rules.csv"
    original_file_path = project + "/git_merged.csv"
    complete_rules_path = project + "/example_rules.csv"

    out_rules = []

    with open(rules_file_path, "r") as rules_file:
        rules = csv.DictReader(rules_file, fieldnames=["lhs","rhs","support","confidence","lift","count"])

        with open(original_file_path, "r") as original_file:
            originals = list(csv.DictReader(original_file))
        # 空読み
        rules.__next__()
        all_count = len(originals)
        for rule in rules:
            # 先頭と末尾の{}と_plusは取り除く
            lhs = rule["lhs"][1:-1]
            rhs = rule["rhs"][1:-1]
            if lhs:
                lhs_count = int(int(rule["count"]) / float(rule["confidence"]))
                # 条件に当てはまるもので最新のものを取得
                example = [(ori["ori"], ori["rev"], ori["filename"]) for ori in originals if ori[lhs]=="1" and ori[rhs]=="1"][0]
                out_rules.append([symbols[lhs], symbols[rhs[:-5]],example[2],
                                  example[0], example[1], rule["count"],
                                  str_to_percent(rule["support"]), all_count,
                                  str_to_percent(rule["confidence"]), lhs_count,
                                  rule["lift"]
                                  ])

    with open(complete_rules_path, "w") as complete_rules:
        writer = csv.writer(complete_rules)
        writer.writerow(["lhs","rhs", "no",
                         "ori","rev", "count",
                         "support", "all_num",
                         "confidence", "lhs_count",
                         "lift"])
        writer.writerows(out_rules)

def str_to_percent(ori_str):
    """
    "0.01" to "1%"
    """
    return round(float(ori_str) * 100, 2)

if __name__ == '__main__':
    main()

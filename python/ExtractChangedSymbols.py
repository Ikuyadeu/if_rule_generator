"""
Get changed symbol from patch
python3 ExtractChangedSymbols.py outdir
"""

import os
import re
import sys
import csv
import symbols_set

SYMBOLIC_LIST = symbols_set.SYMBOLIC_LIST

SYMBOLIC_NAMES = symbols_set.SYMBOLIC_NAMES

TEST_DOC = """"
-    if(#{isMplRestricted and empty userBean.loggedInUser}){
+    if(#{isMplRestricted and empty userBean.loggedInUser and userBean.internalAuthMode}){

"""

RE_IF = re.compile(r"-\s*if\s*\((.*)\)\s*\{?\n\+\s*if\s*\((.*)\)\s*\{?\n")

def out_result(result, filename):
    """
    Output result to csv
    """
    with open(filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["filename", "num", "ori", "rev"] + SYMBOLIC_NAMES)
        writer.writeheader()
        writer.writerows(result)

def compare_symbols(ori_symbols, rev_symbols):
    """
    compare frequency of symbols
    """
    return {name + "diff":ori_symbols[symbol] - rev_symbols[symbol] for symbol, name in zip(SYMBOLIC_LIST, SYMBOLIC_NAMES)}

def get_symbols(content):
    """
    Get symbols in conditional statements
    """
    return {name:content.count(symbol) for symbol, name in  zip(SYMBOLIC_LIST, SYMBOLIC_NAMES)}

def main():
    """
    Main
    """
    args = sys.argv
    project = args[1]
    outdir = project + "/diffs"   
    file_names = os.listdir(outdir)

    ori_result = []
    rev_result = []
    for file_name in file_names:
        with open(outdir + "/" + file_name, "r", encoding="utf-8") as file:
            try:
                file_contents = file.read()
            except UnicodeDecodeError:
                continue
            if_statements = RE_IF.findall(file_contents)
            for i, (ori_content, rev_content) in enumerate(if_statements):
                status = {"filename": file_name, "num": i, "ori": ori_content, "rev": rev_content}
                ori_symbols = get_symbols(ori_content)
                ori_symbols.update(status)
                ori_result.append(ori_symbols)
                rev_symbols = get_symbols(rev_content)
                rev_symbols.update(status)
                rev_result.append(rev_symbols)

    out_result(ori_result, project + "/git_ori.csv")
    out_result(rev_result, project + "/git_rev.csv")

if __name__ == '__main__':
    main()

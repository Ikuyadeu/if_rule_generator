"""
gatther ling symbolic list
"""

SYMBOLIC_LIST = ["(", ")", "{", "}", "[", "]",
                 ";", ",", ".", ">", "<", "!", "~", "?", ":",
                 "==", "!=", "&&", "||", "++", "--", "+",
                 "-", "*", "/", "^", "%", "->", "::"]


SYMBOLIC_NAMES = ["LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA",
                  "DOT", "GT", "LT", "BANG", "TILDE", "QUESTION", "COLON", "EQUAL",
                  "NOTEQUAL", "AND", "OR", "INC", "DEC", "ADD", "SUB", "MUL",
                  "DIV", "CARET", "MOD", "ARROW", "COLONCOLON"]


SYMBOLS = {name:symbol for name, symbol in zip(SYMBOLIC_NAMES, SYMBOLIC_LIST)}


def out_put_symbols_csv():
    """
    Outpur symbols to symbols.csv
    """
    from csv import writer
    with open("symbols.csv", "w") as output_file:
        writer = writer(output_file)
        writer.writerow(["name", "symbol"])
        for name, symbol in SYMBOLS.items():
            writer.writerow([name, symbol])

def main():
    """
    Main
    """
    out_put_symbols_csv()

if __name__ == '__main__':
    main()

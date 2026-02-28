grammar = {
    "S": [["NP", "VP"]],
    "NP": [["dog"]],
    "VP": [["runs"]]
}

def parse(sym, words):
    if sym not in grammar:
        return words == [sym]
    return any(parse(r[0], words[:1]) and parse(r[1], words[1:])
               for r in grammar[sym])

print(parse("S", ["dog", "runs"]))

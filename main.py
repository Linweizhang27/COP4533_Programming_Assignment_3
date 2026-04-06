import sys
from Algorithm import find_max_value, find_subsequence

def parse_file(filename):
    with open(filename, "r") as f:
        lines = []
        for line in f:
            lines.append(line.strip())

        K = int(lines[0])
        val = {}
        for i in range(1, K+1):
            char, value = lines[i].split()
            val[char] = int(value)
        
        A = lines[K+1]
        B = lines[K+2]
        return val, A, B

def main():
    filename = sys.argv[1]
    val, A, B = parse_file(filename)

    max, M = find_max_value(val, A, B)
    path = find_subsequence(M, val, A, B) #path is a list, not yet a string here
    print(max)
    
    subsequnece = ""
    for i in range(len(path)):
        subsequnece += path[i]

    print(subsequnece)



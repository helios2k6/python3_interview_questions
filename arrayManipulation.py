import sys

def arrayManipulation(queries):
    return 0

def readInput(fileName):
    queries = []
    with open(fileName) as fp:
        line = fp.readLine()
        queries.append(list(map(int, line.rstrip().split())))
    return queries

def main(fileName):
    print(arrayManipulation(readInput(fileName)))

main(sys.argv[1])
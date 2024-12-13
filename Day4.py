total = 0
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("input.txt")
puzzle = []
for i in file_data:
    array = []
    for char in i:
        array.append(char)
    puzzle.append(array)


def horizontalSearch(data):
    for row in data:
        for ele in row:
            if data[row][ele] == "X" and data[row + 1][ele] and "M" and data[row + 2][ele] == "A" and data[row + 3][ele] == "S":
                total = total + 1

def reverseSearch(data):
    print()

def verticalSearchUp(data):
    print()

def verticalSearchDown(data):
    print()

def diagonalSearchLeftUp(data):
    print()

def diagonalSearchRightUp(data):
    print()

def diagonalSearchLeftDown(data):
    print()

def diagonalSearchRightDown(data):
    print()

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
total = 0
def horizontalSearch(data):
    for row in range(len(data)):
        for ele in range(len(data[row])):
            if data[row][ele + 3] and data[row][ele] == "X" and data[row + 1][ele] == "M" and data[row + 2][ele] == "A" and data[row + 3][ele] == "S":
                total =+ 1
def reverseSearch(data):
    for row in data:
        for ele in row:
            if data[row][ele - 3] and data[row][ele] == "X" and data[row - 1][ele] == "M" and data[row - 2][ele] == "A" and data[row - 3][ele] == "S":
                total = total + 1
def verticalSearchDown(data):
    for row in data:
        for ele in row:
            if data[row + 3][ele] and data[row][ele] == "X" and data[row][ele + 1] and "M" and data[row][ele + 2] == "A" and data[row][ele + 3] == "S":
                total = total + 1
def verticalSearchUp(data):
    for row in data:
        for ele in row:
            if data[row - 3][ele] and data[row][ele] == "X" and data[row][ele - 1] and "M" and data[row][ele - 2] == "A" and data[row][ele - 3] == "S":
                total = total + 1
def diagonalSearchLeftUp(data):
    for row in data:
        for ele in row:
            if data[row - 3][ele - 3] and data[row][ele] == "X" and data[row - 1][ele - 1] and "M" and data[row - 2][ele - 2] == "A" and data[row - 3][ele - 3] == "S":
                total = total + 1
def diagonalSearchRightUp(data):
    for row in data:
        for ele in row:
            if data[row - 3][ele + 3] and data[row][ele] == "X" and data[row - 1][ele + 1] and "M" and data[row - 2][ele + 2] == "A" and data[row - 3][ele + 3] == "S":
                total = total + 1

def diagonalSearchLeftDown(data):
    for row in data:
        for ele in row:
            if data[row + 3][ele - 3] and data[row][ele] == "X" and data[row + 1][ele - 1] and "M" and data[row + 2][ele - 2] == "A" and data[row + 3][ele - 3] == "S":
                total = total + 1

def diagonalSearchRightDown(data):
    for row in data:
        for ele in row:
            if data[row + 3][ele + 3] and data[row][ele] == "X" and data[row + 1][ele + 1] and "M" and data[row][ele + 2] == "A" and data[row][ele + 3] == "S":
                total = total + 1

horizontalSearch(puzzle)

print(total)

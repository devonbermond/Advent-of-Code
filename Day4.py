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
    count = 0
    for row in range(len(data)):
        for ele in range(len(data[row])):
            if row + 3 < len(data) and data[row][ele] == "X" and data[row + 1][ele] == "M" and data[row + 2][ele] == "A" and data[row + 3][ele] == "S":
                count = count + 1
    return count
def reverseSearch(data):
    count = 0
    for row in range(len(data)):
        for ele in range(len(data[row])):
            if row - 3 >= 0 and data[row][ele] == "X" and data[row - 1][ele] == "M" and data[row - 2][ele] == "A" and data[row - 3][ele] == "S":
                count = count + 1
    return count
def verticalSearchDown(data):
    count = 0
    for row in range(len(data)):
        for ele in range(len(data[row])):
            if ele + 3 < len(data[0]) and data[row][ele] == "X" and data[row][ele + 1] and "M" and data[row][ele + 2] == "A" and data[row][ele + 3] == "S":
                count = count + 1
    return count
def verticalSearchUp(data):
    count = 0
    for row in range(len(data)):
        for ele in range(len(data[row])):
            if ele - 3 >= 0 and data[row][ele] == "X" and data[row][ele - 1] and "M" and data[row][ele - 2] == "A" and data[row][ele - 3] == "S":
                count = count + 1
    return count
def diagonalSearchLeftUp(data):
    count = 0
    for row in range(len(data)):
        for ele in range(len(data[row])):
            if row - 3 >= 0 and ele - 3 >= 0 and data[row][ele] == "X" and data[row - 1][ele - 1] and "M" and data[row - 2][ele - 2] == "A" and data[row - 3][ele - 3] == "S":
                count = count + 1
    return count
def diagonalSearchRightUp(data):
    count = 0
    for row in range(len(data)):
        for ele in range(len(data[row])):
            if row - 3 >= 0 and ele + 3 < len(data[0]) and data[row][ele] == "X" and data[row - 1][ele + 1] and "M" and data[row - 2][ele + 2] == "A" and data[row - 3][ele + 3] == "S":
                count = count + 1
    return count
def diagonalSearchLeftDown(data):
    count = 0
    for row in range(len(data)):
        for ele in range(len(data[row])):
            if row + 3 < len(data) and ele - 3 >= 0 and data[row][ele] == "X" and data[row + 1][ele - 1] and "M" and data[row + 2][ele - 2] == "A" and data[row + 3][ele - 3] == "S":
                count = count + 1
    return count
def diagonalSearchRightDown(data):
    count = 0
    for row in range(len(data)):
        for ele in range(len(data[row])):
            if row + 3 < len(data) and ele + 3 < len(data[0]) and data[row][ele] == "X" and data[row + 1][ele + 1] and "M" and data[row][ele + 2] == "A" and data[row][ele + 3] == "S":
                count = count + 1
    return count
total += horizontalSearch(puzzle)
total += reverseSearch(puzzle)
total += diagonalSearchRightDown(puzzle)
total += diagonalSearchRightUp(puzzle)
total += diagonalSearchLeftDown(puzzle)
total += diagonalSearchLeftUp(puzzle)
total += verticalSearchDown(puzzle)
total += verticalSearchDown(puzzle)
print(total)

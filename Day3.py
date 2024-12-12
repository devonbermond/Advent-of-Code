import re
total = 0
var = True
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("input.txt")

def get_nums(str):
    temp = str.lstrip("mul(")
    temp = temp.rstrip(")")
    num = temp.split(",")
    return num


regex = "mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\)"
for i in file_data:
    matches = re.findall(regex, i)
    for item in matches:
        if item == "do()":
            var = True
        elif item == "don't()":
            var = False
        elif var is True:
            nums = get_nums(item)
            total = total + int(nums[0]) * int(nums[1])

print(total)

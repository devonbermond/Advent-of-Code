import re
total = 0
vqar = True
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("input.txt")
def on_or_off(string, index):
    str = string[:index]
    temp = str[::-1]
    do = temp.find(")(od")
    dont = temp.find(")(t'nod")
    return bool(do < dont)


def get_nums(str):
    temp = str.lstrip("mul(")
    temp = temp.rstrip(")")
    num = temp.split(",")
    return num


regex = "mul\\([0-9]+,[0-9]+\\)"
for i in file_data:
    matches = re.findall(regex, i)
    for item in matches:
        idx = i.index(item)
        vqar = on_or_off(i, idx)
        if vqar is True:
            nums = get_nums(item)
            total = total + int(nums[0]) * int(nums[1])

print(total)

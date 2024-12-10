import re
total = 0
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("input.txt")
def on_or_off(string, index):
    str = string.substring(0, index)
    temp = str[::-1]
    do = temp.find("do()")
    dont = temp.find("dont()")
    return bool(do < dont)

split = ""
regex = "mul\\([0-9]+,[0-9]+\\)"
for i in file_data:
    matches = re.findall(regex, i)
    for item in matches:
        idx = i.index(item)
        idk = on_or_off(i, idx)
        if (idk is True ):
            split = item.lstrip("mul(")
            split = split.rstrip(")")
            nums = split.split(",")
            total = total + int(nums[0]) * int(nums[1])

print(total)

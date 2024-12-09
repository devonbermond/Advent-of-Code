import re
total = 0
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("input.txt")

regex = "mul\\([1-9]+,[1-9]+\\)"
for i in file_data:
    matches = re.findall(regex, i)
    for item in matches:
        split = item.lstrip("mul(")
        split = split.rstrip(")")
        
print(split)

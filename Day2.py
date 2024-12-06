def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data
file_data = get_file_data("input.txt")
total = 0
new = 0
for item in file_data:
    temp = item.split(" ")
    for i in range(0, len(temp) - 1):
        if int(temp[i]) - 1 == int(temp[i + 1]) or int(temp[i]) - 2 == int(temp[i + 1]) or int(temp[i]) - 3 == int(temp[i + 1]):
            if i + 1 == len(temp) - 1:
                total = total + 1
        else:
            break
    for i in range(0,len(temp) - 1):
        if int(temp[i]) + 1 == int(temp[i + 1]) or int(temp[i]) + 2 == int(temp[i + 1]) or int(temp[i]) + 3 == int(temp[i + 1]):
            if i + 1 == len(temp) - 1:
                total = total + 1
        else:
            break

print(total)

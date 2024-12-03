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
    for i in range(0, 5):
        if (int(temp[i]) < int(temp[i + 1]) < int(temp[i + 2]) < int(temp[i + 3]) < int(temp[i + 4]) < int(temp[i + 5])) or (int(temp[i]) > int(temp[i + 1]) > int(temp[i + 2]) > int(temp[i + 3]) > int(temp[i + 4]) > int(temp[i + 5])):
            if not(1 <= abs(int(temp[i]) - int(temp[i + 1])) <= 3):
                break
            else:
                new = new + 1

    if new == 4:
        total = total + 1
    new = 0

print(total)
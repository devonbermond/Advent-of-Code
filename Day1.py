def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("input.txt")
list1 = []
list2 = []
total = 0
for item in file_data:
    temp = item.split("   ")
    list1.append(temp[0])
    list2.append(temp[1])
list1.sort()
list2.sort()
x = 0;
for item in list1:
    total = total + abs(int(item) - int(list2[x]))
    x = x + 1
print(total)

sim_score = 0;
for item in list1:
    score = list2.count(item)
    sim_score = sim_score + (int(item) * score)
print(sim_score)
import csv
def holiday(n1):
    line1 = []
    day1 = []
    date1 = []
    holiday1 = []
    state1 = []
    list2 = []
    line2 = []
    lname = []
    sname = []
    file1 = open('holiday1/Holidays_2024.csv', 'r')
    info1 = csv.reader(file1)
    file2 = open("holiday1/states.txt", "r")
    info2 = file2.readlines()
    len2 = len(info2)
    for i in range(0, len2, 1):
        list2.append(info2[i].split(","))
        line2.append(list2[i])
        lname.append(line2[i][0])
        sname.append(line2[i][1].replace("\n", ""))
    name = n1
    for i in range(0, len2, 1):
        if name in lname[i]:
            state2=lname[i]
            state=sname[i]
    for line1 in info1:
        date1.append(line1[0])
        day1.append(line1[1])
        holiday1.append(line1[2])
        state1.append(line1[3].replace("\n", " ").replace("&", ","))
    len1 = len(state1)
    collect=[]
    for i in range(0, len1, 1):
        list1 = state1[i].split(",")
        if state in state1[i]:
            if "National except " not in state1[i]:
                collect.append([date1[i], day1[i], holiday1[i]])
        if "National".strip() in state1[i].strip():
            if "KA" not in state1[i]:
                collect.append([date1[i], day1[i], holiday1[i]])
    return collect
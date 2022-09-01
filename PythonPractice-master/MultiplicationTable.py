'''range(start, stop, step)'''
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [9, 10, 11, 12]


print("Multiplication tables")

for x in range(1, 13):
    print(list1[0], "x ", x, " = ", list1[0] * x, "    ", list1[1], "x ", x, " = ", list1[1] * x, "    ", list1[2], "x ", x, " = ", list1[2] * x, "    ", list1[3], "x ", x, " = ", list1[3] * x)
print("")
for x in range(1, 13):
    print(list2[0], "x ", x, " = ", list2[0] * x, "    ", list2[1], "x ", x, " = ", list2[1] * x, "    ", list2[2], "x ", x, " = ", list2[2] * x, "    ", list2[3], "x ", x, " = ", list2[3] * x)
print("")
for x in range(1, 13):
    print(list3[0], "x ", x, " = ", list3[0] * x, "    ", list3[1], "x ", x, " = ", list3[1] * x, "    ", list3[2], "x ", x, " = ", list3[2] * x, "    ", list3[3], "x ", x, " = ", list3[3] * x)
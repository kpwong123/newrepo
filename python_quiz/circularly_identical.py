list1 = [1,2,3,4,5]
list2 = [2,3,4,5,1]

count = 0
for (x,value1) in enumerate(list1):
    for (y,value2) in enumerate(list2):
        list3 = []
        if value1 == value2:
            for lastitem in list2[y:]:
                list3.append(lastitem)
            for firstitem in list2[0:y]:
                list3.append(firstitem)
            print(list3)
            if list3 == list1:
                count += 1


if count != 0:
    print('the lists are circularly identitical')
else:
    print('the lists are not circularly identitical')
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myList)

for element in myList:
    #print(element)
    pass

print(myList[0])
print(myList[-1])
print(myList[2:7])
print(myList[2:7:2])
print(myList[::-1])
print(myList[::-2])
print(myList[7:2:-2])
print(len(myList))

newList = [[1, 2, 3],[4, 5], [6, 7, 8, 9, 10]]
print(newList)

firstList = newList[0]
print(firstList)
item = firstList[1]
print(item)
print(newList[0][1])

for elem in newList:
    print(elem)
    for num in elem:
        print(num)













from collections import Counter
file = open("input.txt", "r")
list1= []
list2= []

for line in file:
    values = line.strip().split("   ")
    list1.append(int(values[0]))
    list2.append(int(values[1]))

similarity_score = 0
counter2 = Counter(list2) 

for i in range(len(list1)):
    element = list1[i]
    if counter2[element] is not None: 
        similarity_score += counter2[element] * element
        print(element, counter2[element])
print(similarity_score)
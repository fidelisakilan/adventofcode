from heapq import heappush, heappop
file = open("input.txt", "r")
heap1= []
heap2= []

for line in file:
    values = line.strip().split("   ")
    heappush(heap1, int(values[0]))
    heappush(heap2, int(values[1]))

sum = 0
for i in range(len(heap1)):
    sum += abs(heappop(heap1) - heappop(heap2))
print(sum)

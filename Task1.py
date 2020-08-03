list1 = [int(s) for s in input("Enter number: ").split()]
k = int(input())
for i in range(k + 1, len(list1)):
    list1[i - 1] = list1[i]
list1.pop()
print(' '.join([str(i) for i in list1]))

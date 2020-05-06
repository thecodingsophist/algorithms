# Uses python3

n = int(input())
a = [int(x) for x in input().split()]
index = 0
x = range(1, n)
for i in x:
    # print('a[i]: ' + str(a[i]))
    if a[i] > a[index]:
        index = i
    # print("a[index] = " + str(a[index]))
if index == 0:
    k = 1
    for i in range(2, n):
        if i != index and a[i] > a[k]:
            k = i
        # print("a[k] = " + str(a[k]))
    print(a[index]*a[k])
else:
    k = 0
    for i in x:
        if i != index and a[i] > a[k]:
            k = i
        # print("a[k] = " + str(a[k]))
    print(a[index]*a[k])

''' DEBUGGING NOTES: '''

# PROBLEM : with 0 and 1, the return product should be 0, not 1
# Walk through code with 0, 1 to see why
# Changes :
#   - index, k is 0, not 1
#   - range starts at 1

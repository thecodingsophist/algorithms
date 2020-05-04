# Uses python3

n = int(input())
a = [int(x) for x in input().split()]
index = 0
x = range(1, n)
for i in x:
    # print('a[i]: ' + str(a[i]))
    if a[i] > a[index]:
        index = i
k = 0
for i in x:
    if a[i] != a[index] and a[i] > a[k]:
        k = i
print(a[index]*a[k])

''' DEBUGGING NOTES: '''

# PROBLEM : with 0 and 1, the return product should be 0, not 1
# Walk through code with 0, 1 to see why
# Changes :
#   - index, k is 0, not 1
#   - range starts at 1

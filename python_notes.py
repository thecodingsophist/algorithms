# =============================================
# PYTHON NOTES CORRESPONDING TO WEEKLY LESSONS
# =============================================

'''
How to Read in Values from Command Line in Python (WEEK 1)
'''

def print_input():
    return print(input(), input())

if __name__ == "__main__":
# first:
# scanf("%d %d", &x, &y)
# for c?

# second:
    # print_input()

# third:
    # use split() and input()
    x, y = input().split()
    print(x, y)

# the input is in string, so since we are trying to get two integers
# we are going to int() those inputs

    x, y = [int(x), int(y)]

# this can also be done through list comprehension

    x, y = [int(x) for x in input().split()]

# also can be done using the map() function

    x, y = map(int, input().split())

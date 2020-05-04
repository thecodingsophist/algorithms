# python3

def sum_of_digits(first, second):
    return first + second

if __name__ == "__main__":
    # map() function applies the first param, which is a function, to all in sec param, or list
    # input() takes in input
    # split() splits at the space in the input string
    a, b = map(int, input().split())
    print(sum_of_digits(a,b))

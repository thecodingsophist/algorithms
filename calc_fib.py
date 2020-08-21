# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_matrices(n):
    # this method uses matrix exponentiation, where a is the matrix
    # [[1,1], [1,0]] and n is the nth fibonacci number

    fib = [[1,1],
         [1,0]]
    mul = [[1,1],
           [1,0]]

    fib_list = [0, 1]

    if n == 0:
        return "Enter a number greater than 0"

    elif n == 1:
        return [0]

    elif n == 2:
        return fib_list
        
    for i in range(n-2):

        a = fib[0][0] * mul[0][0] + fib[0][1] * mul[1][0]
        #
        b = fib[0][0] * mul[0][1] + fib[0][1] * mul[1][1]
        #
        c = fib[1][0] * mul[0][0] + fib[1][1] * mul[1][0]
        #
        d = fib[1][0] * mul[0][1] + fib[1][1] * mul[1][1]

        mul[0][0] = a
        mul[0][1] = b
        mul[1][0] = c
        mul[1][1] = d

        print("mul = [[" + str(mul[0][0]) + "," + str(mul[0][1]) + "], [" + str(mul[1][0]) + "," + str(mul[1][1]) + "]]")

        fib_list.append(mul[0][1])

    return fib_list

n = int(input())
print(calc_fib_matrices(n))

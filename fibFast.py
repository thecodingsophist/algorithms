# uses python3
def fib_fast(n):
    # n = 0
    # n = 1
    fib_seq = [0,1]
    for n > 1:
        fib_seq = fib_seq[n] + fib_seq[n-1]
    return fib_seq[n]

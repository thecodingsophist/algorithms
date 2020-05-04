# use python3

import random
import sys
import os

# accept the number of tests as a command line parameter
tests = int(sys.argv[1])
# accept the parameter for the tests as a command line parameter
n = int(sys.argv[2])

for i in range(tests):
    print("Test_#" + str(i))
    # run the generator gen.py with parameter n and the seed i
    os.system("python3" + " " + "max_random.py " + str(n) + " " + str(i) +" >input.txt")
    # run the model solution model.py
    # notice that it is no tnecessary that solution is implemented if __name__ == '__main__':
    # python
    os.system("python3" + " " + "maximum_pairwise_product.py" + " <input.txt>model.txt")
    # run the main solution
    os.system("python3 " + "maximum_pairwise_product_fast.py " + "<input.txt>main.txt")

    # read the output of the model solution:
    with open('maximum_pairwise_product.py') as f: model = f.read()
    print("Model:_", model)
    #read the output of the main solution:
    with open("maximum_pairwise_product_fast.py") as f: main = f.read()
    print("Main:_", main)
    if model != main:
        break

'''
Python Iterator Protocol

AN ITERATOR: An object used to iterate through an iterable element.
Most python objects are iterable, for example, a list, a dictionary, a string,
all of which are iterable. EXAMPLE: in a line of 5 boys, you point to the first
boy and ask for his name -- he replies -- you then point to the next boy and ask
him for his name.. etc.. in this way YOU ARE THE ITERATOR

A protocol is a set of rules or procedures. So the Python Iterator
Protocol is about what the steps are for a Python Iterator.

HINT: The Python Iteratort includes an ITER() and a NEXT() function

-The iter() function is used to create an iterator of an iterable element
-The next() funciton is used to get to the next element

'''

list_string = ['Boy1', 'Boy2', 'Boy3', 'Boy4', 'Boy5']

#iter() applies the desired function to each iterable element
iterator_you = iter(list_string)

#point the first boy
output = next(iterator_you)
print(output)

#point to the second boy
output = next(iterator_you)
#print the name of the second boy
print(output)

#point to the third boy
output = next(iterator_you)
#print the name of the third boy
print(output)

#point to the fourth boy
output = next(iterator_you)
#print the name of the fourth boy
print(output)

#point to the fifth boy
output = next(iterator_you)
#print the name of the fifth boy
print(output)

#point to the next boy, but there is no boy left
#so raise 'StopIteration' exception, which is part of next()
output = next(iterator_you)
print(output)

#try running the program! The Traceback spits out 'StopIteration'

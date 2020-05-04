''' Python map() function^ is used to apply a function to all the elements
    of a specified variable and return a map object. The map object itself
    is an ITERATOR^.

    >> see Python Iterator Protocol^

    credit: https://www.journaldev.com/22960/python-map-function
    credit: https://www.journaldev.com/14620/python-iterator
        -> this has more information about the Python Iterator Protocol and writing your
        own Python iterator class
'''


# Examples of the map function in action

# example helper function
def to_upper_case(s):
    return str(s).upper()

# defining a utility function to print iterator elements
def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')

# map() function example with different types of iterables
# STRINGS

map_iterator = map(to_upper_case, 'abc')
print(type(map_iterator))
print_iterator(map_iterator)

# TUPLES

map_iterator = map(to_upper_case, (1, 'a', 'abc'))
print_iterator(map_iterator)

# LISTS

map_iterator = map(to_upper_case, ['x', 'a', 'abc'])
print_iterator(map_iterator)

# converting map to list, tuple, set:
# map obj is an iterator, pass it as an argument to
# factory methods for creating a list, tuple, set.. etc

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_list = list(map_iterator)
print(my_list)

# here, you see that the map_iterator is an object, that
# can be passed into factory methods, such as list

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_list = set(map_iterator)
print(my_list)

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_list = tuple(map_iterator)
print(my_list)

# Python map() with lambda
# lambda functions are mini-functions that is defined
# within the scope of the function
list_numbers = [1,2,3,4] # <-- this can actually be a list, set, or tuple!

map_iterator = map(lambda x: x*2, list_numbers)
print_iterator(map_iterator)

# Python map() multiple arguments
# (with diff obj types!)
list_numbers = [1,2,3,4]
tuple_numbers = (5,6,7,8)
map_iterator = map(lambda x, y: x*y, list_numbers, tuple_numbers)
print_iterator(map_iterator)

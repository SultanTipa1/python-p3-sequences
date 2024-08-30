#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < length:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        print(fib_sequence[:length])

print_fibonacci(9)

# => [0, 1, 1, 2, 3, 5, 8, 13, 21]
























# my_list = [1, 2, 3, 4]
# print(my_list[0])


# #A dynamic sequence of values that allow duplicates
# fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21]

# # An immutale orderd sequence of months
# month_tuple =(
#     'January',
#     'February',
#     'March',
#     'April',
#     'May',
#     'June',
#     'July',
#     'August',
#     'September',
#     'October',
#     'November',
#     'December',
# )

# # a simple pattern of numbers
# even_numbers_up_to_100 = range(0, 101, 2)

# # A gramatical sentence
# sentence_string = "Strings are immutable sequences of unicode code points."

# if we sort numbers, they will e sorted in ascending order
# my_list = [3, 6, 4, 2, 1, 5]
# my_list.sort()
# print(my_list)

# If we sort strings, they will be sorted in alphanumeric order
# my_list = ['Cabbage', 'Apple', 'Banana', 'Tomato', 'Potato']
# my_list.sort()
# print(my_list) 

# my_list =['This is a long sentence', 'Word', 'z']

# What if we want to sort by length of string?
# we can use the key attriute to tell the sort function to sort using the length function

# my_list.sort(key = len)
# print(my_list)

# If we want to sort in descending order we can pass in the reverse parameter into sort
# my_list.sort(key = len, reverse = True)
# print(my_list)

# my_list = [('John', 2), ('Steve', 1), ('Joe', 3)]

# # We can define a function for the list to sort by second key

# def sort_tuple(tuple_value):
    
#     # return the key we want to sort by
#     return tuple_value[1]

# my_list.sort(key = sort_tuple)
# print(my_list)
# => [('Steve', 1), ('John', 2), ('Joe', 3)]


# The sorted() function returns a sorted copy of the original list

# my_list = [3, 6, 4, 2, 1, 5]
# sorted_list = sorted(my_list)
# print(my_list)

# => [3, 6, 4, 2, 1, 5]

# print(sorted_list)

# => [1, 2, 3, 4, 5, 6]

# passing key and reverse parameters to sorted

# my_list = ['Liquisous', 'Chatthy', 'Talkative']
# sorted_list = sorted(my_list, key=len, reverse=True)
# print(my_list)
# print(sorted_list)

# Addind to lists

# my_list = [0, 1, 2, 3]
# my_list[0] = None
# print(my_list)

# => [None, 1, 2, 3]

# Extending a list

# my_list = [0, 1, 2, 3]
# my_list[4] = 4          #Not Advisable
# print(my_list)

# => IndexError: list assignment index out of range

# list.append()  #only add to the end of the list

# my_list = [0, 1, 2, 3]
# my_list.append(4)
# print(my_list)

# => [0, 1, 2, 3, 4]

#list.insert()

# my_list = ['a', 'b', 'c', 'd', 'f']
# my_list.insert(4, 'e')
# print(my_list)

# => ['a', 'b', 'c', 'd', 'e', 'f']

# my_list.insert(1000, 'g')
# print(my_list)

# => ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Removing from Lists
# 1. del()

# my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# del(my_list[0])
# print(my_list)

# => ['b', 'c', 'd', 'e', 'f', 'g']

# del(my_list[0:3])
# print(my_list)

# => ['e', 'f', 'g']

# list.pop()     # removes and returns elements at an indexed pace  "last element" 

# list.remove()   # removes the element passed in as an argument.

#list.clear()     # erases all values of the list

#my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#my_list.pop()

# => 'g'

#my_list.pop(0)

# => 'a'

#my_list.remove('f')

#print(my_list)

# => ['b', 'c', 'd', 'e']
#my_list.clear()

#print(my_list)

# => []

# Ranges

# for n in range(4):
#     print(n)

# => 0
# => 1
# => 2
# => 3

# for n in range(1, 4):
#     print(n)

# for n in range(0, 4, 2):
#     print(n)

# my_list = [0, 1, 2, 3]
# print(my_list)

# # => [0, 1, 2, 3]

# my_range = range(4)
# print(my_range)

# => range(0, 4)

# my_range = range(2, 10, 12)
# print(my_range)

# => range(2, 10, 12)

# Strings

# my_string = 'Hello World'
# for char in my_string:
#     print(char)

# => H
# => e
# => l
# => l
# => o
# => 
# => w
# => o
# => r
# => l
# => d
# => !


# print(my_string[0])
# => 'H'

# Changing Case

# string.upper()
# string.lower()
# string.title() # 1st leeter of each word capitalised

# my_string = 'hello world!'
# print(my_string.upper())

# => HELLO WORLD!


# print(my_string)

# => hello world!
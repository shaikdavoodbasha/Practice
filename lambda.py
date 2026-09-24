# List Comprehension
#1 Create a list of squares of numbers from 1 to 10
# squares = [i**2 for i in range(1,11)]
# print(squares)

#2 Create a list of even numbers from 1 to 50
# eve = [i for i in range(1,51) if i%2==0]
# print(eve)

#3 Convert a list of strings to uppercase
# lsit1 = ['hero','zero','rod']
# str_upper = [i.upper() for i in lsit1]
# print(str_upper)

#4 Create a list of lengths of each word in a sentence
# x = input('Enter sentence Here: ')
# y = x.split(" ")
# list1 = [len(i) for i in y]
# print(list1)

#5 Extract only positive numbers from a list
# x = list(map(int,input('Enter a list of numbers: ').split(" ")))
# res = [i for i in x if i>0]
# print(res)

#6 Create a list of numbers divisible by both 3 and 5 (1–100)
# x = list(map(int,input("Enter a list of number 1-100").split(" ")))
# list1 = [i for i in range(1,101) if i%3==0 and i%5==0]
# print(list1)

#7 Create a list of vowels from a string
# x = input("Enter a string: ")
# list1 = [i for i in x if i in 'aeiouAEIOU']
# print(list1)

#8 Remove duplicates from a list using comprehension
# x = list(map(int,input("Enter a list of numbers: ").split(" ")))
# a =[]
# res = [a.append(i) for i in x if i not in a]
# print(a)

#9 Create a list of numbers and their squares as tuples
# x = list(map(int,input("Enter a list of numbers: ").split(" ")))
# list1 = [i**2 for i in x]
# t1 = tuple(list1)
# print(t1)

#10 Reverse each string in a list
# x = input("Enter a sentence")
# v = x.split(" ")
# list1 = [i[::-1] for i in v]
# print(list1)

#11 Replace negative numbers with 0
# x = list(map(int,input("Enter a list of numbers : ").split(" ")))
# res = [0 if i<0 else i for i in x ]
# print(res)

#12 Create a list where odd numbers → square, even numbers → cube
# x = list(map(int,input('Enter a list of numbes : ').split(" ")))
# res = [i**3 if i%2==0 else i**2 for i in x]
# print(res)

#13 Filter names longer than 5 characters
# x = input('Enter a list of words')
# list_names = x.split(' ')
# res = [i for i in list_names if len(i)>5]
# print(res)

#14 Extract digits from a mixed string ("a1b2c3")
# x = input("Enter a string: ")
# res = [int(i) for i in x if i in '0123456789']
# print(res)

#15 Convert a list of strings to integers, ignoring invalid ones
# x = input("Enter a string: ")
# res = [int(i) for i in x if i in '0123456789']
# print(res)

#16 Flatten a nested list [[1,2],[3,4],[5,6]
# x = [[1,2],[2,3],[3,4],[5,6]]
# flatten_nested_list = [j for i in x for j in i]
# print(flatten_nested_list)

#17 Generate a multiplication table (1–5)
# res = [i*5 for i in range(1,11)]
# print(res)

#18 Create all pairs (i, j) where i < j from [1,2,3,4]
# x = [1,2,3,4]
# r = [(i,j) for i in x for j in x if i<j]
# print(r)

#20 Remove empty strings from a list
#21 Create a list of prime numbers from 1 to 100
# res = [i for i in range(2,100) if all(i%j !=0  for j in range(2,int(i**0.5)+1))]
# print(res)

# Dictionary Comprehension
# 21 Create a dictionary {number: square} from 1 to 10

# res = { i:i**2 for i in range(1,11)}
# print(res)

# 22 Create a dictionary of character frequencies in a string
# x = input("Enter a string: ")
# res = {}
# for i in x:
#     res[i] = res.get(i,0)+1
# print(res)

#23 Convert two lists into a dictionary
# list1 = [1,2,3,4]
# list2  = [5,6,7]
# dict1 = dict(zip(list1,list2))
# print(dict1)

#24 Create a dictionary of words and their lengths
# x = input('Enter the string: ')
# res = {}
# v = x.split(" ")
# for i in v:
#     res[i] = len(i)
# print(res)

# password = input('Enter password: ')
# user_name = input('Enter usename: ')
# if(password=='8121' and user_name=='@davood'):
#     print('You are loggedin')
# else:
#     print("Pleae enter your username or password correctly... ")

#25 Swap keys and values in a dictionary
# dict1 = {'a':1,'b':2,'c':3,'d':4,'e':5}
# swapper = {j:i for i,j in dict1.items()}
# print(dict1)

#26 Filter dictionary values greater than 50
# data = {
#     'apple': 42,
#     'banana': 17,
#     'cherry': 89,
#     'date': 17,
#     'elderberry': 56,
#     'fig': 42,
#     'grape': 73
# }

# fil = {i:data[i] for i in data if data[i]>=50}
# print(fil)
# 27 Create a dictionary of even numbers and their cubes

# eve_cube = {i:i**3 for i in range(1,10) if i%2==0}
# print(eve_cube)

#28 Create a dictionary of vowels and their ASCII values
# x = input('Enter a string: ')
# res = {i:ord(i) for i in x if i in 'aeiouAEIOU'}
# print(res)

#29 Count frequency of elements in a list
# x = list(map(int,input("Enter a list of numbers: ").split(" ")))
# v = {}
# for i in x:
#     v[i] = v.get(i,0)+1
# print(v)

#30 Create a dictionary from a sentence ignoring spaces
# x = input('Enter a sentense').split(" ")
# res = {i:len(i) for i in x}
# print(res)

#31 Keep only items where value is even

# data = {
#     'a': 10,
#     'b': 25,
#     'c': 10,
#     'd': 40,
#     'e': 25
# }
# res = {i:data[i] for i in data if data[i]%2==0}
# print(res)

#32 Replace values less than 10 with 0

# data = {
#     'a': 10,
#     'b': 5,
#     'c': 10,
#     'd': 4,
#     'e': 25
# }
# for i in data :
#     if(data[i]<=10):
#         data[i]=0
# print(data)

#33 Create a dictionary of squares for only odd numbers
# res = {i:i**2 for i in range(1,20) if i%2 !=0}
# print(res)

#34 Map words to their first character
# x = input('Enter a sentense: ').split(" ")
# res = {i:i[0] for i in x}
# print(res)

#35 Convert list of tuples into a dictionary
# list_tuple = [(1,2),(3,4),(5,6),(7,8)]
# #for i,j in list_tuple:
#      print(i,j)
# res = {i:j for i,j in list_tuple}
# print(res)

# Let's Start Lambda functions

#36 Write a lambda to add two numbers
# x = lambda a,b:a+b
# print(x(10,20))

#37 Lambda to check if a number is even
# v = lambda x:x%2==0
# print(v(5))

#38 Lambda to convert string to uppercase
# x = lambda a:a.upper()
# print(x('davood'))

#39 Lambda to return length of a string
# x = lambda a:len(a)
# print(x('davood'))

#40 Use lambda with map() to double all numbers in a list
# list1 = [1,2,3,4]
# result = list(map(lambda x:x +x,list1))
# print(result)

#41 Convert list of strings to integers
# list1 = ['1','2','3','4','5']
# result = list(map(lambda x:int(x),list1))
# print(result)

#42 Find square of each number in a list

# list1 = [1,2,3,4,5,6]
# result = list(map(lambda x:x**2,list1))
# print(result)

#43 Convert temperatures from Celsius to Fahrenheit
# x = int(input('Enter the celsius'))
# result =  x*9/5 + 32
# print(result)

#44 Extract first character from each word
# list1 = input("Enter the sentense: ").split(' ')
# result = list(map(lambda x:x[0],list1))
# print(result)

#45 Use lambda with filter() to get even numbers
# list1 = [1,2,3,4,5,6,7,8]
# result = list(filter(lambda x:x%2==0,list1))
# print(result)

#46 Filter words longer than 4 characters
# list1 = input('Enter a sentence to fileter the word which is longer then 4 chars: ').split(" ")
# v =  list(filter(lambda x:len(x)>4,list1))

#47 Use lambda with reduce() to find sum of list
from functools import reduce
x = [1,2,3,4,5,6]
result = reduce(lambda a,b:a+b,x)
print(result)

#48 Find maximum element using reduce()
x = [1,2,3,4,5,6,7,8]
result = reduce(lambda a,b:a if a>b else b,x)
print(result)
print(result)
print(result)



#49 Sort a list of tuples by second element using lambda

x = [(1,2),(3,4),(5,6),(6,7),(8,9)]
result = sorted(x,key=lambda x:x[1])
print(result)
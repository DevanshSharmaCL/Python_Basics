from functools import reduce 
# Map , Filter , Reduce

#very function in this is high order function 
# what that is ?
# higher order function is a function that does atleast one of the following 
# 1.takes one or more function as an argument 
# 2.return a function as its result 


# MAP

# this is an higer order function because it take 2 arguments

# lets say , hume list mai har ek number ka cube nikalna hai 
# so instead of using loop 
# we will use map function

def cube(x):
    return x**3 # or x*x*x

# now instead of writing the fucntion which probably gonna get used once , 
# we can use lambda function which is a small anonymous function
 
l = [1,2,3,4,6,7,8,9,10]

newl=list(map(lambda x:x*x*x,l))# list is an data structure which is used to store an ordered collection of items
print(newl)

# now what does this code do ?
# map is function ,  which see everyitem in the list and apply the function cube on it and return a new list with the result of the function applied to every item in the list



# FILTER
# filter is also a higher order function because it takes 2 arguments

# THIS IS EXACTLY WHAT U THINKING , 
# u insert the series of number , and filter our either odd or even 


def filter_function(a):
    return a%2==0 # this is the condition for even number
newnewl=list(filter(filter_function,l))
print(newnewl)

# Filter(predicate, iterable) predicate mean condition, iterable mean list , 
# and they are called parameters , of function filter() one is condition , , 2 is list 
# but once a value is given , so that value is called the argument

# predicate is just a function which answer yes or no , and return only yes , takes one value at a time , and return either yes or no 
 # an iterable is anything which u can go one by one , like a list  

# REDUCE
# reduce is a higher order function because it takes 2 arguments
# but we have to import it 


numbers = [1,2,3,4,5,6,7,8,9]

sum = reduce(lambda x,y: x+y, numbers)

print(sum)

# bascially reduce is a function which takes 2 arguments , and apply the function on them , and then take the result and apply the function on it and the next value in the list , and so on ,
# like this 
# 1+2 = 3   [1,2,3,4,5,6,7,8,9]--> [3,4,5,6,7,8,9]
# 3+3 = 6   [3,4,5,6,7,8,9]--> [6,5,6,7,8,9]
# 6+4 = 10  [6,5,6,7,8,9]--> [10,6,7,8,9]
# 10+5 = 15 [10,6,7,8,9]--> [15,7,8,9]
# 15+6 = 21 [15,7,8,9]--> [21,8,9]
# 21+7 = 28 [21,8,9]--> [28,9]
# 28+8 = 36 [28,9]--> [36]
# 36+9 = 45 [36]--> [45]

# so this is what reduce is all about , it can reduce anything , depending on the condition 

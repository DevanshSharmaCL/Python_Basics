name="Cyber"
Age=18
pi=3.14
isReady=True


#list [like js array] kind of array
fruits=['apple','banana','orange']

#tuple (like a read only array)
fruits=('apple','banana','orange')

#dictionary (like js object)
person={
    "name":"Cyber",
    "age":18,
    "isReady":True,
}

#set {can have unique items only}
unique_numbers={1, 2, 3, 4, 5}



#type checking 
print(type(name))  # <class 'str'>
print(type(Age))   # <class 'int'>
print(type(fruits)) # <class 'list'>

#Dynamic Typing
x="cyber"
x=10
x=True
#this wont throw any error since python allow dynamic typing

#type casting
int("5")        # 5
str(10)         # "10"
float("3.14")   # 3.14
list("hello")   # ['h', 'e', 'l', 'l', 'o']

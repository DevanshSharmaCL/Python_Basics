#short and readable way to create a new list from an existing list

#without list comprehension

squares = []
for i in range(5):
    print(i*i)

#with list comprehension

squares = [o*o for o in range(10)]
print(squares)

#basic syntax:
# new_list = [expression for item in iterable if condition]


#example 1:double all the number 

numbers = [1, 2, 3, 4, 5]
doublt=[n*2 for n in numbers]
print(doublt)

#exaple 2: filter even numbers
even =[1,2,3,4,5,6,7,8,9,10]
evens = [n for n in even if n%2==0]
print(evens)

#example 3: uppercase all name 
names = ["devansh", "bhavi", "mandy", "tony"]
uppercase=[name.upper()for name in names ]
print(uppercase)
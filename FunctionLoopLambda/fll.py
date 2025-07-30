#function with the loop

#print even number from the list

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def print_even_numbers(numbers):
    for num in numbers:
        if num %2 ==0 :
            print(num)

print_even_numbers(numbers)  # This will print even numbers from 1 to 20

#=========================================================

#lambda funtion (Anonymous function )
#what is lambda function?
# lambda function is a one-liner , quick function without a name , its used for short task 

#lambda arguments:exporession

#exampple

square = lambda x: x*x
print(square(5))  # Output: 25

add = lambda a,b:a+b
print(add(3,4)) # Output: 7



#Using lambda with maps and filter 


#example : map() applying a function to every item in a list 

numbers = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
square =list(map(lambda x: x**2,numbers))
print(square)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



#exaple : filter() keep only items that return true

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x:x%2==0,numbers1))
print(even)  # Output: [2, 4, 6, 8, 10]
#=========================================================



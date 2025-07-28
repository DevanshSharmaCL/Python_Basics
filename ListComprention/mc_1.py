#🧩 Mini Challenge 1:you have a list of numbers from 1 to 20. Create a new list that only contains the squares of even numbers using list comprehension.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

squares=[n for n in numbers if n%n==0| n%2==0]
print(squares)

#🧩 Mini Challenge 2: Lambda + map + filter
#Use filter() with a lambda to keep only even numbers.

#hen use map() with a lambda to square those even numbers.

#Print the final list.

nums = [1, 2, 3, 4, 5, 6, 7, 8]

even = list(filter(lambda x: x%2 ==0,nums))
print(even)

square = list(map(lambda x :x*2,even))
print(square)  # Output: [4, 16, 36, 64]

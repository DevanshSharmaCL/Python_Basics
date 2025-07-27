#Basic syntax
#new_list=[expression for item in iterable] 


# Example 1: Square numbers from 1 to 5

squares=[x*x for x in range(1,11)]
print(squares)


# Example 2: Convert words to uppercase

words=['Hello', 'world', 'Python', 'is', 'great']
uupercase_words=[word.upper() for  word in words]
print(uupercase_words)


# Example 3: Filter Even Numbers

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number_list=[n for n in numbers if n%2==0]
print(even_number_list)

# example 4 : capitalize words

names = ["devansh", "tony", "bruce", "steve"]
capitalized_names=[name.capitalize() for name in names]
print(capitalized_names)

#==================================================================================

# Dictionary Comprehension

#basic syntax

Person ={
    "name":"Devansh",
    "age": 20,
}


#access and modify values

print(Person["name"])
Person["age"] = 21
print(Person)

#LOOPING THROUGH A DICTIONARY
for key ,value in Person.items():
    print(f"{key}: {value}")

students = [
    {
        "name": "aarav",
        "age": 19,
        "city": "gurgaon",
    },
    {
        "name": "Bhavi",
        "age": 13,
        "city": "gurgaon",
    },
    {
        "name": "mandy",
        "age": 19,
        "city": "gurgaon",
    }
]

# Access student 1 (aarav)
print(students[0]["name"])     # aarav
print(students[0]["age"])      # 19
print(students[0]["city"])     # gurgaon

# Update Bhavi's age (student 2)
students[1]["age"] = 19

# Print all student data
print(students[0])  # aarav
print(students[1])  # bhavi
print(students[2])  # mandy

# We will use for loop to loop everything 


students = {
    "devansh": 90,
    "bhavi": 84,
    "mandy": 70
}
#loop through keys 
for name in students:
    print(name)  # prints the keys (names)

#loop through values
for score in students.values():
    print(score)

#loop through key-value pairs
for name,score in students.items():
    print(f"{name}:{score}")  # prints key-value pairs in the format "name: score"


#.keys()	Returns only keys
#.values()	Returns only values
#.items()	Returns pairs (key, value)



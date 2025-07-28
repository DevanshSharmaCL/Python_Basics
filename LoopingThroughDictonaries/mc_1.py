#🧠 Mini Challenge 1: Topper Finder

students = {
    "devansh": 90,
    "bhavi": 84,
    "mandy": 70,
    "tony": 95
}

# Find the topper in the dictionary
for name,score in students.items():
    if score == max(students.values()):
        print("Topper:", name, "with score:", score)
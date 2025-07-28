#🧠 Mini Challenge 2: Filter Pass/Fail Students

students = {
    "devansh": 90,
    "bhavi": 84,
    "mandy": 70,
    "tony": 95
}

#student =< 70 is fail 

for name, score in students.items():
    if score <= 70:
        print(f"{name} is a fail student")
    else:
        print(f"{name} is a pass student")


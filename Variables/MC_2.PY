# Mini challenge 2: DataBox

#create a dictionary with your name, age, hobbies (as a list), and location
# add a new key "is_prgrammer" with values true
#change the location to india 
#print the dictionary
#pront only hobbies list 


StudentData = {
    "name": "devansh sharma",
    "age":20,
    "hobbies": ["coding", "reading", "gaming"],
    "location": "USA",
}

StudentData.update({"is_programmer": True})
StudentData["location"]="india"
print(StudentData["hobbies"])
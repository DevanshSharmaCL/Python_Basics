#🧩 Mini Challenge 1:

#   Create a text file notes.txt
#   Write "Learning Python is fun!" into it
#   Then append " I’m learning file handling."
#   Finally, read and print the content

# Step 1: Write to the file
with open("notes.txt", "w") as file:
    file.write("Learning Python is fun!")

# Step 2: Append to the file
with open("notes.txt", "a") as file:
    file.write(" I'm learning file handling.")

# Step 3: Read and print the content
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

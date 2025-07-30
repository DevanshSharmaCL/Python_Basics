#1. Opening a file

file = open("data.txt", "r")  # "r" for read

#2. Reading from a file
content= file.read()
print(content)
file.close()  # Always close the file after use

#3. Writing to a file
file = open("data.txt", "w")  # "w" for write (overwrites)
file.write("Hello, world!")
file.close()

#4. Appending to a file
file = open("data.txt", "a")  # "a" for append
file.write("\nThis is new content.")
file.close()


#5. Using with (automatic closing) ✅ BEST PRACTICE
with open("data.txt", "r") as file:
    content = file.read()
    print(content)


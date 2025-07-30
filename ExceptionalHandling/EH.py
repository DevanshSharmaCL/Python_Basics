#✨ Why use try/except?

#Because errors will happen — bad user input, missing files, etc.
#Instead of crashing your prgram, try/except lets you handle errors gracefully.

#try:
    # code that might break
#except SomeError:
    # what to do if it breaks


#example 1 : dividing with zero 

try:
    num = int(input("enter the number:"))
    result = 10 / num
    print("result:",result)

except ZeroDivisionError:
    print("you can't divide by zero!")
except ValueError:
    print("invalid input")


#example 2 :File not found
try:
    with open("random.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Make sure 'random.txt' exists.")


# optional  else and finally 
try:
    print("Trying...")
except:
    print("Something went wrong")
else:
    print("No errors occurred")
finally:
    print("This runs no matter what!")

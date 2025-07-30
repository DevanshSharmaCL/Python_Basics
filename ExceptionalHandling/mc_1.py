
#🧩 Mini Challenges
#✅ Challenge 1:

#Ask the user for a number. Divide 100 by it and handle:

#    Division by zero

#    Invalid input (e.g., letters)


try:
    num = int(input("enter the number:"))
    result = 100 / num
    print("result:",result)

except ZeroDivisionError:
    print("you can't divide by zero!")
except ValueError:
    print("invalid input")
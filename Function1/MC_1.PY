# Return even number 

# Return even number 

Input_Num1 = int(input("Enter a number: "))  # ✅ 1. Convert input to integer

def is_even(Input_Num):  # ✅ 2. Parameter name should match exactly (case-sensitive)
    if Input_Num % 2 == 0:
        print("evem")
    else:
        print("odd")

is_even(Input_Num1)  # ✅ Don't forget to call the function!

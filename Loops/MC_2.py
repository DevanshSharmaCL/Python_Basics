correct_password = 1234
attempts = 0
max_attempts = 3

while attempts <max_attempts:
    user_input = input("Enter the password: ")

    if user_input == str(correct_password):
        print("Access granted.")
    else:
        print("Incorrect password. Try again.")
        attempts+=1 

        if attempts == max_attempts:
            print("Maximum attempts exceeded. Access denied.")
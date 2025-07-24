# Mini challenges 2:smart login 
username ="devansh"
password =1234

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")


if username_input == username and password_input == str(password):
    print("Login successful!")
elif username_input == username and password_input !=str(password):
    print("Incorrect password. Please try again.")
elif username_input != username and password_input == str(password):
    print("Incorrect username. Please try again.")
else:
    print("Both username and password are incorrect. Please try again.")
age=17

if age >=18:
    print("You are an adult.")
elif age>=13:
    print("You are a teenager.")
else: 
    print("You are a child.")



isLoggedIn=True
isAdmin=True

if isLoggedIn and isAdmin:
    print("Welcome Admin!")
elif isLoggedIn:
    print("Welcome User!")
else:
    print("Please log in.")
    print("You are not logged in.")
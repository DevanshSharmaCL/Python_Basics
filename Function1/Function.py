# How can we define the function 

#    def function_name(parameters):
        #code block 
#       return result

def greet(name):
    return  "hello"+" " + name
print(greet("Alice"))


#parameters are the placeholder for the name or value
#arguments are the actual value that we pass to the function

def add(a,b):
    return a+b
result=add(5,3)
print(result)

# function with the default parameter 
def greet(name="world"):
    return "hello " + name
print(greet())
print(greet("devansh"))  # Uses default value

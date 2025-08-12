# Lambda function is also know as anonymous function 
# small , inline , fucntion without a formal name 
# used for one-time operation , where defining a full name would be a unnecessary 

#so

# Instead of writing this 

# def double(x):
#    return x*2

# print(double (5))

#we can write this 
double = lambda x:x*2
print(double(5))  # Output: 10

cube = lambda x:x*x*x
print(cube(5))  # Output: 125

#we can even pass the function from landha function like this 

def test (f,s):
    return 6+f(s)
print(test(cube,4))
# Genrators are used to genrate on the fly value 
# It use "yield" keyword to return value
def genrate_number():
    for i in range(1000):
        yield i 

gen = genrate_number()

for j in gen :
    print(j)

#  function or expression that produce a sequence of values lazily, one at a time, rather than storing all values in memory simultaneously
# they are a powerful tool for creating iterators in a memory-efficient way, especially when dealing with large datasets or infinite sequences. 

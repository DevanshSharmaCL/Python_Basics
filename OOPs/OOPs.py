# OOPs is object-oriented programming system
#It’s how real-world software is structured — reusable, scalable, and easy to manage.
#Even if you're working solo, learning classes and objects gives you superpowers in structuring code.

#| Concept    | Meaning (Simple)                          |
#| ---------- | ----------------------------------------- |
#| Class      | A blueprint or design (like a car design) |
#| Object     | A real thing made from that blueprint     |
#| `__init__` | Special function that sets up the object  |
#| `self`     | Refers to the current object              |
#| Method     | A function inside a class                 |



#Example


class Car :
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour

    def drive(self):
        print(f"{self.brand} car is getting driven in {self.colour}colour!")

    #create object 
my_car = Car("tesla" , "red")
my_car.drive()


 
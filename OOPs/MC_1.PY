#🧩 Mini Challenges
#✅ Challenge 1:

#   Create a class Student with:

#   Attributes: name, marks

#   Method grade() that returns:

#   A (90+), B (75+), C (60+), D (40+), F (else)

#   Then create 2 students and call grade() on each.





class student:
    def __init__(self,name , marks):
        self.name=name
        self.marks=marks

    def grade(self):
        if self.marks>90:
            print(f"{self.name} got A grade")
        elif self.marks>80:
            print(f"{self.name} got B grade")
        elif self.marks>70:
            print(f"{self.name} got C grade")
        else:
            print(f"{self.name} got F grade")

my_grade=student("devansh", 99)
my_grade.grade()
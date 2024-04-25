# A Python program to demonstrate inheritance
class Person(object):
   
  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id
 
  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)
 
 
# Driver code
person_instance = Person("Emma", 102) # An Object of Person
person_instance.Display()

class Student(Person):
  def Print(self):
    print("I am a student")

Student_details = Student("Emma", 103)

Student_details.Display()
Student_details.Print()



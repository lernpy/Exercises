

class Driver:

    def __init__(self, firstname: str, lastname: str, experience: int ):
        self.firstname = firstname
        self.lastname = lastname
        self.experience = experience

    def __str__(self):
        print (f'Driver: {self.firstname} {self.lastname}, {self.experience}')
    

class Person(Driver):

    def __init__(self, age: int):
        self.age = age
        
      
    def __str__(self):
        print (f'Driver: {self.age}')



john = Driver(firstname = input("Enter a driver's name: "), 
              lastname = input("Enter a driver's surname "),
              experience = int(input("Enter a driver's experience : ")))
              
john = Person(age = int(input("Enter a driver's age : ")))


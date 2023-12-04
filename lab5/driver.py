

class Driver:

    def __init__(self, firstname: str, lastname: str, experience: int ):
        self.firstname = firstname
        self.lastname = lastname
        self.experience = experience

    def __str__(self):
        return f'Driver: {self.firstname} {self.lastname}, {self.experience}'
    

class Person(Driver):

    def __init__(self, age: int, fullname: str):
        self.age = age
        self.fullname = self.lastname + " " + self.firstname
      
    def __str__(self):
        return f'Driver: {self.fullname}, {self.age}'
    
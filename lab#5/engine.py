class Engine:

    def __init__(self, power: int, company: str):
        self.power = power
        self.company = company

   
    def __str__(self):
        print (f'Engine: {self.power}, {self.company}')
    


engine = Engine(power = int(input("Enter an engine's power: ")), 
              company = input("Enter an engine's company: "))
              
              
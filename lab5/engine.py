class Engine:

    def __init__(self, power: int, company: str):
        self.power = power
        self.company = company

   
    def __str__(self):
        return f'Engine: {self.power}, {self.company}'
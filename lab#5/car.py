from driver import Driver
from engine import Engine

class Car:

    def __init__(self, mark: str,  klass: str, weight: int):
        self.mark = mark
        self.klass = klass
        self.weight = weight
    
    def __str__(self):
        return f'Car: {self.mark}, {self.klass}, {self.weight}'
    
    def start():
        print (f'Поехали')
    
    def stop():
        print (f'Останавливаемся')
    
    def turn_right():
        print (f'Поворот направо')
    
    def turn_left():
        print (f'Поворот налево')
    
class Lorry(Car):
    def __init__(self, carrying: int):
        self.carrying = carrying
        
    
    def __str__(self):
        return f'Car: {self.mark}, {self.klass}, {self.weight}, {self.carrying}'
    
class SportCar(Car):
    def __init__(self, speed: int):
        self.speed = speed
        
    def __str__(self):
        return f'Car: {self.mark}, {self.klass}, {self.weight}, {self.speed}'

      
               

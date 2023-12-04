from driver import Driver
from engine import Engine

class Car:

    def __init__(self, mark: str,  klass: str, weight: int, driver: Driver, engine: Engine):
        self.mark = mark
        self.klass = klass
        self.weight = weight
    
    def __str__(self):
        return f'Car: {self.mark}, {self.klass}, {self.weight}, {Driver}, {Engine}'
    
    def start():
        return f'Поехали'
    
    def stop():
        return f'Останавливаемся'
    
    def turn_right():
        return f'Поворот направо'
    
    def turn_left():
        return f'Поворот налево'
    
class Lorry(Car):
    def __init__(self, carrying: int):
        self.carrying = carrying
        
    
    def __str__(self):
        return f'Car: {self.mark}, {self.klass}, {self.weight}, {self.carrying}, {Driver}, {Engine}'
    


class SportCar(Car):
    def __init__(self, speed: int):
        self.speed = speed
        
    
    def __str__(self):
        return f'Car: {self.mark}, {self.klass}, {self.weight}, {self.speed}, {Driver}, {Engine}'

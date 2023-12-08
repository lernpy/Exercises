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

info = input ("What's cardo you need: car, lorry or sportcar: ")

if info == "car":
    car = Car(mark = input("Enter a car's mark: "), 
        klass = input("Enter a car's klass: "),
        weight = int(input("Enter a car's weight: ")))
    print (f'{Driver}, {Engine}, {car}')
elif info == "lorry":             
    lorry = Lorry(carrying = int(input("Enter a car's carrying: ")))
    print (f'{Driver}, {Engine}, {Car}, {lorry}')
elif info == "sportcar":
    sportcar = SportCar(speed = int(input("Enter a car's speed: ")))
    print (f'{Driver}, {Engine}, {Car}, {sportcar}')
else:
    print('Wrong information!!!')

run = input("Enter start, stop, right or left: ")
if run == 'start':
    Car.start()
elif run == 'stop':
    Car.stop()
elif run == 'right':
    Car.turn_right()
elif run == 'left':
    Car.turn_left()
else:
    print ('Wrong action!!!')      
               

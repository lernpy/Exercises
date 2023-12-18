from 

info = input ("What's car do you need: car, lorry or sportcar: ")

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
a = float(input())
b = float(input())
c = float(input())
dis = b**2 - 4*a*c

if dis >= 0:
    if dis > 0:
        x1 = (-b+dis**0.5)/(2*a)
        x2 = (-b-dis**0.5)/(2*a)
        print(x1, x2)
    else:
        print(-b/(2*a))





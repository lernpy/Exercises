a = int(input())
b = int(input())
c = int(input())

if a <= b <= c :
    print (a, b, c)
elif b <= a <= c:
    print (b, a, c)
elif c <= b <= a:
    print (c, b, a)
elif a <= c <= b: 
     print (a, c, b)
elif b <= c <= a: 
     print (b, c, a)            
else: 
    print (c, a, b)   
options_list = [
    "Avalilable options:",
    "1. a + b",
    "2. a - b",
    "3. a * b",
    "4. a / b",
    "5. a % b"
]
       
def is_valid_number(num):
    return f'Wrong data {(num)}, enter a number!'        

def addition (num1, num2):
    return num1+num2

def subtraction (num1, num2):
    return num1-num2

def multiplication (num1, num2):
    return num1*num2

def division (num1, num2):
    return num1/num2

def modulo (num1, num2):
    return num1%num2

while True:
    print (*options_list, sep = '\n')
    
    while (first := input('Enter first number: ')).isdigit():
        first = int(first)
        break
    else:
        print(is_valid_number(first))
        continue
    
    while (second := input('Enter second number: ')).isdigit():
        second = int(second)
        break
    else:
        print(is_valid_number(second))
        continue
    num1 = int(first)
    num2 = int(second)
    oper = input ("Choice an avalilable options: '+', '-', '*' '/' or '%': ")
    if oper == "+":
        result = addition(num1, num2)
        print ("Result is:", result)
    elif oper == "-" :
        result = subtraction (num1, num2)
        print ("Result is:", result)
    elif oper == "*" :
        result = multiplication (num1, num2)
        print ("Result is:", result)  
    elif oper == "/" :
        result =  division (num1, num2) 
        print ("Result is:", result)
    elif oper == "%":
        result =  modulo (num1, num2)
        print ("Result is:", result)
    else:
        print ('The option is not avalilable!') 
    
    next = input('Do you want continue? y/n:  ')    
    if next == 'n':
        print ('Good bye') 
        break
    else:
        print ("Let's go!\n")
        continue
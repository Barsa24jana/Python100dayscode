'''Data Type '''
#substring
print("Hello"[0])
#string
print("123"+"123") #string concatenation
#integer:whole number
print(123+123)
#Floating point number
print(14.14)
#boolean
print(True)
print(False)
#print(type("hello")) #0utput class str
#len(int) will not work because it will give type error 
#we can't concatenate a str to a int only str to str so we have to convert the data type which is type conversion.
#mathematical operation 
#+,-,*,/,//,**,%
# we follow PEMDAS RULE
#number manipulation : round function
print (round(234.6789,2))
#+=,-=,*=,/= use it for easy or shortcut
#f string
age = 12
is_winning = True
print(f'my age is {age} is winning{is_winning}')

'''Tip Calculator'''
print("Welcome to the Tip Calculator")
Total_bill = int(input("What was the total bill? : "))
Tip = int(input("How much tip would you want to give? : "))
People = int(input("How many people to split the bill? : "))
Pay = round(((Total_bill * Tip / 100)+Total_bill) / People,2)
print(f'Each person should pay {Pay}')
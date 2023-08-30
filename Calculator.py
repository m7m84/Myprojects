num1 = float(input('enter the first number'))
num2 = float(input('enter the second number'))
o = input('enter the operation')
if o == '+' :
    print(num1+num2)
elif o == '-' :
    print(num1-num2)
elif o == '*' :
    print(num1*num2)
elif o == '/':
    print(num1/num2)
elif o == '^' :
    print(pow(num1, num2))
else :
    print('wrong operation')

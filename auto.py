#the tasks i feel is consuming time is simple operations of math which delay the process of solving


choice = int(input("enter 1 for addition,2 for subtraction , 3 for multiplication and 4 division"))
num1 = int(input("enter the first (greater) number"))
num2 = int(input("enter the second number"))


sum = num1 + num2
dif = num1 - num2
prod = num1*num2
quo = num1/num2


  
if (choice == 1):
   print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
if (choice == 2):
   print('The difference of {0} and {1} is {2}'.format(num1, num2, dif))
if (choice == 3):
   print('The product of {0} and {1} is {2}'.format(num1, num2, prod))
if (choice == 4):
   print('The quotient of {0} and {1} is {2}'.format(num1, num2, quo))

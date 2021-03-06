# -*- coding: utf-8 -*-
"""practice_problems.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BesXmVzQegPxLfpocgK6z8tvq492WvEC

1. Area of circle
"""

#inputing radius
r = float(input('Enter the radius:'))

#calculating area
area = 3.14*r*r

#displaying area
print('\nThe area of the circle is', area)

"""2. Print details"""

#inputing name
name = input('Enter name of the student:')

#inputing roll number
r_no = int(input('Enter roll number of the student:'))

#inputing marks
marks = int(input('Enter mark of the student:'))

#printing all the inputed values
print('\nName:', name)
print('Roll number:', r_no)
print('Mark:', marks )

"""3. Maximum value in a list"""

# method 1
#entering list values
l1 = [1,2,3,4]

#printing maximum value in the list
print('Maximum value in', l1, 'is', max(l1))

# method 2
#creating an empty list to take values
l2 = []

#inputing number of elements in the list
num = int(input('Enter number of list elements: '))

#converting the number of elements to a list
r = range(num)

#inputing the list elements
i = 0
for i in r:
    a = int(input('Enter list elements: '))
    l2.append(a)
    i = i+i

#printing maximum value in the list
print('\nMaximum value in', l2, 'is', max(l2))

"""4. Charecters in string"""

# inputing string 
test_str = input(" Enter the string: ")
  
# counting characters 
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  
# printing result 
print ('Count of all characters in',test_str,' is :\n ', str(all_freq))

"""5. Copying values in a tuple"""

#taking vales to tuple
t1 = (11, 22, 33, 44, 55, 66)

#copying values to new tuple
t2 = t1[3:-1]

#printing output
print(t2)

"""6. Sum of successive numbers"""

#taking first 10 numbers
l = range(1,11)

#calculating sum of current number and previous number
for i in l:
    j = i-1
    sum1 = i+j
    #printing the sum of current and previous number
    print('The sum of current number',i,'and previous number',j,'is', sum1)

"""7. Divisible by 5"""

#inputing number of elements
num = int(input('Enter the number of elements: '))

#creating list with number of elements
r = range(num)

#creating an empty list
l1 = []

#inputing the elements
for i in r:
    s = int(input('Enter the elements: '))
    l1.append(s)
    i += 1
  
#printing values divisible by 5
for j in l1:
    if j%5 == 0:
        print(j, 'is divivisible by 5')
    else:
      print(j, 'is not divivisible by 5')

"""8. Prime number"""

#inputing number
num = int(input('Enter the number: '))

#checking prime or not
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print('The number is zero')

"""9. List reversing"""

l1 = []
l2 = []

num = int(input("Enter the number of list elements: "))
for i in range(1, num + 1):
    value = int(input("Please enter the %d element of list : " %i))
    l1.append(value)

print('\nActual list', l1)
l1.reverse()
print("\nReversed List =  ", l1)

"""10. Pattern printing"""

#inputting number of rows
num = int(input("Enter the number of rows: ")) 
 
#outer loop to handle number of rows  
for i in range(0, num):  
    # inner loop to handle number of columns. values is changing according to outer loop  
        for j in range(0, i + 1):  
            # printing stars  
            print("* ", end="")       
  
        # ending line after each row  
        print()

"""11. Maximum of numbers"""

#inputing number of elements
num = int(input('Enter the number of elements: '))

#inputing elements
r = range(1, num+1)
l1 = []
for i in r:
    a = int(input('Enter the %d number:' %i))
    l1.append(a)

#finding max value
print('\nThe greatest number is ', max(l1))

"""12. Exponent function"""

#defining function
def exponent(base,exp):
    if(exp == 1):
        return(base)
    if(exp != 1):
        return(base*exponent(base,exp-1))

#inputing base and exponent values
base = int(input("Enter base: "))
exp = int(input("Enter exponential value: "))

#printing result
print("\nResult:", exponent(base,exp))

"""13. Sum of cubes"""

#inputing number
num = int(input('Enter the number: '))

#creating list
r = range(2,num)
a = 1

#calculation
for i in r:
    a = a + (i*i*i)
print('Sum of cube of numbers is:', a)

"""14. Pattern printing (nested loop)"""

#inputing the number
num = int(input('Enter the maximum * needed: '))

for i in range(num):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(num,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

"""15. Fizz buzz"""

#inputing number of values
num = int(input('Enter the limit: '))

#creating list
r = range(1, num)

#program for fizzbuzz
for fizzbuzz in r:
    if fizzbuzz % 2 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
        continue
    elif fizzbuzz % 2 == 0:
        print("Fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    print(fizzbuzz)

"""16. Most frequent number"""

#defining function
def most_frequent(n):
    return max(set(n), key = n.count)
  
#inputing numbers
l1 = []
num = int(input('Enter the limit: '))
r = range(1,num)
for i in r:
    a = int(input('Enter the %d number: ' %i))
    l1.append(a)
print('\nThe most frequently occuring number is: ', most_frequent(l1))

"""17. Sum of list elements"""

#inputing values
num = int(input('Enter number of list elements: '))

#inputing list elements
l1 = []
r = range(1,num+1)
for i in r:
    a = int(input('Enter %d element of list: ' %i))
    l1.append(a)
    
#calculating sum of elements in list
sum1 = 0
for j in l1:
    sum1 = sum1 + j
    
print('\nThe sum of elements in the list is', sum1)

"""18. Odd or even"""

#taking numbers from 1 to 15
num = range(1,16)

#displaying each number is odd or even
for i in num:
    if i%2 == 0:
        print(i, 'is even')
    else:
        print(i, 'is Odd')

"""19. Temperature"""

#inputing temperature
far = float(input('Enter temperature in Fahrenheit: '))

#converting to celsius
cel = 0
cel = (5/9)*(far-32)
print('The temperaure in Celsius is:', cel)

"""20. Factorial using function"""

#defining factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
#inputing value
num = int(input("Input a number to compute the factiorial : "))
print('The factorial of ',num, 'is', factorial(num))
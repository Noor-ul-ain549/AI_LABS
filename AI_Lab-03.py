                                    #Task-01
# result=[]
# for i in range(1500,2701):
#     if(i%7==0 and i%5==0):
#         result.append(i)
# print("Numbers Multiple of 5 and divisible by 7 are : ",result)

                                     #Task-02 
# temp=input("Enter C or F for temperature conversion : ")[0]
# x=float(input("Enter Temperature :"))
# farenhiet=(x-32)*(5/9)
# celcius=(x*(9/5))+32
# if(temp=='F' or temp=='f'):
#     print("Temperature in Celcius is : ",farenhiet)
# else:
#     print("Temperature in farenhiet is : ",celcius)

                                    #Task-03
# import random
# # import os
# number=random.randint(1,10)
# while True:
#     guess=int(input("guess the num between 1 to 10 \n "))
#     if guess==number:
#         print("guessed successfully")
#         break
#     else:
#         print("try again")

                                    #Task-04
# for i in range(1,6):
#         print("* " * i)
# for j in range(4, 0, -1):
#                 print("* " * j)
# the range(1,6) generates numbers from 1 to 5, which are used to control the number of asterisks printed in each row. The first loop prints increasing numbers of asterisks, while the second loop (range(4, 0, -1)) generates numbers from 4 down to 1, printing decreasing numbers of asterisks. The "* " * i expression creates a string with i asterisks followed by spaces, which is printed in each iteration. "*" * i means that the string "*" is repeated i times, creating a row of asterisks. The space after the asterisk ensures that the asterisks are separated by spaces for better visibility. The print function outputs each row of asterisks to the console, creating a visual pattern that resembles a diamond shape when combined with the second loop.

                                    #Task-05
# word=input("Enter a word : ")
# print("Reversed word is : ",word[::-1]) 

                                    #Task-06
# even=0
# odd=0
# arr=list(map(,intinput("Enter numbers: ").split()))
# print(arr)
# for i in arr:
#     if(i%2==0):
#         even+=1
#     else:
#         odd+=1
# print("Even numbers are : ",even)
# print("Odd numbers are : ",odd)

                                    #Task-07
# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],{"class":'V', "section":'A'}]
# for item in datalist:
#     print(item," is of type ",type(item))

                                    #Task-08
# for i in range(7):
#     if(i==3 or i==6):
#         continue
#     print(i,end=" ")
                                    #Task-9(a)
# print("Fibonacci series (0 to 50)")
# a=0 
# b = 1
# fib_series = []
# while a <= 50:
#     fib_series.append(a)
#     a, b = b, a + b
# print(" ".join(str(n) for n in fib_series))
# .join() is used to concatenate the elements of the fib_series list into a single string, with each element separated by a space. This allows for a clean and readable output of the Fibonacci series. The str(n) converts each number in the fib_series list to a string, which is necessary for the join operation to work correctly. and for loop iterates through the fib_series list, appending each Fibonacci number to the list until the value of a exceeds 50. The values of a and b are updated in each iteration to generate the next Fibonacci number in the sequence.
                                     #Task-09(b)
# for i in range(0,51):
#     if(i%3==0 and i%5==0):
#         print("FizzBuzz")
#     elif(i%3==0):
#         print("Fizz")
#     elif(i%5==0):
#         print("Buzz")
#     else:
#         print(i)

                                    #Task-10
# print("2D array of i*j")
# m=int(input("Enter number of rows : "))
# n=int(input("Enter number of columns : "))
# arr = [[i*j for j in range(n)] for i in range(m)] 
# #i*J is actually the formula for multiplication table and this is how we can generate a 2D array of multiplication table and the range of i and j is defined by the user input for rows and columns.and how the multiplication table is generated is that the outer loop iterates over the rows and the inner loop iterates over the columns and the value of each element in the 2D array is calculated by multiplying the row index with the column index and this is how we can generate a 2D array of multiplication table using list comprehension in python. and how we apply for loop in the 2D array is that we can use a nested for loop to iterate over the rows and columns of the 2D array and print each element of the 2D array.
# for row in arr:
#     print(row)

                                    #Task-11
# print("Enter lines of text. Enter a blank line to stop:")
# lines = []
# while True:
#     line = input()
#     if line == "":
#         break
#     lines.append(line.lower())
# print("\n".join(lines))

                                    #Task-12
# data = input("Enter comma separated 4-digit binary numbers")
# items = [x.strip() for x in data.split(",")]
# divisible = [x for x in items if int(x, 2) % 5 == 0]
# print(",".join(divisible))

# strip() is used to remove any leading or trailing whitespace from each binary number in the list. This ensures that the binary numbers are clean and ready for processing, especially when checking for divisibility by 5. split(",") is used to split the input string into individual binary numbers based on the comma separator. This creates a list of binary numbers that can be iterated over for further processing. and int(x, 2) is used to convert each binary number (represented as a string) into its decimal equivalent. The second argument, 2, specifies that the input string is in base 2 (binary). This conversion is necessary to perform arithmetic operations, such as checking for divisibility by 5. and % 5 == 0 checks if the decimal equivalent of the binary number is divisible by 5. If the condition is true, the binary number is included in the final output list. and ",".join(divisible) takes the list of binary numbers that are divisible by 5 and joins them into a single string, with each number separated by a comma. This creates a clean output format for displaying the results.

                                    #Task-13
# s = input("Enter a string that contains letters and digits: ")
# letters = 0
# digits = 0
# for ch in s:
#     if ch.isalpha():
#         letters += 1
#     elif ch.isdigit():
#         digits += 1
# print("Letters", letters)
# print("Digits", digits)

                                    #Task-14
password=input("Enter a password: ")
upper=0
lower=0
special=0
digit=0
for char in password:
    if char.islower():
       lower=1
    elif char.isupper():
       upper=1
    elif char.isdigit():
       digit=1
    elif char in "#$@":
       special=1
if 6<= len(password)<=16 and lower and upper and digit and special:
    print("valid Password!!")
else:
    print("invalid Password!!")

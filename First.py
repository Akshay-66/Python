

# def hey(q):
#     def you(w):
#         return q+w
#     return you
# s = hey(22)
# print(s(66))


# def hehe(hoo):
#     print('heee {0}'.format(hoo))
# x = hehe
# x("hooooo")

# def mad(q):
#     x = 'Mad ' + q
#     return x
# def loosu(q):
#     x = "Super mad " + q
#     return x
# def doms(x):
#     rell = x("Goppsssaaalllllaaaaaaaaa")
#     print(rell)

# doms(loosu)
# doms(mad)


# //01.05.2023 DC

# indval = int(input())
# inci = 1
# for i in range(indval):
#     totstr = ""
#     rlval = 'a'
#     fbk = indval
#     srs = inci
#     while(fbk > 0):
#         print(rlval,end=' ')
#         totstr += rlval
#         rlval = chr(ord(rlval) + 1)
#         fbk -= 1
#     while(srs>0):
#         print('*',end=' ')
#         srs -= 1
#     fnl = len(totstr)-1
#     while(fnl>=0):
#         print(totstr[fnl],end=' ')
#         fnl -= 1
#     indval -= 1
#     inci += 2
#     print('\r')





# n = int(input())
# board = [list(input().strip()) for _ in range(n)]

# # Find initial position of rook
# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 'R':
#             x, y = i, j

# m = int(input())
# moves = [input().strip() for _ in range(m)]

# # Apply each move
# for move in moves:
#     direction, steps = move[0], int(move[1:])
#     if direction == 'L':
#         for i in range(steps):
#             if y == 0 or board[x][y-1] == '-':
#                 break
#             y -= 1
#     elif direction == 'R':
#         for i in range(steps):
#             if y == n-1 or board[x][y+1] == '-':
#                 break
#             y += 1
#     elif direction == 'A':
#         for i in range(steps):
#             if x == 0 or board[x-1][y] == '-':
#                 break
#             x -= 1
#     elif direction == 'B':
#         for i in range(steps):
#             if x == n-1 or board[x+1][y] == '-':
#                 break
#             x += 1

# print(x+1, y+1)


# day = int(input("EEh : "))
# print("sec %d"%(day*24*60))

# base_pay = 100.0
# print(base_pay + (base_pay*0.1) + (base_pay*0.05))

# //30.04.2023 DC

# sl = input().strip()
# vol = "aeiou"
# vkol = 0
# rloc = ""
# vvdn = ""
# for i in range(len(sl)):
#     if sl[i] not in vol:
#         vvdn = sl[i]
#         vkol += 1
#     else:
#         if vkol == 1:
#             rloc += vvdn
#         rloc += sl[i]
#         vkol = 0
# if vkol == 1:
#     rloc += vvdn
# print(rloc)



# N = int(input())
# x1 = y1 = z1 = 0
# x = N // 5
# if x > 0:
#     x1 = x
#     N -= x * 5
# y = N // 2
# if y > 0:
#     y1 = y
#     N -= y * 2
# z1 = N
# if y1==0 and z1==0:
#     print("Count of Rs 5: " + str(x1))
# elif z1==0:
#     print("Count of Rs 5: " + str(x1))
#     print("Count of Rs 2: " + str(y1))
# else:
#     print("Count of Rs 5: " + str(x1))
#     print("Count of Rs 2: " + str(y1))
#     print("Count of Rs 1: " + str(z1))

# def eve(n):
#     return n%2==0
# li = [2,4,42,8,2,63,5]
# print(set(filter(eve,li)))


# s1, s2 = input().strip().split()

# # initialize a dictionary to hold common characters and their count
# common_chars = {}

# # iterate over characters in the first string
# for c in s1:
#     # if the character is also in the second string
#     if c in s2:
#         # add the character to the dictionary or increment its count
#         common_chars[c] = common_chars.get(c, 0) + 1

# # calculate the sum of the counts of all common characters
# count = sum(common_chars.values())

# # print the count of common characters
# print(count)
# s1 = input().strip()
# s2 = input().strip()
# x = list(set(s1))
# y = list(set(s2))
# ass = 0
# ssa = 0
# for i in range(len(s1)):
#     if s1[i] in s1[i+1:]:
#         ass += 1
# for i in range(len(s2)):
#     if s2[i] in s2[i+1:]:
#         ssa += 1
# q = 0
# for i in x:
#     if i in y:
#         q += 1
# if ass==ssa and ass>0:
#     print(q+ass)
# else:
#     print(q)
    # # Move to the next line
    # print('\r')
    # input: uvwxyz
    # output:
    # u-v-w 
    # -z-x 
    # --y 

# n = int(input())
# matrix = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# sum_diagonal = 0
# for i in range(n):
#     sum_diagonal += matrix[i][i] # add elements from main diagonal
#     sum_diagonal += matrix[i][n-i-1] # add elements from the other diagonal

# if n % 2 != 0: # subtract the common element from both diagonals if n is odd
#     sum_diagonal -= matrix[n//2][n//2]

# print(sum_diagonal)

# a = 10; b=20; c=1*b; print(c)

# a = 0
# b = 10
# z = (a&b) | (a&a) | (a|b)
# print(z)


# m, n = map(int, input().split())

# # read the input matrix
# matrix = []
# for i in range(m):
#     row = input().split()
#     matrix.append(row)

# # replace characters outside the submatrices with asterisks
# for i in range(m):
#     for j in range(m):
#         if (i < n or i >= m-n) and (j < n or j >= m-n):
#             continue
#         elif (i < n or i >= m-n) and (j >= n and j < m-n):
#             matrix[i][j] = '*'
#         elif (j < n or j >= m-n) and (i >= n and i < m-n):
#             matrix[i][j] = '*'
#         else:
#             matrix[i][j] = '*'

# # print the modified matrix
# for i in range(m):
#     print(' '.join(matrix[i]))
    
# Example Input/Output 1: 
# Input: 
# 6 2
# w u f j p e 
# g p z x d k 
# g n x a z f 
# y d j q v n 
# k r w b a u 
# d k i u e m 
# Output: 
# w u * * p e 
# g p * * d k 
# * * * * * * 
# * * * * * * 
# k r * * a u 
# d k * * e m
# import math
# p1 = [2, 2]
# p2 = [14, 7]
# distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

# print(distance)

# # Python program to find the smallest number which
# # is greater than a given no. has same set of
# # digits as given number

# # Given number as int array, this function finds the
# # greatest number and returns the number as integer
# def findNext(number,n):
	
# 	# Start from the right most digit and find the first
# 	# digit that is smaller than the digit next to it
# 	for i in range(n-1,0,-1):
# 		if number[i] > number[i-1]:
# 			break
			
# 	# If no such digit found,then all numbers are in
# 	# descending order, no greater number is possible
# 	if i == 1 and number[i] <= number[i-1]:
# 		print ("Next number not possible")
# 		return
		
# 	# Find the smallest digit on the right side of
# 	# (i-1)'th digit that is greater than number[i-1]
# 	x = number[i-1]
# 	smallest = i
# 	for j in range(i+1,n):
# 		if number[j] > x and number[j] < number[smallest]:
# 			smallest = j
		
# 	# Swapping the above found smallest digit with (i-1)'th
# 	number[smallest],number[i-1] = number[i-1], number[smallest]
	
# 	# X is the final number, in integer datatype
# 	x = 0
# 	# Converting list upto i-1 into number
# 	for j in range(i):
# 		x = x * 10 + number[j]
	
# 	# Sort the digits after i-1 in ascending order
# 	number = sorted(number[i:])
# 	# converting the remaining sorted digits into number
# 	for j in range(n-i):
# 		x = x * 10 + number[j]
	
# 	print ("Next number with set of digits is",x)


# # Driver Program to test above function
# digits = "218765"		

# # converting into integer array,
# # number becomes [5,3,4,9,7,6]
# number = list(map(int ,digits))
# findNext(number, len(digits))

# This code is contributed by Harshit Agrawal


# def base_n_to_decimal(number, base):
#     decimal_number = 0
#     power = 0
#     while number > 0:
#         last_digit = number % 10
#         decimal_number += last_digit * (base ** power)
#         power += 1
#         number //= 10
#     return decimal_number

# n = int(input())
# x, y = map(int, input().split())

# # convert x and y to base 10
# x_decimal = base_n_to_decimal(x, n)
# y_decimal = base_n_to_decimal(y, n)

# # add x and y in base 10
# sum_decimal = x_decimal + y_decimal

# # print the sum in base 10
# print(sum_decimal)


# x = int(input())
# a,b = map(int,input().strip().split())
# x1 = 0
# x2 = 0
# while(a>0):
#     x1 += a%x
#     a/=x
# while(b>0):
#     b = b%x
#     b/=x
# print(int(x2)+int(x1))


# a = [1,2,3,4]
# b = [3,4]
# del a[2]
# print(a)


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True

# n1 = int(input().strip())
# n2 = int(input().strip())

# count = 0
# for num in range(n1, n2+1):
#     if is_prime(num):
#         count += 1

# print(count)


# s = input().split()
# for i in range(len(s)):
#     s[i] = s[i][0].upper() + s[i][1:]
# print(" ".join(s))

##Class
# for i in range(2):print("hello"),print('ist akhay')
# print('i=',i)

# class Devas:
#     def Seva(self):
#         print("Hey Everyone! This is Akshay.B\nMy mom's gonna meet his guru tomorrow")

# obj = Devas()
# obj.Seva()
#print(obj)

# class Hello:
#     print("HI!")

# Hello()

# class Eno:
#     def GB():
#         print("Its !Good")

# Eno.GB()




# ##Kwargs
# def func(**kwargs):
#     if 'name' in kwargs:
#         print("My Name is {0}".format(kwargs['name']))
#     if 'age' in kwargs:
#         print("My Age is {0}".format(kwargs['age']))
#     else:
#         print("No Key Found")
        
# func(name='champ',age=24,marks=99)


##args

# def sums(*ehe):
#     return sum(ehe)
# print(sums(4,52,4,62,46,4,624,4))

##Lambda function

# ##normal fn
# def sum(a):
#     return a**2
# print(sum(5))

# num = lambda sum : sum**2
# print(num(5))



# ##Map keyword
# def even(num):
#     return num % 2 == 0

# tocheck = [10,25,426,246,5,74,72,78,4,374,7,8]
# print(list(map(even,tocheck)))
# print(list(filter(even,tocheck)))




# ##Functions
# def Akshay(a):
#     print(f"He is the most %s and best decision making boy"%a)

# Akshay("intelligent")

# def mult(a,b):
#     return a*b

# print(mult(8,9))

# def prime(nums):
#     prims = []
#     for num in nums:
#         if num > 0:
#             for chk in range(2,(int)(num/2)+1):
#                 if(num % chk == 0):
#                     print(num," is not a prime number")
#                     break
#             else:
#                 print(num," is a prime number")
#                 prims.append(num)
#         else:
#             pass
#     return prims

# x = [10,34,25,4,24,6,7,357,5,8,42,8,5,77,9,4,72,7,6]
# print(prime(x))





# a = ["Name: ", "Place: ", "Gender: ", "Age: "]
# b = ["Akshay.B", "Chennai", "M", 18]
# c = set(zip(a,b))
# d = list(zip(a,b))
# e = tuple(zip(a,b))
# f = dict(zip(a,b))
# print("SET === {0}\nLIST === {1}\nTUPLE === {2}\nDICTIONARY === {3}".format(c,d,e,f))


# for i,r in enumerate("Elon Musk"):
#     print(i,r)


# a = [i for i in range(88) if i%10==8]
# print(a)

# for i in range(8,88,8):
#     print(i)

# a = 1
# j = 0
# x = int(input())
# b = x-1
# q = b
# for i in range(x):
#     j = x
#     z = q
#     while j > 0:
#         while z > 0:
#             print("*",end="")
#             z-=1
#             j-=1
#         print(a,end="")
#         a+=1
#         j-=1
#         b-=1
#     print("\r")
#     q-=1



# a = 0
# while a < 10:
#         if a==8:
#             print("Its it")
#             break
#         else:
#             print("its !") 


# import re
# #a = "Hello im checking whether its working || not"
# a = "The rain in India"
# x = re.search("India",a)
# if x:
#     print("s")
# else:
#     print("no")

##String to list and list to tuple and dictionary
# a = "Vilasavathi"
# x = [i for i in a]
# y = tuple(x)
# z = set(x)
# print(y, z)

##String to list
# a = [i for i in "Sujatha"]
# print(a)

##Dictionary
# a = {"Dom":{"Dan":{"Dab": "Hello","Dib":"Bye"}}}
# print(a["Dom"]["Dan"]["Dib"])


# #format
# a = "Akshay"
# print(f"This is {a}")

# ##Upper case and Lower case
# a = 'Hello'
# b = "! This is Akshay"
# c = a+b
# # print(c.lower())
# # print(c.upper())
# d = c.split()
# e = c.split('!') ## Delimiter
# print(d[0])
# print(d)
# print(e)
# ##Index characters
# a = 'Champ'
# print(a[3])
# print(a[2:])
# print(a[:2])
# print(a[-1])
# print(a[:-1])
# print(a[::2])
# print(a[::-1])


# #Types of Output in Python
# a = int(input("Enter First NUmber: "))
# b = int(input("Enter Second Number: "))
# sum = a+b
# div = a/b
# rem = a%b
# print("Sum is: %d, Division is: %.2f, Remainder is: %d"%(sum,div,rem))
# print("Sum is {0} Divided value is {1} Remainder of Division is {2}".format(sum,div,rem))
# print(" {0:<3} | {1:^3} | {2:<3}".format("Total", "Quoient", "Remainder"))
# print(" {0:<3} | {1:^3} | {2:<3}".format(sum, div, rem))

# ##power
# a = 8
# b = 6
# print(a**b)

# ##Contatenation and length
# a = "Gem"
# b = ' python'
# print(a+b)
# print(len(a))


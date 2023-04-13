


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
#     print("\n")
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


# n = [5,10,15,20,25,30]  
# t = int(input("too: "))
# l = 0
# r = len(n)-1
# while l <=r:    
#     mid = (r+l)//2
#     if n[mid]==t:
#         print("ollo")
#         break
#     elif n[mid]<t:
#         l = mid+1
#     else:
#         r=mid-1

# task 1
# def gg(n,t):
#     if t in n:
#         print("oldloo ")
#     else:
#         print("oldsongvi")
# n = list(map(int,input("toonuud:").split()))
# t = int(input("too: "))
# gg(n,t)

# def lst(n,t):
#     l = 0
#     r = len(n)-1
#     while l<=r:
#         mid = (r+l)//2
#         if n[mid]==t:
#             print("oldlo")
#             return n,t
#         elif n[mid]<t:
#             l=mid+1
#         else:
#             r=mid-1
#     else:
#         print("oldsongvi")
# n = list(map(int,input("toonuud: ").split()))
# t = int(input("too: "))
# lst(n,t)

# task 2
# def lst(n,t):
#     l = 0
#     r = len(n)-1
#     while l<=r:
#         mid = (r+l)//2
#         if n[mid]==t:
#             print(mid)
#             return n,t
#         elif n[mid]<t:
#             l = mid+1
#         else:
#             r = mid-1
# n = list(map(int,input("toonuud: ").split()))
# t = int(input("haih too: "))
# lst(n,t)


# task 3
# def lst(n,t):
#     l = 0 
#     r = len(n)-1
#     while l<=r:
#         mid = (r+l)//2
#         if n[mid]==t:
#             print(n[0],mid)
#             return n,t
#         elif n[mid]<t:
#             l = mid+1
#         else:
#             r = mid-1
# n = list(map(int,input("toonuud: ").split()))
# t = n[0]
# lst(n,t)


# task 4
# numbers = [6, 12, 18, 24, 30, 36, 42]

# target = 42

# left = 0
# right = len(numbers) - 1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         print("too:", mid)
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# # task 5
# numbers = [10, 20, 30, 40, 50, 60]

# target = int(input("baihgvi: "))

# left = 0
# right = len(numbers) - 1
# found = False

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         found = True
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if found:
#     print("too")
# else:
#     print("baihgvi")

# task6

# numbers = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32]

# target = int(input("too: "))

# left = 0
# right = len(numbers) - 1
# count = 0

# while left <= right:
#     mid = (left + right) // 2
#     count += 1

#     if numbers[mid] == target:
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print("too:", count)

# # task 7
# scores = [45, 50, 58, 65, 72, 80, 88, 95]

# target = int(input("too: "))

# left = 0
# right = len(scores) - 1
# found = False

# while left <= right:
#     mid = (left + right) // 2

#     if scores[mid] == target:
#         print("too:", mid)
#         found = True
#         break
#     elif scores[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if not found:
#     print("oldsongvi")

#     # task 8

#     codes = [101, 105, 112, 120, 135, 148, 160, 175]

# target = int(input("baraani vne: "))

# left = 0
# right = len(codes) - 1
# found = False

# while left <= right:
#     mid = (left + right) // 2

#     if codes[mid] == target:
#         found = True
#         break
#     elif codes[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if found:
#     print("baihgvi")
# else:
#     print("baihgvi")

# # task 9
# book_ids = [1002, 1015, 1028, 1040, 1055, 1072, 1090]

# target = int(input("too: "))

# left = 0
# right = len(book_ids) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if book_ids[mid] == target:
#         result = mid
#         break
#     elif book_ids[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(result)

# # task 10
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# target = int(input("too: "))

# left = 0
# right = len(numbers) - 1
# found = False

# while left <= right:
#     mid = (left + right) // 2

#     print("left =", left, "right =", right, "mid =", mid)

#     if numbers[mid] == target:
#         print("Индекс:", mid)
#         found = True
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if not found:
#     print("Олдсонгүй")

# # task 11

# numbers = [2, 4, 4, 4, 6, 8, 10, 10]

# target = int(input("too: "))

# left = 0
# right = len(numbers) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         result = mid
#         right = mid - 1
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(result)

# # task 12

# numbers = [1, 3, 3, 3, 5, 7, 7, 9]

# target = int(input("too: "))

# left = 0
# right = len(numbers) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         result = mid
#         left = mid + 1
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(result)

# # task 13
# numbers = [10, 20, 30, 40, 50, 60]

# target = int(input("tooo: "))

# left = 0
# right = len(numbers)

# while left < right:
#     mid = (left + right) // 2

#     if numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid

# print("too:", left)

# # task 14

# numbers = [5, 12, 19, 26, 33, 40, 47]

# target = int(input("too: "))

# left = 0
# right = len(numbers) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] < target:
#         result = numbers[mid]
#         left = mid + 1
#     else:
#         right = mid - 1

# if result == -1:
#     print("baihgvi")
# else:
#     print(result)

# # task 15
# numbers = [3, 8, 13, 18, 23, 28, 33, 38, 43]

# a = int(input("too: "))
# b = int(input("too: "))

# for target in [a, b]:
#     left = 0
#     right = len(numbers) - 1
#     result = -1

#     while left <= right:
#         mid = (left + right) // 2

#         if numbers[mid] == target:
#             result = mid
#             break
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     print(target, "too:", result)

# # task 16
# numbers = [3, 8, 13, 18, 23, 28, 33, 38, 43]

# a = int(input("too: "))
# b = int(input("too: "))

# for target in [a, b]:
#     left = 0
#     right = len(numbers) - 1
#     result = -1

#     while left <= right:
#         mid = (left + right) // 2

#         if numbers[mid] == target:
#             result = mid
#             break
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     print(target, "too:", result)

# # task 17
# numbers = [95, 82, 70, 61, 49, 35, 20, 11]

# target = int(input("tooo: "))

# left = 0
# right = len(numbers) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         result = mid
#         break
#     elif numbers[mid] > target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(result)

# # task 18
# def binary_search(numbers, target):
#     left = 0
#     right = len(numbers) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if numbers[mid] == target:
#             return mid
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


# numbers = [3, 7, 12, 18, 25, 31, 40]

# target = int(input("tooo: "))

# print(binary_search(numbers, target))

# # task 19
# numbers = [1, 2, 2, 2, 2, 4, 5, 5, 7, 8]

# target = int(input("tooo: "))

# left = 0
# right = len(numbers) - 1
# first = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         first = mid
#         right = mid - 1
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# left = 0
# right = len(numbers) - 1
# last = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         last = mid
#         left = mid + 1
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if first == -1:
#     print("0")
# else:
#     count = last - first + 1
#     print("dawtagdsan:", count)

#     # task 20
#     numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
#            22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

# target = 38

# # Linear Search
# linear_count = 0

# for i in range(len(numbers)):
#     linear_count += 1

#     if numbers[i] == target:
#         linear_index = i
#         break

# # Binary Search
# left = 0
# right = len(numbers) - 1
# binary_count = 0

# while left <= right:
#     mid = (left + right) // 2
#     binary_count += 1

#     if numbers[mid] == target:
#         binary_index = mid
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1


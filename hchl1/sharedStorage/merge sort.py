# Merge Sort:

# def merge_sort(numbers):                # [5,1,3,2,4]
#     if len(numbers) <= 1:           
#         return numbers

#     mid = len(numbers) // 2            #goliin toog oloh [5,1] [3] [2,4]

#     left = numbers[:mid]                # [5,1] [2,4]
#     right = numbers[mid:]               #slice(method)

#     left = merge_sort(left)             # uurig n dahin duudah: 1 1 tusdaa bolgohod ashiglana
#     right = merge_sort(right)           # left[5] [1] mid [3] right [2] [4] tus tusd n list dotor hiij bn

#     result = []                         

#     i = 0                               # left
#     j = 0                               # right

#     while i < len(left) and j < len(right):         # 0 deh indexees leftr rightiin urt n ih bh ym bol dawtna:
#         if left[i] <= right[j]:                     # leftiin 0 rightiin 0 ees baga buyu = bwl
#             result.append(left[i])                  # vr dvng left iin 0 deh indexd oruulna
#             i += 1                                  # daraah vr dvng shalgahiin tuld i buyu 0 deh index dr 1iig nemj draagin indexiig olno
#         else:                                       # esrgere bwl:
#             result.append(right[j])                 # rightiin 0 deh indexd oruulna
#             j += 1                                  # daraah vr dvng shalgahiin tuld j buyu 0 deh index dr 1iig nemj draagin indexiig olno

#     while i < len(left):                            
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# numbers = [8, 3, 5, 4, 7, 6, 1, 2]

# print(merge_sort(numbers))

# Merge Sort — Дасгал ажлууд :

# task 1
# def merge_sort(n):
#     if len(n)<=1:
#         return n
#     mid = len(n)//2

#     left = n[:mid]
#     right = n[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     r = []

#     i = 0 
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i]<=right[j]:
#             r.append(left[i])
#             i+=1
#         else:
#             r.append(right[j])
#             j+=1
#     while i < len(left):
#         r.append(left[i])
#         i+=1
#     while j < len(right):
#         r.append(right[j])
#         j+=1
#     return r
# n = list(map(int,input("too:  ").split()))
# print(merge_sort(n))

# def merge_sort(n):
#     if len(n)<=1:
#         return n
#     mid = len(n)//2
#     left = n[:mid]
#     right = n[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     r=[]

#     i = 0 
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i]>=right[j]:
#             r.append(left[i])
#             i+=1
#         else:
#             r.append(right[j])
#             j+=1
#     while i<len(left):
#         r.append(left[i])
#         i+=1
#     while j<len(right):
#         r.append(right[j])
#         j+=1
#     return r
# n = list(map(int,input("too:  ").split()))
# print(merge_sort(n))

# task 3
# def merge_sort(n):
#     if len(n)<=1:
#         return n
#     mid = len(n)//2
#     left = n[:mid]
#     right = n[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)

#     r = []
#     i = 0
#     j = 0
#     while i<len(left) and j<len(right):
#         if left[i]<=right[j]:
#             r.append(left[i])
#             i+=1
#         else:
#             r.append(right[j])
#             j+=1
#     while i<len(left):
#         r.append(left[i])
#         i+=1
#     while j<len(right):
#         r.append(right[j])
#         j+=1
#     return r
# n = list(map(int,input("too:  ").split()))
# print(merge_sort(n))

# task 4
# def merge_sort(n):
#     if len(n)<=1:
#         return n
#     mid = len(n)//2
#     left = n[:mid]
#     right = n[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)

#     r = []
#     i = 0
#     j = 0
#     while i<len(left) and j<len(right):
#         if left[i]<=right[j]:
#             r.append(left[i])
#             i+=1
#         else:
#             r.append(right[j])
#             j+=1
#     while i<len(left):
#         r.append(left[i])
#         i+=1
#     while j<len(right):
#         r.append(right[j])
#         j+=1
#     return r
# n = list(map(int,input("too:  ").split()))
# print(merge_sort(n))

# task 5
# def merge_sort(n):
#     if len(n)<=1:
#         return n
#     mid = len(n)//2
#     left = n[:mid]
#     right = n[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)

#     r = []
#     i = 0
#     j = 0
#     while i<len(left) and j<len(right):
#         if left[i]<=right[j]:
#             r.append(left[i])
#             i+=1
#         else:
#             r.append(right[j])
#             j+=1
#     while i<len(left):
#         r.append(left[i])
#         i+=1
#     while j<len(right):
#         r.append(right[j])
#         j+=1
#     return r
# n = list(map(int,input("too:  ").split()))
# a = merge_sort(n)
# p = []
# l = []
# for i in a:
#     if i%2==0:
#         p.append(i)
#     else:
#         l.append(i)
# k = p + l
# print (k)
# print(p)
# print(l)


# task 6
# def merge_sort(n):
#     if len(n)<=1:
#         return n
#     mid = len(n)//2
#     left = n[:mid]
#     right = n[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)

#     r = []
#     i = 0
#     j = 0
#     while i<len(left) and j<len(right):
#         if left[i]<=right[j]:
#             r.append(left[i])
#             i+=1
#         else:
#             r.append(right[j])
#             j+=1
#     while i<len(left):
#         r.append(left[i])
#         i+=1
#     while j<len(right):
#         r.append(right[j])
#         j+=1
#     return r
# n = list(map(int,input("too:  ").split()))
# a = list(map(int,input("too:  ").split()))
# print(merge_sort(a+n))


# task 7
# def merge_sort(n):
#     if len(n)<=1:
#         return n
#     mid = len(n)//2
#     left = n[:mid]
#     right = n[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)

#     r = []
#     i = 0
#     j = 0
#     while i<len(left) and j<len(right):
#         if left[i]<=right[j]:
#             r.append(left[i])
#             i+=1
#         else:
#             r.append(right[j])
#             j+=1
#     while i<len(left):
#         r.append(left[i])
#         i+=1
#     while j<len(right):
#         r.append(right[j])
#         j+=1
#     return r
# n = list(map(int,input("too:  ").split()))
# b = merge_sort(n)
# print(b[0:3])

# task 8
# def merge_sort(n):
#     if len(n)<=1:
#         return n
#     mid = len(n)//2
#     left = n[:mid]
#     right = n[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)

#     r = []
#     count = 0
#     i = 0
#     j = 0
#     while i<len(left) and j<len(right):
#         if left[i]<=right[j]:
#             r.append(left[i])
#             i+=1
#             count+=1
#         else:
#             r.append(right[j])
#             j+=1
#     while i<len(left):
#         r.append(left[i])
#         i+=1
#     while j<len(right):
#         r.append(right[j])
#         j+=1
#     return r
# n = list(map(int,input("too:  ").split()))
# print(count)

# task9
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] >= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# def largest_two(arr):
#     arr = merge_sort(arr)
#     return arr[:2]
# print(largest_two([4, 15, 9, 23, 6, 11]))
# print(largest_two([7, 7, 3]))

# task10
# def merge_sort(names):
#     if len(names) <= 1:
#         return names
#     mid = len(names) // 2
#     left = merge_sort(names[:mid])
#     right = merge_sort(names[mid:])
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# names = ["Болд", "Анар", "Дорж", "Батаа", "Гэрэл"]
# print(merge_sort(names))

# task11
# def merge_sort(students):
#     if len(students) <= 1:
#         return students
#     mid = len(students) // 2
#     left = merge_sort(students[:mid])
#     right = merge_sort(students[mid:])
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i][1] > right[j][1]:
#             result.append(left[i])
#             i += 1
#         elif left[i][1] < right[j][1]:
#             result.append(right[j])
#             j += 1
#         else:
#             if left[i][0] <= right[j][0]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# students = [
#     ("Анар", 85),
#     ("Дорж", 92),
#     ("Сараа", 78),
#     ("Болд", 92),
#     ("Гэрэл", 88)
# ]
# print(merge_sort(students))

# task12
# def merge_sort(words):
#     if len(words) <= 1:
#         return words
#     mid = len(words) // 2
#     left = merge_sort(words[:mid])
#     right = merge_sort(words[mid:])
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if len(left[i]) < len(right[j]):
#             result.append(left[i])
#             i += 1
#         elif len(left[i]) > len(right[j]):
#             result.append(right[j])
#             j += 1
#         else:
#             if left[i] <= right[j]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# print(merge_sort(["алим", "ус", "банана", "аарц", "тараг", "цай"]))
# print(merge_sort(["ccc", "a", "bb", "b"]))

# task13
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# def binary_search(arr, target):
#     arr = merge_sort(arr)
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# print(binary_search([42, 7, 19, 3, 25, 11], 19))
# print(binary_search([42, 7, 19, 3, 25, 11], 20))

# task14
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# def is_anagram(word1, word2):
#     letters1 = merge_sort(list(word1))
#     letters2 = merge_sort(list(word2))
#     if letters1 == letters2:
#         return True
#     else:
#         return False
# print(is_anagram("нас", "сан"))
# print(is_anagram("ном", "мод"))
# print(is_anagram("listen", "silent"))

# task15
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# def closest_pair(arr):
#     arr = merge_sort(arr)
#     min_diff = arr[1] - arr[0]
#     pair = (arr[0], arr[1])
#     for i in range(len(arr) - 1):
#         diff = arr[i + 1] - arr[i]
#         if diff < min_diff:
#             min_diff = diff
#             pair = (arr[i], arr[i + 1])
#     return pair, min_diff
# print(closest_pair([15, 3, 22, 8, 10, 30]))
# print(closest_pair([9, 1, 5, 3]))
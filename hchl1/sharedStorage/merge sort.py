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

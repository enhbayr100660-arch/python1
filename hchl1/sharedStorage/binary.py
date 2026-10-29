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




# bubble sort:
# number = [5,3,2,1,8]
# for i in range (len(number)-1):
#     for j in range(len(number)-1-i):
#         if number[j]>number[j+1]:
#             temp = number[j]
#             number[j]=number[j+1]
#             number[j+1]=temp
# print(number)

# task 1
# number = list(map(int,input("too:  ").split()))
# for i in range (len(number)-1):
#     for j in range(len(number)-1-i):
#         if number[j]>number[j+1]:
#             temp = number[j]
#             number[j]=number[j+1]
#             number[j+1]=temp
# print(number)

#task 3
# n = list(map(int,input("too:  ").split())) 
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j]<n[j+1]: 
#             a = n[j]
#             n[j] = n[j+1]  
#             n[j+1]=a  
# print(n)


# task 4
# n = list(map(int,input("too:  ").split())) 
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j]>n[j+1]: 
#             a = n[j]
#             n[j] = n[j+1]  
#             n[j+1]=a  
# print(n)


# task 5
# n= list(map(int,input("too:  ").split())) 
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j]>n[j+1]: 
#             a = n[j]
#             n[j] = n[j+1]  
#             n[j+1]=a  
# print(n,end=",")


# task 6
# n = list(map(str,input("ners:  ").split()))
# for i in range (len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j]>n[j+1]:
#             a = n[j]
#             n[j] = n[j+1]
#             n[j+1]=a
# print(n)

# task 7
# onoo = list(map(int,input("onoo:  ").split()))
# for i in range(len(onoo)-1):
#     for j in range(len(onoo)-1-i):
#         if onoo[j]>onoo[j+1]:
#             a = onoo[j]
#             onoo[j]=onoo[j+1]
#             onoo[j+1]=a
# print(onoo)

# task 8
# n = list(map(int,input("too:  ").split()))
# for i in range (len(n)-1):
#     if n[i]>n[i+1]:
#         a = n[i]
#         n[i]=n[i+1]
#         n[i+1]=a
# print(n)


# task 9
# count = 0
# n = list(map(int,input("too:  ").split()))
# for i in range(len(n)-1):
#     count+=1
#     for j in range (len(n)-1-i):
#         if n[j]>n[j+1]:
#             a = n[j]
#             n[j]=n[j+1]
#             n[j+1]=a
# print(f"toirog:  {count}\n{n}")

            
# task 10
# count = 0
# n = list(map(int,input("too:  ").split()))
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j]>n[j+1]:
#             count+=1
#             a = n[j]
#             n[j]=n[j+1]
#             n[j+1]=a
# print(count)

# task 11
# n = [12, 5, 20, 8, 15]
# for i in range (len(n)-1):
#     if n[i]>n[i+1]:
#         a = n[i]
#         n[i]=n[i+1]
#         n[i+1]=a
# print(n[-2])

# task 12
# n = [4, -3, 0, -1, 7, -8, 2]
# for i in range (len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j]>n[j+1]:
#             a = n[j]
#             n[j] = n[j+1]
#             n[j+1]=a
# print(n)

# task 13
# n = list(map(int,input("too:  ").split()))
# for i in range (len(n)-1):
#     if n[i]>n[i+1]:
#         a = n[i]
#         n[i]=n[i+1]
#         n[i+1]=a
#         print(n)

# task 14

# n = list(map(int,input("too:  ").split()))
# swapped = False
# for i in range (len(n)-1):
#     for j in range(len(n)-1-i):

#         if n[j]>n[j+1]:
#             a = n[j]
#             n[j] = n[j+1]
#             n[j+1]=a
#             swapped = True
# if swapped == False:
#     print("eremblegdesen")
# else:
#     print("eremblegvi bna")
# print(n)


# task 15

# n = list(map(int,input("too:  ").split()))
# round_count = 0
# for i in range (len(n)-1):
#         swapped = False
#         round_count+=1
#         for j in range(len(n)-1-i):

#             if n[j]>n[j+1]:
#                 a = n[j]
#                 n[j] = n[j+1]
#                 n[j+1]=a
#                 swapped = True
#         if swapped == False:  
#             break
# else:
#     print("eremblegvi bna") 

# print(round_count)


# task 16
# students=[]
# n = int(input("heden suragch: "))
# for s in range(n):
#     b = input("ner:  ")
#     c = int(input("too:  "))
#     students.append([b, c])
# for i in range(len(students)-1):
#         for j in range(len(students)-1-i):
#             if students[j][1]>students[j+1][1]:
#                 a = students[j]
#                 students[j]=students[j+1]
#                 students[j+1]=a
# print(students[-1][0])

# task 17

# students = []
# n = int(input("heden too:"))
# for i in range(n):
#     b = input("ner: ")
#     c = int(input("nas: "))
#     students.append([b,c])
# for x in range(len(students)-1):                        
#     for j in range(len(students)-1-x):
#         if students[j][0]>students[j+1][0]:
#             a = students[j]
#             students[j]= students[j+1]
#             students[j+1]= a
# print(students)
# print(students)

# Selection Sort — 15 бодлого:
# n = [4,6,5,3,1,2]
# for i in range(len(n)-1):
#     min_idx = i

#     for j in range(i+1,len(n)):
#         if n[j]<n[min_idx]:
#             min_idx=j

#     t = n[i]
#     n[i]= n[min_idx]
#     n[min_idx]=t

# print(n)


# task 1
# n = list(map(int,input("too: ").split()))
# for i in range(len(n)-1):
#     min_indx = i
#     for j in range(i+1,len(n)):
#         if n[j]<n[min_indx]:
#             min_indx = j
#     t = n[i]
#     n[i]=n[min_indx]
#     n[min_indx]=t
# print(n)


# task 2
# n = list(map(int,input("too:  ").split()))
# for i in range(3):
#     min_indx = i
#     for j in range(i+1,len(n)):
#         if n[j]<n[min_indx]:
#             min_indx = j
#     a = n[i]
#     n[i]= n[min_indx]
#     n[min_indx]=a
# print(n)

# task 3
# n = list(map(int,input("too:  ").split()))
# for i in range(len(n)-1):
#     min_indx = i
#     for j in range(i+1,len(n)):
#         if n[j]>n[min_indx]:
#             min_indx = j
#     a = n[i]
#     n[i]= n[min_indx]
#     n[min_indx]=a
# print(n)

# task 4
# arr = [3, -2, 7, -5, 1]
# for i in range(len(arr)-1):
#     min_indx = i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[min_indx]:
#             min_indx = j
#     t = arr[i]
#     arr[i]=arr[min_indx]
#     arr[min_indx]=t
# print(arr)            

# task 5 
# arr = [4, 2, 4, 1, 2, 3]
# for i in range(len(arr)-1):
#     min_indx = i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[min_indx]:
#             min_indx = j
#     t = arr[i]
#     arr[i]=arr[min_indx]
#     arr[min_indx]=t
# print(set(arr))            


# task 6
# arr = [8, 5, 3, 9, 2]
# for i in range(1):
#     min_indx = i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[min_indx]:
#             min_indx = j
#     t = arr[i]
#     arr[i]=arr[min_indx]
#     arr[min_indx]=t
    

# print(arr)            


# task 7
# arr = [7, 4, 9, 2, 5]
# for i in range(len(arr)-1):
#     min_indx = i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[min_indx]:
#             min_indx = j
#     t = arr[0]
#     arr[0]=arr[min_indx]
#     arr[min_indx]=t
# print(arr)

# task 8
# arr = [6, 3, 8, 1, 5]
# for i in range(2):
#     min_indx = i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[min_indx]:
#             min_indx = j
#     t = arr[i]
#     arr[i]=arr[min_indx]
#     arr[min_indx]=t
#     print(arr)

# task 9
# arr = [4, 1, 3, 2]
# count = 0
# for i in range(len(arr)-1):
#     min_indx = i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[min_indx]:
#             min_indx = j
#     if min_indx != i:

#         t = arr[i]
#         arr[i]=arr[min_indx]
#         arr[min_indx]=t
#         count+=1
# print(count)

# task 10
# def ff(arr):
#     for i in range(len(arr)-1):
#         if arr[i]>arr[i+1]:
#             return False
#     return True
# a = [2, 4, 1, 5, 3]
# b = [1, 2, 3, 4, 5]
# c = [3, 1, 2, 5, 4]

# print("a:",ff(a))
# print("b:",ff(b))
# print("c:",ff(c))


# task 11
# def arr(n):
#     for i in range(len(n)-1):
#         min_indx = i
#         for j in range(i+1,len(n)):
#             if n[j]<n[min_indx]:
#                 min_indx = j
    
#         t = n[i]
#         n[i]=n[min_indx]
#         n[min_indx]=t
#     return n
# n = list(map(int,input("too: ").split()))
# print(arr(n))

# task 12
# def arr(n):
#     for i in range(len(n)-1):
#         min_indx = i
#         for j in range(i+1,len(n)):
#             if n[j]>n[min_indx]:
#                 min_indx = j
    
#         t = n[i]
#         n[i]=n[min_indx]
#         n[min_indx]=t
#     return n
# n = list(map(int,input("too: ").split()))
# print(arr(n))

# task 13

# arr = list(map(int,input("too: ").split()))
# for i in range(len(arr)-1):
#     min_index = i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[min_index]:
#             min_index = j
#     t = arr[i]
#     arr[i]=arr[min_index]
#     arr[min_index]=t
# print(arr[0])

# task 14
# arr = [5, 3, 4, 1, 2]
# for i in range(len(arr)-1):
#     min_indx = i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[min_indx]:
#             min_indx = j
#     t = arr[i]
#     arr[i]=arr[min_indx]
#     arr[min_indx]=t
#     print(arr)

# # task 15
# n = list(map(int,input("bubble sort:  ").split()))
# for i in range (len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j]>n[j+1]:
#             a = n[j]
#             n[j] = n[j+1]
#             n[j+1]=a
# arr = list(map(int,input("Selection Sort:  ").split()))
# for i in range(len(arr)-1):
#     min_indx = i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[min_indx]:
#             min_indx = j
#     t = arr[i]
#     arr[i]=arr[min_indx]
#     arr[min_indx]=t
# if n == arr:
#     print("vr dvn adil")
# else:
#     print("vr dvn oor")



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


# Stack ба Queue
# 1.b
# 2.a
# 3.c
# 4.d
# 5.a
# 6.b
# 7.d
# 8.c
# 9.d
# 10.d
# 11.a
# 12.c
# 13.b
# 14.d
# 15.a
# 16.c
# 17.d
# 18.b
# 19.a
# 20.b
# 21.b
# 22.a
# 23.b
# 24.c
# 24.c
# 25.d
# 26.a
# 27.c
# 28.d
# 29.b
# 30.c

# task 
# 1.a
# 2.b
# 3.d
# 4.d
# 5.d
# 6.a
# 7.a
# 8.c
# 9.b
# 10.d
# 11.a
# 12.d
# 13.d
# 14.b
# 15.c
# 16.a
# 17.c
# 18.a
# 19.c
# 20.a


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = [8, 3, 1, 7, 0, 10, 2]

# print(quick_sort(numbers))

# task 1
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = list(map(int,input("too: ").split()))
# print(quick_sort(numbers))

# task 2
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num >pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = list(map(int,input("too: ").split()))
# print(quick_sort(numbers))


# task 3
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num <pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = list(map(int,input("too: ").split()))
# print(quick_sort(numbers))


# task 4
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num <pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = list(map(int,input("too: ").split()))
# print(quick_sort(numbers))

# task 5
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num <pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = list(map(int,input("too: ").split()))
# quick_sort(numbers)
# print(quick_sort(numbers)[0:3])



# task 6
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num >pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = list(map(int,input("too: ").split()))
# print(quick_sort(numbers)[0:3])


# task 7
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num[1] <pivot[1]:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers  =  [("Bat", 85), ("Bold", 70), ("Saraa", 95), ("Anu", 60)]
# print(quick_sort(numbers))


# task 8
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if len(num) <len(pivot):
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers  = "banana", "cat", "apple", "hi", "dog"
# print(quick_sort(numbers))


# task 9
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    for num in arr:
        if num <pivot:
            left.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            right.append(num)

    return quick_sort(left) + middle + quick_sort(right)


numbers  = [7, 1, 5, 3, 9]
quick_sort(numbers)
n = len(quick_sort)//2
print(n)


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

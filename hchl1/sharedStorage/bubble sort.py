
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



# task18
# nums= list(map (int, input().split()))
# count= 0
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1-i):
#         if nums[j]> nums[j+1]:
#             t=nums[j]
#             nums[j]= nums[j+1]
#             nums[j+1] = t
#         if j==4:
#             count+=1
# print(nums, count)

# task19
# pro = [
#     ["Mouse", 25000],
#     ["Keyboard", 65000],
#     ["USB", 12000],
#     ["Headphone", 80000]
# ]
# for i in range(len(pro)):
#     for j in range(len(pro) - 1 - i):
#         if pro[j][1] < pro[j + 1][1]:
#             pro[j], pro[j + 1] = pro[j + 1], pro[j]
# for i in range(3):
#     print(pro[i][0], pro[i][1])

# task20
# nums = [7, 3, 5, 1, 6, 2, 4]
# n = len(nums)
# c = 0
# swap = 0
# toirog = 0
# for i in range(n - 1):
#     toirog += 1
#     for j in range(n - 1 - i):
#         c += 1
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
#             swap += 1
# print("Haritsuulalt:", c)
# print("soliltsoo:", swap)
# print("gadna toirog:", toirog)
# print("etses:", nums)

# task21
# nums= list(map (int, input().split()))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1-i):
#         if nums[j]> nums[j+1]:
#             t=nums[j]
#             nums[j]= nums[j+1]
#               nums[j+1] = t
# print(nums)
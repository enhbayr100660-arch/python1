# 1
# 
# # a = input("neree oruul : ")
# print("saainuu",a)
# 1


# 2

# a = int(input())
# b = int(input())
# print(a + b)

# 3

# a = float(input())
# a=a*2
# print(a)

# 4

# a = input()
# print(type(a))
# print(type(int(a)))

# 5

# a = input()
# print(len(a))




# a = input()
# print(a[0])
# print(a[-1])


# 7


# a = int(input())
# for i in range(1,a +1):
#     print(i)

# 8


# a = input().split()

# numbers = []

# for i in a:
#     numbers.append(int(i))

# print(sum(numbers))

# 9


# a = list(map(int,input().split()))
# print(max(a),min(a))

# 10


# a = input().split()
# b = 0
# c = 0
# for i in a:
#     b+=int(i)
#     c+=1
# d = b/c
# print(d)


# 11


# a = ["cat", "dog"]
# a.append("tiger")
# print(a)

# 12


# a = ["cat","tiger"]
# a.insert(1,"dog")
# print(a)

# 13


# a = input().split()
# ner = input()
# a.remove(ner)
# print(a)
# 14


# n = input("ners: ").split()
# n.pop(1)
# print(*n)

# 15

# a = list(map(int,input().split()))
# a.sort()
# print(a)
# a.reverse()
# print(a)

# 16

# a = list(map(int,input().split()))
# a.reverse()
# print(a)


# 17
# n = input()
# print(f"[{n.strip()}]")
# print(f"[{n.lstrip()}]")
# print(f"[{n.rstrip()}]")

# 18
# a = input().split()
# print(len(a))
# 19
# a = "BANana"
# a.lower()
# print(a.count("a"))
# text = "banana"
# print(text.count("a"))



# 20
# a = input()
# b = input()

# x = a.find(b)
# print(x)

# if x != -1:
#     print(a.index(b))
# else:
#     print("Олдсонгүй")


# 21
# a = input().split()
# for i in a:
#     if i.startswith("report"):
#         i.endswith(".pdf")
#         print(i)
# if i ==0:
#     print("oldohgui")


# 22
# a = input()
# b = input()
# c = input()
# print(a.replace(b,c))


# 23
# a = input().lower().split()
# name = input().lower()
# if name in a:
#     print("yes")
# else:
#     print("no")



# 24
# a = input()
# print(a[:3])
# print(a[-3:])


# 25
# a = input().strip().lower()
# print(a[::-1])
# if a==a:
#     print("yes")
# else:
#     print("no")


# 26
# a = input().split()
# print(len(a))


# 27
# a = [10,20,30]
# print(a[:-1])  

# a = (10,20,30)
# b,c,d = a
# print(b,c,d)

# a = (10,20,30)
# b,*c = a
# print(b,c)



# 26#########
# a = list(map(input("ug").split()))
# a.len(a)


1
# a = tuple(map(str,input().split()))
# print(a)


2
# a = tuple(map(str,input().split()))
# print(f"{a[0]}\n{a[1]}")


# 3

# a = (100,)
# print(type(a))



# 4

# a  = tuple(map(str,input("to").split()))
# print(f"{a[0]}\n{a[2]}\n{a[-1]}")

# 5


# a = (10,20,30,40,50)
# print(a[0:3])

# 6


# a = (10,20,30,40,50,)
# print(a[2:5])

# 7


# a = ("alim","banana","jirj","usan uzem")
# print(len(a))

# 8


# a = (45,12,89,23,7)
# print(max(a))
# print(min(a))
# 9



# a =(80,90,70,100)
# print(f"niilber:{sum(a)}\ndundaj:{sum(a)/len(a)}")


# 10


# a = (50,10,40,20,30)
# print(sorted(a))
# 11


# a = (10,20,10,30,10,40)
# b = 10

# print(f"{a.count(b)}")


# 12


# a = (tuple(map(str,input("too").split())))
# print(a.index("jurj"))    


# 13


# a = tuple(input().split())
# b = input()
# if b in a:
#     print("baina")
# else:
#     print("baihgu")

# 14


# student = ("anu,12,7a")
# name  = input()
# classroom = input()
# angi = input()
# name += classroom
# classroom += angi
# angi = student
# print("student")

# student = ("anu","12","7a") 
# name, age, student_class = student
# print(f"{name}\n{age}\n {student_class}")


# 15

# a = tuple(map(int,input().split()))
# x,y =a
# print(f"x = {x}\n y = {y}")

# 16

# a  = ("python surah","bat",250)
# name, zohiolch, huudas = a
# print(f" ner: {name} \n nom:  {zohiolch} \n huudas: {huudas}")



# 17
# a, b = tuple(map(int, input("too: ").split()))
# a, b = b, a
# print(a, 


# 18
# a,b = tuple(map(int,input("oruul").split()))
# print(f"")

# 19


# a = (10,20,30,40,50)
# print(a[0:1])
# print(a[1:5]) 

# a = tuple(map(int,input("toogoo").split()))
# first, *middle, last = a
# print(f"{first}\n {middle}\n{last}")



# # 20
# a = (tuple(input().split()))
# b,*c=a
# print(f"name : {b}\n hiceel : {c}")

# b = "niit"
# a = tuple(map(str,input("ugee").split()))
# name, price, quantity  = a
# print(f"name : {name}\nprice : {price}\nquantity{quantity}")

# 21


# a = tuple(map(str,input("ugee").split()))
# name, price, quantity = a
# price=int(price)
# quantity=int(quantity)
# total = price * quantity
# print(f"baraa{name}")
# print(f"negj une{price}")
# print(f"too{quantity}")
# print(f"niit une{total}")

# 22

# # students  (
#     ("Ану", 90),
#     ("Бат", 75),
#     ("Сараа", 100)
# )

# for name,score in students:
#     print(f"{name} : {score}")


# 23
# score = 0
# students = (
#     ("Ану", 90),
#     ("Бат", 75),
#     ("Сараа", 100)
# )
# for name, score in students:
#     if score >=80:
#         print(name)



# # 24
# a = tuple(input().split())
# b = input()
# c = list(a)
# c.append(b)
# d = tuple(c)
# print(d)



# a = {"bat", "bold", "saraa",}
# b = {"bat "}





 
# a = {"name" : "temuulen", 
#      "age" : 24,
#      "phone" : 99110082
#     }
# a["age"] = "er" 
# print(a)

# Гурвалжин
# a = map(int,input("3n too:").split())
# print(sum(a))

# 2 тооны нийлбэр
# a,b = map(int,input("2 too:").split())
# c = a+b
# print(c)

# Куб
# a = int(input("too:"))
# b = 5*5*5
# c = b+5*5
# print(b,c)

# Тэгш өнцөгт
# a,b = map(int,input("2 too:").split())
# c = a+b
# v = c*2
# x = a*b
# print(v,x)

# Функц 1
# a = int(input("too:"))
# y=3*a-5
# print(y)

# Функц 2
# x = int(input("too:"))
# y=4*x**2-3*x+5
# print(y)

# Сүүлийн цифр
# a = int(input("too:"))
# b = a%100
# c = b%10
# print(c)

# Аравтын орны цифр
# a = int(input("too:"))
# b = a%100
# c = b//10
# print(c)

# 2 оронтой тоо
# a = int(input("too:"))
# b = a%100
# c = b%10
# v = b//10
# x = c*v
# print(x)

# 3 оронтой тоо
# a= int(input("too:"))
# b = a%100
# c = b%10
# v = b//10
# x = v//10
# z = v+c+x
# print(z)

# Минут секунд
# a = int(input("sec:"))
# b = a//60
# c = a%60
# print(b,c)

# Цаг минут секунд
# a = int(input("sec:"))
# b = a//3600
# c = b//60
# d = a%3600
# print(b,c,d)

# Минут секунд -> секунд
# a,b = map(int,input("2 too:").split())
# c = a*60
# v = c+b
# print(v)

# Хоног цаг
# a = int(input("tsag:"))
# b = a//24
# c = a%24
# print(b,c)

# Хоног цаг -> цаг
# a,b = map(int,input("2 too:").split())
# c = a*24
# v = c+b
# print(v)

# Жил сар
# a = int(input("tsag:"))
# b = a//12
# c = a%12
# print(b,c)


# Жил сар -> сар
# a,b = map(int,input("2 too:").split())
# c = a*12
# x = c+b
# print(x)

# Хоёр тооны их
# a,b = map(int,input("2 too:").split())
# a=[a,b]
# print(max(a))

# Хоёр тооны бага
# a,b = map(int,input("2 too:").split())
# a=[a,b]
# print(min(a))

# 3 тооны их
# a,b,c = map(int,input("2 too:").split())
# n=[a,b,c]
# print(max(n))

# 4 тооны бага
# a = list(map(int,input("2 too:").split()))

# print(min(a))

# Нийлбэр 80:
# b = []
# a = list(map(int,input("too:").split()))
# for i in a:
#   if i > 80:
#         b.append(i)
# print(sum(b))

# Үржвэр:
# a = list(map(int,input("too:").split()))
# b = 1
# for i in a:
#     if i<5:
        
#         b*=i
# print(b)

# Тэгш тоонуудын нийлбэр:

# a = list(map(int,input("too:").split()))
# b = 0
# for i in a:
#     if i%2==0:
#         b = i+b
# print(b)


# Сондгой тоонуудын үржвэр:
# a = list(map(int,input("too:").split()))
# b = 1
# for i in a:
#     if i%2!=0:
#         b = i*b
# print(b)

# Тэнцүү 5:
# a = list(map(int,input("too").split()))
# print(a.count(5))

# 3-д хуваагдах:
# a = list(map(int,input("too").split()))
# count = 0
# for i in a:
#     if i %3 == 0:
#         count+=1
# print(count)

# 11-д хуваагддаггүй:
# a = list(map(int,input("too").split()))
# count = 0
# for i in a:
#     if i %11 != 0:
#         count+=i
#         count==count
# print(count)

# 10-аас их:
# a = int(input("too:"))
# if a>=10:
#     print("yes")
# else:
#     print("no")

# 5-аас бага:
# a = int(input("too:"))
# if a<=5:
#     print("yes")
# else:
#     print("no")

# Тэгш тоонууд YES NO:
# a =list (map(int,input("too:").split()))
# b = 0
# for i in a:
#     if i%2 ==0:
#         i+=b
#     print("yes")
# else:
#     print("no")

# IOI:
# print("I0I")

# IOI 3 удаа:
# for i in range(3):
#     print("IOI")
# n = int(input("heden udaa:"))
# for i in range(n):
#     print("IoI")

# Эхний n тооны нийлбэр:
# total = 0
# n = int(input("too:"))
# for i in range(1,n+1):
#     total+=i
# print(total)

# n!:
# total = 1
# n = int(input("too:"))
# for i in range(1,n+1):
#     total*=i
# print(total)

# 100-г n удаа нэм:
# n = int(input("too:"))
# a = n*100
# print(a)

# a тоог n удаа нэм:
# a,b = map(int,input("too:").split())
# z = a*b
# print(z)

# 2-ын n зэрэг:
# a = int(input("too:"))
# b = 2**a
# print(b)

# Тэнцсэн, унасан:
# a = int(input("dvn:"))
# if a<3:
#     print("unsan")
# else:
#     print("tentssen")

#  5-аас онц руу:
# a = int(input("dvn:"))
# if a>=5:
#     print("onts")
# elif a>=4:
#     print("sain")
# elif a>=3:
#     print("dund")
# else:
#     print("muu")

# Тоон үнэлгээнээс үсгэнд:
# a = int(input("too:"))
# if a<=100:
#     if a<=89:
#         print("A")
#     elif a<=79:
#         print("B")
#     elif a>69:
#         print("C")
#     elif a<59:
#         print("D")
#     else:
#         print("F")

# Гараг:
# udur = int(input("udur:"))
# if  udur == 1:
#     print("Monday")
# elif udur==2:
#     print("Tuesday")
# elif udur == 3:
#     print("Wednesday")
# elif 4==udur:
#     print("Thursday")
# elif 5==udur:
#     print("Friday")
# elif 6==udur:
#     print("Saturday")
# elif udur==7:
#     print("sunday")

# Улирал:
# a = int(input("sar:"))
# if a==12 or a==1 or a==2:
#     print("Winter")
# elif a == 3 or a==4 or a==5:
#     print("Spring")
# elif a==6 or a==7 or a==8:
#     print("Summer")
# elif a==9 or a==10 or a==11:
#     print("Autumn")


# Гурвалжин эсэх:

# a,b,c = map(int,input("too:").split())
# if a+b>c:
#     print("yes")
# else:
#     print("no")

# Тооны хүрд:
# n = int(input("too:"))
# total = 1
# i = 1
# while i<=10:
    
#     print(n,"*", total*i,"=",n* total*i)
#     i+=1

# Тооны зэр
# a = [1,2,3] 
# a.insert(0,6)
# print(a)
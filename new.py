# print("Hello world")

# a=10
# b=13
# print("The sum is:",a+b)
# c=a+b
# print(c);print(a)

# # n=input("What is you name\n")
# n = input();

# print("Your name is",n)


# print("Enter the cost\n")
# c = input()

# d= int(c)

# ans = 0.9*d

# print("The cost after the discount is",ans)


# ans = 0
# for j in range(100):
#     ans = ans + j
# print(ans)


# n = input("enter the table to be printed\n")
# n= int(n)

# for i in range(11):
#     print(n,"X",i,"=",n*i)


# c = input("Enter a number")
# c= int(c)
# print(c*5)

# print( ‘Hello’ )

# print( “ ‘Hello’ “ )

# print( “ “Hello” ” )






# print( ' hello' )

# print(""HEllo"")

# print(" ' hello ' ")




# for i in range(3,30,3):
#     print(i)

# c=30
# a=4
# print(c/a)
# print(c//a)
# b=3
# c = b**3
# print(c)

# c=input()
# print(type(c))

# c=10
# b=20
# e=c>b
# print(e)


# n=int(input())
# print(n*n)

# n = int(input("enter the number"))

# d= n
# print(d*0.85)



# print("fkewjibyfwyd2232323232h")


# r = input("enter your number")

# print(r)

# x = ("100+2")  
# # This is a input to take numbrs
# print(x)

# print("123" + "abc")


# x=3


# x=x+2


# x = x+1




 

# i = input()
# print("Hello ",i)



# a = int(input("Enter the first number\n"))
# b = int(input("Enter the second number\n"))

# print("The sum of both the number is:",a+b)

# mystr = "Rohan is an good boy"
# print(mystr[0:4])


# n = int(input())
# m = int(input())
# print(n*m)


# n,m = input().split()
# print(m*n)

# x, y = input().split()

# x = int(x)
# y= int(y)
# print(x*y)

# a = input().split()
# print(abs(int(max(a))-int(min(a))),end="")

# d = {"Name":"Rakesh","USN":"1NT19CS145"}
# print(d["Name"],d["USN"])





# Exercise 1 #

# d = {"pig":"It's an animal","restoration":"The action of returning something to it's original condition","highway":"A main road, Espically the one connecting two main cities","neighbour":"A person living next door","lung":"It's an part of the body"}

# print("Welcome to a mini dictionary")
# print("Enter any one word from these 5 words to know their meaning")
# print("1.pig")
# print("2.restoration")
# print("3.highway")
# print("4.neighbour")
# print("5.lung")
# i = input()
# print(d[i])





# Conditional statements

# v1 = 5
# v2 = int(input())

# if v1>v2:
#     print("Smaller")

# elif v1==v2:
#     print("Equal")

# else:
#     print("Greater")



# l = [2,4,1,5,8,7]

# print("Enter a number to check if it is persent in the list")
# l1 = int(input())

# if l1 in l:
#     print("Yes,it is present in the list")

# elif l1 not in l:
#     print("No,it is not present in the list")



# l = [31,0,31,30,31,30,31,31,30,31,30,31]
# a=1900

# if(a%4==0 and a%100!=0 or a%400==0):
#     l.insert(1,29)

# else:
#     l.insert(1,28)

# print("In the year 1900,february had",l[1],"days")





# n = int(input())
# fact = 1
  
# for i in range(1,n+1):
#     fact = fact * i
      
# # print ("The factorial of 23 is : ",end="")
# print (fact)







# l = []
# print("Enter the size of the list\n")
# n = int(input())
# c= 0 

# for i in range(0,n):
#     ele = int(input())
#     l.append(ele)

# print(l)

# for i in range(0,n):
#     if (i%3==0) or (i%5==0):
#         c= c+1

# print("The number of multiples of 3 or 5 are",c) 








# list1 = [["make",1],["bake",2],["take",3],["fake",4]]

# for i,j in list1:
#     print(j,i)






# list11 = [int,float,"name","place","animal","thing",4,5,3,5,3,2,5,5,55,33,21,67,1,2,3,2,1,4,5,6,55]

# list11.append(6)

# for x in list11:
#     if str(x).isnumeric() and x>=6:
#         print(x)










#Quiz

# i = 0

# while(True):
#     print("Enter a number")
#     i = int(input())

#     if i<=100 :
#         continue

#     else:
#         print("Congo!!, You broke the barrier")
#         break












#Finding the number game

# u=0
# while(True):
#     n=18
#     print("Enter a number")
#     i = int(input())


#     if i<n:
#         print("lesser")
#         u= u+1
#         continue

#     if i>n:
#         print("greater")
#         u = u+1
#         continue

#     if i==n:
#         u = u+1
#         print("You found the number in",u,"number of tries")
#         break













# x=5
# print(x)
# x += 7
# print(x)


# a= True
# b= False

# print(a and a)
# print(a and b)
# print(b and a)
# print(b and b)

# print("\n")

# print(a or a)
# print(a or b)
# print(b or a)
# print(b or b)




# def function2(a,b):
#     """This is a function which gives the sum of two numbers"""
#     res = a+b
#     return res


# v = function2(3,9)
# print(function2.__doc__)
# print(v)









#Exception handling
# n1 = input()
# n2 = input()

# try:
#     print("The sum of the numbers is",int(n1)+int(n2))

# except Exception as e:
#     print(e)


# print("This is after the exception handling")







#Files











#moudles

# import random

# r_no = random.randint(0,12)
# print(r_no)

# lst = ["one","two","three","four","five"]

# for x in range(0,7):
#     choice = random.choice(lst)
#     print(choice)


# from PyDictionary import PyDictionary
# dictionary=PyDictionary()
# x=input("Enter the word you want to search\n")
# print(dictionary.meaning(x))











#Stone,Paper,Scissor game

# import random 
# lst = ['t','p','s']


# hp=0
# cp=0
# chances= 0
# left=10

# print("Welcome to the stone paper scissor game")
# name = input("enter your name: ")

# print("Enter t for stone\n enter p for paper\n and enter s scissor")


# while chances<left:
#     inp=input("enter your choice: ")
#     ran = random.choice(lst)


#     if inp == ran:
#         print("You both got tied")

#     elif inp=="t" and ran=="s":
#         hp = hp+1
#         print(name + " choose stone and the computer choose scissor")
#         print("You won!!")
    

#     elif inp=="t" and ran=="p":
#         cp = cp+1
#         print(name + " choose stone and the computer choose paper")
#         print("You loose")


#     elif inp=="p" and ran=="t":
#         hp = hp+1
#         print(name + " choose paper and the computer choose stone")
#         print("You won!!")

#     elif inp=="p" and ran=="s":
#         cp = cp+1
#         print(name + " choose paper and the computer choose scissor")
#         print("You lose")

#     elif inp=="s" and ran=="p":
#         hp = hp+1
#         print(name + " choose scissor and the computer choose paper")
#         print("you won!!")

#     elif inp=="s" and ran=="t":
#         cp = cp+1
#         print(name + " choose scissor and the computer choose stone")
#         print("You lose")

#     else:
#         print("wrong input")

    
#     chances = chances+1



# print("Game over!")


# # print(name + "points" + hp)

# # print("computer point" + cp)


# print(f" {name} points {hp} ")

# print(f"Computer points {cp}")

# if hp==cp:
#     print("You both got tied")


# elif hp>cp:
#     print(name + " wins!")


# elif cp>hp:
#     print("Computer wins!!")










# def functionargs(*args):
#     for x  in args:
#         print(x)

# def functionnorm(no,*noargs):
#     print(no)

#     for i in noargs:
#         print(i)

# hr=["Name","colour","city","anilmal"]

# functionargs(*hr)

# normal = "This is an normal string"
# functionnorm(normal,*hr)




















# object oriented programming #


# class student:
#     pass

# harry = student()
# larry = student()

# harry.name="This is my name"

# larry.name="This is my name Larry"

# harry.age=20

# print( harry.name,"\n",larry.name,"\n" ,harry.age)










# class student:
#     no_of_leaves=9
#     pass


# hr=student()
# vr=student()

# hr.name="Name"
# vr.name="my name is virtual reality"

# hr.age=20
# vr.age=10

# print(vr.name)
# # print(vr)

# print(student.__dict__)

# print("Before the creation of the instance variable")
# print(hr.no_of_leaves)
# print(vr.no_of_leaves)

# vr.no_of_leaves=10

# print("After the creation of the instance variable")

# print(hr.no_of_leaves)
# print(vr.no_of_leaves)








# class Student:
#     year:3

#     def __init__(self,aname,arole,ayear):
#         self.name=aname
#         self.role=arole
#         self.year=ayear


    

#     def printd(selfq):
#         return f"The name is {selfq.name} and the role is {selfq.role}"

#     @staticmethod
#     def printff(string):
#         print("passed string is" + string)  
    

# # name1 = Student()

# # name1.name="This is my name"
# # name1.role = "My role is an Instructor"


# name2 = Student("Rakesh","Student",4)

# print(name2.printd())

# print(name2.role)

# Student.printff(" passed string")

# # print(name1.printd())






# Single inheritance

# class Employee:

#     def __init__(self,aname,asal,arole):
#         self.name=aname
#         self.sal = asal
#         self.role = arole

#     def pfemp(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.sal} and the role of the employee is {self.role}")
        


# class Programmer(Employee):
#     def __init__(self,aname,asal,arole,alang):
#         self.name = aname
#         self.sal = asal
#         self.role = arole
#         self.lang = alang

#     def pfprog(self):
#         print(f"{self.name} is an {self.role} with the knowledge of {self.lang} and gets paid {self.sal}")


# harry = Employee("Harry",555,"Manager")
# larry = Programmer("Larry",444,"Programmer",["python","C++","C","Java"])
# harry.pfemp()
# larry.pfemp()
# larry.pfprog()







# multiple inheritance

# class Employee:

#     def __init__(self,aname,asal,arole):
#         self.name=aname
#         self.sal = asal
#         self.role = arole

#     def pfemp(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.sal} and the role of the employee is {self.role}")
        

# class Programmer(Employee):
#     def __init__(self,aname,asal,arole,alang):
#         self.name = aname
#         self.sal = asal
#         self.role = arole
#         self.lang = alang

#     def pfprog(self):
#         print(f"{self.name} is an {self.role} with the knowledge of {self.lang} and gets paid {self.sal}")

# class player:
#     game = "cricket"
    
#     def __inti__(self,name,game):
#         self.name = name
#         self.game = game

#     def printd(self):
#         print(f" This is the name {self.name} and the game he plays is {self.game}")


# class coolprog (Employee,player):
#     # def printd(self):
#     #     print(f"{self.name} is an cool employee, and he plays {self.game} ")
#     pass

# karan = coolprog ("Karan",65656,"Cool programmer")
# karan.printd()







# mulitlevel inheritance

# class Dad:
#     basketball = 1

# class Son(Dad):
#     dance = 1

#     def canhe(self):
#         print(f"Yes he can dance {self.dance} number of times")

# class Gson(Son):
#     dance = 6

#     def canhe(self):
#         print(f"Yes he can dance {self.dance} number of times")



# daddy = Dad()

# son = Son()

# child = Gson()

# child.canhe()
# son.canhe()
# res = child.basketball
# print(res)






# exercise for multilevel inheritance

# class Electroinc_device:
    
    
#     def needspower(self):
#         return "YESS"

#     def pocketable(self):
#         return "NOO"

#     def camultitask(self):
#         return "Can't do that"




# class Pocket_device(Electroinc_device):
    

#     def pocketable(self):
#         return "YESS"

#     def camultitask(self):
#         return "Nahh"





# class Mobile(Pocket_device):

#     def camultitask(self):
#         return "YEAH!!!"



# radio = Electroinc_device()

# pager = Pocket_device()

# mobilee = Mobile()


# print("Status of power requirement / Not")

# print(f" Radio-->{radio.needspower()}")
# print(f" Pager-->{pager.needspower()}")
# print(f" Mobile phone-->{mobilee.needspower()}")



# print("Status of pocketable / Not")

# print(f" Radio--> {radio.pocketable()}")
# print(f" Pager--> {pager.pocketable()}")
# print(f" Mobile phone--> {mobilee.pocketable()}")



# print("Status of Multitasking / Not")

# print(f" Radio--> {radio.camultitask()}")
# print(f" Pager--> {pager.camultitask()}")
# print(f" Mobile phone--> {mobilee.camultitask()}")



class one:
    vara = "I'm the variable of class one"

    def __init__(self):
        self.var1 = "Im the varibale of the init func"
        self.vara = "I'm the instance variable of the variable vara"
        self.sp = "special"


class two(one):
    varb = "I'm the varibale of the class two"

    def __init__(self):
        # super().__init__()
        self.var2 = "Im the variable of the class two init func"
        self.varb = "I'm the instance variable of the varible varb"




a = one()
b = two()

print(a.vara)
print(b.vara)
print(b.sp)
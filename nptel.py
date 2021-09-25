# dict1={
#     "ID":"0121",
#     "Name":"zzz"
# }

# dict2={
#     "Name":"ZZZ"
# }

# dict2.update({"ID":"0121"})

# if(dict1==dict2):
#     print("They are equal")

# else:
#     print("Not equal")


# dictA={
#     "name":"Joy",
#     "Length":"12 weeks",
#     "Language":"Python"
# }

# dictB={

# }

# dictB.update(dictA)

# for x,y in dictB.items():
#     print(x,y)




#try 1
# ar = input().split()
# k=int(input())
# an=[]
# for i in ar:
#   an.append(int(i))
# an.sort()
# print(an[k-1],end="")












#try 2
# ar = input().split()
# k=int(input())
# ans=[]
# for i in ar:
#   ans.append(int(i))
# ans.sort(reverse=True)
# #print(*ans)
# print(ans[k-1],end="")






# import random
# a=[1,2,3,4,5,6]
# s=0
# for i in range (0,2):
#     s=s+random.choice(a)
# print(s)




# a=["1","2","3","4","5"]
# f=len
# print(f(a))


# import string
# s="hello, and welcome to joy of computing course"
# print(s[::2].replace("e","l"))



# week 6 quiz 1

# a,b=input().split()
# a,b=int(a),int(b)
# c=1

# for i in range(1,a+1):
#     for j in range (1,b+1):
#         if j!=b:
#             print(c,"",end="")
#         else:
#             print(c,end="")
#         c+=1
#     if i!=a:
#         print("")
#     else:
#         print("",end="")





# quiz 2
# n=int(input())

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     if i!=n:
#         print("")
#     else:
#         print("",end="")





#assignment 3
# n=int(input())
# mat=[]
# f=0
# for i in range(n):
#     mat.append(input().split())
# for a in range(len(mat)):
#     for b in range (n):
#         if mat[a][b]!=mat[b][a]:
#             f=1
# if f==0:
#     print("Yes",end="")
# else:
#     print("No",end="")





#turtle drawing

# import turtle
# tr = turtle.Turtle()
# turtle.pencolor("green")

# for i in range (9):
    
#     tr.forward(90)
#     tr.left(45)





#Lottery simulation

# import random
# # import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt

# acc=0
# x=[]
# y=[]

# for i in range(365):
#     x.append(i+1)
#     num=random.randint(1,10)
#     gues=random.randint(1,10)

#     print(f"Random number {num}")
#     print(f"Gussed number {gues}")

#     if num==gues:
#         acc=acc+900

#     else:
#         acc=acc-100
    
#     y.append(acc)
    
#     print(f"the amount left after the round is {acc}")

# plt.plot(x,y)
# plt.show()














# import random
# import matplotlib.pyplot as plt

# acc=0
# x=[]
# y=[]

# for i in range(365):
#     x.append(i+1)
#     num=random.randint(1,10)
#     gus=random.randint(1,10)


#     print(f"The random number is {num}")
#     print(f"The random guess is {gus}")

#     if num==gus:
#         acc=acc+900

#     else:
#         acc=acc-100

#     print(f"The money left after the round is {acc}")
#     y.append(acc)

# plt.plot(x,y)
# plt.show()












# form pil import Image

# img  = Image.open('demo-image.jpg')

# t_img = img.transpose(Image.FLIP_LEFT_RIGHT)

# t_img.save("corrected_img.jpg")

# print("Process completed")





# t=(1,2,3)
# (a,b,c)=t
# print(a,b,c)


# import random
# i = random.randint(1,100)

# if(i%3==0):
#     print(i)


# import matplotlib.pyplot as plt
# x=[]
# y=[]

# for i in range(1,11):
#     x.append(i)
#     y.append(i)

# x.reverse()
# print(x)
# print(y)
# plt.plot(y,x)
# plt.show()


# a=input()
# if(a==a[::-1]):
#     print("True")
# else:
#     print("False")
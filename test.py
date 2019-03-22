# a=[
#     'a,1',
#     'b,3,22',
#     'c,3,4',
# ]
# b=[
#     'a,2',
#     'b,1',
#     'd,5',
# ]
# a_dic = {}
# for i in a:
#     k,v = i.split(",",1)
#     a_dic[k] = v
#
# b_dic = {}
# for i in b:
#     k,v = i.split(",",1)
#     b_dic[k] = v
# c_dic = a_dic
#
# for k,v in b_dic.items():
#
#     if k in c_dic:
#         c_dic[k] = ",".join([c_dic[k],v])
#     c_dic[k] = v
#
# c=[','.join([k,c_dic[k]]) for k in c_dic]
# print(c)


# A=[1,2,3,[4,1,['j1',1,[1,2,3,'aa']]]]
# def lis(arg):
#     for i in arg:
#         if type(i) == list:
#             lis(i)
#         else:
#             print(i)
#
# lis(A)


a = range(10)
print(a[::-3])
#
#
# lst = [1,2,4,8,16,32,64,128,256,512,1024,32769,65536,4294967296]
#
# dic = {}
# for i in lst:
#     len_i = len(str(i))
#     dic.setdefault(len_i,[]).append(i)
#
#     # if len(i) == 1:j
#     #     dic[len(i)] = i
# print(dic)
#
# lst2 = []
# lst =[[1,2,3],[4,5,6],[7,8,9]]
# for i in lst:
#     print(i)
#     lst2.extend(i)
# print(lst2)

# a = [7,-8,5,4,0,-2,-5]
# c = sorted(a,key=lambda x:(x<0,abs(x)))
# print(c)
# import copy
# a=[1,2,3,[4,5],6]
# b=a
# c=copy.copy(a)
# d=copy.deepcopy(a)
# b.append(10)
# c[3].append(11)
# d[3].append(12)
# print(a)
# print(b)
# print(c)
# print(d)

import urllib.request as request
a = request.urlopen("https://www.cnblogs.com/huangbiquan/p/8030298.html").read().decode('utf-8')
# print(a)


d={'a':30,'g':17,'b':25,'c':18,'d':50,'e':36,'f':57,'h':25}
# for i in d.values():
#     print(i)
#
# ll = sorted(d.items(),key=lambda x:x[1])
# print(ll)


# list1=[1,2,3,5,8,7,11,10]
# list2=[5,15,25,10]
#
# l1 = [i for i in list1 if i in list2]
# print(l1)
#
# l2 = [i for i in list2+list1 if i not in l1]
# print(l2)


# import random
# a = random.sample(range(100),10)
# print(a)

# lis=['This','is','a','Man','B','!']
# a = list(map(str.lower,lis))
# print(a)

dict = {'Alice': '12', 'Beth': '34', 'Cecil': '56'}
a = ["12","24"]


# lis = [2,4,5,6,7]
# for i in lis:
#     if i % 2==0:
#         lis.remove(i)
# print(lis)
# a = [3,1,-4,-2]
# b = sorted(a,key=lambda x:(abs(x)))
#
# c = list(reversed(sorted(a,key=lambda x:(abs(x)))))
# print(c)


# lis=[3,1,-4,-2]
# a = len(lis)
# print(a)
# lis=sorted(lis,key=lambda x:abs(x))
# print(lis)

#
# l= list(range(100))
# print(l)
# print(l[:3])
# print(l[-10::])
#
# s = "1"
# if isinstance(s,str):
#     print("aaa")
# else:
#     print("sss")

# a = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
# print(a)


# for i in  range(5,0,-1):
#     print(i)

# x = "sss"
# y = 2
# print(x+y)

# k = {"1":1,"2":2}
# v = k
# k["1"] = 5
# print(v)


# print(type(1 + 2L * 3.14))
#
# k = 1000
# while k> 1:
#     print(k)
#     k = k / 2

# 2 = k
# print(type(k))

# a = ["a","b","c"]
# b = map(str,a)
# print(b)

#
# import os
# os.path
# with open("aaa.txt","r",encoding="utf-8") as f:
#     for i in f:
#         print(i,end="")


# s = "sadadasdczxczcfad"
a = ["A","b","c"]
# a.append([1,2,3])
# s = "".join(a)
# if "a" in a:
#     print("aaaa")
# else:
#     print("111")
# print(type(1/2))
# print(type(s))

#
# a = "aaabbccd"
# aa = ""
# print(set(a))
# for i in sorted(list(set(a)),key=a.index):
#     # print(i)
#     aa=aa+i+str(a.count(i))
# print(aa)

#
#
# a =5
# print(abs(5))

li = []

for i in range(3):
    def func(x,y=i):
        print(x*y)
    li.append(func)

for  func in li:
    func(2)





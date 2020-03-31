import sys
#
# a = 10
# b = '''system
#     1
#     2
#     success'''
#
# #print("values are ",a,b)
#
# tup1 = ('a','b',100, 'a')
# # print(tup1.count('a'))
# # print(tup1.index(100))
# # print(len(tup1))
# # how to find elelemt at index 0
#
# lis1 = ['a','b',100, 'a']
# lis2 = []
# print(lis1.count('a'))
# lis2.append('a')
# lis2.append('c')
# lis2.append('d')
# #lis2[1]='b' # not allowed
# lis2.insert(1,'b')
# lis2.insert(5,'b')
# lis2.append(100)
# lis2.append('a')
# lis2.append('ab')
# print(lis2)
# print(lis2.pop()) # last element is popped off
# print(lis2.pop(2)) # second index element is popped off
# print(lis2.remove(100))
# print(lis2.sort(reverse=True))
# print(lis2)

Dic1 = {
    "Name":"Sree",
    "Address": {
        "Line1" : "8 Donald Preston Dr",
        "Line2" : "Preserve at Lafayette",
        "State" : "DE",
        "Zip" : 19702
    },
    "Tech" : ["Pyhon","AWS","Spark"],
    "Distance" : "within 25 miles"
}

# print(Dic1["Name"])
# print(Dic1["Address"])
# print(Dic1["Tech"][0])
#print(Dic1["Address"]["Line1"]["Line2"])

# print(Dic1)
# print(Dic1.get('Tech'))
# print(Dic1.keys())
# print(Dic1.values())
# Dic1.update({"Tech" : ["Python", "AWS", "Spark", "ETL"]})
# # did not work Dic1['Close to public transport'] : 'Y'
# Dic1.pop("Distance")
# print(Dic1)

techset = set()
techset = {'AWS EMR','Spark','Python','PySpark'}
techset1 = {'AWS EMR','Spark','Python','PySpark','Unix','c#'}
# print(techset.pop())
# print(techset.add("ETL"))
# final_techset= tech.union(tech1)
# diff_techset = tech.difference(tech1)  # did not work
# inter_techset = tech.intersection(tech1)
# print(final_techset)
# print(diff_techset)
# print(inter_techset)

var1 = 10
var2 = 20
var3 = 30

# if (var2 > var1 and var3 > var1 and var2 > var3):
#     print('var2 is greater than var3 and var1')
# elif (var2 > var1 and var3 > var1 and var3 > var2):
#     print('var3 is greater than var2 and var1')
#
# mylist = list()\
# for i in range(1,5):
#     mylist.append(i)
#     print(mylist)

# mytuple = (1,2,3,4)
# print(type(mytuple))
# mylist = list(mytuple)
# print(type(mylist))
#
# mylist1=[1,2,3,4]
# print(type(mylist1))
# mytuple1=tuple(mylist1)
# print(type(mytuple1))

# mylist = ['This', 'is', 'Python', 'class']
# print(type(mylist))
# mystr=' '.join(mylist)
# mystr=str(mylist)
# print(type(mystr))
# print(mystr)

#str to list
# mystr = 'This is Pyspark class'
# print(type(mystr))
# mylist = list(mystr)
# mylist = list(mystr.split(' '))
# print(type(mylist))
# print(mylist)

#file = open('C:/Users/Sreec/DataScience/Data/african_crises.csv','r')
# print(file.read())
# file.close()
#print(file.readline())

#write to a file
strinput = "this is line 1"
with open('C:/Users/Sreec/DataScience/Data/test.txt','w') as file:
    file.write(strinput)
strinput = "this is line 2"
with open('C:/Users/Sreec/DataScience/Data/test.txt','a') as file:
    file.write(strinput)
strinput = "this is line 3"
with open('C:/Users/Sreec/DataScience/Data/test.txt','w') as file:
    file.write(strinput)

import os
os.remove('C:/Users/Sreec/DataScience/Data/test.txt')













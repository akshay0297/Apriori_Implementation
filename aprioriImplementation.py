import  math
import sys
import csv

def gen_c(L , l):
    C = {}
    temp = []
    for i in L:
        temp.append(list(i))
    print("Set : " , temp)
    for i in range(0 , len(temp)-1):
        for j in range(i+1 , len(temp)):
            flag = 1
            for k in range(0 , len(temp[i]) -1 ):
                if temp[i][k] != temp[j][k]:
                    flag = 0

            if flag == 1:
                item = []
                for k in range(0 , len(temp[i])):
                    item.append(temp[i][k])
                item.append(temp[j][len(temp[i])-1])

                C[tuple(item)] = 0

    for i in C:
        count = 0
        for ite in l:
            for j in i:
                flag = 0
                for k in ite:
                    if j == k:
                        flag = 1
                        break
                if flag == 0:
                    break
            if flag == 1:
                count = count + 1
        C[i] = count
    return (C)


def gen_fis(C , ms):
    L = {}
    for i in C:
        if C[i] >= ms:
            L[i] = C[i] 
    return(L)

print ("1.Open Transaction Database File \n2.Generate Candidate Set \n3.Generate Frequent Item Set \n4.Exit")
print("Enter CSV file name :" , end = " ")
fame = input()
print("Enter min_sup =  " , end = "")
ms = int(input())

print("Enter Choice :" , end = " ")
ch = int(input())

f_obj = open(fame)
r = csv.reader(f_obj)

li = []
ld = {}

for row in r:
    li.append(row)
if ch == 1 :
    for row in r :
        print(" ".join(row))
print("Items Are  :: " , li)
for i in li:
    for j in i:
        if j not in ld :
            ld[j] = 1
        else:
           ld[j] += 1
d = {}
for key in sorted(ld.keys()):
    d[key] = ld[key]
print("Items With Count are :: " , d)

k = {}

if ch == 2:
   l = gen_fis(d , ms)
   while len(l) != 0:
       k =  gen_c(l,li)
       l = gen_fis( k , ms )
       print("Items Generated Are :: " , k)

lf = {}
if ch == 3:
    l = gen_fis(d , ms)
    p = 1
    print("Frequent Itemset 1 Generated is ::" , l)
    while len(l) != 0 :
        p += 1
        k =  gen_c(l,li)
        l = gen_fis(k , ms)
        print("Frequent Itemset " + str(p) + "  Generated are :: "  , l)
        
if ch == 4:
    exit(0)


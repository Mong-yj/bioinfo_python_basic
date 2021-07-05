#! /usr/bin/env python
"""
# dictionary 
d_dict = {
        'a_str':'Apple!',
        'b_list':[1,2,3,4],
        'c_tuple':('a','b','c'),
        'e_dict':{1:'one',2:'two'}
        }
print('d_dict:',d_dict)
print('d_dicta:',d_dict['a_str'])
print('d_dictb:',d_dict['b_list'])
print('d_dictb[0]:',d_dict['b_list'][0])
print('d_dictb[1]:',d_dict['b_list'][1])
print('d_dictc:',d_dict['c_tuple'])
print('d_dictb:',d_dict['e_dict'])
print('d_dictb:',d_dict['e_dict'][2])

# set
print(set([1,2,3,2,5,5,2,3,4,1,7,5,3,1,2]))
my_set = {'a','b','c'}
print(my_set)

a = {2,4,6,8,10,12}
b = {3,6,9,12}
print('a:',a, 'b:',b)
print(a | b)
print(set.union(a,b))
print(a & b)
print(set.intersection(a,b))
print(a^b)
print(set.symmetric_difference(a,b))
print(a-b)
print(set.difference(a,b))

a |= {100}
print(a)
a.update({200})
print(a)
a.add(1000)
print(a)
a.remove(200)
print(a)

# Boolean
print(True, False)

print(bool('aa'))
print( 1<10 )

# example1
ex1 = 'We tried list and we tried dicts also we tried Zen'
l_ex1 = ex1.split()
d_output = {}
for i in list(set(l_ex1)):
    d_output[i] = l_ex1.count(i)
for i,j in d_output.items():
    print(i,j)
 
# input
my_var1 = input("var1: ")
my_var2 = input("var2: ")
my_var3 = input("var3: ")
print(my_var1)
print(my_var2)
print(my_var3)

# condition
condition=True

if condition == True:
    print('condition: True')
elif condition == False:
    print('condition: False')
else:
    print('condition: ???')
print("I'm Free~~\n")

var1 = input("var1: ")
if var1 == '1':
    print('var1 is 1!')
else:
    raise Exception('var is not 1')
print('Good bye~\n')

# example 2
num0 = 5
num1 = 7
if num0 > num1:
    print(num0)
else:
    print(num1)

print(num1) if num0<num1 else print(num0)

fruit = 'apple'
if fruit == 'peach':
    print('peach')
if fruit == 'apple':
    print('apple')
else:
    print('else~~~')

# example 3
score = input("Write your score: ")
if score.isdigit():
    score = int(score)
else:
    print("score is not numeric")
    import sys
    sys.exit()

if (score <= 100) and (score >=90):
    print('A')
elif (score < 90) and (score >= 80):
    print('B')
elif (score < 80) and (score >= 70):
    print('C')
elif (score < 70) and (score >= 60):
    print('D')
elif score < 60:
    print('F')
else:
    print('Incorrect score')

# example 4
money = '10 USD, 5 EUR, 7 JPY, 9 CNY'
d_value = { 'USD':1203.82,
            'EUR':1365.73,
            'JPY':11.22,
            'CNY':172.04 }

money = money.split(', ')
out1 = str(round(int(money[0][:-3])*d_value[money[0][-3:]],2))
out2 = str(int(money[1][:-3])*d_value[money[1][-3:]])
out3 = str(int(money[2][:-3])*d_value[money[2][-3:]])
out4 = str(int(money[3][:-3])*d_value[money[3][-3:]])
out_money = ' KRW, '.join([out1,out2,out3,out4])+' KRW'
print(out_money)

for i in range(len(money)):
    i_split = money[i].split()
    if i != (len(money)-1):
        print(round(int(i_split[0])*d_value[i_split[1]],2),"KRW",end=', ')
    else:
        print(round(int(i_split[0])*d_value[i_split[1]],2),"KRW")
"""
""" nonononono!!!!
for i in money:
    if i[-3:]=='USD':
       print(int(i[:-3])*1203.82,"KRW",end=', ')
    elif i[-3:]=='EUR':
        print(int(i[:-3])*1365.73,"KRW",end=', ')
    elif i[-3:]=='JPY':
        print(int(i[:-3])*11.22,"KRW",end=', ')
    elif i[-3:]=='CNY':
        print(int(i[:-3])*172.04,"KRW",end=', ')
print('\n')
"""

# while
i = 1
while i < 11:
    print('loop test : while. ' + str(i))
    i+=1

i = 40
while 1:
    print('loop test : while. ' + str(i))
    i+=1
    if i > 50:
        break
i = 40
while 1:
    print('loop test : while. ' + str(i))
    if i > 50:
        break
    i+=1

# example 5
i = 1
while i < 7:
    print("*"*i)
    i+=1 

i=0
star=''
while 1:
    print(star)
    star += "*"
    i+=1
    if 7 < i:
        break

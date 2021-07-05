#! /usr/bin/env python
"""
fruit='apple'
print(fruit)
print("fruit[1] = ", fruit[1])
print("fruit[3] = ", fruit[3])
print("fruit[:3] = ", fruit[:3])

# example1
A = 'red apple'
B = 'yellow banana'
print(B[:7]+A[4:])
print(A[:4]+B[7:])
print("-" * 50)

# example2
ex = "HumptyDumptysatonawallHumptyDu\
mptyhadagreatfallAlltheKingshorsesa\
ndalltheKingsmenCouldntputHumpty\
Dumptyinhisplaceagaing"
print(ex[22:28],ex[97:103])
print(ex[22:28]+' '+ex[97:103])
print(ex[22:28],end=' ')
print(ex[97:103])
print("-" * 50)

# string formatting
cutApple=1
print("There are %d apples." %cutApple)
cutApple=2
print("There are %d apples." %cutApple)
cutApple=3
print("There are %d apples." %cutApple)
cutApple=4
print("There are %d apples." %cutApple)
print("-" * 30)

fruit='apples'
print("There are %s from %s tree."%(fruit,fruit))
fruit='peachs'
print("There are %s from %s tree."%(fruit,fruit))
fruit='plum'
print("There are %s from %s tree."%(fruit,fruit))

print("-" * 30)
cnt=1
print('There are {} apples.'.format(cnt))
cnt='one'
print('There are {} {}.'.format(cnt,'peaches'))
print("-" * 50)

# string function
fruit = 'apple'
print('apple.count(p):',fruit.count('p'))
print('apple.find(p):',fruit.find('p'))
print('apple.find(k):',fruit.find('k'))
print('apple.index(p):',fruit.index('p'))
#print('apple.index(k):',fruit.index('k')) error!!
print('"".join(p):', "_".join('apple'))
print('Apple:','Apple'.upper())
print('Apple:','Apple'.lower())
print('  apple  .lstrip():','  apple  '.lstrip())
print('  apple  .rstrip():','  apple  '.rstrip())
print('  apple  .strip():','  apple  '.strip())
print('"apple from apple tree".replace("apple","peach"):\n',
"apple from apple tree".replace("apple","peach"))
print('"apple from apple tree".split(" "):\n',
"apple from apple tree".split(" "))
print("-" * 30)

# example3
CMA = "1,234,567"
print(int(CMA.replace(",",""))+100)

# exmaple4
DNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
print("Count:",DNA.count("A"),DNA.count("C"),DNA.count("G"),DNA.count("T"))
DNA2 = "GATGGAACTTGACTACGTAAATT"
print("Transcription:",DNA2.replace("T","U"))

print("-" * 50)
# list
one2three = [1,2,3]
print(one2three)
strlist = ['string','list']
print(strlist)

l_test = [1,2,3,'apple',' ']
print(l_test[1:4])
print(l_test[-1:])
l_test2 = ['a','b','c']
print(l_test+l_test2)

list_list = [1,2,['one','two','three',4]]
print(list_list)
print(list_list[1:])
print(list_list[2][1:3])
print(list_list[-1][1])
print(list_list[::-1])

num=[10,9,8,7,6,5,4,3,2,1,0]
print(num[::-1])
print(num[::-2])
print(num[-2:-6:-2])

num = [0,1,2,3]
print(num)
num[2]=5
print(num)

l_num=[0,1,2,3]
print(l_num)
l_num.append(4)
print(l_num)
l_num.remove(2)
print(l_num)

l_num=[0,1,2,3,5,4]
l_num.sort()
print(l_num)
l_num.reverse()
print(l_num)
print(l_num.index(2))
print(l_num.pop())
print(l_num.pop())
print(l_num.pop())
print(l_num)

l_num=[0,1,2,3,5,4]
l_num.insert(2,'a')
print(l_num)
print(l_num.pop(2))
print(l_num)

l_num=[1,1,2,1,1,3,4,4]
print(l_num.count(1))
l_num.extend([1,2,3])
print(l_num)

num=[1,2,3,4]
print(num)
num[1]=6
print(num)
del num[2:]
print(num)

num.append(3)
print('append 3 : ',num)
num.append([1,2])
print('append [1,2] : ',num)
num.remove([1,2])
print(num)
num.sort()
print(num)
num.reverse()
print(num)

num=[1,3,6,7]
print(num)
print(num.index(3))
num.insert(0,0)
num.insert(3,2)
print(num)
print(num.pop(0))
print(num.pop(0))
print(num.pop(0))
print(num)

print(num.pop(0))
print(num)


# example5
lang0 = ['Python','JAVA']
lang1 = ["C","C++","VB"]
totalLang = lang0+lang1
print(totalLang)
print("-" * 50)

# tuple
t_num=(1,2,3,'a')
print(t_num[0])
print(t_num[0:3])
#t_num[1]=5   error
#print(t_num)
print("-" * 50)

# dictionary
d_table={'fruit':'apple','color':'red','dia':10}
print(d_table)
d_table['color']='orange'
print(d_table)
d_table['price']=1000
print(d_table)

print(d_table.keys())
print(list(d_table.keys()))
print(d_table.values())
print(d_table.items())
print(list(d_table.items())[0][0])
print(list(d_table.items())[0][1])

print(d_table.get('color'))
print(d_table['color'])
print('price' in d_table)
d_table.clear()
print(d_table)
print("-" * 30)
"""

# example6
reg_num0 = '951213-0000000'
reg_num1 = '960125-0000000'
reg_num2 = '970705-0000000'
d_month = {'01':'Jan','02':'Feb','03':'Mar','04':'Apr',
'05':'May','06':'Jun','07':'Jul','08':'Aug','09':'sept',
'10':'Oct','11':'Nov','12':'Dec'}

date0 = d_month[reg_num0[2:4]]+'-'+reg_num0[4:6]
date1 = d_month[reg_num1[2:4]]+'-'+reg_num1[4:6]
date2 = d_month[reg_num2[2:4]]+'-'+reg_num2[4:6]
print("reg_num0:",date0)
print("reg_num1:",date1)
print("reg_num2:",date2)

#print("reg_num0:"+d_month[reg_num0[2:4]]+'-'+reg_num0[4:6])
#print("reg_num1:"+d_month[reg_num1[2:4]]+'-'+reg_num1[4:6])
#print("reg_num2:"+d_month[reg_num2[2:4]]+'-'+reg_num2[4:6])



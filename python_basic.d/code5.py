#! /usr/bin/env python
"""
chicken = 10

def count_chicken(people):
    chicken = 20
    chicken -= people
    print(chicken, "chicken remained.")

def count_chicken_global(people):
    global chicken
    chicken -= people
    print(chicken, "chicken remained.")

print('chicken:',chicken) #전역변수
count_chicken(5) #지역변수 사용
print('chicken:',chicken) #전역변수
print()
print('chicken:',chicken) #전역변수 사용
count_chicken_global(5) #전역변수 변경됨

FILE = open('./test_file.txt', 'r') #read
print(FILE.read(), end='')
FILE.close()

FILE = open('./test_file.txt', 'r') #read
print(FILE.readline())
print(FILE.readline())
print(FILE.readline())
FILE.close()

FILE = open('./test_file.txt', 'r') #read
for i in FILE.readlines():
    print(i.strip())
FILE.close()

FILE = open('./write_file.txt', 'w') #write
FILE.write('hello\n')
FILE.close()

FILE = open('./write_file.txt', 'a') #write
FILE.write('append\n')
FILE.close()

with open('./test_file.txt','r') as FI:
    for i in FI.readlines():
        print(i.strip())
    print('with out! Bye!')

import pickle
l_list = [1,3,5,7]
d_dict = {'a':'A','b':'B',1:3,2:4}

FO = open('./pi_test','wb')
pickle.dump(l_list, FO)
pickle.dump(d_dict, FO)
FO.close()

FI = open('./pi_test','rb')
l_list = pickle.load(FI)
d_dict = pickle.load(FI)
FI.close()

print(l_list)
print(d_dict)

# class
class Person:
    nation = 'A nation'

    def greeting(self):
        print('(method)greeting:','Hi')
    
    def hi1(self):
        self.greeting()
    
    def hi2(self):
        greeting()

def greeting():
    print('(function)greeting:','Hello!')

me = Person()
me.greeting()
print()
me.hi1()
me.hi2()

class Person:
    def __init__(self, in_nation):
        self.nation = in_nation
    def show_nation(self):
        print(self.nation)

me = Person('Korea')
me1 = Person('AAA')
me.show_nation()
me1.show_nation()

class Cat:
    def __init__(self):
        self.sleepy = True
    def snack(self):
        print('myeo~')

class KoShort(Cat):
    def snack(self):
        print('야옹')

catcat = Cat()
catcat.snack()
print(catcat.sleepy, end = '\n\n')

minyong = KoShort()
minyong.snack()
print(minyong.sleepy)

# example 1
f = open('./test.txt','r')
test = f.readlines()
f.close()
for i in range(len(test)):
    if i % 2 != 0:
        print(test[i].strip())

# example 2

def area(inp):
    result = 2*inp*3.141592
    return result

inp = int(input())
print(area(inp))

# example 3
d_persons = {'Guillaume':'Canada','Niklas':'Germany',
            'Mark':'USA','Alex':'Swiss',
            'Alberto':'Italia'}

class Guillaume:
    nation = d_persons['Guillaume']
    def showNation(self):
        print(self.nation)

class Niklas:
    nation = d_persons['Niklas']
    def showNation(self):
        print(self.nation)

class Mark:
    nation = d_persons['Mark']
    def showNation(self):
        print(self.nation)

class Alex:
    nation = d_persons['Alex']
    def showNation(self):
        print(self.nation)

class Alberto:
    nation = d_persons['Alberto']
    def showNation(self):
        print(self.nation)

who = Alberto()
who.showNation()
# example 4
class Student:
    def __init__(self,korean,english, math):
        self.__korean = korean
        self.__english = english
        self.__math = math
    def showKorean(self):
        print('korean : %d'%self.__korean)
    def showEnglish(self):
        print('english : %d'%self.__english)
    def showMath(self):
        print('math : %d'%self.__math)
    def showEverage(self):
        avg = (self.__korean + self.__english + self.__math)/3
        print('average : {}'.format(avg))

score = Student(90,80,70)
score.showKorean()
score.showEnglish()
score.showMath()
score.showEverage()
# example 3_re
class Person:
    d_persons = {'Guillaume':'Canada','Niklas':'Germany',
                'Mark':'USA','Alex':'Swiss',
                'Alberto':'Italia'}
    def showNation(self,name):
        print(self.d_persons[name])
    def setNation(self,name,new_nation):
        self.d_persons[name]=new_nation
        print("set new nation: %s - %s"%(name, new_nation))

me = Person()
me.showNation('Alex')
me.setNation('Ryu','Korea')
"""


# example 5
class Account:
    def __init__(self,pw,balance):
        self.__password = pw
        self.__balance = balance

    def deposit(self, money):
        self.__balance += money
        print("depotsit:",self.__balance)
    def withdraw(self, money):
        self.__balance -= money
        print("withdraw:",self.__balance)
    def transfer(self, money, who):
        self.__balance -= money
        who.__balance += money
        print("my_balance :",self.__balance)
    def showBalance(self):
        print("my_balance :",self.__balance)

me = Account(1234,50000)
you = Account(1234,100000)

me.showBalance()
you.showBalance()
me.deposit(5000)
me.withdraw(5000)
me.transfer(10000,you)
you.showBalance()



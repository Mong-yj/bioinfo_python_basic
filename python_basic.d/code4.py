#! /usr/bin/env python
"""
# for
for i in [1,2,5]:
    print(i)
print("done!")

l_range = [1,2,5,3,1,7]
for i in l_range:
    if i == 1:
        print('i =',i)
    else:
        continue
    print('continue~~')

for i in range(2):
    print(i)

print(list(range(5,1,-1)))

total_sum = 0
for i in range(0,3,1):
    total_sum += 1
    print(i)

print('total_sum:',total_sum)

# example 1
in_num = input('Write number: ')

while 1:
    if not in_num.isdigit():
        print(in_num,'is not number')
        in_num = input('Write number again: ')
    elif not (2 <= int(in_num) <= 19):
        print('please input between 2 and 19')
        in_num = input('Write number again: ')
    else:
        in_num = int(in_num)
        break

for i in range(1,10):
    print(in_num*i)


# example 2
a = int(input('Write number a: '))
b = int(input('Write number b: '))
odd_sum = sum([i for i in range(a,b) if i % 2 != 0])
print(odd_sum)


# example 3
in_seq = input("Write sequence: ")
complement = {'A':'T','G':'C','T':'A','C':'G'}
comp_seq = ""
for i in in_seq:
    comp_seq += complement[i] 
rev_seq = in_seq[::-1]
if comp_seq == rev_seq:
    print(in_seq,"is palindromic.")
else:
    print(in_seq,"is not palindromic.")

# dictionary example1
ex1 = 'We tried list and we tried dicts also we tried Zen'
l_ex1 = ex1.split()
d_output = {}
for i in l_ex1:
    if i in d_output:
        continue
    else:
        d_output[i] = l_ex1.count(i)
for i,j in d_output.items():
    print(i,j)

# library
from collections import Counter
ex1 = 'We tried list and we tried dicts also we tried Zen'
l_ex_count = ex1.split()
cnt = Counter(l_ex_count)
print(cnt)

# function
def show_Hello():
    print("Hello")
    return '1'
show_Hello()
print(show_Hello())

def add(a,b):
    print('add',a,'and',b)
    print('%d + %d = '%(a,b),a+b)
    return a+b
result = add(3,4)
print('result:',result)

def hello() -> None:
    print("hello")
hello()

def add(a,b) -> int:
    return a+b
print(add(3,4))

def add(a, b=3):
    return a+b
print(add(3))

def book_0(name, age, book1, book2):
    print('name: {0} age: {1}'.format(name, age), end = ' ')
    print('book:',book1, book2)

def book_1(name, age, *books):
    print('name: {0} age: {1}'.format(name, age), end = ' ')
    print('book:', end = ' ')
    for book in books:
        print(book, end = ' ')
    print()

book_0('yune', 5, 'python','basic')
book_1('yune', 5, 'python','basic')
book_1('yune', 5, 'python','basic','photo')
#book_0('yune', 5, 'python','basic','photo') error!!!

print((lambda a,b: a+b)(3,4))
"""

# example 4
def calc(num0, num1, op):
    if op == "+":
        result = num0 + num1
    elif op == '-':
        result = num0 - num1
    elif op == "*":
        result = num0 * num1
    elif op == "/":
        result = num0/num1
    return result
print(calc(1,2,'+'))
print(calc(6,5,'*'))

# example 5
number = int(input("Write fibonacci number: "))
def fibonacci(num):
    print('n_th pivo:',num)
    l_result = [0,1]
    for i in range(2,num+1):
        result = l_result[i-2]+l_result[i-1]
        l_result.append(result)
    print(result)
    return l_result
print(fibonacci(number))

"""
# programmers ex: 소수만들기
def solution(nums):
    answer = 0
    nums = sorted(nums)
    l_val = []
    for i in range(len(nums)-2):
        for j in range(1,len(nums)-1):
            for k in range(2,len(nums)):
                values = nums[i]+nums[j]+nums[k]
                if values not in l_val:
                    l_val.append(values)
                    divisor = []
                    for v in range(1,values+1):
                        if values % v == 0:
                            divisor.append(v)
                    if len(divisor) == 2:
                        answer += 1
    return answer
aw = solution([1,2,3,4])
print(aw)
"""



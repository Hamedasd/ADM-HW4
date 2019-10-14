# ===== PROBLEM1 =====
# Exercise 1 - Introduction - Say "Hello, World!" With Python
print("Hello, World!")
# Exercise 2 - Introduction - Python If-Else
n = int(input())
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and n > 20 or n < 6: 
    print("Not Weird")
elif n % 2 == 0 and n in range (6,20):
    print("Weird")
else:
    print("Weird")
# Exercise 3 - Introduction - Arithmetic Operators
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)
# Exercise 4 - Introduction - Python: Division
a = int(input())
b = int(input())
print(a//b)
print(a/b)
# Exercise 5 - Introduction - Loops
N = int(input())
for i in range(0,N):
    print(i**2)
# Exercise 6 - Introduction - Write a function
def is_leap(year):
    leap = False
    return year%4==0 and year%100!=0 or year%400==0
# Exercise 7 - Introduction - Print Function
n = int(input())
i = 1
while i<= n: 
    print(i, end="") 
    i+=1
# Exercise 8 - Basic data types - List Comprehensions
x = int(input())   
y = int(input())
z = int(input())
n = int(input())
print([[i,j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ])
# Exercise 9 - Basic data types - Find the Runner-Up Score!
n = int(input())
s = [int(x) for x in input().split()]
if len(s)==n:
    sa=sa=(set(sorted(s)))
    sa.remove(max(sa))
    print(max(sa))
# Exercise 10 - Basic data types - Nested Lists
students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.extend([[name, score]])
    
minst = (sorted(set([b for a, b in students]))[1])
for i,j in sorted(students):
    if j == minst:
        print(i)  
# Exercise 11 - Basic data types - Finding the percentage
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

print('%.2f' %(sum(student_marks[input()])/3))
# Exercise 12 - Basic data types - Lists
lst =[]
m = int(input())
for i in range (m):
    c = input().split()
    if c[0] == "insert":
        lst.insert(int(c[1]) ,int(c[2]))    
    elif c[0] == "remove":
        lst.remove(int(c[1]))      
    elif c[0] == "reverse":
        lst.reverse()      
    elif c[0] == "append":
        lst.append(int(c[1]))
    elif c[0] == "sort":
        lst.sort()
    elif c[0] == "pop":
        lst.pop(-1)
    elif c[0] == "print":
        print(lst)    
    i +=1    
# Exercise 13 - Basic data types - Tuples
import builtins
n = int(input())
t = [int(x) for  x in input().split()]
t = tuple(t)
if len(t) == n:
     print(hash(t))
# Exercise 14 - Strings - sWAP cASE
s=input()
l=''
for i in s:
    if i.isupper ():
        l=l+i.lower()
    elif i.islower():
        l=l+i.upper()
    else:
        l=l+i
print(l)
# Exercise 15 - Strings - String Split and Join
def split_and_join(line):
    return "-".join(line.split())
# Exercise 16 - Strings - What's Your Name?
def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a,b))
# Exercise 17 - Strings - Mutations
def mutate_string(string, position, character):
    return string[:position:]+character+string[position+1:]
# Exercise 18 - Strings - Find a string
def count_substring(string, sub_string):
    count=0
    for i in range(0,len(string)):
        if string[i:len(sub_string)+i]==sub_string:
            count+=1   
    return count
# Exercise 19 - Strings - String Validators
S=input()
fun=["isalnum()", "isalpha()", "isdigit()", "islower()", "isupper()"]
for x in fun:
    print(any(eval("k."+x) for k in S))
# Exercise 20 - Strings - Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'
for i in range(0,thickness):
    print((thickness-i-1)*" " + (2*i+1)*c)

for i in range(thickness+1):
    print((thickness)//2*" " + c*thickness+(thickness*3)*" "+ c*thickness)

for i in range((thickness+1)//2):
    print((thickness)//2 *" " +c*(thickness*5))
    
for i in range(thickness+1):
    print((thickness)//2*" " + c*thickness+(thickness*3)*" "+ c*thickness)
    
for i in range(thickness-1,-1,-1):
     print((thickness*4)*" "+(thickness-i-1)*" " + (2*i+1)*c)   
        
#Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))  
      
# Exercise 21 - Strings - Text Wrap
def wrap(string, max_width):
    ss=" ".join(textwrap.wrap(string, max_width))
    return textwrap.fill(ss,max_width )
# Exercise 22 - Strings - Designer Door Mat
n, m = map(int,input().split())
k = 1
for i in range(1,n+1):
    
    if i == 1+(n-1)/2:
        print("-"*((m-len('WELCOME'))//2)+ 'WELCOME'+ "-"*((m-len('WELCOME'))//2))

        
    elif i> 1+(n-1)//2:
        k-=2
        print( "-"*((m-3*k)//2) + ".|."*k  + "-"*((m-3*k)//2))
    
    else:
        
        print("-"*((m-3*k)//2)+".|."*k + "-"*((m-3*k)//2))
        k+=2

# Exercise 23 - Strings - String Formatting
def print_formatted(number):
    
    for i in range(1,number+1):
        
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width= len(bin(n))-2))
# Exercise 24 - Strings - Alphabet Rangoli
def print_rangoli(size):
    alpa= 'abcdefghijklmnopqrstuvwxyz'
    for i in range(-size+1,size):
        t= '-'.join(alpa[size-1:abs(i):-1]+alpa[abs(i):size])
        print(t.center(4*size-3, '-'))
# Exercise 25 - Strings - Capitalize!
def solve(s):
    import string 
    return string.capwords(s,' ')
# Exercise 26 - Strings - The Minion Game
def minion_game(s):
    # your code goes here
    vw = 'AEIOU'
    stl = len(s)
    kevin = sum(stl-i for i in range(stl) if s[i] in vw)
    stuart = stl*(stl + 1)/2 - kevin

    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print( 'Kevin {}'.format(int(kevin)))
    else:
        print('Stuart {}'.format(int(stuart)))

# Exercise 27 - Strings - Merge the Tools!
def merge_the_tools(string, k):
# your code goes here
    let = list(string)
    for i in range(1,len(let)//k+1):
        w = let[k*i-k :k*i]
        d = []
        for j in w:
            if j not in d:
                d.append(j)
        print("".join(d))
# Exercise 28 - Sets - Introduction to Sets
def average(array):
    # your code goes here
    return sum(set(array))/len(set(array))
# Exercise 29 - Sets - No Idea!
n , m = map(int , input().split())
l = list(map(int , input().split()))
A = set(map(int , input().split()))
B = set(map(int , input().split()))
# temp =set(set(l)(A|B)&)
# a = set([i for i in A if i in temp])
# b = set([j for j in B if j in temp])
happiness = 0
# for elem in l:
#     happiness += elem in A
#     happiness -= elem in B
print(sum([(i in A) - (i in B) for i in l ]) )
#print(happiness)
# Exercise 30 - Sets - Symmetric Difference
a = int(input())
s = set(map(int , input().split()))
b = int(input())
d = set(map(int , input().split()))
for i in sorted((s.difference(d)| d.difference(s))):
    print(i)
# Exercise 31 - Sets - Set .add()
s= set()
for _ in range(int(input())):
    s.add(input())
print(len(s))
# Exercise 32 - Sets - Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    x = input().split()
    if x[0]=='pop':
        s.pop()
    else:
        eval('s.%s(%d)' % (x[0] , int(x[1])))
print(sum(s)) 
# Exercise 33 - Sets - Set .union() Operation
n = int(input())
e = set(map(int,input().split()))
m =int(input())
f = set(map(int,input().split()))

print(len(set(f|e)))
# Exercise 34 - Sets - Set .intersection() Operation
n = int(input())
f = set(map(int,input().split()))
m = int(input())
e = set(map(int,input().split()))

print(len(f&e))
# Exercise 35 - Sets - Set .difference() Operation
n = int(input())
e = set(map(int,input().split()))
m = int(input())
f = set(map(int,input().split()))

print(len(e.difference(f)))
# Exercise 36 - Sets - Set .symmetric_difference() Operation
n = int(input())
e = set(map(int,input().split()))
m = int(input())
f = set(map(int,input().split()))

print(len(e.symmetric_difference(f)))
# Exercise 37 - Sets - Set Mutations
n = int(input())
A = set(map(int, input().split()))

for _ in range(int(input())):
    
    x = input().split()
    y = set(map(int, input().split()))
    eval('A.%s(%s)' %(x[0] , y))
print(sum(A))

# Exercise 38 - Sets - The Captain's Room
import collections
k =int(input())
d = [int(x) for x in input().split()]
count = collections.Counter(d)
print(count.most_common()[-1][0])
# Exercise 39 - Sets - Check Subset
for _ in range(int(input())):
    int(input()); A = set(map(int, input().split()))
    int(input()); B = set(map(int, input().split()))
    print(A.issubset(B))
# Exercise 40 - Sets - Check Strict Superset
issuperset= True
superset = set(input().split())
n = int(input())
for i in range (1, n+1):
    subset = set(input().split())
    if not all(x in superset for x in subset):
        issuperset = False
    elif len(superset) <= len(subset):
        issuperset = False
print(issuperset)  
# Exercise 41 - Collections - collections.Counter()
n n = int(input())

size = list(map(int, input().split()))
amount = 0
for _ in range(int(input())):
    x = input().split()

    try:
        size.remove(int(x[0]))
        amount += int(x[1])

    except:
        pass
     
print(amount)
# Exercise 42 - Collections - DefaultDict Tutorial
from collections import defaultdict
d = defaultdict(list)

x = list(map(int, input().split()))
l = []
for i in range(1, x[0]+1):
    z =input()
    d[z].append(i)
for k in range(x[1]):
    l.append(input())

    
for j in l:
    if d[j]==[]:
        print(-1)
    else:
        print(*d[j])

# Exercise 43 - Collections - Collections.namedtuple()

from collections import namedtuple
n, marks = int(input()), input().split().index("MARKS")
print (sum([int(input().split()[marks]) for _ in range(n)]) / n)

# Exercise 44 - Collections - Collections.OrderedDict()
from collections import defaultdict
d = defaultdict(list)

x = list(map(int, input().split()))
l = []
for i in range(1, x[0]+1):
    z =input()
    d[z].append(i)
for k in range(x[1]):
    l.append(input())

    
for j in l:
    if d[j]==[]:
        print(-1)
    else:
        print(*d[j])



# Exercise 45 - Collections - Word Order
from collections import Counter
l = []
for _ in range(int(input())):
    l.append(input())

print(len(set(l)))
print(*list(Counter(l).values()))

# Exercise 46 - Collections - Collections.deque()
from collections import deque
d = deque()
for _ in range(int(input())):
    a = input().split()
    if( a[0]=='pop' or a[0]=='popleft'):
        eval('d.%s()'%(a[0]) )
    else:    
        eval('d.%s(%d)' % (a[0] , int(a[1])))
print(*list(d))
# Exercise 47 - Collections - Company Logo
# Exercise 48 - Collections - Piling Up!
# Exercise 49 - Date time - Calendar Module
import calendar
i,j ,k = [int(x) for x in input().split()]
print(calendar.day_name[calendar.weekday(k, i ,j)].upper())
# Exercise 50 - Date time - Time Delta
from datetime import datetime
for _ in range(int(input())):
    t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    print(int(abs((t1-t2).total_seconds())))
# Exercise 51 - Exceptions -

for _ in range(int(input())):
    try:
        a,b= map(int,input().split())
        print(a//b)
    except BaseException as error:
        print("Error Code:",error)

# Exercise 52 - Built-ins - Zipped!
# Exercise 53 - Built-ins - Athlete Sort
# Exercise 54 - Built-ins - Ginorts
# Exercise 55 - Map and lambda function
# Exercise 56 - Regex - Detect Floating Point Number
# Exercise 57 - Regex - Re.split()
import re
number = re.split(r'[. ,]+',input().strip('. ,'))
for i in number:
    print(i)
# Exercise 58 - Regex - Group(), Groups() & Groupdict()
import re
z= re.findall(r'([A-Za-z0-9])\1', input().strip())
print(z[0] if z else -1)
# Exercise 59 - Regex - Re.findall() & Re.finditer()
# Exercise 60 - Regex - Re.start() & Re.end()
# Exercise 61 - Regex - Regex Substitution
# Exercise 62 - Regex - Validating Roman Numerals
# Exercise 63 - Regex - Validating phone numbers
# Exercise 64 - Regex - Validating and Parsing Email Addresses
# Exercise 65 - Regex - Hex Color Code
# Exercise 66 - Regex - HTML Parser - Part 1
# Exercise 67 - Regex - HTML Parser - Part 2
# Exercise 68 - Regex - Detect HTML Tags, Attributes and Attribute Values
# Exercise 69 - Regex - Validating UID
# Exercise 70 - Regex - Validating Credit Card Numbers
# Exercise 71 - Regex - Validating Postal Codes
# Exercise 72 - Regex - Matrix Script
# Exercise 73 - Xml - XML 1 - Find the Score
# Exercise 74 - Xml - XML 2 - Find the Maximum Depth
# Exercise 75 - Closures and decorators - Standardize Mobile Number Using Decorators
# Exercise 76 - Closures and decorators - Decorators 2 - Name Directory
# Exercise 77 - Numpy - Arrays
# Exercise 78 - Numpy - Shape and Reshape
# Exercise 79 - Numpy - Transpose and Flatten
# Exercise 80 - Numpy - Concatenate
# Exercise 81 - Numpy - Zeros and Ones
# Exercise 82 - Numpy - Eye and Identity
# Exercise 83 - Numpy - Array Mathematics
# Exercise 84 - Numpy - Floor, Ceil and Rint
# Exercise 85 - Numpy - Sum and Prod
# Exercise 86 - Numpy - Min and Max
# Exercise 87 - Numpy - Mean, Var, and Std
# Exercise 88 - Numpy - Dot and Cross
# Exercise 89 - Numpy - Inner and Outer
# Exercise 90 - Numpy - Polynomials
import numpy
p = [float(x) for x in input().split()]
val = float(input())
value = numpy.polyval(p, val)
print(value)
# Exercise 91 - Numpy - Linear Algebra
import numpy
p = []
for _ in range (int(input())):
    p.extend([[float(x) for x in input().split()]])
print(numpy.linalg.det(p))
# Exercise 91 - Python Functionals - Reduce Function
cs = []  
numerator , denominator = 1,1
for _ in range (int(input())):
    i = [int(x) for x in input().split()]
    cs.extend([i])
for i, j in cs:
    numerator = numerator* i
    denominator = denominator * j
k = Fraction(numerator,denominator)    
print(k.numerator,k.denominator) 

# Exercise 92 - Python Functionals - Validating Email Addresses With a Filter
def check_email(email):
    try:   
        username, web = email.split("@")
        website, extention = web.split(".")
        valid = username.replace("_", "").replace("-", "")
        if len(extention)<= 3 and valid.isalnum() and website.isalnum():
            return email
    except:
        False

emails = []
for _ in range (int(input())):
    emails.append(input())
valid = list(filter(check_email, emails))
print(sorted(valid))
# ===== PROBLEM2 =====

# Exercise 92 - Challenges - Birthday Cake Candles
# Exercise 93 - Challenges - Kangaroo
# Exercise 94 - Challenges - Viral Advertising
# Exercise 95 - Challenges - Recursive Digit Sum
# Exercise 96 - Challenges - Insertion Sort - Part 1
# Exercise 97 - Challenges - Insertion Sort - Part 2

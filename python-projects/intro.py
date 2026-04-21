print("Hello World!")

# single line comment
'''
comment line 1
comment line 2
'''

x=10
y=1.5
z=2
x="hello"

x=100//10
print(x)
y=1.5
x=int(y)
print(x)

min_value=min(1,3)
min_value=min([4,3,5,6])
r=2**4
r=pow(2,4)
print(r)

if x>10:
    x=5
    y=100

if x>10 and y<5:
    x=0
    y=100

if x>10 or y>20:
    x=0
    y=100

if x>10:
    print("x")
elif y>10:
    print("y")
else:
    print("neither")

for i in range(5):
    print(i)

lst=[1,2,3,4,5]
for i in range(1,len(lst)):
    print(i, lst[i])

for i, num in enumerate(lst):
    print(i,num)

for value in lst:
    print(value)

count=0
while count<10:
    print(count)
    count+=1

def hello():
    print("Hello World!")
hello()

def greeting(name="buddy"):
    print("Hello",name)
greeting("Bob")
greeting()

demo="Bob's email address is"
email='bob@gmail.com'
my_string=demo+" "+email
print(my_string)

for c in demo:
    print(c)
first_char=email[0]
last_char=email[-1]
print(last_char)

if "gmail" in email:
    print("has an gmail address")
#string slicing
domain=email[4:]
username=email[:3]
print(domain)
print(username)
a=[10,20,30,40,50]
a.append(50)
a.append(5)
a.append(6)
a.append(7)
print(a)

a.remove(50)
print(a)
if 99 in a:
    a.remove(99)

a.pop()
print(a)
a.pop(2)
print(a)

a.sort()
print(a)
a.reverse()
print(a)

slice=a[2:4]
print(a,slice)

b=a
print(a,b)
b[0]=99
print(b,a)

b=a.copy()
b=a[:]
print(b[-2])

empty=[]
empty.append(5)
for val in a:
    if val>=20 and val<=100:
        empty.append(val)
print(empty)

empty=[0]*5
print(empty)
empty[0]=50
print(empty)

squares=[]
for i in range(1,10):
    squares.append(i*i)
print(squares)

squares=[x*x for x in range(1,10) if x%2==0]
print(squares)

aset=set()
aset.add(1)
aset.add(1)
aset.add(2)
aset.add(3)
aset.add(3)
print(aset)
no_dups=set([1,1,1,2,2,2,33,3,3,3])
print(no_dups)

fav_foods={'kathleen':'tacos','steve':'pizza','savannah':'fries',
           'michelle':'pasta','patrick':'ribs'}
print(fav_foods)


if 'dan' in fav_foods:
    food=fav_foods['dan']
else:
    fav_foods['dan']='brownies'

food=fav_foods.get('bob','pizza')
print(food)

for key,value in fav_foods.items():
    print(key,value)

for key in fav_foods:
    print(key)
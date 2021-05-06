import numpy
n = int(input())
a=[]
for i in range(n):
    b = list(map(float,input().split()))
    a.append(b)
c = numpy.linalg.det(a)
print(round(c,2))




# Enter your code here. Read input from STDIN. Print output to STDOUT
a=str(input())
b,c,d,e=[],[],[],[]
for i in a:
    if i.islower():
        b.append(i)
    elif i.isupper():
        c.append(i)
    elif i.isnumeric():
        if int(i)%2==0:
            d.append(i)
        else:
            e.append(i)
b.sort()
c.sort()
d.sort()
e.sort()

f="".join(b)+"".join(c)+"".join(e)+"".join(d)
print(f)
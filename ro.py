s=str(input("Enter the word: "))
x=[]
c=''
for i in s:
  if i not in c:
    c+=i
  else:
    x.append(c)
    c=''
    c+=i
x.append(c)
print(len(x))
print(x)
print(tuple(x))
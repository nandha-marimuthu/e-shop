
import pandas as pd
import numpy as np
import re
import random
o=[]
data = pd.DataFrame({'name':['nandha','tom','ram','jon','sam','robb'],"FirstWeekscore":[92,82,91,93,91,95],"SecondWeekscore":[91,81,95,93,92,96],'emailid':['nandha12@abc.com','tom34@gmail.com','ram78@gmail.com','jon21@yahoo.com','sam11@gmail.com','robb@abc.com']})

data['average'] = [(data["FirstWeekscore"][i]+data["SecondWeekscore"][i])/2  for i in range (len(data["FirstWeekscore"]))]
data['ThirdWeekscore'] = [j+3 for j in data["SecondWeekscore"] ]
print("Data after adding average and 3rd week score")
print(data)

print("Students using Gmail Domain are: ")
for i in range(len(data['emailid'])):
  x = data['emailid']
  y = data['SecondWeekscore']
  a = re.findall('@gmail.com', x[i])
  if a != []:
    c = re.split('@', x[i])
    print(c[0])
    if y[i]>90:
      o.append(data['name'][i])


print("Students using gmail domain whose  2nd week mark is <90:")
print("\n".join(o))
r = []
for i in range(6):
  n = random.randint(1,3)
  r.append(n)
data['group'] = r
print("Data after adding Group coloumn: ")
print(data)
table = pd.pivot_table(data=data, values ='FirstWeekscore',index=["group"],aggfunc = np.mean)
print("Mean of 1st week score by group:")
print(table)


    
  
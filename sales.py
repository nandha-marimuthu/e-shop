import pandas as pd
import json
from pandas.io.json import json_normalize


def appliances():
  data = pd.read_json("/Users/Nandhu/Desktop/eShop/customers/orders.json")
  o = int(input("Enter the appliance that you want to check:\n1 For Electronics\n2 For Laptops\n3 For Phones\nEnter:  "))
  if (o==1):
    a1 = "/Users/Nandhu/Desktop/eShop/stock/electronics.json"
    a = 'electronics'
  elif(o==2):
    a1 = "/Users/Nandhu/Desktop/eShop/stock/laptops.json"
    a = 'laptops'
  elif(o==3):
    a1 = "/Users/Nandhu/Desktop/eShop/stock/phones.json"
    a = 'phone'
  else:
    print('Invalid code')
  df = data.where(data['type']== a)
  print("\nNumber of orders placed: ",list(data['type']).count(a),"\nTotal number sold:",int(sum([ i  for i in df['number'] if i>0])),'\n')
  y = str(input("Do you want to check the model count(y/n):  "))
  if y == 'y':
    items(a1,a)

def items(a1,a):
  data = pd.read_json("/Users/Nandhu/Desktop/eShop/customers/orders.json")
  a_file = open(a1, "r")
  outfile = json.load(a_file)
  for i in outfile:
    x = outfile[i]
    for j in x:
      print(j['name'])
  b = str(input("\nEnter the model of appliance that you want to check: "))
  df1 = data.where(data['order']== b)
  print("\nNumber of orders placed: ",list(data['order']).count(b),"\nTotal number sold:",int(sum([ i  for i in df1['number'] if i>0])),'\n')
  
def cities():
  data = pd.read_json("/Users/Nandhu/Desktop/eShop/customers/orders.json")
  print('\nNumber of orders placed citywise: ')
  print(print(data['place'].value_counts()))

name = input('Username: ')
password = input('Password: ')

a_file = open("/Users/Nandhu/Desktop/eShop/customers/creds.json", "r")
outfile = json.load(a_file)
if name in outfile and password == outfile[name]:
  print("Welcome admin !\n")
  while True:
    n = int(input("Enter 1 for sales details\nEnter 2 for appliance wise sales details\nEnter 3 for citywise sales detail\nEnter 4 to Exit\nEnter: "))
    if n==1:
      print("\n")
      data = pd.read_json("/Users/Nandhu/Desktop/eShop/customers/orders.json")
      print(data)
      print("\n")
    elif n==2:
      appliances()
    elif n==3:
      cities()
    elif n==4:
      break
else:
  print("Invalid Username or password")
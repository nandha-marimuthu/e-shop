import json
class Eshop:

  def login(self,n,p):
    a_file = open("/Users/Nandhu/Desktop/eShop/customers/creds.json", "r")
    outfile = json.load(a_file)
    if n in outfile and p == outfile[n]:
      print('Welcome to eShop\n')
      a_file.close()
      return True
    else:
      a_file.close()
      return False
  def order(self,n):
    
    place = str(input("Enter where ar you from: "))
    o = int(input("\n1 For Electronics\n2 For Laptops\n3 For Phones\nEnter: "))
    if (o==1):
      a = "/Users/Nandhu/Desktop/eShop/stock/electronics.json"
    elif(o==2):
      a = "/Users/Nandhu/Desktop/eShop/stock/laptops.json"
    elif(o==3):
      a = "/Users/Nandhu/Desktop/eShop/stock/phones.json"
    else:
      print('Invalid code')
    a_file = open(a, "r")
    outfile = json.load(a_file)
    for i in outfile:
      c=0
      x = outfile[i]
      na=i
      print(i)
      print('------------------------------------------------------------')
      for j in x:
        print(c,'.',j['name'],'-',j['price'])
        c+=1
      print('------------------------------------------------------------')
      co=int(input('Enter id of the appliance: '))
      no=int(input('Number of item you want: '))
      o_name = outfile[na][co]['name']
      outfile[na][co]['stock']-=no
      bill = outfile[na][co]['price']*no
      off=input('Enter the offer Code: ')
      offer=['FAN50','LIGHT10','MOTOR25']
      if off in offer:
        bill-=bill/10
      else:
        print("invalid code")
      
      
      a_file = open(a, "w")
      json.dump(outfile, a_file)
      a_file.close()
      w_file = open("/Users/Nandhu/Desktop/eShop/customers/orders.json",'r')
      o_file = json.load(w_file)
      o_file["name"].append(n)
      o_file["order"].append(o_name)
      o_file["type"].append(na)
      o_file["number"].append(no)
      o_file["bill"].append(bill)
      o_file["pid"].append(o)
      o_file["place"].append(place)
      # o_file["orders"].append({
      #   "name":n,
      #   "order":o_name,
      #   "type":na,
      #   "number":no,
      #   "bill":bill,
      #   "pid":o
      # })

      w_file = open("/Users/Nandhu/Desktop/eShop/customers/orders.json" ,"w")
      json.dump(o_file,w_file)
      w_file.close()
      print(print('Item : %s  Quantity : %d  Bill : %d'%(o_name,no,bill),'\nYour order will reach you soon!'))
n = input('Username: ')
p = input('Password: ')
o = Eshop()

a = o.login(n,p)
if a==True:
  o.order(n)
else:
  print("Invalid Id and password")
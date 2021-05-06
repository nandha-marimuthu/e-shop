import json
import random
def cancel():
  n = str(input("Username: "))
  otp=random.randrange(11111,99999)
  print('Generating OTP: ',otp)
  o=int(input('Enter the OTP: '))
  if otp==o:
    w_file = open("/Users/Nandhu/Desktop/eShop/customers/orders.json" ,"r")
    a = json.load(w_file)
    x = [i for i in a["orders"] if i["name"] == n]
    a["orders"] = [i for i in a["orders"] if not (i['name'] == n)]
    w_file = open("/Users/Nandhu/Desktop/eShop/customers/orders.json" ,"w")
    json.dump(a,w_file)
    w_file.close()
    print("Order Cancelled\n")
  

    pid = x[0]['pid']
    pname = x[0]['order']
    pquan = x[0]['number']
    na = x[0]['type']

    if (pid==1):
      a = "/Users/Nandhu/Desktop/eShop/stock/electronics.json"
    elif(pid==2):
      a = "/Users/Nandhu/Desktop/eShop/stock/laptops.json"
    elif(pid==3):
      a = "/Users/Nandhu/Desktop/eShop/stock/phones.json"
    a_file = open(a, "r")
    outfile = json.load(a_file)
    for i in outfile[na]:
      if (i["name"]==pname):
        i["stock"]+=pquan
        a_file = open(a, "w")
        json.dump(outfile, a_file)
        a_file.close()
        print("Stock refilled")
  else:
    print("invalid otp")
      
    





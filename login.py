a = int(input("1 For Order\n2 For Cancel\nEnter: "))

if a==1:
  from order import Eshop
  Eshop()

elif a==2:
  from cancel import cancel
  cancel()
  
else:
  print("Invalid code")


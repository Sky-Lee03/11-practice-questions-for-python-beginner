no=int(input("Please enter an integer from 1-1000:"))
condition1=no>1
condition2=no<1000
if condition1 & condition2 == 1:
  var=no%2
  if var!=0:
    print("Odd number")
  else:
    print("Even number")
else:
  print("Integer error, please check and re-enter")
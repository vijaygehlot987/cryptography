print("lpp bt graphical method by 2 constrainst")
maxmin = input("enter 'max' for maximation or 'min' for minimisation:")
if(maxmin == "max" or maxmin == "min"):
  print("enter value for Z:")
  zx1 = int(input("enter x1 value for Z:"))
  zx2 = int(input("enter x2 value for Z:"))
  print("enter value for constraint 1:")
  c1x1 = int(input("enter x1 value: "))
  c1x2 = int(input("enter x2 value:"))
  c1c1 = int(input("enter less than value:"))
  print("enter value for constraint 2:")
  c2x1 = int(input("enter x1:"))
  c2x2 = int(input("enter x2:"))
  c2c2 = int(input("enter less than value:"))
  if(maxmin == "max"):
    print("\nmaximize Z,")
    if(zx2 > 0):
      print(" Z = "+str(zx1)+"x1"+"-"+str(zx2)+"x2")
    else:
      print(" Z = "+str(zx1)+"x1"+"-"+str(abs(zx2))+"x2")
  else:
    print("\nminimize Z,")
    if(zx2 > 0):
      print(" Z = "+str(zx1)+"x1"+"-"+str(zx2)+"x2")
    else:
      print(" Z = "+str(zx1)+"x1"+"-"+str(abs(zx2))+"x2")
      print("sub to:")
  if(c1x2 > 0):
      print(" " +str(c1x1)+"x1"+"+"+str(c1x2)+"x2<="+str(c1c1))
  else:
      print(" " +str(c1x1)+"x1"+"+"+str(abs(c1x2))+"x2<="+str(c1c1))
  if(c2x2 > 0):
      print(" " +str(c2x1)+"x1"+"+"+str(c2x2)+"x2<="+str(c2c2))
  else:
      print(" " +str(c2x1)+"x1"+"+"+str(abs(c2x2))+"x2<="+str(c2c2))
      print(" x1 and x2 >=0")

  z=[0,0,0]
  x1=0
  x2=0
  x1 =(((c1c1 * c2x2)-(c2c2 * c1x2))/((c1x1*c2x2)-(c2x1*c1x2)))
  x2 =(((c1c1 * c2x1)-(c2c2 * c1x1))/((c1x2*c2x1)-(c2x2*c1x1)))
  p1=(0,c1c1/c1x2)
  p2=(c1c1/c1x1,0)
  p3=(0,c2c2/c2x2)            
  p4=(c2c2/c2x1,0)
  poi=(x1,x2)
  z[0]=((zx1*x1)+(zx2*p1[1]))
  if(p1[1]<p3[1]):
    z[1]=((zx1*0)+(zx2*p1[1]))
  else:
    z[1]=((zx1*0)+(zx2*p3[1]))
  if(p2[0]<p4[0]):
    z[2]=((zx1*p2[0])+(zx2*0))
  else:
    z[2]=((zx1*p4[0])+(zx2*0))
  if(maxmin=="max"):
    print("\nmaximum solution for Z is:",max(z))
  elif(maxmin=="min"):
    print("\nminimun solution for Z is:",min(z))
  else:
    print("\ninvalid input!!")
else:
    print("invalid input!!")
  
      
 
    
        
       
  

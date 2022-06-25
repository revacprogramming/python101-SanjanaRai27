#Conditional Execution

 score = input("Enter Score: ")
y=float (score)

if y>=1.0:
  print("Error")
    
elif y<=0:
  print("Error")
        
elif y>=0.9:
  print("A")
  
elif y>=0.8:
  print("B")
  
elif y>=0.7:
  print("C")
  
elif y>=0.6:
  print("D")
  
elif y<0.6:
  print("F")
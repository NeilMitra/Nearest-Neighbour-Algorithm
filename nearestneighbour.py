import math as m 

print("Enter your two starting coordinates:")

# creating an empty list 
sp = []


#converting starting point into list

for i in range(0, 2): 
    x = int(input()) 
  
    sp.append(x)       

print(sp) 

print("What is your second coordinate?:")

sc = []

for i in range(0, 2): 
    x = int(input()) 
  
    sc.append(x)       
print(sc)


x1 = (sp[0])
y1 = (sp[1])

x2 = (sc[0])
y2 = (sc[1])


def distanceformula():
    print(m.sqrt( ((y2-y1)**2) + ((x2-x1)**2)))


distanceformula()

print(distanceformula)

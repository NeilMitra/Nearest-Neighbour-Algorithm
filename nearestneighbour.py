import math as m 


#funtions

def distanceformulafs():
    return float(m.sqrt( ((y2-y1)**2) + ((x2-x1)**2)))

def distanceformulaft():
    return float(m.sqrt( ((ya2-y1)**2) + ((xa2-x1)**2)))



print("Enter your two starting coordinates:")

sp = []


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

print("What is your third coordinate?:")

tc = []

for i in range(0, 2): 
    x = int(input()) 
  
    tc.append(x)       
print(tc)

xa2 = (tc[0])
ya2 = (tc[1])



a = distanceformulafs()
b = distanceformulaft()


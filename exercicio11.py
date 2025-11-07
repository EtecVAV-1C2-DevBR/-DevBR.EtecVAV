v=[]

for i in range(8):
    n=int(input(f"digite o {i+1} numero: "))  
    v.append(n)
    
p=[]
n=[]

for n in v:
    if n>0:
        p.append(n)
    else:
        n.append(n)
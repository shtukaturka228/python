import random
let="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dig="0123456789"
sym="!@#$%^&*"
p=[]
for i in range(3):
    p.append(random.choice(let))
for i in range(3):
    p.append(random.choice(dig))
for i in range(2):
    p.append(random.choice(sym))
random.shuffle(p)
p="".join(p)
print(p)

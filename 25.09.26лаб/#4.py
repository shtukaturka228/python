text=input().lower()
chars=[]
counts=[]
for i in text:
    if i in chars:
        counts[chars.index(i)]+=1
    else:
        chars.append(i)
        counts.append(1)
for _ in range(3):
    m=max(counts)
    n=counts.index(m)
    print(chars[n],counts[n])
    chars.pop(n)
    counts.pop(n)

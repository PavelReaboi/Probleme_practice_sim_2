with open('input.txt','r') as f:
    x=list(eval(f.readline()))
for a in x:
     y=sorted(x)
with open('doc.txt','w') as f:
    for i in y:
        f.write(i)
        f.write('\n')
    
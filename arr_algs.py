arg=[1,2,3,4,5,6,7,8,9,0,-1]
n1=arg[0]
s=0
for n in arg:
    n2=arg[n]
    s=n2+s
    if n2<n1:
        n1=n2
s=s/len(arg)
print(n1,s)


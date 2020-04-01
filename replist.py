l1=[1,2,3,4,3,4,8,10,2,3]
k=int(input("enter choice to replace in list"))
for i in range(1,10):
    if l1[i] not in l1[0:i-1]:
        continue
    else:
        l1.pop(i)
        l1.insert(i,k)
print(l1)


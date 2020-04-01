dict1={"student1":"Aman","student2":"Dheeraj","student3":"Mohit","student4":"Kanika","student5":"Amrita"}
k=0
l1=sorted(dict1.values())
for key in dict1.keys():
    print(key,end=":")
    print(l1[k])
    k+=1
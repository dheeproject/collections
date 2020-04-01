testlist=[(4,5),(6,1),(3,6),(4,3),(2,5)]
"""
here we are finding the pairs which have sum equal to a particular value k
"""
k=int(input("Enter choice for sum of pairs"))
for a,b in testlist:
    if a+b==k:
        print(a,b)



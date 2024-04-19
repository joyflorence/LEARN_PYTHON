def linearsearch(list,targetval):
    for i in range(len(list)):
        if targetval == list[i]:
           return i
    return -1
list = [4,8,1,6,7,3]
targetval = int(input("Enter key element: "))
result = linearsearch(list,targetval)

if result!= -1:
    print("Target value",targetval,"found at index",result)
else:
    print("Target value",targetval,"Not found")
 


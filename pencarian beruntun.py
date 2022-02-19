def sequentialsearch(alist, value):
    pos=0
    found=False
    for pos in range (len(alist)) :
        if alist[pos]== value:
            found=True
            print(found)
            break
        else:
            return found
data=[1,7,8,3,5]
nilai=sequentialsearch(data,1)
print(nilai)
        
    
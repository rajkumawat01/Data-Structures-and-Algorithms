def binarySearchAscending(array,value):
    l=0
    u=len(array)-1
    while l<=u:
        mid=(l+u)//2
        if array[mid]==value:
            return mid
        elif array[mid]<value:
            l=mid+1
        else:
            u=mid-1
    return -1

def binarySearchDescending(array,value):
    l=0
    u=len(array)-1
    while l<=u:
        mid=(l+u)//2
        if array[mid]==value:
            return mid
        elif array[mid]>value:
            l=mid+1
        else:
            u=mid-1
    return -1

if __name__=="__main__":
    array=list(map(int,input("Array: ").split()))
    value=int(input("Value: "))
    print("1 - Ascending")
    print("2 - Descending")
    option=int(input())
    if option==1:
        print(binarySearchAscending(array,value))
    else:
        print(binarySearchDescending(array,value))
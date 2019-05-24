lst = [1, 2, 3, 4]
low = 0
upp = len(lst)
element = int(input("Enter the element to be searched : "))
mid = (low + upp)//2
while(low < upp):
    if(element < lst[mid]):
        upp = mid - 1
    elif(element > lst[mid]):
        low = mid + 1
    elif(element==lst[mid]):
        print("Element found")
        break
    mid = (upp + low) / 2


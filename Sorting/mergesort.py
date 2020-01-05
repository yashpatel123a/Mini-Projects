def merge(list0,list1):
    result = []
    while len(list1) and len(list0):
        if list0[0]<list1[0]:
            result.append(list0.pop(0))
        else:
            result.append(list1.pop(0))
    result.extend(list0)
    result.extend(list1)
    return result

def mergesort(item):
    if len(item)<=1:
        return item
    mid = int(len(item)/2)
    left = item[0:mid]
    right = item[mid:len(item)]
    left = mergesort(left)
    right = mergesort(right)
    result = merge(left,right)
    return result

if __name__ == '__main__':
    print('Enter a list of numbrt saperated by space.')
    arr = list(map(int,input().split()))
    print(mergesort(arr))
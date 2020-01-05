def bubblesort(item):
    for i in range(len(item)):
        for j in range(len(item) - i-1):
            if item[j]>item[j+1]:
                item[j],item[j+1] = item[j+1],item[j]
    return item

if __name__ == '__main__':
    print('Enter a list of numbrt saperated by space.')
    arr = list(map(int,input().split()))
    print(bubblesort(arr))

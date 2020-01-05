def sortX(points):
    points.sort(key = lambda x:x[0])
    return points

def sortY(points):
    points.sort(key = lambda x:x[1])
    return points

def compareX(a,b):
    return a[0] - b[0]

def compareY(a,b):
    return a[1] - b[1]

def distance(a,b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def bruteforce(points):
    min = 1e20
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            if distance(points[i],points[j]) < min:
                min = distance(points[i],points[j])
    return min

def stripClosest(strip,d):
    min = d
    strip = sortY(strip)
    for i in range(len(strip)):
        for j in range(i+1,len(strip)):
            if compareY(strip[j],strip[i]) < min:
                if distance(strip[i],strip[j]) < min:
                    min = distance(strip[i],strip[j])
    return min

def closestUtil(points):
    if len(points) <= 3:
        return bruteforce(points)
    mid = len(points)//2
    midpoint = points[mid]
    dl = closestUtil(points[:mid])
    dr = closestUtil(points[mid:])
    d = min(dl,dr)
    strip = []
    for i in range(len(points)):
        if abs(compareX(points[i],midpoint)) < d:
            strip.append(points[i])
    
    return min(d,stripClosest(strip,d))

def closest(points):
    points = sortX(points)
    return closestUtil(points)

if __name__ == '__main__':
    size = int(input('Enter a total number of points: '))
    points = []
    for i in range(1,size+1):
        a,b = input(f'Enter point {i}: ').split()
        points.append((int(a),int(b)))
    print(f'Closest distance between point is {round(closest(points),3)}')

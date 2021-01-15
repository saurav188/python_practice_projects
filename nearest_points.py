class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def closest_points(points, k, p):
    dist={}
    for point in points:
        dist[point]=(((point.x-p.x)**2)+((point.y-p.y)**2))**(1/2)
    result=[]
    for i in range(k):
        min=0
        min_key=None
        for key in dist:
            if min_key==None:
                min=dist[key]
                min_key=key
            if dist[key]<dist[min_key]:
                min=dist[key]
                min_key=key
        dist.pop(min_key)
        result.append(min_key)
    return result

points = [
    Point(0, 0),
    Point(1, 1),
    Point(2, 2),
    Point(3, 3),
]
print(closest_points(points, 1, Point(0, 2)))
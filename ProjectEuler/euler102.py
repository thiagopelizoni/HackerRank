# https://www.hackerrank.com/contests/projecteuler/challenges/euler102/problem
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

def is_inside_triangle(triangle, x=0, y=0):
    x1, y1, x2, y2, x3, y3 = triangle
    
    area_orig = area(x1, y1, x2, y2, x3, y3)
    
    area1 = area(x, y, x2, y2, x3, y3)
    area2 = area(x1, y1, x, y, x3, y3)
    area3 = area(x1, y1, x2, y2, x, y)
    
    return (area_orig == area1 + area2 + area3)
    
def count_triangles(triangle_coords):
    count = sum(is_inside_triangle(triangle) for triangle in triangle_coords)
    return count

if __name__ == '__main__':
    t = int(input())
    items = []
    for i in range(t):
        n = list(map(int, input().split()))
        items.append(n)
   
    answer = count_triangles(items)
    print(answer)
# https://www.hackerrank.com/contests/projecteuler/challenges/euler110/problem
# That's my attempt to solve but not passed on all test cases and I don´t know how to fix it
def almost_equilateral_triangles(N):
    sum_perimeters = 0
    
    side = 5
    
    while True:
        perim_minus = 3 * side - 1
        perim_plus = 3 * side + 1
        
        if perim_minus > N:
            break
        
        area_minus = side**2 - (side // 2)**2
        area_plus = side**2 - ((side + 1) // 2)**2
        
        if int(area_minus**0.5)**2 == area_minus:
            sum_perimeters += perim_minus

        if int(area_plus**0.5)**2 == area_plus:
            sum_perimeters += perim_plus

        side += 2
    
    return sum_perimeters

t = int(input())
for _ in range(t):
    n = int(input())
    
    answer = almost_equilateral_triangles(n)
    print(answer)

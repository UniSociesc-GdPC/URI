#2802 - Dividindo Círculos
n = int(input())
g2 = (n*(n-1))/2
g4 = (n*(n-1)*(n-2)*(n-3))/(4*3*2)

print(int(1+g2+g4))
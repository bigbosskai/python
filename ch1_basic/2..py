import math
x=input('please input two edges and theta ')
a,b,theta=map(float,x.split())
c=math.sqrt(a**2+b**2-2*a*b*math.cos(theta*math.pi/180))
print('c=',c)
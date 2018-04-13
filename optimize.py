from scipy.optimize import minimize
import math
import random
import matplotlib.pyplot as plt



f = open('windows.txt','r')
n = 10
a = []
for line in f:
    a.append(line.split())
x0 = [0]*n
for i in range(n):
    x0[i] = random.uniform(float(a[i][1]),float(a[i][2]))

def length(x):
    s = 0
    for i in range(len(a)-1):
        s += math.sqrt((float(a[i][0])-float(a[i+1][0]))**2+(x[i]-x[i+1])**2)
    return s

def length2(x):
    s = 0
    for i in range(len(a)-1):
        s += abs(x[i]-x[i+1])
    return s


b = []
for i in range(n):
    b.append((float(a[i][1]),float(a[i][2])))
res = minimize(length,x0,bounds=b)
res2 = minimize(length2,x0,bounds=b)
x1 = res.x
x2 = res2.x
print(x1)
print(x2)

points_x = []
points_y = []
p_x = []
p_y = []
p_x2 = []
p_y2 = []
for i in range(n):
	p_x.append(a[i][0])
	p_x2.append(a[i][0])
	points_x.append(a[i][0])
	points_x.append(a[i][0])
	p_y.append(x1[i])
	p_y2.append(x2[i])
	points_y.append(a[i][1])
	points_y.append(a[i][2])
p = []
for i in range(n):
    p.append((a[i][0],x1[i]))


plt.plot(points_x,points_y, 'ro')
plt.plot(p_x,p_y, linewidth=2.0)
plt.plot(p_x,p_y,'g^')
plt.plot(p_x2,p_y2,'b^')
plt.plot(p_x2,p_y2, color='r', linewidth=1.0)
plt.show()




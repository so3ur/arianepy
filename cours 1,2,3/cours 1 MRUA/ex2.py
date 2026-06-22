x = 0
v = 0
T = 1
dt = 0.2
a = 2
t = 0
while t < T:
    t = t + dt 
    x = v*dt + x
    v = a*dt + v
    print(t, x, v)


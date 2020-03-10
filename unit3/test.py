k=2
x = []
y = []
R = 0
def position()
    import random
    import math
    while 1:
        for m in range(1,5000):
            for i in range(0, k - 1):
                x[i] = random.randrange(-1, 1, 0.01)
                y[i] = random.randrange(-1, 1, 0.01)
                r = math.sprt((x[i]-x[i+1])**2 + (y[i]-y[i+1])**2)

            if x[i]>r-1 & x[i]<1-r & y[i]>r-1 & y[i]<1-r & r-1-x[i]<=0 & r-1-y[i]<=0 & r+x[i]-1<=0 & r+y[i]-1<=0:
                if r > R :
                    R=r
            else:
                continue

            if R








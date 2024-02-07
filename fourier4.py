from tools import *

g = [-1,0,0,-3,4,0]

def dft(g):
    N = len(g)
    Gn = []
    for n in range(N):
        G = 0
        for k, gk in enumerate(g):
            G += gk*np.exp(-j*n*k*2*pi/N)
        Gn.append(G)
        print(n, G)

    return Gn

def Pars(g):
    g_sum = 0
    G_sum = 0
    G = dft(g)
    N = len(g)
    for gk in g:
        g_sum += np.abs(gk)**2
    print(g_sum)

    for Gn in G:
        part = np.abs(Gn)**2
        print(part)
        G_sum += part
    G_sum = 1/N*G_sum
    print(G_sum)
    print(G_sum-g_sum)

def Cn(n):
    c0 = 1/2
    if n == 0:
        return c0
    else:
        return -4/pi**2*1/(2*n-1)**2

print(Cn(1)**2)
from tools import *

def Fsarja1(t, n):
    vakio = -4
    summa = 0
    return vakio + 4*np.cos(2*t) + 4*np.sqrt(3)*np.sin(2*t)

def Fsarja3(t, n):
    vakio = -4
    summa = vakio + (2-2*j*np.sqrt(3))*np.exp(+j*2*t) + (2+2*j*np.sqrt(3))*np.exp(-j*2*t)
    return summa

def Fsarja2(t,n):
    vakio = -4
    summa = vakio + 8*np.cos(2*t-pi/3)
    return summa

def plot_func():
    fig = plt.figure(figsize=(8,4))
    ax1 = fig.add_subplot(5,1,1)
    ax2 = fig.add_subplot(5,1,3)
    ax3 = fig.add_subplot(5,1,5)
    t = np.linspace(-4,4,100)
    sarja1 = Fsarja1(t,100)
    sarja2 = Fsarja2(t,1)
    sarja3 = Fsarja3(t,100)
    x =-1
    ax1.plot(t,sarja1)
    ax2.plot(t,sarja2)
    ax3.plot(t,sarja3)
    ax3.set_title("{},{},{}".format(Fsarja1(x,1),Fsarja2(x,1),Fsarja3(x,1)))
    plt.show()

plot_func()
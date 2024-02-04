import matplotlib.pyplot as plt
import numpy as np

j = complex(0,1)
pi = np.pi

def plot_func(func, x):
    fig, ax = plt.subplots()
    points = np.linspace(-3,3,10)
    y = 0*points
    ax.set(xlim=(-5, 5), ylim=(-7,7))
    ax.plot(points,y, color="red")
    ax.plot(y,points, color="red")
    ax.plot(x, func(x), color="blue")
    plt.show()

x = np.linspace(0,pi,10000)

def func(t):
    return np.exp(-t)*np.sin(2*t)

plot_func(func,x)
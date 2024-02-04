import matplotlib.pyplot as plt
import numpy as np

j = complex(0,1)
pi = np.pi

plt.style.use("_mpl-gallery")

def linspace(start, end, n):
    return np.linspace(start, end, n)

x = 1/6

out = np.exp(j*pi*x)
plot_x = out.real
plot_y = out.imag

fig, ax = plt.subplots()
ax.scatter(plot_x,plot_y)
ax.set(xlim=(-1.2, 1.2), xticks=np.arange(-1, 1),
       ylim=(-1.2, 1.2), yticks=np.arange(-1, 1))
plt.show()
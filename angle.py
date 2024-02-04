import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction

j = complex(0,1)
pi = np.pi

frac = input("Give angle: ")
fig, ax = plt.subplots()

x = np.linspace(-10,10,1000)
y = 0*x
ax.plot(x,y, color="red")
ax.plot(y,x, color="red")
ax.set(xlim=(-1.2, 1.2), ylim=(-1.2, 1.2))

x = np.linspace(0,1,1000)

angle = Fraction(frac)
points = np.exp(j*angle*pi*x)
points = np.append(points,[0])
end = np.exp(pi*j*angle)
x = np.linspace(0, end.real, 100)
y = x*end.imag/end.real
ax.fill_between(points.real,points.imag, color="blue")
ax.set_title(end)

plt.show()

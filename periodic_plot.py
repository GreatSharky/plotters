from tools import *


def periodically_continued(a, b):
    interval = b - a
    return lambda f: lambda x: f((x - a) % interval + a)

@periodically_continued(-pi/3, pi/3)
def f(x):
    return np.cos(x)

x = np.linspace(-3,3,1000)

plt.plot(x,f(x))
plt.show()
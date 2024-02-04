from tools import *

def plotter(upper_plot, lower_plot):
    fig = plt.figure(figsize=(8,4))
    ax1 = fig.add_subplot(3,1,1)
    ax2 = fig.add_subplot(3,1,3)
    ax1.set_title(upper_plot["title"])
    ax2.set_title(lower_plot["title"])
    ax1.plot(upper_plot["x"], upper_plot["y"], color=upper_plot["color"], linestyle=upper_plot["style"])
    ax2.plot(lower_plot["x"], lower_plot["y"], color=lower_plot["color"], linestyle=lower_plot["style"])
    plt.show()

def create_plot(x,y,color="blue", title="", style="-"):
    funcdict = {}
    funcdict["x"] = x
    funcdict["y"] = y
    funcdict["color"] = color
    funcdict["title"] = title
    funcdict["style"] = style
    return funcdict

def periodically_defined(a, b):
    interval = b - a
    return lambda f: lambda x: f((x - a) % interval + a)

# returns fourier series of func with period for n members
def fourier_series(func, period, n, t):
    return

# return a_n of func from 0 to n
def fourier_an(func,period, n, t):
    omega = 2*pi/period
    f = np.exp
    return

# returns b_n of func from 1 to n
def fourier_bn(func, period, n, t):
    return

def fourier_cn(func, period, n, t):
    omega = 2*pi/period
    c = func(t)*np.exp(-j*omega*t*n)


@periodically_defined(-1,1)
def func(x):
    t = x
    y = []
    for xi in x:
        if xi < 0:
            y.append(9)
        else:
            y.append(2)
    return np.array(y)

def main():
    x = np.linspace(-5,5,1000)
    y = func(x)
    plot = create_plot(x,y, style=":")
    plotter(plot,plot)

main()

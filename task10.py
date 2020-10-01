from scipy.integrate import nquad


def f(x, y):
    return x * y


def bounds_y():
    return [0, 0.5]


def bounds_x(y):
    return [0, 1 - 2 * y]


y, err = nquad(f, [bounds_x, bounds_y])
print("The result of Monte Carlo integration for this multiple integral is {}".format(y))

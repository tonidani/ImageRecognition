from PyQt5 import QtGui


def ar3(fot, q, w):
    ar = []
    for y in [w - 1, w, w + 1]:
        for x in [q - 1, q, q + 1]:
            ar.append(QtGui.QColor(fot.pixel(x, y)).getRgb()[0])
    return ar


def ar9(fot, q, w):
    ar = []
    for y in [w - 4, w - 3, w - 2, w - 1, w, w + 1, w + 2, w + 3, w + 4]:
        for x in [q - 4, q - 3, q - 2, q - 1, q, q + 1, q + 2, q + 3, q + 4]:
            ar.append(QtGui.QColor(fot.pixel(x, y)).getRgb()[0])
    return ar


def c_ar(ar, c):
    dz = 0
    for x, y in zip(ar, c):
        dz = dz + (x * y)
    return dz


def nor(x):
    if x > 255:
        return 255
    elif x < 0:
        return 0
    return x


def c_f(f):
    if f == 1:
        h = [1, 2, 1, 0, 0, 0, -1, -2, -1]
        v = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
    else:
        h = [1, 1, 1, 0, 0, 0, -1, -1, -1]
        v = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

    return h, v


def cor_5x5(fot, col, x, y):
    c = []
    for p_y in range(y - 2, y + 3):
        for p_x in range(x - 2, x + 3):
            c.append(fot.pixel(p_x, p_y))
    return c


def gausser(c, f):
    n_r, n_g, n_b = 0, 0, 0
    for pix, zxc in zip(c, f):
        colors = QtGui.QColor(pix).getRgb()
        r = colors[0] * zxc
        g = colors[1] * zxc
        b = colors[2] * zxc
        n_r += r
        n_g += g
        n_b += b
    n_r /= 273
    n_g /= 273
    n_b /= 273
    return (int(n_r % 255), int(n_g % 255), int(n_b % 255))


def gpixel(width, height, k, dict):
    ap = width * height

    bp = round(100 * sum([dict[i] * i / 255 for i in range(k)]) / ap, 3)

    op = round(100 * sum([dict[i] * i / 255 for i in range(k, 255)]) / ap, 3)

    bpp = round(100 * sum([dict[i] for i in range(k)]) / ap, 3)

    opp = round(100 * sum([dict[i] for i in range(k, 255)]) / ap, 3)

    app = round(100 * sum([dict[i] * i / 255 for i in range(255)]) / ap, 3)

    return bp, op, bpp, opp, app


ARR = [[5, 5, 5, -3, 0, -3, -3, -3, -3],
       [5, 5, -3, 5, 0, -3, -3, -3, -3],
       [5, -3, -3, 5, 0, -3, 5, -3, -3],
       [-3, -3, -3, 5, 0, -3, 5, 5, -3],
       [-3, -3, -3, -3, 0, -3, 5, 5, 5],
       [-3, -3, -3, -3, 0, 5, -3, 5, 5],
       [-3, -3, 5, -3, 0, 5, -3, -3, 5],
       [-3, 5, 5, -3, 0, 5, -3, -3, -3]]

ARR2 = [1 / 6, 2 / 3, 1 / 6, 2 / 3, -10 / 3, 2 / 3, 1 / 6, 2 / 3, 1 / 6]
ARR3 = [0, 1, 1, 2, 2, 2, 1, 1, 0,
        1, 2, 4, 5, 5, 5, 4, 2, 0,
        1, 4, 5, 3, 0, 3, 5, 4, 1,
        2, 5, 3, -12, -24, -12, 3, 5, 2,
        2, 5, 0, -24, -50, -24, 0, 5, 2,
        2, 5, 3, -12, -24, -12, 3, 5, 2,
        1, 4, 5, 3, 0, 3, 5, 4, 1,
        1, 2, 4, 5, 5, 5, 4, 2, 0,
        0, 1, 1, 2, 2, 2, 1, 1, 0]

g_filter = [1, 4, 7, 4, 1,
            4, 16, 26, 16, 4,
            7, 26, 41, 26, 7,
            4, 16, 26, 16, 4,
            1, 4, 7, 4, 1]

slX = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
slY = [-1, -2, -1, 0, 0, 0, 1, 2, 1]
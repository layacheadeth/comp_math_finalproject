from tkinter import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt


def raise_frame(frame):
    frame.tkraise()


root = Tk()
root.geometry('600x600+600+200')
root.title('Interpolation')

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

background_image = tk.PhotoImage(file='/Users/deth/Desktop/download.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

for i in (f1, f2, f3, f4):
    i.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

Label(f1, text='Welcome to Interpolation').place(relx=0.28, rely=0, relwidth=0.5, relheight=0.1)

Button(f1, text='Direct_Interpolation', command=lambda: raise_frame(f2)).place(relx=0.3, rely=0.1, relwidth=0.45,
                                                                               relheight=0.1)
Button(f1, text='Newton_Interpolation', command=lambda: raise_frame(f3)).place(relx=0.3, rely=0.3, relwidth=0.45,
                                                                               relheight=0.1)
Button(f1, text='Lagrange_Interpolation', command=lambda: raise_frame(f4)).place(relx=0.3, rely=0.5, relwidth=0.45,
                                                                                 relheight=0.1)

Label(f2, text='Direct_Interpolation').place(relx=0.3, rely=0, relwidth=0.4, relheight=0.1)
b1 = tk.Button(f2, text='Go_back', command=lambda: raise_frame(f1)).place(relx=0.55, rely=0.7, relwidth=0.2,
                                                                          relheight=0.1)
b2 = tk.Button(f2, text='Display the graph', command=lambda: direct()).place(relx=0.1, rely=0.7, relwidth=0.4,
                                                                             relheight=0.1)
Label(f2, text='Input_Degree: ').place(relx=0.1, rely=0.1, relwidth=0.4, relheight=0.1)
options = []
for i in range(1, 30):
    options.append(i)
clicked = IntVar()
clicked.set(options[0])


def direct(*args):
    x = [21, 22, 23, 24, 25, 26]
    y = [24, 56, 189, 290, 345, 555]
    n = clicked.get()
    b = [[None for row in range(0, n + 1)] for col in range(0, n + 1)]
    c = [None for row in range(0, n + 1)]

    for i in range(0, n + 1):
        c[i] = y[i]
        for j in range(0, n + 1):
            b[i][j] = x[i] ** j

    a = np.linalg.solve(b, c)

    yp = 0
    xp = 27
    xplt=np.linspace(x[0],x[-1])
    yplt=[]
    for i in range(0, n + 1):
        yp = yp + a[i] * xp ** i
        yplt.append(yp)




    plt.plot(x, y, '-ro', xp, yp, '-')
    # plt.plot(x, y, '-ro', xplt, yplt, '-')
    plt.show()



drop = tk.OptionMenu(f2, clicked, *options).place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.1)

Label(f3, text='Newton_Interpolation').place(relx=0.3, rely=0, relwidth=0.4, relheight=0.1)
b3 = tk.Button(f3, text='Go_back', command=lambda: raise_frame(f1)).place(relx=0.55, rely=0.7, relwidth=0.2,
                                                                          relheight=0.1)
b4 = tk.Button(f3, text='Display the graph', command=lambda: newton()).place(relx=0.1, rely=0.7, relwidth=0.4,
                                                                             relheight=0.1)
Label(f3, text='Input_Degree: ').place(relx=0.1, rely=0.1, relwidth=0.4, relheight=0.1)


def dy_dx(xa, xb, ya, yb):
    return (ya - yb) / (xa - xb)


def newton():
    x = [21, 22, 23, 24, 25, 26]
    y = [24, 56, 189, 290, 345, 555]
    n = clicked.get()
    b = [[None for row in range(n + 1)] for col in range(n + 1)]
    b[0][0] = y[0]
    for i in range(0, n + 1):
        for j in range(0, n + 1 - i):
            if (i == 0):
                b[i][j] = y[j]
            else:
                b[i][j] = dy_dx(x[j + i], x[j], b[i - 1][j + 1], b[i - 1][j])

    yp = b[0][0]
    xp = 27

    for i in range(1, n + 1):
        m = 1
        for j in range(0, i):
            m = m * (xp - x[j])
    yp = yp + b[i][0] * m
    plt.plot(x, y, '-ro', xp, yp, '-')
    plt.show()


drop = tk.OptionMenu(f3, clicked, *options).place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.1)

Label(f4, text='Lagrange_Interpolation').place(relx=0.3, rely=0, relwidth=0.4, relheight=0.1)
b5 = tk.Button(f4, text='Go_back', command=lambda: raise_frame(f1)).place(relx=0.55, rely=0.7, relwidth=0.2,
                                                                          relheight=0.1)
b6 = tk.Button(f4, text='Display the graph', command=lambda: lagrange()).place(relx=0.1, rely=0.7, relwidth=0.4,
                                                                               relheight=0.1)
Label(f4, text='Input_Degree: ').place(relx=0.1, rely=0.1, relwidth=0.4, relheight=0.1)


def lagrange():
    x = [21, 22, 23, 24, 25, 26]
    y = [24, 56, 189, 290, 345, 555]
    l = []
    n = clicked.get()
    xp = 27
    for i in range(0, n + 1):
        m = 1
        for j in range(0, n + 1):
            if (j != i):
                m = m * (xp - x[j]) / (x[i] - x[j])
        l.append(m)

    yp = 0

    for i in range(0, n + 1):
        yp = yp + l[i] * y[i]
    plt.plot(x, y, '-ro', xp, yp, '-')
    plt.show()


drop = tk.OptionMenu(f4, clicked, *options).place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.1)

raise_frame(f1)
root.mainloop()

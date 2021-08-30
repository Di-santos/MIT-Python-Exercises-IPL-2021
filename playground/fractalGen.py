import numpy as np
import matplotlib.pyplot as plt
import time

def percentageCount(i, x_len):
    print((i/x_len)*100,"% completed")

def mandelbrot(n_rows, n_columns, iterations):
    x_cor = np.linspace(-2,1,n_rows)
    y_cor = np.linspace(-2,1,n_columns)
    x_len = len(x_cor)
    y_len = len(y_cor)
    output = np.zeros((x_len,y_len))

    for i in range(x_len):
        percentageCount(i, x_len)
        for j in range(y_len):
            c = complex(x_cor[i],y_cor[j])
            z = complex(0, 0)
            count = 0
            for k in range(iterations):
                z = (z * z) + c
                count = count + 1
                if (abs(z) > 4):
                    break
            output[i,j] = count
    return output

output = mandelbrot(500,500,6000)

plt.imshow(output.T, cmap = "rainbow")
plt.axis("off")
plt.show()

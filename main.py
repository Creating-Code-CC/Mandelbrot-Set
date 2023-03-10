import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(h,w, max_iters=20):
    # setup a list of complex numbers representing the pixels on the screen
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    # initialize the output image with the number of iterations it takes for the 
    # corresponding point in the complex plane to escape
    z = c
    divtime = max_iters + np.zeros(z.shape, dtype=int)

    for i in range(max_iters):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2          # who is diverging
        div_now = diverge & (divtime==max_iters)  # who is diverging now
        divtime[div_now] = i                  # note when
        z[diverge] = 2                        # avoid diverging too much

    return divtime

plt.imshow(mandelbrot(400,400))
plt.show()
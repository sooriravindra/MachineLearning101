# Raveendra Soori - sooriravindra@gmail.com

# Get rid of annoying toolbar
import matplotlib as mplt
mplt.rcParams['toolbar'] = 'None'

import matplotlib.pyplot as plt
import numpy as np

# Generate 100 x and y values for f(x) = 2x + 3
x_val = map(lambda i: (i/10.0),range(100))
y_val = map(lambda x: (2*x + 3 + np.random.randn(1)[0]), x_val)
plt.plot(x_val,y_val, 'ro')

t0 = 0
t1 = 0

def hypothesis(x):
    # h(x) = t1*x + t0
    return (t1*x + t0)

m = len(x_val)
alpha = 0.01

for i in range(10000):
    h_val = np.array(map(hypothesis,x_val))
    error_val = np.subtract(h_val,y_val)

    #t0 = t0 - alpha * 1/m * SUM(h(x) -y)
    #t1 = t1 - alpha * 1/m * SUM(x*(h(x) -y))

    t0 -= alpha/m*sum(error_val)
    t1 -= alpha/m*sum(error_val*x_val)

    # Uncomment the following lines to visualize the algorithm
    # plt.clf()
    # plt.plot(x_val,y_val, 'ro')
    # plt.plot(x_val,h_val)
    # plt.pause(0.0001)


plt.plot(x_val,h_val)
plt.show()

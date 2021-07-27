import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
b=[1/(1+np.exp(-k)) for k in x]
plt.plot(x, b)
plt.show()

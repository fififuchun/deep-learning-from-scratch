import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

x = np.arange(0, 6, 0.1)
y = np.sin(x)

plt.plot(x,y)
plt.show()

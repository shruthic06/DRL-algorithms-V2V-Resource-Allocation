import numpy as np
from matplotlib import pyplot as plt




data2=np.load('rewards_sim0.npy')
plt.ylim([-25, 5])
plt.plot(data2)
plt.xlim([0,500])
plt.xticks(np.arange(0, 500, 100))
plt.show()

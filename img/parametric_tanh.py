import numpy as np

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize


def ptanh(a):
    return lambda x: a * x + (1-a) * np.tanh(x)


x = np.linspace(-3, 3, 100)

cmap = cm.get_cmap('viridis')

for a in np.linspace(1, 0, 20):
    plt.plot(x, ptanh(a)(x), c=cmap(a))

#plt.gca().set_ylabel(r"$ptanh(x, a) = a x + (1 - a)\, \tanh (x)$")
plt.suptitle(r"$ptanh(x, a) = a x + (1 - a)\, \tanh (x)$")

plt.colorbar(
    cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap)
).ax.set_ylabel("a")

plt.savefig("parametric_tanh.svg")
plt.savefig("parametric_tanh.pdf")

plt.show()

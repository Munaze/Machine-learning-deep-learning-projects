"""Softmax."""

scores = [[1, 2, 3, 6],
                   [2, 4, 5, 6],
                   [3, 8, 7, 6]]
import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) /np.sum(np.exp(x),axis=0) # TODO: Compute and return softmax(x)


print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()

a = input("Press Enter")

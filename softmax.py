import numpy as np
from functools import reduce

"""Softmax."""

#scores = [3.0, 1.0, 0.2]

scores = [1.0, 2.0, 3.0]

#scores = [1.0,2.0,3.0,4.0,1.0,2.0,3.0]

scores = np.array([[1, 2, 3, 6],
                   [2, 4, 5, 6],
                   [3, 8, 7, 6]])

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    values = np.array([hardmax(y, x) for y in x])
    return values

def hardmax(item, scores):
    numerator = ez(item)
    scores = np.array([ez(x) for x in scores])
    denominator = reduce(lambda x,y: x + y, scores)
    return numerator / denominator

def ez(item):
    return np.power(np.e, item)

values = softmax(scores)
print(values)
print(sum(values))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()

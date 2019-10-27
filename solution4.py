import numpy as np
import matplotlib.pyplot as plt
import math

def is_pareto_efficient(x, a):
    return np.sum(np.all((x > a), axis=1).astype(np.int32)) == 0


X = np.random.sample((100, 5))
p_eff = np.array([], dtype=int)
p_not_eff = np.array([], dtype=int)

for idx, value in enumerate(X):
    if is_pareto_efficient(X, X[idx, :]):
        p_eff = np.append(p_eff, int(idx))
    else:
        p_not_eff = np.append(p_not_eff, int(idx))


ax = plt.subplot(111, projection="polar")
plt.thetagrids(np.arange(0, 360, 360.0/X.shape[1]))

for i in range(p_not_eff.shape[0]):
    ax.plot(np.append(np.arange(0, X.shape[1], 1) *2 * math.pi/X.shape[1], 0), np.append(X[p_not_eff[i], :], X[p_not_eff[i], 0]), color="b")

for i in range(p_eff.shape[0]):
    ax.plot(np.append(np.arange(0, X.shape[1], 1), 0) *2 * math.pi/X.shape[1], np.append(X[p_eff[i], :], X[p_eff[i], 0]), color="r")


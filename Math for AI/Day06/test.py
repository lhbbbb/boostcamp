import numpy as np

x = np.array([0, 1])
y = np.array([0, 2])


def l2_norm(x):
    x_norm = x * x
    x_norm = np.sum(x_norm)
    x_norm = np.sqrt(x_norm)
    return x_norm


def angle(x, y):
    v = np.inner(x, y) / (l2_norm(x) * l2_norm(y))

    theta = np.arccos(v)

    return theta


print(angle(x, y))

X = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 0]])
X_inv = np.linalg.inv(X)
print(np.linalg.inv(X))

X = np.array([[1, 0, 1], [0, 1, 0]])
print(np.linalg.pinv(X))

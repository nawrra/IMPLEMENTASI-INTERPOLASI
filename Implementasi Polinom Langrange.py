import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk menghitung basis Lagrange
def lagrange_basis(x, x_data, k):
    term = 1
    for i in range(len(x_data)):
        if i != k:
            term *= (x - x_data[i]) / (x_data[k] - x_data[i])
    return term

# Fungsi interpolasi Lagrange
def lagrange_interpolation(x, x_data, y_data):
    y = 0
    for i in range(len(x_data)):
        y += y_data[i] * lagrange_basis(x, x_data, i)
    return y

# Menguji fungsi dengan membuat plot
x_plot = np.linspace(5, 40, 400)
y_lagrange = [lagrange_interpolation(x, x_data, y_data) for x in x_plot]

plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'o', label='Data Points')
plt.plot(x_plot, y_lagrange, label='Lagrange Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolasi Polinom Lagrange')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

#Data yang diberikan
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

#Implementasi polinom Lagrange
def lagrange_interpolation(x, x_data, y_data):
    def L(k, x):
        term = 1
        for j in range(len(x_data)):
            if j != k:
                term *= (x - x_data[j]) / (x_data[k] - x_data[j])
        return term
    
    y = 0
    for i in range(len(x_data)):
        y += y_data[i] * L(i, x)
    return y

#Implementasi polinom Newton
def newton_interpolation(x, x_data, y_data):
    n = len(x_data)
    divided_diff = np.zeros((n, n))
    divided_diff[:, 0] = y_data

    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i, j] = (divided_diff[i + 1, j - 1] - divided_diff[i, j - 1]) / (x_data[i + j] - x_data[i])

    def N(x):
        result = divided_diff[0, 0]
        product_term = 1
        for i in range(1, n):
            product_term *= (x - x_data[i - 1])
            result += divided_diff[0, i] * product_term
        return result
    
    return N(x)

#Plotting interpolasi
x_plot = np.linspace(5, 40, 400)
y_lagrange = [lagrange_interpolation(x, x_data, y_data) for x in x_plot]
y_newton = [newton_interpolation(x, x_data, y_data) for x in x_plot]

plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'o', label='Data Points')
plt.plot(x_plot, y_lagrange, label='Lagrange Interpolation')
plt.plot(x_plot, y_newton, label='Newton Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolasi Polinom Lagrange dan Newton')
plt.grid(True)
plt.show()

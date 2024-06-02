import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([15, 19, 14, 11, 6, 4, 6, 8])

# Fungsi untuk menghitung koefisien perbedaan terbagi Newton
def newton_divided_differences(x_data, y_data):
    n = len(x_data)
    coef = np.zeros([n, n])
    coef[:,0] = y_data
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x_data[i + j] - x_data[i])
    
    return coef[0, :]

# Fungsi interpolasi Newton
def newton_interpolation(x, x_data, coef):
    n = len(x_data)
    y = coef[0]
    for i in range(1, n):
        term = coef[i]
        for j in range(i):
            term *= (x - x_data[j])
        y += term
    return y

# Menghitung koefisien perbedaan terbagi
coefficients = newton_divided_differences(x_data, y_data)

# Menguji fungsi dengan membuat plot
x_plot = np.linspace(5, 40, 400)
y_newton = [newton_interpolation(x, x_data, coefficients) for x in x_plot]

plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'o', label='Data Points')
plt.plot(x_plot, y_newton, label='Newton Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolasi Polinom Newton')
plt.grid(True)
plt.show()

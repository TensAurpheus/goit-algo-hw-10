import matplotlib.pyplot as plt
import numpy as np
import inspect
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return (x - 1) ** 3 + 1


def graph(low, high, func, tolerance=0.1):
    # Створення діапазону значень для x
    x = np.linspace(low - tolerance, high + tolerance, 400)
    y = func(x)
    func_expression = inspect.getsource(func).split('return')[1].strip()

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(low, high)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування f(x) = {func_expression} від {low} до {high}')
    plt.grid()
    plt.show()


def monte_carlo_integrate(func, low, high, y_min_, y_max_, num_points):
    x = np.random.uniform(low, high, num_points)
    y = np.random.uniform(y_min_, y_max_, num_points)
    under_curve = np.sum(y < func(x))
    # print(under_curve)
    area = (high - low) * (y_max_ - y_min_) * (under_curve / num_points)
    return area


if __name__ == '__main__':
    a, b = 0, 2
    x = np.linspace(a, b, 400)
    y = f(x)
    y_min = min(y)
    y_max = max(y)

    mc_result = monte_carlo_integrate(f, a, b, y_min, y_max, 1_000_000)
    result, error = spi.quad(f, a, b)

    graph(a, b, f)
    print("Метод Монте-Карло: ", mc_result)
    print("Інтеграл: ", result)
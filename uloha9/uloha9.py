import numpy as np
from scipy import integrate


start_interval = 0
end_interval = 1
step = 0.01


def polynomial(x):
    return 1 * x**3 + 2 * x**2 + 3 * x + 4


def logarithmic(x):
    return np.log(1 / 2 * x + 3)


def harmonic(x):
    return np.sin(x**1 - 2)


def calculate(function, x, start_interval, end_interval) -> tuple[float, float, float]:
    y = function(x)
    trapezoid_result = integrate.trapezoid(y, x, dx=step)
    romberg_result = integrate.romberg(function, start_interval, end_interval)
    simpson_result = integrate.simpson(y, x)

    return trapezoid_result, romberg_result, simpson_result


def print_result(text, result):
    print(text)
    print(f"Trapezoid result: {result[0]}")
    print(f"Romberg result: {result[1]}")
    print(f"Simpson result: {result[2]}\n")


x = np.linspace(start_interval, end_interval, int((end_interval - start_interval) / step))

polynomial_result = calculate(
    polynomial,
    x,
    start_interval,
    end_interval,
)

logarithmic_result = calculate(
    logarithmic,
    x,
    start_interval,
    end_interval,
)

harmonic_result = calculate(
    harmonic,
    x,
    start_interval,
    end_interval,
)

print_result("Polynomial", polynomial_result)
print_result("Logarithmic", logarithmic_result)
print_result("Harmonic", harmonic_result)

import math
import random


def simulate_gravel_sizes(supplier, n=100):
    """
    Simulates n gravel sizes for a supplier, based on their screening process.

    Parameters:
    - supplier: Identifier for the supplier ('A' or 'B').
    - n: Number of gravel sizes to simulate.

    Returns:
    A list of simulated gravel sizes.
    """
    if supplier == 'A':
        # Supplier A: Sizes between 3/8" and 1"
        min_size, max_size = 3 / 8, 1
    else:
        # Supplier B: Sizes up to 7/8"
        min_size, max_size = 3 / 8, 7 / 8

    return [random.uniform(min_size, max_size) for _ in range(n)]


def calculate_mean(data):
    """Calculates the mean of the given data."""
    return sum(data) / len(data)


def calculate_std_dev(data, mean):
    """Calculates the standard deviation of the given data."""
    return math.sqrt(sum((x - mean) ** 2 for x in data) / (len(data) - 1))


def simpsons_rule(f, a, b, n):
    """
    Numerically integrates f from a to b using Simpson's 1/3 rule with n intervals.

    Parameters:
    - f: The function to integrate.
    - a, b: The interval to integrate over.
    - n: The number of intervals (must be even).

    Returns:
    The estimated integral of f from a to b.
    """
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]
    return (h / 3) * (y[0] + 4 * sum(y[i] for i in range(1, n, 2)) + 2 * sum(y[i] for i in range(2, n, 2)) + y[n])


def t_distribution(x, df):
    """
    Computes the value of the t-distribution PDF for a given x and degrees of freedom.
    """
    coeff = math.gamma((df + 1) / 2) / (math.sqrt(df * math.pi) * math.gamma(df / 2))
    return coeff * (1 + x ** 2 / df) ** (-(df + 1) / 2)


def perform_t_test(mean_a, std_dev_a, mean_b, std_dev_b, n_a, n_b):
    """
    Performs a 1-sided t-test to compare the means of two samples.

    Parameters:
    - mean_a, std_dev_a: Mean and standard deviation of sample A.
    - mean_b, std_dev_b: Mean and standard deviation of sample B.
    - n_a, n_b: Sample sizes for A and B.

    Returns:
    The t-statistic and p-value for the test.
    """
    se_diff = math.sqrt(std_dev_a ** 2 / n_a + std_dev_b ** 2 / n_b)
    t_stat = (mean_a - mean_b) / se_diff
    df = min(n_a, n_b) - 1  # Simplified calculation of degrees of freedom

    # Use Simpson's rule to estimate the p-value from the t-distribution
    p_value = simpsons_rule(lambda x: t_distribution(x, df), t_stat, 10,
                            1000)  # 10 is an arbitrary upper limit for integration

    return t_stat, p_value


def main():
    sample_a = simulate_gravel_sizes('A')
    sample_b = simulate_gravel_sizes('B')

    mean_a = calculate_mean(sample_a)
    mean_b = calculate_mean(sample_b)
    std_dev_a = calculate_std_dev(sample_a, mean_a)
    std_dev_b = calculate_std_dev(sample_b, mean_b)

    t_stat, p_value = perform_t_test(mean_a, std_dev_a, mean_b, std_dev_b, len(sample_a), len(sample_b))

    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")

    if p_value < 0.05:  # Corresponding to α = 0.95
        print("Supplier B's gravel size is statistically significantly smaller than Supplier A's at α = 0.95.")
    else:
        print("No statistically significant difference in gravel size between Supplier A and B at α = 0.95.")


if __name__ == "__main__":
    main()

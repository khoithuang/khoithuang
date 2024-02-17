import math
import random


def simulate_sample(mean, stddev, n=100):
    """
    Simulate a sample of gravel sizes from a normal distribution.

    Parameters:
    - mean: The mean size of gravel particles.
    - stddev: The standard deviation of gravel sizes.
    - n: The number of gravel particles in the sample.

    Returns:
    A list of simulated gravel sizes.
    """
    return [random.gauss(mean, stddev) for _ in range(n)]


def calculate_mean(sample):
    """
    Calculate the mean of a sample.

    Parameters:
    - sample: A list of numeric values.

    Returns:
    The mean of the sample.
    """
    return sum(sample) / len(sample)


def calculate_stddev(sample, mean):
    """
    Calculate the standard deviation of a sample.

    Parameters:
    - sample: A list of numeric values.
    - mean: The mean value of the sample.

    Returns:
    The standard deviation of the sample.
    """
    variance = sum((x - mean) ** 2 for x in sample) / (len(sample) - 1)
    return math.sqrt(variance)


def t_test(mean_a, mean_b, stddev_a, stddev_b, n_a, n_b):
    """
    Perform a t-test to compare two independent samples.

    Parameters:
    - mean_a: The mean of sample A.
    - mean_b: The mean of sample B.
    - stddev_a: The standard deviation of sample A.
    - stddev_b: The standard deviation of sample B.
    - n_a: The size of sample A.
    - n_b: The size of sample B.

    Returns:
    The t-statistic for comparing the two samples.
    """
    pooled_se = math.sqrt(stddev_a ** 2 / n_a + stddev_b ** 2 / n_b)
    t_statistic = (mean_a - mean_b) / pooled_se
    return t_statistic


def main():
    """
    Main function to execute the gravel size comparison test.
    It simulates samples for both suppliers, calculates their means and standard deviations,
    performs a t-test, and reports if there's a significant difference in gravel sizes.
    """
    n = 100  # Sample size for each supplier
    # Assuming normal distribution parameters for Supplier A
    mean_a, stddev_a = 0, 1
    # Adjusted mean for smaller size by Supplier B
    mean_b, stddev_b = -0.1, 0.9

    # Simulate samples for both suppliers
    sample_a = simulate_sample(mean_a, stddev_a, n)
    sample_b = simulate_sample(mean_b, stddev_b, n)

    # Calculate means and standard deviations for both samples
    mean_a = calculate_mean(sample_a)
    mean_b = calculate_mean(sample_b)
    stddev_a = calculate_stddev(sample_a, mean_a)
    stddev_b = calculate_stddev(sample_b, mean_b)

    # Perform a t-test to compare the two samples
    t_statistic = t_test(mean_a, mean_b, stddev_a, stddev_b, n, n)
    print(f"T-statistic: {t_statistic}")

    # Critical t-value for α = 0.95 and df = n*2 - 2
    critical_t = 1.660  # Approximate for df=198, consult t-table for exact value
    if t_statistic > critical_t:
        print("Supplier B's gravel size is statistically significantly smaller than Supplier A's at α = 0.95.")
    else:
        print("No statistically significant difference in gravel size between Supplier A and B at α = 0.95.")


# Execute the main function
if __name__ == "__main__":
    main()

import math
import random


def generate_rock_size(mean, variance):
    """Generate a normally distributed rock size given the mean and variance using Box-Muller transform."""
    # Box-Muller transform requires two uniformly distributed random numbers
    u1, u2 = random.random(), random.random()
    # Convert uniform random numbers to normal distribution
    z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
    # Scale by variance and mean
    return mean + math.sqrt(variance) * z0


def calculate_mean(data):
    """Calculate the mean of a list of numbers."""
    return sum(data) / len(data)


def calculate_variance(data, mean):
    """Calculate the variance of a list of numbers given the mean."""
    return sum((x - mean) ** 2 for x in data) / len(data)


def simulate_crushing_operation(n_samples=11, sample_size=100, lower_bound=3 / 8, upper_bound=1):
    """
    Simulate a rock crushing operation. Generates rock sizes based on a normal distribution
    with unknown mean and variance. Captures rocks that are too big to pass through a 3/8" mesh
    but too small to pass through a 1" mesh.

    Parameters:
    - n_samples (int): The number of samples to generate.
    - sample_size (int): The size of each sample (number of rocks).
    - lower_bound (float): The lower size limit for rocks (in inches).
    - upper_bound (float): The upper size limit for rocks (in inches).

    Returns:
    - A tuple containing the sample means, sample variances, mean of sample means, and variance of sample means.
    """

    # Assume a reasonable mean and variance for the distribution of rock sizes
    assumed_mean = (upper_bound + lower_bound) / 2
    assumed_variance = ((upper_bound - lower_bound) / 4) ** 2

    sample_means = []
    sample_variances = []

    for i in range(n_samples):
        # Generate the sample
        sample = [generate_rock_size(assumed_mean, assumed_variance) for i in range(sample_size)]
        # Filter the sample based on size constraints
        filtered_sample = [rock for rock in sample if lower_bound < rock < upper_bound]
        # Calculate sample mean and variance
        sample_mean = calculate_mean(filtered_sample)
        sample_variance = calculate_variance(filtered_sample, sample_mean)
        # Store sample statistics
        sample_means.append(sample_mean)
        sample_variances.append(sample_variance)

    # Calculate the mean of the sample means
    overall_mean = calculate_mean(sample_means)
    # Calculate the variance of the sample means
    overall_variance = calculate_variance(sample_means, overall_mean)

    return sample_means, sample_variances, overall_mean, overall_variance


# Run the simulation
sample_means, sample_variances, overall_mean, overall_variance = simulate_crushing_operation()

# Display the results
print("Sample Means:", sample_means)
print("Sample Variances:", sample_variances)
print("Mean of Sample Means:", overall_mean)
print("Variance of Sample Means:", overall_variance)

# I get help from ChatGPT especially on how to turn the equations into coding for python.
import random

# Constants
N = 100  # Number of rocks in each sample
NUM_SAMPLES = 11  # Number of samples
MAX_ROCK_SIZE = 1.0  # Maximum size of rocks (inclusive upper bound for uniform distribution)
MIN_ROCK_SIZE = 3 / 8  # Minimum size of rocks (inclusive lower bound for uniform distribution)
MESH_1 = 1.0  # Size of mesh screen 1"x1" (not directly used in this simulation)
MESH_2 = 3 / 8  # Size of mesh screen 3/8"x3/8" (not directly used in this simulation)


def simulate_crushing_and_sieving():
    """
    Simulates the process of crushing rocks and sieving them through mesh screens.

    This function generates NUM_SAMPLES samples, each containing N rock sizes
    uniformly distributed between MIN_ROCK_SIZE and MAX_ROCK_SIZE, simulating
    the result of a rock crushing operation followed by sieving through mesh screens.

    Returns:
        A list of samples, where each sample is a list of rock sizes.
    """
    samples = []
    for i in range(NUM_SAMPLES):
        # Generate a sample of N rocks with sizes uniformly distributed
        # between MIN_ROCK_SIZE and MAX_ROCK_SIZE.
        sample = [random.uniform(MIN_ROCK_SIZE, MAX_ROCK_SIZE) for i in range(N)]
        samples.append(sample)

    return samples


def calculate_mean(data):
    """
    Calculates the mean of a dataset.

    Parameters:
        data (list): A list of numeric values.

    Returns:
        The mean of the data.
    """
    return sum(data) / len(data)


def calculate_variance(data, mean):
    """
    Calculates the variance of a dataset.

    Parameters:
        data (list): A list of numeric values.
        mean (float): The mean of the data.

    Returns:
        The variance of the data.
    """
    # Variance is the average of the squared differences from the Mean.
    return sum((x - mean) ** 2 for x in data) / len(data)


def main():
    """
    Main function that orchestrates the simulation of rock crushing and sieving,
    calculates sample means and variances, and reports the overall mean and variance
    of the sampling means.
    """
    # Simulate rock crushing and sieving to generate samples.
    samples = simulate_crushing_and_sieving()

    # Lists to store the means and variances of the samples.
    sampling_means = []
    sampling_variances = []

    # Calculate and print the mean and variance for each sample.
    for sample in samples:
        mean = calculate_mean(sample)
        variance = calculate_variance(sample, mean)

        sampling_means.append(mean)
        sampling_variances.append(variance)

        print("Sample Mean:", mean)
        print("Sample Variance:", variance)
        print()

    # Calculate and print the overall mean and variance of the sampling means.
    overall_mean = calculate_mean(sampling_means)
    overall_variance = calculate_variance(sampling_means, overall_mean)

    print("Mean of Sampling Means:", overall_mean)
    print("Variance of Sampling Means:", overall_variance)


if __name__ == "__main__":
    main()


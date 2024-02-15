import random

# Constants
N = 100  # Number of rocks in each sample
NUM_SAMPLES = 11  # Number of samples
MAX_ROCK_SIZE = 1.0  # Maximum size of rocks
MIN_ROCK_SIZE = 0.0  # Minimum size of rocks
MESH_1 = 1.0  # Size of mesh screen 1"x1"
MESH_2 = 3 / 8  # Size of mesh screen 3/8"x3/8"


# Function to simulate rock crushing and sieving
def simulate_crushing_and_sieving():
    samples = []
    for _ in range(NUM_SAMPLES):
        sample = [random.uniform(MIN_ROCK_SIZE, MAX_ROCK_SIZE) for _ in range(N)]
        samples.append(sample)

    return samples


# Function to calculate mean
def calculate_mean(data):
    return sum(data) / len(data)


# Function to calculate variance
def calculate_variance(data, mean):
    return sum((x - mean) ** 2 for x in data) / len(data)


# Main function
def main():
    samples = simulate_crushing_and_sieving()

    sampling_means = []
    sampling_variances = []

    for sample in samples:
        mean = calculate_mean(sample)
        variance = calculate_variance(sample, mean)

        sampling_means.append(mean)
        sampling_variances.append(variance)

        print("Sample Mean:", mean)
        print("Sample Variance:", variance)
        print()

    overall_mean = calculate_mean(sampling_means)
    overall_variance = calculate_variance(sampling_means, overall_mean)

    print("Mean of Sampling Means:", overall_mean)
    print("Variance of Sampling Means:", overall_variance)


if __name__ == "__main__":
    main()

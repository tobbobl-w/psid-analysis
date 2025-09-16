def hello(name):
    return print(f"Your name is and it still is : {name}%")


def calculate_skewness(data):
    """
    Calculate the skewness of a dataset.

    Skewness measures the asymmetry of a distribution:
    - Skewness = 0: symmetric distribution
    - Skewness > 0: right-skewed (tail extends to the right)
    - Skewness < 0: left-skewed (tail extends to the left)

    For normal distribution: skewness = 0
    """
    if len(data) < 3:
        raise ValueError("Need at least 3 data points to calculate skewness")

    n = len(data)
    mean = sum(data) / n

    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5

    if std_dev == 0:
        return 0

    # Calculate skewness using the third standardized moment
    third_moment = sum(((x - mean) / std_dev) ** 3 for x in data) / n

    return third_moment


def calculate_kurtosis(data):
    """
    Calculate the kurtosis of a dataset.

    Kurtosis measures the "tailedness" of a distribution:
    - Kurtosis = 3: normal distribution (mesokurtic)
    - Kurtosis > 3: heavy tails, peaked center (leptokurtic)
    - Kurtosis < 3: light tails, flat center (platykurtic)

    For normal distribution: kurtosis = 3

    Note: This returns the raw kurtosis. Some definitions use "excess kurtosis" 
    which subtracts 3, making normal distribution have excess kurtosis = 0.
    """
    if len(data) < 4:
        raise ValueError("Need at least 4 data points to calculate kurtosis")

    n = len(data)
    mean = sum(data) / n

    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5

    if std_dev == 0:
        return float('inf')  # Undefined for no variation

    # Calculate kurtosis using the fourth standardized moment
    fourth_moment = sum(((x - mean) / std_dev) ** 4 for x in data) / n

    return fourth_moment

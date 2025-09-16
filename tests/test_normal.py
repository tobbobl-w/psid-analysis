
"""
Tests for the camp.analysis module
"""
import pytest
import pandas as pd
import numpy as np
import camp
from scipy import stats


def test_normal_distribution_properties():
    """
    Test that samples from normal distribution have skewness ≈ 0 and kurtosis ≈ 3
    """
    print("Testing Normal Distribution Properties")
    print("="*50)

    # Set random seed for reproducibility
    np.random.seed(42)

    sample_sizes = [100, 1000, 10000, 50000]

    for n in sample_sizes:
        # Draw from standard normal distribution
        data = np.random.normal(loc=0, scale=1, size=n)

        # Calculate our statistics
        skew = camp.utils.calculate_skewness(data)
        kurt = camp.utils.calculate_kurtosis(data)
        excess_kurt = camp.utils.calculate_kurtosis(data) - 3

        # Calculate scipy statistics for comparison
        scipy_skew = stats.skew(data)
        # Raw kurtosis (not excess)
        scipy_kurt = stats.kurtosis(data, fisher=False)
        scipy_excess_kurt = stats.kurtosis(
            data, fisher=True)  # Excess kurtosis

        print(f"\nSample size: {n:,}")
        print(f"Skewness:")
        print(f"  My function:  {skew:8.4f}")
        print(f"  Scipy:        {scipy_skew:8.4f}")
        print(f"  Expected:     {0:8.4f}")
        print(f"  |Error|:      {abs(skew):8.4f}")

        print(f"Kurtosis:")
        print(f"  My function:  {kurt:8.4f}")
        print(f"  Scipy:        {scipy_kurt:8.4f}")
        print(f"  Expected:     {3:8.4f}")
        print(f"  |Error|:      {abs(kurt - 3):8.4f}")

        print(f"Excess Kurtosis:")
        print(f"  My function:  {excess_kurt:8.4f}")
        print(f"  Scipy:        {scipy_excess_kurt:8.4f}")
        print(f"  Expected:     {0:8.4f}")
        print(f"  |Error|:      {abs(excess_kurt):8.4f}")

        # Check if values are reasonably close to expected
        # Rough rule of thumb for standard error
        skew_tolerance = 3 / np.sqrt(n)
        kurt_tolerance = 6 / np.sqrt(n)   # Kurtosis has higher variance

        if abs(skew) < skew_tolerance:
            print(
                f"  ✓ Skewness within expected range (±{skew_tolerance:.3f})")
        else:
            print(
                f"  ⚠ Skewness outside expected range (±{skew_tolerance:.3f})")

        if abs(kurt - 3) < kurt_tolerance:
            print(
                f"  ✓ Kurtosis within expected range of 3 (±{kurt_tolerance:.3f})")
        else:
            print(
                f"  ⚠ Kurtosis outside expected range of 3 (±{kurt_tolerance:.3f})")

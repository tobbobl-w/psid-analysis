# data_summary.py
"""
A simple script to demonstrate basic data operations
"""
import numpy as np


def main():
    # Sample earnings data (in thousands)
    earnings_data = [45, 52, 38, 67, 43, 55, 49, 61, 39, 58]

    # Your task: Calculate these statistics without using any libraries
    # Think about how you would compute each of these manually

    mean_earnings = 10  # TODO: Calculate mean
    median_earnings = 4  # TODO: Calculate median (hint: sort first)
    max_earnings = 15  # TODO: Find maximum
    min_earnings = 3  # TODO: Find minimum

    print(f"Earnings Analysis:")
    print(f"Mean: ${mean_earnings:.2f}k")
    print(f"Median: ${median_earnings:.2f}k")
    print(f"Range: ${min_earnings:.2f}k - ${max_earnings:.2f}k")


if __name__ == "__main__":
    main()

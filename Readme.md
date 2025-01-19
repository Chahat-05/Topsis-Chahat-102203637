# Topsis Package

A Python package to calculate **TOPSIS** (Technique for Order Preference by Similarity to Ideal Solution) scores for decision-making.

## Installation

Install the package from PyPI using `pip`:

```bash
pip install Topsis-Chahat-102203637
```
## Usage
Run the TOPSIS algorithm via the command line using the topsis-cli tool.
```bash
topsis-cli <input_file.csv> <weights> <impacts> <output_file.csv>
```
<input_file.csv>: Path to the input CSV file with alternatives and criteria.
<weights>: Comma-separated list of weights for each criterion (e.g., 0.3, 0.4, 0.3).
<impacts>: Comma-separated list of impacts for each criterion (+ for positive, - for negative).
<output_file.csv>: Path for saving the output with TOPSIS scores.

Example:
Input file (input.csv):
Model, P1, P2, P3
Model1, 25, 35, 30
Model2, 30, 40, 35
Model3, 20, 30, 25

Run the command:
topsis-cli input.csv 0.3,0.4,0.3 +,+,- output.csv

Sample Output:
output.csv
Model, P1, P2, P3, Topsis Score, Rank
Model1, 25, 35, 30, 0.72, 1
Model2, 30, 40, 35, 0.85, 2
Model3, 20, 30, 25, 0.60, 3

How it Works
Normalization: The input data is normalized using the root sum of squares method for each column.
Weight Normalization: The normalized data is then weighted according to the provided weights.
Best and Worst Values: The best and worst values for each criterion are determined based on the given impacts.
Performance Calculation: The Euclidean distance to the best and worst values is computed, and a performance score is generated.
Ranking: The alternatives are ranked based on their performance scores.
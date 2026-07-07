# Probability Calculator

A Python project that estimates probabilities using **Monte Carlo Simulation**. The program models a hat containing colored balls, performs repeated random experiments without replacement, and approximates the probability of drawing a desired combination of balls.

## Features

- Create hats containing any combination of colored balls
- Randomly draw balls without replacement
- Simulate thousands of independent experiments
- Estimate probabilities for custom draw conditions
- Supports any number of ball colors and quantities

## Example

### Creating a Hat

```python
hat = Hat(black=6, red=4, green=3)
```

### Running an Experiment

```python
probability = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000
)

print(probability)
```

Example Output

```text
0.356
```

> **Note:** Since the simulation relies on random sampling, the probability will vary slightly each time the program is executed.

---

## How It Works

1. Create a hat containing colored balls.
2. Randomly draw a specified number of balls without replacement.
3. Check whether the drawn balls satisfy the expected conditions.
4. Repeat the experiment many times.
5. Estimate the probability using:

```text
Estimated Probability =
(Number of Successful Experiments) /
(Total Number of Experiments)
```

The larger the number of experiments, the closer the estimate approaches the true probability.

---

## Concepts Demonstrated

- Monte Carlo Simulation
- Probability Estimation
- Random Sampling Without Replacement
- Object-Oriented Programming (OOP)
- Classes and Objects
- Lists and Dictionaries
- Algorithm Design

---

## Project Structure

```
Probability Calculator/
├── probability_calculator.py
└── README.md
```

---

## Learning Outcomes

This project helped me strengthen my understanding of:

- Estimating probabilities through simulation
- Applying Monte Carlo methods to real-world problems
- Designing reusable Python classes
- Working with randomization algorithms
- Managing collections using lists and dictionaries
- Writing modular and maintainable Python code

---

## Technologies Used

- Python 3
- Standard Python Library

---

## Part of

This project was completed as part of the **Scientific Computing with Python** curriculum and demonstrates practical applications of probability, simulation, object-oriented programming, and algorithmic problem solving in Python.

# Budget App

A Python-based budget management application built using Object-Oriented Programming (OOP). The project models different budget categories, allowing users to manage deposits, withdrawals, transfers, and balances while also generating a text-based spending chart that visualizes expenditure across categories.

## Features

- Create multiple budget categories (e.g., Food, Clothing, Entertainment)
- Record deposits with optional descriptions
- Withdraw funds with balance validation
- Transfer money between budget categories
- Calculate current category balances
- Display formatted transaction ledgers
- Generate an ASCII bar chart showing spending percentages by category

## Example

### Creating Categories

```python
food = Category("Food")
clothing = Category("Clothing")

food.deposit(1000, "Initial Deposit")
food.withdraw(45.67, "Groceries")
food.transfer(100, clothing)
```

### Output

```text
*************Food*************
Initial Deposit       1000.00
Groceries              -45.67
Transfer to Clothing  -100.00
Total: 854.33
```

---

### Spending Chart

```python
print(create_spend_chart([food, clothing]))
```

Produces a text-based chart similar to:

```text
Percentage spent by category
100|
 90|
 80|
 70|
 60| o
 50| o
 40| o
 30| o
 20| o  o
 10| o  o  o
  0| o  o  o
    ----------
     F  C
     o  l
     o  o
     d  t
        h
        i
        n
        g
```

---

## Class Overview

### `Category`

Represents an individual budget category.

### Methods

- `deposit(amount, description="")`
- `withdraw(amount, description="")`
- `transfer(amount, category)`
- `get_balance()`
- `check_funds(amount)`

---

## Concepts Demonstrated

- Object-Oriented Programming (OOP)
- Classes and Objects
- Instance Variables
- Methods
- Data Encapsulation
- Lists and Dictionaries
- String Formatting
- Data Visualization using ASCII Graphics

---

## Project Structure

```
Budget App/
├── budget.py
└── README.md
```

---

## Learning Outcomes

This project helped me strengthen my understanding of:

- Designing reusable Python classes
- Managing financial transactions using object-oriented principles
- Implementing validation and error checking
- Formatting structured console output
- Creating text-based data visualizations
- Working with lists, dictionaries, and custom objects

---

## Technologies Used

- Python 3
- Standard Python Library (No external dependencies)

---

## Part of

This project was completed as part of the **Scientific Computing with Python** curriculum and demonstrates practical application of object-oriented programming, data management, and algorithmic problem solving in Python.

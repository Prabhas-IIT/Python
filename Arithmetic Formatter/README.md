# Arithmetic Formatter

A Python program that formats arithmetic expressions vertically in the traditional column format used in elementary mathematics. The formatter supports addition and subtraction problems, validates user input, and can optionally display the calculated answers.

## Features

- Formats arithmetic problems vertically
- Supports addition (`+`) and subtraction (`-`)
- Right-aligns operands for proper formatting
- Displays multiple problems side by side
- Optionally computes and displays answers
- Performs comprehensive input validation with descriptive error messages

## Example

### Input

```python
arithmetic_arranger(
    ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],
    True
)
```

### Output

```text
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

---

## Error Handling

The program validates the input and returns meaningful error messages for invalid cases:

- More than five arithmetic problems
- Unsupported operators (only `+` and `-` are allowed)
- Non-numeric operands
- Operands containing more than four digits

Example:

```python
arithmetic_arranger(["3 / 855", "3801 - 2"])
```

Returns:

```text
Error: Operator must be '+' or '-'.
```

---

## Concepts Demonstrated

- Python Functions
- String Manipulation and Formatting
- Conditional Statements
- Input Validation
- Lists and Iteration
- Error Handling

---

## Project Structure

```
Arithmetic Formatter/
├── arithmetic_formatter.py
└── README.md
```

---

## Learning Outcomes

This project strengthened my understanding of:

- Building reusable Python functions
- Designing clear input validation logic
- Producing well-formatted console output
- Working with strings, spacing, and alignment
- Writing clean and maintainable Python code

---

## Technologies Used

- Python 3
- Standard Python Library (No external dependencies)

---

## Part of

This project was completed as part of the **Scientific Computing with Python** curriculum and demonstrates fundamental Python programming and problem-solving skills.

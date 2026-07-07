# Time Calculator

A Python program that calculates the resulting time after adding a specified duration to a given start time. The calculator supports the 12-hour clock format, handles day transitions, computes future weekdays, and correctly tracks elapsed days.

## Features

- Adds any duration to a given start time
- Supports 12-hour time format (AM/PM)
- Correctly handles transitions between AM and PM
- Detects and reports the next day
- Calculates multiple days later
- Supports optional weekday calculation (case-insensitive)
- Handles durations spanning several days

## Example

### Input

```python
add_time("11:43 PM", "24:20", "Tuesday")
```

### Output

```text
12:03 AM, Thursday (2 days later)
```

---

### Another Example

```python
add_time("10:10 PM", "3:30")
```

Returns

```text
1:40 AM (next day)
```

---

## Supported Function Signature

```python
add_time(start_time, duration, starting_day=None)
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| `start_time` | Starting time in 12-hour format (AM/PM) |
| `duration` | Duration to add in hours and minutes |
| `starting_day` *(optional)* | Starting weekday (case-insensitive) |

---

## Concepts Demonstrated

- Time Arithmetic
- Modular Arithmetic
- String Parsing and Formatting
- Conditional Logic
- Functions
- Input Processing

---

## Project Structure

```
Time Calculator/
├── time_calculator.py
└── README.md
```

---

## Learning Outcomes

This project helped me develop skills in:

- Working with time calculations
- Handling edge cases involving date and time transitions
- Designing reusable Python functions
- Implementing modular arithmetic for cyclic data (hours and weekdays)
- Producing clean and user-friendly output formatting

---

## Technologies Used

- Python 3
- Standard Python Library (No external dependencies)

---

## Part of

This project was completed as part of the **Scientific Computing with Python** curriculum and demonstrates practical problem-solving using Python functions, arithmetic operations, and string manipulation.

# Polygon Area Calculator

A Python project demonstrating Object-Oriented Programming (OOP) through the implementation of `Rectangle` and `Square` classes. The project performs geometric calculations, generates ASCII representations of shapes, and showcases inheritance, method overriding, and polymorphism.

## Features

- Create `Rectangle` and `Square` objects
- Calculate area, perimeter, and diagonal length
- Modify dimensions after object creation
- Generate ASCII art representations of shapes
- Determine how many times one shape can fit inside another
- Demonstrate inheritance between `Rectangle` and `Square`

## Example

### Creating a Rectangle

```python
rect = Rectangle(10, 5)

print(rect.get_area())
print(rect.get_perimeter())
print(rect.get_diagonal())
```

Output

```text
50
30
11.180339887498949
```

---

### Creating a Square

```python
sq = Square(4)

print(sq.get_area())
print(sq)
```

Output

```text
16
Square(side=4)
```

---

### ASCII Shape Representation

```python
print(Rectangle(6, 3).get_picture())
```

Output

```text
******
******
******
```

---

### Shape Fitting

```python
rect = Rectangle(16, 8)
sq = Square(4)

print(rect.get_amount_inside(sq))
```

Output

```text
8
```

---

## Classes

### `Rectangle`

Represents a rectangle defined by its width and height.

#### Methods

- `set_width(width)`
- `set_height(height)`
- `get_area()`
- `get_perimeter()`
- `get_diagonal()`
- `get_picture()`
- `get_amount_inside(shape)`

---

### `Square`

A subclass of `Rectangle` where width and height are always equal.

#### Additional Method

- `set_side(side)`

The class overrides the width and height setters to ensure all sides remain equal.

---

## Concepts Demonstrated

- Object-Oriented Programming (OOP)
- Classes and Objects
- Inheritance
- Method Overriding
- Polymorphism
- Encapsulation
- Geometry Calculations
- String Formatting

---

## Project Structure

```
Polygon Area Calculator/
├── polygon_area_calculator.py
└── README.md
```

---

## Learning Outcomes

This project helped me develop a deeper understanding of:

- Object-oriented design principles
- Creating class hierarchies using inheritance
- Reusing and extending existing code
- Implementing geometric algorithms
- Generating formatted console output
- Writing clean and maintainable Python code

---

## Technologies Used

- Python 3
- Standard Python Library (No external dependencies)

---

## Part of

This project was completed as part of the **Scientific Computing with Python** curriculum and demonstrates practical application of object-oriented programming, inheritance, and geometric problem solving in Python.

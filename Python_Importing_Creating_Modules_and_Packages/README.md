# Python Modules and Packages

A Python project demonstrating how to create, structure, import, and test custom modules and packages.

---

## 📁 Project Structure

```text
Python_Importing_Creating_Modules_and_Packages/
├── README.md
└── modules_assignment/
    ├── main.py                     # Main test driver / entry point script
    ├── math_utils.py               # Task 1: Mathematical utility functions
    ├── string_utils.py             # Task 2: String utility functions
    └── shop_package/               # Task 3: Custom package for shop operations
        ├── __init__.py             # Package marker
        ├── billing.py              # Billing and tax calculation module
        └── discount.py             # Discount calculation module
```

---

## 📦 Modules & Functions Overview

### 1. `math_utils.py` (Task 1)
Provides basic mathematical operations:

| Function | Parameters | Description | Return Value |
| :--- | :--- | :--- | :--- |
| `add(a, b)` | `a` (number), `b` (number) | Calculates addition of two numbers | `a + b` |
| `substract(a, b)` | `a` (number), `b` (number) | Calculates subtraction of two numbers | `a - b` |
| `square(n)` | `n` (number) | Calculates square of a number | `n ** 2` |

---

### 2. `string_utils.py` (Task 2)
Provides common string manipulation helpers:

| Function | Parameters | Description | Return Value |
| :--- | :--- | :--- | :--- |
| `capitalize_words(word)` | `word` (str) | Capitalizes the given word | `word.capitalize()` |
| `reverse_string(word)` | `word` (str) | Reverses the given string | `word[::-1]` |
| `word_character_length(word)` | `word` (str) | Computes the length of the string | `len(word)` |

---

### 3. `shop_package` (Task 3)
A custom package that contains modules for shop billing and discount calculations:

#### `shop_package/billing.py`
| Function | Parameters | Description | Return Value |
| :--- | :--- | :--- | :--- |
| `calculate_total(prices)` | `prices` (list of numbers) | Computes the sum of all item prices | `sum(prices)` |
| `apply_tax(price)` | `price` (number) | Adds 5% tax to the given price | `price + (price * 0.05)` |

#### `shop_package/discount.py`
| Function | Parameters | Description | Return Value |
| :--- | :--- | :--- | :--- |
| `apply_discount(price, percent)` | `price` (number), `percent` (number) | Calculates the discount amount for a given percentage | `price * (percent / 100)` |
| `flat_discount(price)` | `price` (number) | Calculates price after subtracting a flat 50 discount | `price - 50` |

---

### 4. `main.py`
The driver script that demonstrates various import styles in Python:

- **Module Import:** `import math_utils`, `import string_utils`
- **Selective Import:** `from math_utils import square`, `from shop_package.billing import calculate_total`
- **Aliased Import:** `import shop_package.discount as disc`, `import shop_package.billing as bil`

It prompts the user for inputs to test the math and string functions, then executes and prints results for the shop package calculations.

---

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher installed on your system.

### Execution

Navigate to the `modules_assignment` directory and run `main.py`:

```bash
cd modules_assignment
python main.py
```

### Sample Interactive Session

```text
Enter first number: 5
Enter second number: 3
Addition of the numbers: 8
Substraction of two number: 2
Given First number square : 25
Enter word: python
Capitalize word is:  Python
Reverse word is:  nohtyp
Word count is : 6
The 100 price after discount: 10.0
the 100 price after 50 flat discount: 950
Total calculation: 600
Total bill and add 5% tax : 630.0
```

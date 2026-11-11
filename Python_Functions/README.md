# 🐍 Python Functions – GenAI Course Tasks

**Author:** Atik Tambakwale  
**Course:** GenAI Course – Python Functions Module  
**Language:** Python 3  

---

## 📁 Project Structure

```
Python_Functions/
├── GenAI-Task1-AtikTambakwale/
│   └── basic-function_price_after_discount.py
├── GenAI-Task2-AtikTambakwale/
│   └── recursive_function_factorial_utility.py
├── GenAI-Task3-AtikTambakwale/
│   └── lambda_function_gst_calculation.py
├── GenAI-Task4-AtikTambakwale/
│   └── using_map_apply_gst_to_list_f_prices.py
├── GenAI-Task5-AtikTambakwale/
│   └── using_filter_method_filter_expensive_products.py
├── GenAI-Task6-AtikTambakwale/
│   └── combined-utility_functions.py
└── GenAI-Task7-AtikTambakwale/
    └── menus_using_functions.py
```

---

## 📋 Tasks Overview

| # | Task | Concept | File |
|---|------|---------|------|
| 1 | Price After Discount | Basic Functions & Default Parameters | `basic-function_price_after_discount.py` |
| 2 | Factorial Utility | Recursive Functions | `recursive_function_factorial_utility.py` |
| 3 | GST Calculation | Lambda Functions | `lambda_function_gst_calculation.py` |
| 4 | Apply GST to Price List | `map()` with Lambda | `using_map_apply_gst_to_list_f_prices.py` |
| 5 | Filter Expensive Products | `filter()` with Lambda | `using_filter_method_filter_expensive_products.py` |
| 6 | Combined Utility Functions | `map()` + `filter()` Combined | `combined-utility_functions.py` |
| 7 | Interactive Price Menu | Functions + While Loop + Menu | `menus_using_functions.py` |

---

## 🔍 Task Details

### Task 1 – Basic Function: Price After Discount

**File:** `GenAI-Task1-AtikTambakwale/basic-function_price_after_discount.py`

Demonstrates a basic Python function with a **default parameter** for discount percentage.

**Key Concepts:**
- Defining functions with `def`
- Default parameter values (`discount=5`)
- Conditional logic to cap discount at 60%

**Function:**
```python
def apply_discount(price, discount=5):
    if discount > 60:
        return "Discount Not Exceeds Above 60%"
    return price * (discount / 100)
```

**Sample Output:**
```
100.0          # apply_discount(1000, 10)
25.0           # apply_discount(500)  → uses default 5%
Discount Not Exceeds Above 60%   # apply_discount(2000, 67)
```

---

### Task 2 – Recursive Function: Factorial Utility

**File:** `GenAI-Task2-AtikTambakwale/recursive_function_factorial_utility.py`

Implements a **recursive** factorial function with guard clauses for edge cases.

**Key Concepts:**
- Recursion (`factorial(n-1)`)
- Handling edge cases: zero, negative numbers, and base case `n=1`

**Function:**
```python
def factorial(n):
    if n == 0:   return "zero can't be calculated factorial number"
    elif n == 1: return 1
    elif n < 0:  return "negative number can't be calculated factorial number"
    elif n > 1:  return n * factorial(n - 1)
```

**Sample Output:**
```
120    # factorial(5)  →  5! = 5×4×3×2×1
zero can't be calculated factorial number   # factorial(0)
negative number can't be calculated factorial number   # factorial(-3)
```

---

### Task 3 – Lambda Function: GST Calculation

**File:** `GenAI-Task3-AtikTambakwale/lambda_function_gst_calculation.py`

Uses **lambda functions** to compute GST-inclusive prices and combined discount+GST pricing.

**Key Concepts:**
- Anonymous functions with `lambda`
- Composing lambdas (using one lambda inside another)
- 18% GST calculation

**Lambdas:**
```python
gst_amt      = lambda price: price + (0.18 * price)
discount_amt = lambda price, discount: price + gst_amt(price) + (discount / 100)
```

**Sample Output (price = 100):**
```
The Given price :  100
given price with 18% gst : 118.0
Compute final price discount amount after GST + 10% discount :  218.1
```

---

### Task 4 – `map()`: Apply GST to a List of Prices

**File:** `GenAI-Task4-AtikTambakwale/using_map_apply_gst_to_list_f_prices.py`

Applies an 18% GST to every item in a price list using Python's built-in **`map()`** function.

**Key Concepts:**
- `map()` with a lambda to transform all list elements
- Converting map object back to a list

**Core Logic:**
```python
prices = [100, 250, 400, 1200, 50]
price_with_gst = list(map(lambda price: price + (0.18 * price), prices))
```

**Sample Output:**
```
Original Prices:
[100, 250, 400, 1200, 50]
Price after GST:
[118.0, 295.0, 472.0, 1416.0, 59.0]
```

---

### Task 5 – `filter()`: Filter Expensive Products

**File:** `GenAI-Task5-AtikTambakwale/using_filter_method_filter_expensive_products.py`

Uses **`filter()`** to split a price list into "expensive" (> 500) and "affordable" (≤ 500) products.

**Key Concepts:**
- `filter()` with a lambda predicate
- Filtering for both conditions independently

**Core Logic:**
```python
prices = [100, 250, 400, 1200, 50, 2000, 850]
prices_greater_list = list(filter(lambda price: price > 500, prices))
prices_less_list    = list(filter(lambda price: price <= 500, prices))
```

**Sample Output:**
```
Origina List :
 [100, 250, 400, 1200, 50, 2000, 850]
List of prices greater then 500 :
 [1200, 2000, 850]
List of prices less then and equal to 500 :
 [100, 250, 400, 50]
```

---

### Task 6 – Combined Utility Functions: Discount + Filter

**File:** `GenAI-Task6-AtikTambakwale/combined-utility_functions.py`

Combines `map()` and `filter()` inside a single utility function to apply a 10% discount to all items and then filter those that remain above 300.

**Key Concepts:**
- Encapsulating `map()` + `filter()` logic inside a named function
- Returning multiple results as a list
- Real-world pipeline: transform → filter

**Function:**
```python
def process_price(prices_list):
    discounted_prices_list       = list(map(lambda p: p + (p * 0.10), prices_list))
    discounted_prices_above_list = list(filter(lambda p: p > 300, discounted_prices_list))
    return [discounted_prices_list, discounted_prices_above_list]
```

**Sample Output:**
```
Given Original list:
 [100, 500, 900, 50, 750]
Apply 10% discount to all prices list:
 [110.0, 550.0, 990.0, 55.0, 825.0]
Only Discounted prices list that are above 300:
 [550.0, 990.0, 825.0]
```

---

### Task 7 – Interactive Menu Using Functions

**File:** `GenAI-Task7-AtikTambakwale/menus_using_functions.py`

Builds a **console-based interactive menu** with three utility functions managed through a `while` loop for a seamless user experience.

**Key Concepts:**
- Multiple named functions (`add_price`, `get_average_price`, `get_max_price`)
- `while True` loop with `continue` / `break` control flow
- `input()` for user interaction
- Guard clauses for empty list handling

**Functions:**
```python
def add_price(price_list, price):         # Appends price to the list
def get_average_price(price_list):        # Returns sum/len or 0 if empty
def get_max_price(price_list):            # Returns max() or "none" if empty
```

**Menu Options:**
```
1 -- Add Price
2 -- Show Average Price
3 -- Show Maximum Price
q -- Quit
```

---

## 🧠 Concepts Covered

| Concept | Tasks |
|---------|-------|
| Basic function definition (`def`) | Task 1, 2, 6, 7 |
| Default parameter values | Task 1 |
| Recursion | Task 2 |
| Lambda (anonymous) functions | Task 3, 4, 5, 6 |
| `map()` built-in | Task 4, 6 |
| `filter()` built-in | Task 5, 6 |
| `while` loop & menu-driven programs | Task 7 |
| Input validation & edge-case handling | Task 1, 2, 7 |
| List operations (`append`, `sum`, `max`, `len`) | Task 7 |

---

## ▶️ How to Run

Make sure Python 3 is installed, then run any script from the terminal:

```bash
# Example – Task 1
python "GenAI-Task1-AtikTambakwale/basic-function_price_after_discount.py"

# Example – Task 7 (interactive)
python "GenAI-Task7-AtikTambakwale/menus_using_functions.py"
```

> **Note:** Task 7 (`menus_using_functions.py`) is interactive — it will prompt for user input at the terminal.

---

## 📌 Requirements

- Python 3.x (no external libraries required — all standard built-ins)


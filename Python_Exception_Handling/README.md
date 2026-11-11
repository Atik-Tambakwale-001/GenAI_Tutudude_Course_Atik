# Python Exception Handling

This repository contains practical implementations and exercises demonstrating robust **Exception Handling** techniques in Python. Developed as part of the GenAI Course coursework by **Atik Tambakwale**, the project covers standard exception handling patterns including `try`, `except`, `else`, and `finally` blocks, custom input validation, file operations, and interactive CLI utilities.

---

## 📁 Repository Structure

```text
Python_Exception_Handling/
│
├── GenAI-Task1-AtikTambakwale/
│   └── safe_division_utility.py          # Safe division utility handling ZeroDivisionError & ValueError
│
├── GenAI-Task2-AtikTambakwale/
│   └── bill_calculator_with_error_handling.py # List processing & validation with error handling
│
├── GenAI-Task3-AtikTambakwale/
│   └── custom_exception_age_validator.py # Age validation logic with error catching
│
├── GenAI-Task4-AtikTambakwale/
│   ├── file_reader_with_exception_handling.py # File I/O handling FileNotFoundError & PermissionError
│   └── sales_data.txt                    # Sample data file for file reader testing
│
├── GenAI-Task5-AtikTambakwale/
│   └── safe_shopping_cart.py             # Interactive CLI shopping cart with input validation
│
└── README.md                             # Repository documentation
```

---

## 🛠️ Tasks & Modules Overview

### 1. Task 1: Safe Division Utility
- **File:** `GenAI-Task1-AtikTambakwale/safe_division_utility.py`
- **Concepts:** `try`, `except ValueError`, `except ZeroDivisionError`, `else`, `finally`
- **Description:** Prompts the user to enter a numerator and a denominator, converting both inputs to floating-point numbers and performing division.
- **Error Handling:**
  - `ValueError`: Handled when non-numeric input is provided.
  - `ZeroDivisionError`: Handled when the denominator is `0`.
  - `else`: Displays the division result only when no exceptions occur.
  - `finally`: Guarantees completion output regardless of errors.

```bash
python GenAI-Task1-AtikTambakwale/safe_division_utility.py
```

---

### 2. Task 2: Bill Calculator with Error Handling
- **File:** `GenAI-Task2-AtikTambakwale/bill_calculator_with_error_handling.py`
- **Concepts:** Defensive data validation, `isinstance`, `try-except-finally`, `TypeError`, `ValueError`
- **Description:** Processes a collection of prices containing mixed data types (integers, floats, negative values, and strings). Iterates through the list, filters out invalid values, and computes a running total of valid items.
- **Validation Checks:**
  - Skips non-numeric items using `isinstance(price, (int, float))`.
  - Rejects negative price amounts (`price < 0`).
  - Wraps execution inside `try-except` blocks for `TypeError` and `ValueError` to ensure resilient execution.

```bash
python GenAI-Task2-AtikTambakwale/bill_calculator_with_error_handling.py
```

---

### 3. Task 3: Age Validator
- **File:** `GenAI-Task3-AtikTambakwale/custom_exception_age_validator.py`
- **Concepts:** Functional validation, boundary checking, `ValueError`, `TypeError`, `finally`
- **Description:** Accepts user input for age, converts it to an integer, and invokes a validation function `check_age(age)`.
- **Validation Rules:**
  - Validates that age falls within a realistic human range ($1 \le \text{age} \le 120$).
  - Catches `ValueError` when input conversion fails.
  - Catches `TypeError` if incompatible data types are supplied.
  - Runs a `finally` block to signal operation conclusion.

```bash
python GenAI-Task3-AtikTambakwale/custom_exception_age_validator.py
```

---

### 4. Task 4: File Reader with Exception Handling
- **File:** `GenAI-Task4-AtikTambakwale/file_reader_with_exception_handling.py`
- **Companion File:** `GenAI-Task4-AtikTambakwale/sales_data.txt`
- **Concepts:** Context managers (`with open`), `FileNotFoundError`, `PermissionError`, file streaming
- **Description:** Prompts user for a file name inside the task folder and safely reads the top 3 lines using a `while` loop.
- **Error Handling:**
  - `FileNotFoundError`: Gracefully alerts the user if the specified file does not exist.
  - `PermissionError`: Flags files lacking appropriate read permissions.
  - `finally`: Confirms that a file operation was attempted.

```bash
python GenAI-Task4-AtikTambakwale/file_reader_with_exception_handling.py
```

---

### 5. Task 5: Safe Shopping Cart
- **File:** `GenAI-Task5-AtikTambakwale/safe_shopping_cart.py`
- **Concepts:** Continuous interactive loop (`while True`), Sentinel value termination (`q`), `ValueError`, list aggregation (`len`, `sum`)
- **Description:** Provides an interactive CLI shopping cart. Users can repeatedly enter item prices or type `'q'` to finalize their cart.
- **Features:**
  - Converts input strings to float/integer values safely inside a `try...except` block.
  - Checks against negative price entries.
  - Handles invalid entries via `ValueError` with descriptive messaging.
  - Computes and prints the total number of items and overall bill amount upon exit.

```bash
python GenAI-Task5-AtikTambakwale/safe_shopping_cart.py
```

---

## 🎯 Summary of Exception Handling Concepts Covered

| Exception / Keyword | Purpose in Codebase |
| :--- | :--- |
| **`try`** | Defines the code block monitored for runtime errors. |
| **`except`** | Catches and handles specific exception classes without terminating the application. |
| **`else`** | Executes only when the `try` block succeeds without raising any exceptions. |
| **`finally`** | Executes unconditionally, useful for cleanup and logging actions. |
| **`ZeroDivisionError`** | Prevents crashes when dividing by zero in mathematical operations. |
| **`ValueError`** | Handles conversion errors (e.g., non-numeric strings passed to `int()` or `float()`). |
| **`TypeError`** | Manages invalid operations between incompatible data types. |
| **`FileNotFoundError`** | Protects file I/O operations when targeting missing files. |
| **`PermissionError`** | Protects file I/O when access rights are restricted. |

---

## 🚀 How to Run the Projects

Ensure you have Python 3.8+ installed on your system. Run any task from the root directory:

```bash
# Task 1
python GenAI-Task1-AtikTambakwale/safe_division_utility.py

# Task 2
python GenAI-Task2-AtikTambakwale/bill_calculator_with_error_handling.py

# Task 3
python GenAI-Task3-AtikTambakwale/custom_exception_age_validator.py

# Task 4 (Enter 'sales_data.txt' when prompted)
python GenAI-Task4-AtikTambakwale/file_reader_with_exception_handling.py

# Task 5 (Enter prices or 'q' to quit)
python GenAI-Task5-AtikTambakwale/safe_shopping_cart.py
```

---

## 👤 Author
- **Atik Tambakwale**

# Python Control Flow — Tasks & Implementations

Comprehensive implementation of Python control flow concepts developed as part of the **GenAI Course**. This repository contains solutions demonstrating conditional decision-making, iterative processing with loops, jump/loop control statements, and interactive command-line interfaces.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Tasks Breakdown](#tasks-breakdown)
  - [Task 1: Discount Rules ]
    (#task-1-discount-ruels)
  - [Task 2: Process Multiple Orders](#task-2-process-multiple-orders)
  - [Task 3: User Menu (while loop + break/continue)](#task-3-user-menu-while-loop-break/continue)
  - [Task 4: Loop Control with Conditions](#task-4-loop-control-with-conditions)
- [Key Python Concepts Covered](#key-python-concepts-covered)
- [How to Run](#how-to-run)
- [Author](#author)

---

## 🔍 Overview

Control flow is the order in which individual statements, instructions, or function calls are executed or evaluated. This project showcases practical applications of:

- **Conditional Branching (`if`, `elif`, `else`)**: Evaluating business logic and discount tiers.
- **Definite Iteration (`for` loops)**: Batch processing collections of transaction records.
- **Indefinite Iteration (`while` loops)**: Driving interactive user menus and continuous execution.
- **Flow Control Statements (`break`, `continue`)**: Filtering data anomalies and gracefully terminating processing pipelines.

---

## 📁 Folder Structure

```text
Python_Control_Flow/
│
├── GenAI-Task1-AtikTambakwale/
│   └── discount_rules.py               # Task 1: Conditional discount & tax engine
│
├── GenAI-Task2-AtikTambakwale/
│   └── processing_multiple_orders.py   # Task 2: Batch order processing & revenue accumulation
│
├── GenAI-Task3-AtikTambakwale/
│   └── user_menu.py                    # Task 3: Interactive CLI menu with while loop
│
├── GenAI-Task4-AtikTambakwale/
│   └── loop_control_and_condition.py   # Task 4: Stream validation with break & continue
│
└── ReadMe.md                           # Project documentation
```

---

## 🚀 Tasks Breakdown

### Task 1: Tiered Discount & Tax Calculator

- **File:** `GenAI-Task1-AtikTambakwale/discount_rules.py`
- **Objective:** Accept a single order amount from the user, evaluate the appropriate discount percentage using multi-branch conditional statements, apply the discount, and calculate the final invoice amount including a 5% tax.

#### Business Logic & Discount Tiers:

| Order Amount Range              | Discount Applied | Formula                                       |
| :------------------------------ | :--------------: | :-------------------------------------------- |
| $\ge 2000$                      |     **15%**      | $\text{Amount} - (\text{Amount} \times 0.15)$ |
| $1500 \le \text{Amount} < 2000$ |     **10%**      | $\text{Amount} - (\text{Amount} \times 0.10)$ |
| $1000 \le \text{Amount} < 1500$ |      **7%**      | $\text{Amount} - (\text{Amount} \times 0.07)$ |
| $< 1000$                        |  **0%** (None)   | No discount applied                           |

**Tax Calculation:** A 5% tax is calculated on top of the discounted amount:
$$\text{Total Amount} = \text{Final Amount} + (\text{Final Amount} \times 0.05)$$

#### Sample Run:

```text
Enter your order Amount: 2200
After Discount 15%,The Final Amount :  1870.0
added 5% Tax ,Total Amount :  1963.5
```

---

### Task 2: Batch Order Processing & Revenue Analytics

- **File:** `GenAI-Task2-AtikTambakwale/processing_multiple_orders.py`
- **Objective:** Process a predefined list of order values (`[1200, 2500, 800, 1750, 3000]`) in batch using a `for` loop. The script dynamically applies discount logic per order, displays an itemized summary, and computes total accumulated revenue.

#### Execution Output:

```text
1200 --> 7% ---> 1116.0
2500 --> 15% ---> 2125.0
800 --> 0% ---> 800
1750 --> 10% ---> 1575.0
3000 --> 15% ---> 2550.0
The Total Revenue Amount After Discounts : 8166.0
```

---

### Task 3: Interactive Menu-Driven Order Manager

- **File:** `GenAI-Task3-AtikTambakwale/user_menu.py`
- **Objective:** Provide an interactive Command-Line Interface (CLI) using an infinite `while True` loop that allows users to dynamically input orders into a running list, compute and review discounted totals at any time, and cleanly exit.

#### Menu Options:

- **`1`**: Prompt the user to enter an order amount and append it to `order_menu_list`.
- **`2`**: Calculate and print each stored order with its applicable discount rate and discounted price, along with the grand total revenue.
- **`q`**: Exit the application cleanly via `break`.
- **Default/Other**: Provide invalid option feedback and prompt again using `continue`.

#### Sample Session:

```text
Menu Option :
1 -- Add order amount to a running list
2 -- Show all orders and totals after applying discounts
q -- Quit
Provide menu option: 1
Add order Amount to a running list : 1800
Order Amount added successfully!

Menu Option :
1 -- Add order amount to a running list
2 -- Show all orders and totals after applying discounts
q -- Quit
Provide menu option: 2
1800 --> 10% ---> 1620.0
Total after discount:  1620.0

Menu Option :
1 -- Add order amount to a running list
2 -- Show all orders and totals after applying discounts
q -- Quit
Provide menu option: q
Exit .........
```

---

### Task 4: Daily Sales Stream & Loop Control

- **File:** `GenAI-Task4-AtikTambakwale/loop_control_and_condition.py`
- **Objective:** Simulate stream ingestion of daily sales numbers (`[200, 150, 0, 400, 50, -1, 300]`) demonstrating fine-grained loop control using `break` and `continue`.

#### Control Flow Rules:

- **`sale_value > 0`**: Valid sale transaction. Added to `total_sales` and running total is printed.
- **`sale_value == 0`**: Non-revenue event. Skipped using `continue` without incrementing sales.
- **`sale_value == -1`**: Corrupted/invalid data sentinel. Halts further processing immediately via `break` (elements following `-1` such as `300` are safely ignored).

#### Execution Output:

```text
adding sales value:  200
Running total sale value :  200
adding sales value:  150
Running total sale value :  350
skipping adding to revenue
adding sales value:  400
Running total sale value :  750
adding sales value:  50
Running total sale value :  800
processing loop due corrupted data value like  -1
The Final Total Daily sales :  800
```

---

## 🛠️ Key Python Concepts Covered

| Category                    | Concept                            | Code Example / Task                                              |
| :-------------------------- | :--------------------------------- | :--------------------------------------------------------------- |
| **Branching**               | `if`, `elif`, `else`               | Multi-tier discount thresholds in Tasks 1, 2, and 3              |
| **Loops**                   | `for ... in ...`                   | Iterating through order lists in Tasks 2 and 4                   |
| **Loops**                   | `while True`                       | Continuous menu loop in Task 3                                   |
| **Loop Control**            | `break`                            | Terminating on menu exit (`Task 3`) or corrupted data (`Task 4`) |
| **Loop Control**            | `continue`                         | Skipping zero sales (`Task 4`) and re-prompting menu (`Task 3`)  |
| **Data Structures**         | `list`, `.append()`                | Dynamic order list accumulation in Task 3                        |
| **Input / Type Conversion** | `input()`, `int()`, `isinstance()` | Reading and validating user input in Tasks 1 and 3               |
| **Output Formatting**       | F-strings (`f"{var}"`)             | Structured receipt outputs in Tasks 2 and 3                      |

---

## 💻 How to Run

Ensure Python 3.8 or higher is installed. Open a terminal in the root directory of the project:

### Run Task 1

```bash
python GenAI-Task1-AtikTambakwale/discount_rules.py
```

### Run Task 2

```bash
python GenAI-Task2-AtikTambakwale/processing_multiple_orders.py
```

### Run Task 3

```bash
python GenAI-Task3-AtikTambakwale/user_menu.py
```

### Run Task 4

```bash
python GenAI-Task4-AtikTambakwale/loop_control_and_condition.py
```

---

## 👤 Author

- **Developer:** Atik Tambakwale
- **Course:** GenAI Course — Python Control Flow Module

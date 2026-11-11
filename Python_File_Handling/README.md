# Python File Handling - GenAI Course Tasks

A collection of hands-on Python exercises focused on core file handling concepts, file pointer manipulation, formatted reporting, and defensive programming.

**Author:** Atik Tambakwale  
**Environment:** Python 3.x

---

## 📁 Repository Structure

```text
Python_File_Handling/
│
├── GenAI-Task1-AtikTambakwale/
│   ├── write_sales_record_to_a_file.py   # Basic file writing (newline and comma separated) & reading
│   └── sales_data.txt                   # Sales data output file
│
├── GenAI-Task2-AtikTambakwale/
│   ├── read_files_in_different_ways.py   # Demonstrates read(), readline(), readlines(), and f.seek(0)
│   └── sales_data.txt                   # Sample sales numbers
│
├── GenAI-Task3-AtikTambakwale/
│   ├── append_new_sales.py              # Appending data in 'a' mode and counting lines
│   └── sales_data.txt                   # Sales data file with appended entries
│
├── GenAI-Task4-AtikTambakwale/
│   ├── generate_summary_report_from_file.py # Reading numeric data & generating summary statistics
│   └── sales_data.txt                   # Sales numbers dataset
│
├── GenAI-Task5-AtikTambakwale/
│   ├── create_product_info_file.py      # Capturing dynamic user input and storing pipe-delimited records
│   └── products_data.txt                # Delimited product catalog (Product|Price)
│
├── GenAI-Task6-AtikTambakwale/
│   ├── read_file_safely.py              # Defensive file reading checking file existence via os.path.exists()
│   ├── products_data.txt                # Sample product data
│   └── sales_data.txt                   # Sample sales data
│
├── GenAI-Task7-AtikTambakwale/
│   ├── export_discounted_prices.py      # Processing dictionary prices, applying discounts, and generating a report
│   └── discount_report.txt              # Formatted export (Product|OriginalPrice|DiscountedPrice)
│
└── README.md                            # Project documentation
```

---

## 📝 Task Descriptions & Code Highlights

### Task 1: Writing Sales Records to a File

- **Folder:** `GenAI-Task1-AtikTambakwale/`
- **File:** `write_sales_record_to_a_file.py`
- **Concepts:** Standard `open()` and `close()`, write mode (`"w"`), read mode (`"r"`), writing newline-delimited (`\n`) and comma-delimited (`,`) data.
- **Description:** Writes a list of sales integers to `sales_data.txt`, verifies by reading the contents, and repeats with comma-separated formatting.

---

### Task 2: Reading Files in Different Ways

- **Folder:** `GenAI-Task2-AtikTambakwale/`
- **File:** `read_files_in_different_ways.py`
- **Concepts:** Context manager (`with open(...) as f`), `f.read()`, `f.readline()`, `f.readlines()`, and file pointer management with `f.seek(0)`.
- **Description:** Demonstrates the three distinct file reading methods in Python. Highlights the importance of resetting the file pointer (`f.seek(0)`) so subsequent reads do not hit EOF prematurely.

---

### Task 3: Appending New Sales Records

- **Folder:** `GenAI-Task3-AtikTambakwale/`
- **File:** `append_new_sales.py`
- **Concepts:** Append mode (`"a"`), line-by-line reading, data cleaning with `.strip()`, string-to-integer conversion, and `len()`.
- **Description:** Appends new sales transactions to `sales_data.txt` without overwriting existing entries. Computes and displays the total number of records after appending.

---

### Task 4: Generating Summary Report from Sales Data

- **Folder:** `GenAI-Task4-AtikTambakwale/`
- **File:** `generate_summary_report_from_file.py`
- **Concepts:** Data aggregation, statistical calculations (`sum()`, `max()`, `min()`, average).
- **Description:** Reads numerical data from `sales_data.txt`, converts the lines into integers, and calculates:
  - **Total Sales**
  - **Highest Sale**
  - **Lowest Sale**
  - **Average Sale**

---

### Task 5: Dynamic Product Information File

- **Folder:** `GenAI-Task5-AtikTambakwale/`
- **File:** `create_product_info_file.py`
- **Concepts:** User input (`input()`), while-loop iteration, structured formatting with custom delimiters (`|`), writing and re-reading formatted lines.
- **Description:** Prompts the user to enter product names and prices, writes them in a pipe-delimited format (`Product|Price`), and prints the saved catalog.

---

### Task 6: Safe File Reading with Validation

- **Folder:** `GenAI-Task6-AtikTambakwale/`
- **File:** `read_file_safely.py`
- **Concepts:** Defensive programming, `os.path.exists()`, graceful error handling.
- **Description:** Asks the user for a target filename and verifies its existence on disk prior to attempting to open it, preventing unhandled `FileNotFoundError` exceptions.

---

### Task 7: Discount Calculation and Report Export

- **Folder:** `GenAI-Task7-AtikTambakwale/`
- **File:** `export_discounted_prices.py`
- **Concepts:** Dictionary traversal, percentage arithmetic, formatted multi-column export, aggregate calculation.
- **Description:** Takes an existing product-price dictionary, prompts for a discount percentage, calculates the discounted amounts, writes a pipe-separated report (`Product|ActualPrice|DiscountedPrice`), and computes average discounted prices.

---

## 🛠️ Summary of Key Python Concepts Covered

| Concept               | Python Syntax / Function        | Purpose                               |
| :-------------------- | :------------------------------ | :------------------------------------ |
| **Write Mode**        | `open("file.txt", "w")`         | Creates or truncates file to write    |
| **Read Mode**         | `open("file.txt", "r")`         | Opens file for reading                |
| **Append Mode**       | `open("file.txt", "a")`         | Adds content without truncating       |
| **Context Manager**   | `with open(...) as f:`          | Automatically closes file handles     |
| **File Navigation**   | `f.seek(0)`                     | Resets cursor back to file beginning  |
| **Full Read**         | `f.read()`                      | Reads entire content as single string |
| **Single Line Read**  | `f.readline()`                  | Reads one line at a time              |
| **All Lines Read**    | `f.readlines()`                 | Returns a list of lines               |
| **Path Verification** | `os.path.exists(path)`          | Checks if target file exists          |
| **Data Parsing**      | `.strip()`, `int()`, `.split()` | Cleans whitespace and casts types     |

---

## 🚀 How to Run

1. Clone or navigate into the root directory:

   ```bash
   cd "Python_File_Handling"
   ```

2. Run any task directly with Python:

   ```bash
   # Run Task 1
   python "GenAI-Task1-AtikTambakwale/write_sales_record_to_a_file.py"

   # Run Task 2
   python "GenAI-Task2-AtikTambakwale/read_files_in_different_ways.py"

   # Run Task 3
   python "GenAI-Task3-AtikTambakwale/append_new_sales.py"

   # Run Task 4
   python "GenAI-Task4-AtikTambakwale/generate_summary_report_from_file.py"

   # Run Task 5
   python "GenAI-Task5-AtikTambakwale/create_product_info_file.py"

   # Run Task 6
   python "GenAI-Task6-AtikTambakwale/read_file_safely.py"

   # Run Task 7
   python "GenAI-Task7-AtikTambakwale/export_discounted_prices.py"
   ```

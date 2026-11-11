# Python Data Structures — GenAI Course Tasks

A collection of practical Python exercises demonstrating fundamental and combined data structures, including **Lists**, **Tuples**, **Sets**, and **Dictionaries**.

---

## 📁 Repository Structure

```text
Python_Data_Structure/
├── GenAI-Task1-AtikTambakwale/
│   └── product_collection.py       # Lists, Tuples, Indexing & Mutability
├── GenAI-Task2-AtikTambakwale/
│   └── categories.py               # Sets, Deduplication & Membership Testing
├── GenAI-Task3-AtikTambakwale/
│   └── product_pricing.py          # Dictionaries, CRUD Operations & Aggregation
├── GenAI-Task4-AtikTambakwale/
│   └── combined_operations.py      # Complex Data Structures & Categorization
└── README.md                       # Project documentation
```

---

## 📚 Task Breakdown

### 1. Task 1: Lists & Tuples (`GenAI-Task1-AtikTambakwale/product_collection.py`)
Focused on indexing, element manipulation, and handling immutability in tuples.

- **Key Operations**:
  - **List Indexing**: Accessing the second (`products[1]`) and last element (`products[len(products)-1]`).
  - **List Modification**: Appending new items (`pen`, `cabinet`) to the list.
  - **Tuple Immutability Workaround**: Converting an immutable tuple `("casio", 1300, "fashion")` into a list to update a value (price updated to `1350`), and converting it back into a tuple.

---

### 2. Task 2: Sets & Membership (`GenAI-Task2-AtikTambakwale/categories.py`)
Demonstrates unique collections, automatic deduplication, and fast lookup operations.

- **Key Operations**:
  - **Set Conversion**: Converting a list of product categories containing duplicates into a unique `set`.
  - **Deduplication Demonstration**: Attempting to add an existing category (`Accessories`) to show that sets enforce unique values.
  - **Membership Testing**: Checking item presence using the `in` operator (`"Electronics" in categories_set` returns `True`, `"Clothing" in categories_set` returns `False`).
  - **Length Calculation**: Counting total unique categories via `len()`.

---

### 3. Task 3: Dictionaries & Aggregation (`GenAI-Task3-AtikTambakwale/product_pricing.py`)
Covers dictionary key-value pair management and basic statistical calculations.

- **Key Operations**:
  - **Dictionary Initialization**: Creating a product-to-price lookup table.
  - **Insertion**: Adding a new product (`products["pen"] = 10`).
  - **Update**: Modifying an existing product's price (`products["book"] = 300`).
  - **Deletion**: Removing an item with the `del` keyword (`del products["pen"]`).
  - **Aggregation**: Computing the average product price using `sum(products.values()) / len(products)`.

---

### 4. Task 4: Combined Operations & Grouping (`GenAI-Task4-AtikTambakwale/combined_operations.py`)
Demonstrates working with composite structures by transforming a catalog of tuples into a grouped dictionary.

- **Key Operations**:
  - **Tuple Catalog**: Storing records as a list of tuples: `[(product, price, category), ...]`.
  - **Grouping / Inverted Index**: Iterating over the catalog to group products by category inside a dictionary (`category_to_product`), where each category maps to a list of product names.
  - **Category Query**: Extracting all products matching a specific category (`category_to_product["electronics"]`).

---

## 🚀 Running the Code

Each script can be run independently using Python 3:

```bash
# Task 1: Product Collection
python GenAI-Task1-AtikTambakwale/product_collection.py

# Task 2: Categories
python GenAI-Task2-AtikTambakwale/categories.py

# Task 3: Product Pricing
python GenAI-Task3-AtikTambakwale/product_pricing.py

# Task 4: Combined Operations
python GenAI-Task4-AtikTambakwale/combined_operations.py
```

---

## 🧠 Summary of Data Structures Covered

| Data Structure | Ordered | Mutable | Allows Duplicates | Primary Use Case |
| :--- | :---: | :---: | :---: | :--- |
| **List** (`[]`) | Yes | Yes | Yes | Ordered sequences, dynamic collections |
| **Tuple** (`()`) | Yes | No | Yes | Fixed records, immutable sequences |
| **Set** (`set()`) | No | Yes | No | Uniqueness, deduplication, membership testing |
| **Dictionary** (`{}`) | Yes* | Yes | Keys: No / Values: Yes | Key-value lookup, associative mapping, grouping |

*\* Dictionaries maintain insertion order as of Python 3.7+.*


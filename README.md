# Date Converter

A Python utility designed to read a text file, locate specific date patterns using Regular Expressions, and transform their layout efficiently.

---

## Project Overview

The **Date Converter** script automates the process of finding dates in a traditional `DD-MM-YYYY` format within text files and swapping them into an international `YYYY-MM-DD` standard format using Python's built-in `re` module[cite: 1].

---

## Features

* **File I/O Handling**: Dynamically opens and reads raw text data from a designated file path (`sample 5.txt`)[cite: 1].
* **Advanced Regular Expressions**: Utilizes robust regex patterns (`\b(\d{2})-(\d{2})-(\d{4})\b`) to isolate and capture day, month, and year components into discrete regex groups[cite: 1].
* **Automated Substitution**: Employs `re.sub()` to reorder the captured groups (`\3-\2-\1`), seamlessly converting the date layout[cite: 1].
* **Clean Output Presentation**: Clearly displays the final transformed date string via the console[cite: 1].

---

## Code Structure

* `file(filepath)`: Opens the target text file and returns its complete content as a string[cite: 1].
* `pattern(text)`: Defines the regex rules and executes the search-and-replace conversion logic[cite: 1].
* `main()`: Orchestrates the execution flow by loading the file, running the date transformation, and printing the results[cite: 1].

---

## Requirements

* Python 3.x (Uses only the standard built-in `re` library; no external packages needed)[cite: 1].

---

## Usage Instructions

1. Ensure your source text file is named `sample 5.txt` and placed in the same directory as the script[cite: 1].
2. Open your terminal or command prompt in the project directory.
3. Run the script using the command:
   ```bash
   python "Date converter.py"

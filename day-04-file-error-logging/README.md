# Day 4: File Handling, JSON, CSV, Exceptions and Logging

## Topics Covered

- File handling
- Reading and writing text files
- CSV files
- `csv.DictReader`
- JSON files
- `json.load()` and `json.dump()`
- Custom exceptions
- `try`, `except`, and `finally`
- `ValueError` and `FileNotFoundError`
- Logging
- `logging` module
- `FileHandler`
- Data validation
- Processing and filtering data

## Exercises

1. Line & Word Counter
2. Inventory Value from CSV
3. Filtering a JSON Library Catalog
4. Custom Exception for User Registration
5. Order Pipeline with Logging

## What I Learned

During Day 4, I learned how to work with text, CSV, and JSON files using Python. I also learned how to handle errors using exceptions and create custom exceptions.

I practiced using csv.DictReader, JSON processing, logging, and data validation to build programs that can safely process real-world data.

## Challenges Faced

One challenge I faced was handling different data types when reading CSV and JSON files because CSV values are read as strings. I also found custom exceptions, error handling, and logging challenging at first.

I solved these challenges by testing different inputs and carefully checking the errors and output produced by each program.

## Key Takeaways
    Files can be safely handled using with open().
    CSV data needs to be converted from strings to appropriate data types.
    JSON can be loaded and saved using Python's json module.
    Exceptions help programs handle unexpected situations.
    Custom exceptions can be created for specific validation errors.
    Logging helps track errors and successful operations.
    Data validation is important when processing real-world datasets.

## How to Run

First look at the file structure because you should be inside the `day-04-file-error-logging` folder.

Run the Python file using the following command:

```bash
python exercise-01-line-word-counter.py
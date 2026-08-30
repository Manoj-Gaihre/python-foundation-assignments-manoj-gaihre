# day-05&06-assignment: Comprehensions and Mini Log Analyzer

## Topics Covered

* List comprehensions
* Set comprehensions
* Dictionary comprehensions
* Generator expressions
* Nested comprehensions
* Filtering data with comprehensions
* Working with strings
* Processing log data
* Extracting values from log lines
* Counting log levels
* Building a mini log analyzer

## Practice Exercises

### Easy

1. Build a list of cubes of numbers from 1 through 10 using a list comprehension.
2. Strip surrounding whitespace from strings using a list comprehension.
3. Create a set of unique vowels from a given string.

### Medium

1. Use a dictionary comprehension to determine whether numbers are even.
2. Build a dictionary mapping words to their lengths, filtering words longer than 3 characters.
3. Use a generator expression to calculate the sum of squares from 1 to 100 without creating a list.

### Hard

1. Flatten a 2D list using a nested comprehension while keeping only even values.
2. Invert a dictionary and understand what happens when duplicate values exist.
3. Build a dictionary containing counts of `INFO`, `WARN`, and `ERROR` log levels.

## Challenge Project

### Mini Log Analyzer

Built a small log analyzer that processes server log lines using comprehensions.

The analyzer performs the following tasks:

1. Extracts all `ERROR` log lines.
2. Finds the unique users mentioned in the logs.
3. Counts the number of `INFO`, `WARN`, and `ERROR` log entries.
4. Identifies login failures and returns `(user, msg)` pairs.

## How to Run

First look at the file structure because you should be inside the `day-05&06-assignment` folder.

Run the Python file using:

```bash
python comprehension.py
```

If the program reads from a log file, make sure `server.log` is present in the correct folder.

## What I Learned

During Day 3, I learned how to use list, set, and dictionary comprehensions to write shorter and cleaner Python code. I also learned how generator expressions can process data without creating a complete list in memory.

I practiced applying comprehensions to real-world log data by filtering errors, finding unique users, counting log levels, and identifying login failures.

## Challenges Faced

One challenge I faced was understanding nested comprehensions and generator expressions. I also found it challenging to extract specific information from log lines and combine filtering with comprehensions.

I solved these challenges by breaking the problem into smaller steps and testing each comprehension separately.

## Key Takeaways

* List comprehensions are useful for creating filtered or transformed lists.
* Set comprehensions help find unique values.
* Dictionary comprehensions create dictionaries efficiently.
* Generator expressions are useful for memory-efficient processing.
* Nested comprehensions can process nested data structures.
* Comprehensions can be useful for practical data-processing tasks.
* Log analysis can be performed by filtering, extracting, and counting information from log files.

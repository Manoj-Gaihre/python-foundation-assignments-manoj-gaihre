# Day 2: Loops and Data Structures

## Topics Covered

- `for` loops
- `while` loops
- `range()`
- `break`
- `continue`
- Modulo operator (`%`)
- `isinstance()`
- Lists
- List comprehensions
- Dictionaries
- Dictionary comprehensions
- Nested dictionaries
- Sets
- Set operations
- Dictionary methods
- User input
- Menu-driven programs

## Exercises Completed

1. Batch Processor
2. Retry Simulation
3. Clean Numeric Values
4. Sales List Analysis
5. Dataset Comparison
6. Student Score Dictionary
7. Nested Order Summary
8. Stretch Exercise: Contact Book Menu

## Exercise Overview

### Exercise 1: Batch Processor

Used a `for` loop and `range()` to process batches from 1 to 10.

Used the modulo operator to display a checkpoint after every third batch.

### Exercise 2: Retry Simulation

Used a `while` loop to simulate a process with a maximum of three attempts.

Used `break` to stop the loop when the operation succeeds.

### Exercise 3: Clean Numeric Values

Worked with a list containing valid integers, `None`, and invalid string values.

Used:

- `for` loop
- `continue`
- `isinstance()`
- List comprehension

to create a list containing only valid integer values.

### Exercise 4: Sales List Analysis

Analyzed a monthly sales list by:

- Sorting sales from highest to lowest
- Filtering sales above 100000
- Adding 13% tax
- Calculating total sales
- Calculating average sales

Used list comprehensions where appropriate.

### Exercise 5: Dataset Comparison

Used Python sets to compare two datasets.

Performed:

- Union
- Intersection
- Difference

to identify unique and common dataset names.

### Exercise 6: Student Score Dictionary

Created a dictionary containing student names and scores.

Performed:

- Iteration through dictionary items
- Filtering students who passed
- Finding the highest score
- Calculating the average score
- Dictionary comprehension

### Exercise 7: Nested Order Summary

Worked with nested dictionaries containing order information.

Performed:

- Customer and order ID extraction
- Filtering completed orders
- Calculating completed order amounts
- Counting pending orders
- Adding a new order

### Stretch Exercise: Contact Book

Built an interactive contact book using a `while` loop.

The program supports:

- Adding contacts
- Searching contacts
- Deleting contacts
- Displaying all contacts
- Exiting the program

Contacts are stored using nested dictionaries.

The program also handles missing contacts without crashing.

## What I Learned

During Day 2, I learned how loops can be used to repeatedly process data and how `break` and `continue` can control loop execution.

I also learned how to work with Python data structures such as lists, dictionaries, sets, and nested dictionaries. List and dictionary comprehensions helped me write more concise code for filtering and transforming data.

The Contact Book exercise helped me understand how loops, conditional statements, user input, and dictionaries can be combined to build a simple interactive application.

## Challenges Faced

One of the challenges I faced was understanding how list comprehensions work, especially the difference between creating a list of values and creating a list of Boolean results.

I also had to understand how nested dictionaries are accessed and updated. Working on the Contact Book helped me understand how to store user-entered data inside an empty dictionary and retrieve, update, and delete that data.

Another challenge was understanding how dictionary methods such as `.items()`, `.get()`, `.update()`, and `del` can be used when working with structured data.

## How to Run

Make sure Python is installed on your system.

Run each exercise from the terminal using:

```bash
python exercise-01-batch-processor.py
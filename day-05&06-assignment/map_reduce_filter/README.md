# Day 6: Higher-Order Functions, Lambda, Map, Filter, Reduce and Dispatch Tables

## Topics Covered

* Lambda functions
* Higher-order functions
* `map()`
* `filter()`
* `reduce()`
* `sorted()` with `key=`
* `max()` and `min()` with `key=`
* Dispatch tables
* Dictionary-based function lookup
* Function calls using `ops[op](a, b)`

## Exercises

1. Lambda Function and `def`
2. `map()` and `filter()` with Lists
3. Sorting with `key=`
4. Finding Maximum and Minimum with `key=`
5. Calculator Using a Dispatch Table
6. Product and Flattening Using `reduce()`
7. Custom `my_max()` Using `reduce()`
8. Sales Processing Pipeline Using `map()`, `filter()`, `reduce()`, and `sorted()`
9. Alternative Calculator Using a Dispatch Table

## Challenge Project

Built a sales processing pipeline that:

* Used `map()` to calculate the total for each sale.
* Used `filter()` to keep sales with a total of at least 50.
* Used `reduce()` to calculate the grand total revenue.
* Used `sorted()` to arrange the filtered sales from highest to lowest total.
* Used a dispatch table to select and execute calculator operations.

## How to Run

First, make sure you are inside the Day 6 assignment folder.

Run the Python file using:

```bash
python filename.py
```

For example:

```bash
python higher-order-functions.py
```

If the exercises are separated into multiple files, run each file using:

```bash
python exercise-01.py
```

## What I Learned

During Day 6, I learned how lambda functions and higher-order functions can make Python code shorter and more flexible. I learned that `map()` is used to transform data, `filter()` is used to select data based on a condition, and `reduce()` is used to combine multiple values into one final result.

I learned how `map()` can add a new `total` field to each sales record using `qty * price`. I also learned how `reduce()` uses an accumulator to process values one by one and calculate a final result such as total revenue.

I learned how dispatch tables can store functions inside a dictionary. Using `ops[op](a, b)`, Python first finds the function associated with the operator and then calls that function with `a` and `b`.

## Challenges Faced

One challenge was understanding how `map()`, `filter()`, and `reduce()` work together in the sales pipeline. I learned that `map()` and `filter()` return iterators, so an iterator can be exhausted after being consumed by `reduce()`. Converting the result to a list allows it to be reused for other operations such as sorting.

Another challenge was understanding `reduce()`, especially the difference between the accumulator (`acc`) and the current item (`r`). I learned how the accumulator stores the result calculated so far and is updated during each step.

I also had to understand how `ops[op](a, b)` works in a dispatch table. I learned that `ops[op]` retrieves the function from the dictionary, while `(a, b)` calls that function and performs the actual calculation.

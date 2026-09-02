# Day 5: Iterators and Generators

## Topics Covered

- Iterators
- `iter()` and `next()`
- `StopIteration`
- Generator functions
- `yield`
- Generator expressions
- Lazy evaluation
- Memory efficiency
- Infinite generators
- `itertools.islice`
- Generator pipelines

## Exercises

1. Iterator using `iter()` and `next()`
2. `count_up()` Generator
3. Even Numbers Generator
4. List Comprehension vs Generator Expression
5. Three-Value Sliding Window Generator
6. Safe `Number` Iterator with a Limit
7. `read_chunks()` Generator

## Challenge Project

### Memory-Efficient Log/CSV Processor + Infinite Number Generator

The challenge project was divided into two parts:

- **Part A:** Built a lazy generator pipeline to read, parse, and filter log/CSV records without loading the entire file into memory.
- **Part B:** Created an infinite Fibonacci generator and a `take()` helper to safely retrieve a fixed number of values.

## How to Run

First, make sure you are inside the iterator_generator assignment folder.

Run the Python files cell using:

```bash
Shift + Enter
```

## What I Learned

During Day 5, I learned how iterators and generators work using iter(), next(), yield, and StopIteration. I also learned how generators provide lazy evaluation and help reduce memory usage when processing large amounts of data.

I practiced creating generator functions, generator expressions, sliding windows, file-reading generators, and infinite generators such as Fibonacci.

## Challenges Faced

One challenge was understanding the difference between a list and a generator and how generators produce values only when requested. I also practiced handling StopIteration and updating multiple variables using tuple assignment such as a, b = b, a + b.

Another challenge was understanding how generator pipelines can process large files efficiently without storing the entire file in memory.
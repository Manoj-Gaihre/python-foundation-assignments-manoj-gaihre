# Month 2 — Week 1: Git, NumPy & Pandas

## Topics Covered

* Git fundamentals and version control
* Working directory, staging area, and repository
* Git initialization and cloning
* Commits and meaningful commit messages
* Git status, log, and diff
* Remote repositories and origin
* Git push, pull, and fetch
* Branching and merging
* Merge conflicts and Pull Requests
* GitHub Issues, labels, and assignees
* Project structure and `.gitignore`
* Environment variables and secrets
* Virtual environments and requirements.txt
* Force push and force-with-lease
* NumPy arrays and array attributes
* Array reshaping and flattening
* Indexing and slicing
* Boolean masking
* Views and copies
* Vectorization and performance comparison
* Broadcasting
* Matrix multiplication
* Aggregation along axes
* Reproducible randomness and train/test splitting
* Using np.where(), argmax(), and argmin()
* Pandas Series and DataFrames
* Loading and inspecting CSV data
* Selecting rows and columns
* Boolean filtering and query()
* Cleaning inconsistent text data
* Handling missing values
* Removing duplicate records
* Parsing and extracting date information
* Sorting and renaming columns
* Creating derived columns
* Converting columns to category dtype
* Grouping and aggregating data
* Creating pivot tables
* Exporting summary results to CSV

## Exercises

### Part A — Git & Project Foundations

1. Git Working Directory, Staging Area and Repository
2. git init vs git clone
3. Commits and Git Identity
4. git status, git log and git diff
5. Writing Meaningful Commit Messages
6. Local Repository and Remote origin
7. git fetch vs git pull
8. Branching and Collaboration
9. Merge Conflicts
10. Pull Requests
11. GitHub Issues and Linking Work
12. .gitignore
13. .env and .env.example
14. Virtual Environments and requirements.txt
15. git push --force vs --force-with-lease

### Part B — NumPy

1. Array Anatomy and Reshaping
2. Indexing and Slicing
3. Boolean Masks
4. Views vs Copies
5. Vectorization vs a Python Loop
6. Broadcasting
7. Matrix Multiplication
8. Aggregating Along an Axis
9. Reproducible Randomness and Train/Test Split
10. np.where(), argmax() and argmin()

### Part C — Pandas

1. Creating Series and DataFrames by Hand
2. Loading and Inspecting CSV Data
3. Selecting Rows and Columns
4. Boolean Filtering
5. Cleaning Inconsistent Text
6. Handling Missing Values
7. Removing Duplicate Rows
8. Working with Dates
9. Sorting and Renaming Columns
10. Creating Derived Columns
11. Data Types and Memory Usage
12. Aggregation and Summary Tables

### Bonus Exercises

1. Build a Reporting Pipeline using load(), clean(), and summarise()
2. Analyze how Cleaning Decisions Can Mislead Conclusions

## How to Run

First look at the file structure because you should be inside the `assignment-1` assignment folder.

Create and activate a virtual environment:

```bash
python -m venv assignment1
```

For Windows:

```bash
assignment1\Scripts\activate
```

Install the required packages using:

```bash
pip install -r requirements.txt
```

Generate the CSV dataset:

```bash
python data/make_data.py
```

Run the NumPy assignment:

```bash
python answers/02_numpy.py
```

Run the Pandas notebook:

```bash
jupyter nbconvert --execute --to notebook --inplace answers/03_pandas.ipynb
```

## What I Learned

During Month 2 — Week 1, I learned the fundamentals of Git, NumPy, and Pandas through practical exercises and written explanations.

I learned how Git manages changes using the working directory, staging area, and repository. I also practiced understanding commits, branches, remote repositories, Pull Requests, merge conflicts, and the importance of `.gitignore`, virtual environments, and secure environment variables.

I learned how to work with NumPy arrays, inspect their dimensions and shapes, reshape and slice arrays, apply Boolean masks, and perform vectorized calculations efficiently without unnecessary loops.

I also practiced broadcasting, matrix multiplication, aggregations along different axes, reproducible random operations, and using functions such as `np.where()`, `argmax()`, and `argmin()`.

Using Pandas, I learned how to load and inspect CSV data, select and filter records, clean inconsistent text, handle missing values, remove duplicates, parse dates, and create derived columns.

I learned how to group data, calculate statistics, create pivot tables, optimize memory usage with categorical data types, and export summary results to CSV files.

## Challenges Faced

* One challenge I faced was understanding the difference between the working directory, staging area, and repository in Git. I solved this by practicing the Git workflow and learning how changes move from one stage to another.

* Another challenge was understanding the difference between NumPy views and copies. Modifying a view can change the original array, so I practiced using `.copy()` when an independent array was required.

* Working with broadcasting and matrix multiplication was challenging because the array dimensions must align correctly. I improved my understanding by checking array shapes and practicing operations with different dimensions.

* Cleaning the Pandas dataset was another challenge, especially handling inconsistent city spellings, missing values, duplicate rows, and impossible marks. I solved these challenges by inspecting the data carefully and applying appropriate cleaning methods.

* Understanding the difference between `loc` and `iloc`, especially how they handle slicing endpoints, was also challenging. I practiced both methods to understand label-based and position-based selection.

* Another challenge was working with Git branches, merge conflicts, and remote repositories. I learned how to manage changes carefully and understand the importance of collaboration workflows.

## Key Takeaways

* Git helps track changes and supports organized collaboration on software projects.
* Meaningful commit messages make project history easier to understand.
* Branches and Pull Requests support safer and more organized teamwork.
* `.gitignore` helps prevent unnecessary files and sensitive information from being committed.
* Virtual environments and requirements.txt help maintain reproducible Python projects.
* NumPy provides efficient tools for numerical computing using arrays.
* Vectorization is generally more efficient than unnecessary Python loops for numerical operations.
* Broadcasting allows operations between compatible arrays without manually repeating data.
* Array shapes and dimensions are important when performing mathematical operations.
* Pandas makes it easier to clean, transform, analyze, and summarize structured datasets.
* Missing values should be handled according to their meaning in the dataset.
* Duplicate records and inconsistent text can affect the accuracy of analysis.
* GroupBy and pivot_table are useful for calculating statistics across categories.
* Data types such as category can help reduce memory usage when appropriate.
* Clean, reproducible, and well-documented projects are important for data science workflows.

## Project Structure

```text
assignment-1/
├── answers/
│   ├── 01_git_theory.ipynb
│   ├── 02_numpy.ipynb
│   └── 03_pandas.ipynb
├── data/
│   ├── make_data.py
│   └── scores_raw.csv
├── outputs/
│   └── summary.csv
├── requirements.txt
└── README.md
```


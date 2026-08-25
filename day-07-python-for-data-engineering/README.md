# Day 5: Pandas, Data Cleaning, Grouping and APIs

## Topics Covered

- Loading CSV data with Pandas
- Working with DataFrames
- Parsing dates
- Handling missing values
- Creating boolean columns
- Data cleaning
- Filtering data
- Grouping data
- Calculating averages and totals
- Sorting results
- Merging DataFrames
- Calling a public API using `requests`
- Parsing JSON responses
- API error handling and fallback
- Creating DataFrames from API data

## Exercises

1. Load and Get Oriented
2. Clean the Data
3. Average Late Fees by Genre
4. Look Up Book Information Using Open Library API
5. Total Late Fees by Author

## How to Run

First look at the file structure because you should be inside the `day-05` assignment folder.

Install the required packages using:

```bash
pip install -r requirements.txt
```

## What I Learned

During Day 5, I learned how to load, clean, filter, group, and merge data using Pandas. I also practiced handling missing values correctly and working with dates and boolean columns.

I learned how to call a public API using requests, extract information from JSON responses, and use a fallback when an API request fails.

Differences between the isnull() and notna().

## Challenges Faced

- One challenge I faced was handling missing values correctly, especially understanding that a missing return_date represents a book that is still checked out rather than bad data.

- Another challenge was working with API responses and combining the returned book information with the library checkout data. I solved these challenges by checking the data structure and processing each step carefully.

- Another challenge was the Assetion Error.

## Key Takeaways
- Pandas makes it easier to work with structured datasets.
- Missing values should be handled according to their meaning.
- Boolean columns can help represent data states clearly.
- groupby() can be used to calculate statistics for different categories.
- DataFrames can be merged using common columns.
- APIs allow programs to retrieve external data.
- JSON responses can be parsed and converted into useful DataFrame data.
- Fallback logic helps make programs more reliable when an API request fails.
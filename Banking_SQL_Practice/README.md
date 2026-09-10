# Day 9: Advanced SQL and Banking Data Analysis

## Topics Covered

- SQL JOINs
- INNER JOIN
- LEFT JOIN
- FULL OUTER JOIN
- GROUP BY and HAVING
- Aggregate Functions
- Subqueries
- Correlated Subqueries
- EXISTS and NOT EXISTS
- IN
- UNION, UNION ALL
- INTERSECT and EXCEPT
- CTEs
- Views and Materialized Views
- Window Functions
- ROW_NUMBER()
- RANK() and DENSE_RANK()
- LAG() and LEAD()
- Running Totals
- NTILE()
- CASE WHEN
- Data Quality Checks
- PostgreSQL Transactions
- BEGIN, COMMIT and ROLLBACK
- PostgreSQL with Python

## Exercises

1. Find Active accounts with customer details.
2. Find customers without accounts.
3. Find orphaned accounts.
4. Combine customers and accounts using FULL OUTER JOIN.
5. Join customers, accounts and transactions.
6. Calculate total balance by branch.
7. Find the top 5 branches by Active account balance.
8. Find account types with average balance above 50,000.
9. Find customers with more than one account.
10. Find the branch and account type with the highest transaction amount.
11. Compare customer balances with the overall average.
12. Find accounts above their account-type average.
13. Find customers with Withdrawal transactions using EXISTS.
14. Find accounts without transactions using NOT EXISTS.
15. Find customers from cities having more than 3 customers.
16. Calculate account count and average balance by branch using a subquery.
17. Practice UNION.
18. Practice UNION ALL.
19. Practice INTERSECT.
20. Practice EXCEPT.
21. Calculate account transaction totals using CTEs.
22. Find the highest-balance account in each branch.
23. Use multiple CTEs to compare deposits with balances.
24. Create an Active accounts view.
25. Create and refresh a materialized view.
26. Find the latest transaction using ROW_NUMBER().
27. Rank customers using RANK().
28. Rank branches using DENSE_RANK().
29. Find previous transactions using LAG().
30. Find next transactions using LEAD().
31. Calculate running transaction totals.
32. Find duplicate customer records.
33. Find missing and orphaned records.
34. Categorize Active accounts using CASE WHEN.
35. Practice safe transactions using BEGIN, COMMIT and ROLLBACK.
36. Divide customers into income quartiles using NTILE().
37. Find low-credit customers with high account balances.
38. Find flagged transactions.
39. Find customers with expired KYC and Active accounts.
40. Find joint accounts above their branch average.

## Assignment Project

Worked with a **banking database containing customers, accounts, and transactions**.

The project focused on analyzing banking data using advanced PostgreSQL queries, including joins, aggregations, subqueries, CTEs, set operations, views, window functions, data quality checks, and transactions.

SQL queries were executed using PostgreSQL and Python.

## What I Learned

During Day 9, I learned how to use SQL JOINs to combine data from multiple tables.

- I learned how `GROUP BY`, `HAVING`, `SUM()`, `COUNT()`, and `AVG()` can be used for data analysis.

- I practiced subqueries, correlated subqueries, `EXISTS`, `NOT EXISTS`, and set operations such as `UNION`, `INTERSECT`, and `EXCEPT`.

- I learned how CTEs and views can make complex SQL queries easier to organize.

- I also practiced window functions such as `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LAG()`, `LEAD()`, running totals, and `NTILE()`.

- Finally, I learned how to identify duplicate, missing, and orphaned data and how to safely modify data using SQL transactions.

## Challenges Faced

- One challenge was understanding the differences between `INNER JOIN`, `LEFT JOIN`, and `FULL OUTER JOIN`.

- I also found correlated subqueries and window functions such as `LAG()`, `LEAD()`, and `RANK()` challenging at first.

- Another challenge was understanding `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT` and when to use each one.

- Handling orphaned accounts and missing customer information also helped me understand real-world data quality problems.

- I also learned the importance of using `BEGIN`, `COMMIT`, and `ROLLBACK` when performing multiple database changes safely.

## Tools Used

- PostgreSQL
- Python
- VS Code
- Jupyter Notebook
- SQL
- psycopg

## Summary

Day 9 helped me move from basic SQL queries to **advanced SQL and real-world banking data analysis**.

I practiced joins, aggregations, subqueries, CTEs, set operations, views, window functions, data quality checks, and safe database transactions.
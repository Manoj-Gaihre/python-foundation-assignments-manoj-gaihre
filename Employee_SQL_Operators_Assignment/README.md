# Day 8: SQL Operators and Employee Data Analysis

## Topics Covered

- Arithmetic Operators
- Comparison Operators
- Logical Operators
- `AND`
- `OR`
- `NOT`
- `LIKE`
- `IN`
- `BETWEEN`
- `IS NULL`
- `IS NOT NULL`
- SQL `WHERE` clause
- Column Aliases using `AS`
- Calculations using SQL expressions
- Filtering employee records
- Combining multiple SQL conditions
- PostgreSQL with Python
- Executing SQL queries using Python
- Fetching query results using `fetchall()`

## Exercises

1. Calculate increased salary using arithmetic operators.
2. Calculate reduced salary using arithmetic operators.
3. Calculate annual salary from monthly salary.
4. Calculate average monthly bonus.
5. Find the remainder of employee age using the modulus operator.
6. Calculate total compensation.
7. Find employees with salary greater than 100000.
8. Find employees younger than 30.
9. Find employees with a performance rating of 4.5 or higher.
10. Find employees with 5 or fewer years of experience.
11. Find employees working in the IT department.
12. Find employees whose employment status is not Active.
13. Find Kathmandu employees earning more than 100000.
14. Find employees from Kathmandu or Pokhara.
15. Find IT or Analytics employees with a performance rating greater than 4.
16. Find employees who are not remote workers.
17. Find Active employees younger than 40 with more than 5 years of experience.
18. Find Full-Time employees with salary greater than 80000 or performance rating greater than 4.5.
19. Find employees whose first name starts with `A`.
20. Find employees whose first name ends with `a`.
21. Find employees whose first name contains `i`.
22. Find employees whose last name starts with `S`.
23. Find employees whose job title contains `Analyst`.
24. Find employees whose email ends with `@company.com`.
25. Find employees from Kathmandu, Pokhara, or Lalitpur using `IN`.
26. Find employees from IT, Analytics, or Finance departments.
27. Find employees with Full-Time or Contract employment types.
28. Find employees with Bachelor, Master, or PhD education levels.
29. Find employees aged between 25 and 40.
30. Find employees with monthly salary between 80000 and 150000.
31. Find employees with performance rating between 3.5 and 4.5.
32. Find employees with 3 to 10 years of experience.
33. Find employees who joined between 2020 and 2024.
34. Find employees whose email is `NULL`.
35. Find employees whose phone is `NULL`.
36. Find employees whose emergency contact is `NULL`.
37. Find employees whose certification is `NULL`.
38. Find employees whose email and phone are `NOT NULL`.
39. Find Active employees from Kathmandu or Lalitpur with salary between 90000 and 180000.
40. Find IT or Analytics employees whose first name starts with `A` and performance rating is at least 4.
41. Find employees who are not Interns and have completed more than 5 projects.
42. Find employees whose certification or emergency contact is `NULL`.
43. Find Active employees whose job title contains `Manager`.
44. Find remote employees aged 30–50 with salary greater than 120000.
45. Calculate annual salary and total compensation for Finance, IT, and Analytics employees.
46. Find employees eligible for promotion with an Excellent performance category.
47. Find employees with 20–60 overtime hours and fewer than 15 leave days.
48. Find employees outside Kathmandu whose first name contains `u`.
49. Find employees with salary greater than 100000 or annual bonus greater than 150000.
50. Display employee details and calculate annual salary for Active employees.

## Assignment Project

Worked with an employee dataset containing **150 employee records and 29 columns**.

The project involved importing the employee dataset into a PostgreSQL database and writing SQL queries to analyze and filter employee information.

The assignment covered different types of SQL operators:

- Arithmetic operators for salary and compensation calculations.
- Comparison operators for filtering values.
- Logical operators for combining multiple conditions.
- `LIKE` for pattern matching.
- `IN` for checking multiple possible values.
- `BETWEEN` for filtering values within a range.
- `IS NULL` for finding missing values.
- `IS NOT NULL` for finding records where values are present.

The SQL queries were executed using Python and PostgreSQL, and the results were retrieved using `fetchall()`.

## What I Learned

During Day 8, I learned how SQL operators can be used to perform calculations, compare values, and filter records from a database.

I learned how arithmetic operators such as +, -, *, /, and % can be used to calculate values such as increased salary, reduced salary, annual salary, monthly bonus, and total compensation.

I learned how comparison operators such as >, <, >=, <=, =, and <> can be used to filter employee records based on conditions.

I learned how logical operators such as AND, OR, and NOT can be combined to create more specific filtering conditions.

I learned how the LIKE operator can be used for pattern matching. For example, A% finds values starting with A, %a finds values ending with a, and %i% finds values containing i.

I learned how the IN operator makes it easier to check whether a column contains one of several specified values.

I learned how the BETWEEN operator can be used to find values within a specific range, such as employees aged between 25 and 40 or employees earning between 80000 and 150000.

I also learned the difference between IS NULL and IS NOT NULL. IS NULL is used to find missing values, while IS NOT NULL is used to find records where a value exists.

I learned how SQL queries can be executed from Python using PostgreSQL and how fetchall() can be used to retrieve the query results.

## Challenges Faced

One challenge was understanding the difference between column names and values in SQL conditions. For example, when checking employment status, the correct condition is:
```
WHERE employment_status <> 'Active'
```

rather than comparing the numeric monthly_salary column with the text 'Active'.

Another challenge was understanding how AND and OR work together. I learned that parentheses are important when combining multiple conditions to make sure SQL evaluates the conditions in the intended order.

I also faced a challenge with IS NULL. Some missing values from the dataset were imported as the text 'NaN' instead of actual SQL NULL values. I learned that IS NULL only works with actual SQL NULL values.

For example:
```
WHERE email IS NULL
```
finds actual NULL values, while:
```
WHERE email = 'NaN'
```
finds the text NaN.

I also learned how to convert missing values to actual SQL NULL values when importing the dataset so that IS NULL and IS NOT NULL queries work correctly.

Another challenge was handling PostgreSQL transaction errors. When a SQL query fails, the transaction can become aborted. I learned that I can use:
```
conn.rollback()
```
to reset the transaction before running another query.
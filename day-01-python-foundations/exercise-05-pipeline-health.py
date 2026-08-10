# variables
rows_loaded = 9800
rows_failed = 200
runtime_minutes = 18

failure_percentage = (rows_failed / rows_loaded) * 100

if failure_percentage <= 2 and runtime_minutes <= 20:
    health_status = "Healthy"
elif failure_percentage > 2 and failure_percentage <=5:
    health_status = "Warning"
else:
    health_status = "Critical"


# display the results
print(f"Failure rate: {failure_percentage:.2f}%")
print(f"Final pipeline status: {health_status}")




#  testing with the following data
rows_loaded = 9500
rows_failed = 500
runtime_minutes = 15

failure_percentage = (rows_failed / rows_loaded) * 100


if failure_percentage <= 2 and runtime_minutes <= 20:
    health_status = "Healthy"
elif failure_percentage > 2 and failure_percentage <=5:
    health_status = "Warning"
else:
    health_status = "Critical"


# display the results
print(f"Failure rate: {failure_percentage:.2f}%")
print(f"Final pipeline status: {health_status}")




#  testing with the following data
rows_loaded = 9900
rows_failed = 100
runtime_minutes = 30

failure_percentage = (rows_failed / rows_loaded) * 100


if failure_percentage <= 2 and runtime_minutes <= 20:
    health_status = "Healthy"
elif failure_percentage > 2 and failure_percentage <=5:
    health_status = "Warning"
else:
    health_status = "Critical"


# display the results
print(f"Failure rate: {failure_percentage:.2f}%")
print(f"Final pipeline status: {health_status}")
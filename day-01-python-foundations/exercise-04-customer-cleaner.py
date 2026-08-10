raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

cleaned_name = raw_name.strip().title()
cleaned_city = raw_city.strip().lower().title()
cleaned_age = int(raw_age.strip())
cleaned_email = raw_email.strip().lower()


print(f"Name: {cleaned_name}")
print(f"City: {cleaned_city}")
print(f"Age: {cleaned_age}")
print(f"Email: {cleaned_email}")
Status = "Adult" if cleaned_age >= 18 else "Minor"
print(f"Status: {Status}")


# variables
user_role = "analyst"
is_active = True
requested_dataset = "sales_data"

# allowed roles and restricted datasets
allowed_roles = ["analyst", "scientist", "engineer"]
restricted_datasets = ["salary_data", "personal_data"]


if is_active:
    if user_role in allowed_roles:
            if requested_dataset not in restricted_datasets:
                print(f"Access granted to {requested_dataset} for {user_role}.")
            else:
                print(f"Access denied because the dataset '{requested_dataset}' is restricted.")
    else:
        print(f"Access denied because the user role '{user_role}' is not allowed.")
else:
    print("Access denied because the user is not active.")




# testing
# variables
user_role = "hr"
is_active = True
requested_dataset = "sales_data"

# allowed roles and restricted datasets
allowed_roles = ["analyst", "scientist", "engineer"]
restricted_datasets = ["salary_data", "personal_data"]


if is_active:
    if user_role in allowed_roles:
            if requested_dataset not in restricted_datasets:
                print(f"Access granted to {requested_dataset} for {user_role}.")
            else:
                print(f"Access denied because the dataset '{requested_dataset}' is restricted.")
    else:
        print(f"Access denied because the user role '{user_role}' is not allowed.")
else:
    print("Access denied because the user is not active.")




# testing with the another variables
# variables
user_role = "analyst"
is_active = False
requested_dataset = "sales_data"

# allowed roles and restricted datasets
allowed_roles = ["analyst", "scientist", "engineer"]
restricted_datasets = ["salary_data", "personal_data"]


if is_active:
    if user_role in allowed_roles:
            if requested_dataset not in restricted_datasets:
                print(f"Access granted to {requested_dataset} for {user_role}.")
            else:
                print(f"Access denied because the dataset '{requested_dataset}' is restricted.")
    else:
        print(f"Access denied because the user role '{user_role}' is not allowed.")
else:
    print("Access denied because the user is not active.")





# variables
user_role = "analyst"
is_active = True
requested_dataset = "salary_data"

# allowed roles and restricted datasets
allowed_roles = ["analyst", "scientist", "engineer"]
restricted_datasets = ["salary_data", "personal_data"]


if is_active:
    if user_role in allowed_roles:
            if requested_dataset not in restricted_datasets:
                print(f"Access granted to {requested_dataset} for {user_role}.")
            else:
                print(f"Access denied because the dataset '{requested_dataset}' is restricted.")
    else:
        print(f"Access denied because the user role '{user_role}' is not allowed.")
else:
    print("Access denied because the user is not active.")




# variables
user_role = "hr"
is_active = True
requested_dataset = "salary_data"

# allowed roles and restricted datasets
allowed_roles = ["analyst", "scientist", "engineer"]
restricted_datasets = ["salary_data", "personal_data"]


if is_active:
    if user_role in allowed_roles:
            if requested_dataset not in restricted_datasets:
                print(f"Access granted to {requested_dataset} for {user_role}.")
            else:
                print(f"Access denied because the dataset '{requested_dataset}' is restricted.")
    else:
        print(f"Access denied because the user role '{user_role}' is not allowed.")
else:
    print("Access denied because the user is not active.")




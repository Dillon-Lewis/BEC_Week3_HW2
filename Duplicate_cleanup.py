# Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. 
# Write a Python function to remove duplicates and display the unique customer IDs.

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
print(f'list of IDs with doubles: {customer_ids}')

set_list =set(customer_ids)
print(f"Unique customer IDs: {set_list}")



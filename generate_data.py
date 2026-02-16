import pandas as pd
import random
from datetime import datetime, timedelta

rows = []

start_date = datetime(2026, 1, 1)

for i in range(300):  # change to 1000 or 5000 if you want
    date = start_date + timedelta(days=i)
    
    duration = random.randint(60, 240)
    tasks = random.randint(1, 5)
    errors = random.randint(0, 3)

    rows.append([date, "E001", "Task", duration, tasks, errors])

df = pd.DataFrame(rows, columns=[
    "Date", "Employee_ID", "Task_Name",
    "Task_Duration(min)", "Tasks_Completed", "Errors"
])

df.to_csv("employee_productivity.csv", index=False)

print("Bulk dataset created successfully!")

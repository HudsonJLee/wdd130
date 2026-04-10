# HR System
# Author: Hudson Lee
# Reads employee data from hr_system.txt and displays paycheck amounts.
# Engineers receive a $1000 bonus added to their bimonthly paycheck.

with open("hr_system.txt") as file:
    for line in file:
        line = line.strip()
        parts = line.split()

        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])

        paycheck = salary / 24
        if job_title == "Engineer":
            paycheck += 1000

        print(f"{name} (ID: {id_number}), {job_title} - ${paycheck:.2f}")

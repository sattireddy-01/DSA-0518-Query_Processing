import pandas as pd

data = {
    "JOB_ID": [
        "AD_PRES", "AD_VP", "AD_ASST", "FI_MGR", "FI_ACCOUNT", "AC_MGR", "AC_ACCOUNT",
        "SA_MAN", "SA_REP", "PU_MAN", "PU_CLERK", "ST_MAN", "ST_CLERK", "SH_CLERK",
        "IT_PROG", "MK_MAN", "MK_REP", "HR_REP", "PR_REP"
    ],
    "JOB_TITLE": [
        "President", "Administration Vice President", "Administration Assistant",
        "Finance Manager", "Accountant", "Accounting Manager", "Public Accountant",
        "Sales Manager", "Sales Representative", "Purchasing Manager",
        "Purchasing Clerk", "Stock Manager", "Stock Clerk", "Shipping Clerk",
        "Programmer", "Marketing Manager", "Marketing Representative",
        "Human Resources Representative", "Public Relations Representative"
    ],
    "MIN_SALARY": [
        20080, 15000, 3000, 8200, 4200, 8200, 4200, 10000, 6000, 8000,
        2500, 5500, 2008, 2500, 4000, 9000, 4000, 4000, 4500
    ],
    "MAX_SALARY": [
        40000, 30000, 6000, 16000, 9000, 16000, 9000, 20080, 12008, 15000,
        5500, 8500, 5000, 5500, 10000, 15000, 9000, 9000, 10500
    ],
}

df = pd.DataFrame(data)

# Method 1: Using ascending=False with sort_values
sorted_jobs_1 = df.sort_values(by="JOB_TITLE", ascending=False)

# Method 2: Using ascending with a list
sorted_jobs_2 = df.sort_values(by=["JOB_TITLE"], ascending=[False])

# Method 3: Using reverse=True by applying sort on the index
sorted_jobs_3 = df.loc[df["JOB_TITLE"].sort_values(ascending=False).index]

# Method 4: Using iloc and applying argsort for custom sorting
sorted_jobs_4 = df.iloc[df["JOB_TITLE"].argsort()[::-1]]

# Method 5: Using sort_index after sorting the column
sorted_jobs_5 = df.loc[df["JOB_TITLE"].sort_values(ascending=False).index]

# Printing the results for all methods
print("Method 1: Using ascending=False with sort_values")
print(sorted_jobs_1)

print("\nMethod 2: Using ascending with a list")
print(sorted_jobs_2)

print("\nMethod 3: Using reverse=True by applying sort on the index")
print(sorted_jobs_3)

print("\nMethod 4: Using iloc and applying argsort for custom sorting")
print(sorted_jobs_4)

print("\nMethod 5: Using sort_index after sorting the column")
print(sorted_jobs_5)

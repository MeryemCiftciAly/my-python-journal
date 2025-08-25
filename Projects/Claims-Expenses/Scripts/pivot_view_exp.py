from utils import remove_duplicates, clean_text
import pandas as pd

print("Importing dataset")
url = "https://raw.githubusercontent.com/MeryemCiftciAly/my-python-journal/main/Projects/Claims-Expenses/Data/expense_claims.xlsx"

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)

#loading and reading the file
df = pd.read_excel(url, engine="openpyxl")


print("calling the duplicate function")
df = remove_duplicates(df)

clean_text_columns = ["Category", "Currency","EmployeeID"]
df = clean_text(df, clean_text_columns)

print("---Extracting year and month from date---")

df["Year"] = df["SubmitDate"].dt.year
df["Month"] = df["SubmitDate"].dt.month

print("--constructing a pivot table layout---")

pivot_table = df.pivot_table(
    index=["Year", "Category", "Currency"],
    columns="Month",
    values="Amount",
    aggfunc="sum",
    fill_value=0
).sort_index()

pivot_table["Total"] = pivot_table.sum(axis=1)
print(pivot_table)
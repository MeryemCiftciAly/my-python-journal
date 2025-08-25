from utils import remove_duplicates, clean_text
import pandas as pd

print("---Importing dataset---")
url = "https://raw.githubusercontent.com/MeryemCiftciAly/my-python-journal/main/Projects/Claims-Expenses/Data/expense_claims.xlsx"

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

#loading and reading the file
df = pd.read_excel(url, engine="openpyxl")
print(df.head())

print("---calling the duplicate function---")
df = remove_duplicates(df)

clean_text_columns = ["Status", "Currency","EmployeeID"]
df = clean_text(df, clean_text_columns)

print(df.head())

print("---\n#Grouping the expense by category\n---")

report_1 = (df.groupby(["Status", "Currency","EmployeeID"], as_index=False)["Amount"].sum()
)

print(report_1.head(5))
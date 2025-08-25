import pandas as pd

#---------------------------------------
# Option 1: Loading data from local file
#----------------------------------------

#Local_path = localpath/data.xlsx
#df = pd.read_excel(local_path)

print("""#---------------------------------------
# Option 12: Loading via url
#----------------------------------------\n""")
url = "https://raw.githubusercontent.com/MeryemCiftciAly/my-python-journal/main/Projects/Claims-Expenses/Data/expense_claims.xlsx"

#loading and reading the file
df = pd.read_excel(url, engine="openpyxl")

#Check the data after loading to show only 25 rows
print(df.head(25))

print("""
#------------------------------
# Cleaning the data
      --checking dup
      --trimming white space
      --checking distinct spelling in text-type data
      --converting PayDate to real date and time data type
#------------------------------\n""")

def remove_duplicates(df, remove=True):
    dup_count = df.duplicated().sum()
    if dup_count == 0:
        print(" No duplicates found.\n")
    else:
        print(f" Found{dup_count} duplicate rows.")
        if remove:
            df = df.drop_duplicates()
            print(f"{dup_count} duplictes removed.\n")
        else:
            print("Duplicates not removed.\n")
    return df

print("# making sure data in not truncated")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
df = remove_duplicates(df, remove=True)
print(df.head())

print("\n# Cleaning text columns by removing white spaces\n")

clean_columns = ["Category", "Description","Status", "ApprovedBy"]
for columns in clean_columns:
    df[columns] = df[columns].str.strip().str.title()

    print(f"\nDistinct values in '{columns}':")

    print(df[columns].unique(), "\n")
    

print("\n# Handling date, making sure date is of type date and not strings\n")

df["PayDate"] = pd.to_datetime(df["PayDate"], errors = "coerce")
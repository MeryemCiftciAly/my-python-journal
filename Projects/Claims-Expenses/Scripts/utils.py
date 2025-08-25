print("#putting all reusable codes here so as not to retype")

import pandas as pd
import datetime
import time

def remove_duplicates(df, remove=True):
    dup_count = df.duplicated().sum()
    if dup_count > 0 and remove:
        df = df.drop_duplicates()
    return df


def clean_text(df, columns):      
    for col in columns:
        df[col] = df[col].str.strip().str.title()
    return df
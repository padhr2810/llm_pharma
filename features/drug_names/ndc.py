
import pandas as pd
from json import loads, dumps

# ndc = pd.read_csv("20220906_package.csv")
ndc_df = pd.read_csv("20220906_product.csv")

cols = ndc_df.columns
print(f"cols = {cols}")
print(ndc_df.head())

ndc_df = ndc_df[["productndc", "proprietaryname", "nonproprietaryname"]]
ndc_df["drug_list"] = "[\"" + ndc_df["proprietaryname"] + "\", \"" + ndc_df["nonproprietaryname"] + "\"]"

print("\n\nDrug List!!!\n\n")
print(ndc_df["drug_list"] )
print("\n\nproductndc!!!\n\n")
print(ndc_df["productndc"] )

ndc_df["productndc"] = ndc_df["productndc"].replace({'-':''}, regex=True)
ndc_df = ndc_df[["productndc", "drug_list"]]
ndc_df["drug_list"] = ndc_df["drug_list"].str.lower() 

result = dict(zip(ndc_df.productndc, ndc_df.drug_list))

print("\n\n")
print(result)

import sqlite3
conn = sqlite3.connect("qn.db")
ndc_df.to_sql("ndc_table", conn, if_exists="replace", index=False)
back_from_sql_df = pd.read_sql("select * from ndc_table", conn)
print("\n\nSuccessfully read from the sqlite db!!!")

print(f"\n\nback_from_sql_df = {back_from_sql_df.head()}")


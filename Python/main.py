import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:gowshi@127.0.0.1:3306/powerbi_db"
)

df = pd.read_sql("SELECT * FROM filterdata", engine)

print("Database connected successfully")
print(df.head())
print(df.describe())
print(np.mean(df['Tenure']))
print(np.where(df['Tenure'] > 12, 'Long Term', 'Short Term'))
df.to_sql(
    name="customer_table",   # new table name
    con=engine,
    if_exists="replace",     # overwrite if exists
    index=False,

    method="multi"
)

print("Cleaned data saved to SQL as customer_table")




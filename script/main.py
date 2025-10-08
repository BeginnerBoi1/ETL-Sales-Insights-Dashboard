
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import mysql.connector
data = pd.read_csv('Superstore.csv', encoding='latin1')
data.columns = data.columns.str.replace(' ', '_')
data.drop(columns=['Row_ID', 'Postal_Code', 'Customer_Name', 'Country', 'Product_ID'], inplace=True)


class DataCleaner:
    def __init__(self, dataframe):
        self.data = dataframe

    def normalize_column_names(self):
        self.data.columns = self.data.columns.str.lower()

    def parse_dates(self, date_columns):
        for col in date_columns:
            self.data[col] = pd.to_datetime(self.data[col], errors='coerce')

    def convert_to_numeric(self, numeric_columns):
        for col in numeric_columns:
            self.data[col] = pd.to_numeric(self.data[col], errors='coerce')

    def clean_strings(self):
        for col in self.data.select_dtypes(include=['object']).columns:
            self.data[col] = self.data[col].astype(str).str.strip().str.replace(r'[^\x00-\x7F]+', '', regex=True)
            self.data[col].replace({'nan': None}, inplace=True)

    def drop_duplicates(self):
        self.data.drop_duplicates(inplace=True)

    def add_surrogate_id(self):
        if 'surrogate_id' not in self.data.columns:
            self.data.insert(0, 'surrogate_id', range(1, len(self.data) + 1))

    def summarize_nulls(self):
        print('Null counts:\n', self.data.isnull().sum())

    def connect_to_db(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
    def display_data(self):
        print(self.data.head())


# test
cleaner = DataCleaner(data)
cleaner.normalize_column_names()
cleaner.parse_dates(['order_date', 'ship_date'])
cleaner.convert_to_numeric(['sales', 'quantity', 'discount', 'profit'])
cleaner.clean_strings()
cleaner.drop_duplicates()
cleaner.add_surrogate_id()
cleaner.summarize_nulls()
cleaner.display_data()

# connect to MySQL database
try:
    cleaner.connect_to_db("localhost", "root", "yourpassword", "etl_project")
    if cleaner.conn.is_connected():
        print("Connected to MySQL database")
except mysql.connector.Error as err:
    print("Connection failed")

engine = create_engine("mysql+mysqlconnector://root:yourpassword@localhost/etl_project")
data.to_sql('sales_data', con=engine, if_exists='replace', index=False)
print("Data successfully loaded into MySQL table 'sales_data'!")

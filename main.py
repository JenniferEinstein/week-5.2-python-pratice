import pandas as pd
import numpy as np
import smtplib
from email.message import EmailMessage

#  ====  INPUTS ====  #
# print("Enter your name: ")
# name = input()
# print("Enter the email you want to receive the report: ")
# email = input()

def load_data():
    return pd.read_csv('data/october-2024.csv')

df = load_data()

# Set the display option for left alignment
pd.set_option('display.colheader_justify', 'left')


# The load_data() function reads a CSV file from the data directory and loads it into a Pandas DataFrame. This DataFrame will contain all the customer data from the CSV file, making it ready for further analysis and manipulation using Pandas. We've placed this DataFrame in the variable df.


def explore_dataframe(df):
    print("First 5 rows:")
    print(df.to_string(justify='left'))
    # print(df.head())


print("\n1. Exploring the DataFrame")
explore_dataframe(df)

def data_selection(df):
    print("Selecting 'Description' and 'Amount' columns:")
    print(df[['Description', 'Amount']].head())
    
    print("\nFiltering charges over $100:")
    print(df[df['Amount'] < -100].head())
    
    print("\nUsing loc to select specific rows and columns:")
    print(df.loc[10:14, ['Date', 'Description', 'Amount']])


print("\n2. Data Selection and Indexing")
data_selection(df)

def data_operations(df):
    print("Data operations")




#  ====  EMAIL ====  #

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# # Open the plain text file whose name is in textfile for reading.
# with open(textfile) as fp:
#     # Create a text/plain message
#     msg = EmailMessage()
#     msg.set_content(fp.read())


# msg['Subject'] = f'The contents of {textfile}'
# msg['From'] = name
# msg['To'] = email

# # Send the message via our own SMTP server.
# s = smtplib.SMTP('localhost')
# s.send_message(msg)
# s.quit()



# ------ CODE I DON'T NEED ----------

# def explore_dataframe(df):
#     print("First 5 rows:")
#     print(df.head())
    
#     print("\nDataFrame Info:")
#     print(df.info())
    
#     print("\nSummary Statistics:")
#     print(df.describe())


#  ===================
# print("This is a credit card reconciliation app with reporting tools")
# print("Software engineer: Jennifer Einstein")
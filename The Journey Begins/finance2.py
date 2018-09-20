import csv
import sqlite3

# Create the database
connection = sqlite3.connect('C:/PYTHON_SCRIPTS/btc_hourly.sqlite')
cursor = connection.cursor()

# Create the table
cursor.execute('DROP TABLE IF EXISTS btc_hourly')
cursor.execute('CREATE TABLE  btc_hourly (Open integer, High integer, Low integer, Close integer) ')
connection.commit()

# Load the CSV file into CSV reader
csvfile = open('C:/Users/mzecchini1989/Downloads/Coinbase_BTCUSD_1h.csv', 'r')
creader = csv.reader(csvfile, delimiter=',', quotechar='|')

# Iterate through the CSV reader, inserting values into the database
cursor.executemany('INSERT INTO  btc_hourly (Open, High, Low, Close) VALUES (?,?,?,?)',  )

# Close the csv file, commit changes, and close the connection
csvfile.close()
connection.commit()
connection.close()

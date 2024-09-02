import mysql.connector
from mysql.connector import Error
from flask import current_app
import os

import mysql.connector
from mysql.connector import Error
from flask import current_app
import os

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            database=current_app.config['MYSQL_DB']
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connected to MySQL Server version {db_info}")
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print(f"You're connected to database: {record}")
        
        return connection

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None


def fetch_last_10_records(connection):
    try:
        if connection is None:
            print("No connection to database.")
            return []

        cursor = connection.cursor()
        query = "SELECT * FROM smartlead_campaign_emails ORDER BY id DESC LIMIT 10"
        cursor.execute(query)

        # Fetch all the rows
        records = cursor.fetchall()

        # print("Last 10 records from smartlead_campaign_emails:")
        # for row in records:
        #     print(row)
        
        return records

    except Error as e:
        print(f"Error fetching records: {e}")
        return []

    finally:
        if cursor:
            cursor.close()


def fetch_last_50_records(connection):
    try:
        if connection is None:
            print("No connection to database.")
            return []

        cursor = connection.cursor()
        query = "SELECT * FROM smartlead_campaign_emails ORDER BY id DESC LIMIT 50"
        cursor.execute(query)

        # Fetch all the rows
        records = cursor.fetchall()

        # print("Last 50 records from smartlead_campaign_emails:")
        # for row in records:
        #     print(row)
        
        return records

    except Error as e:
        print(f"Error fetching records: {e}")
        return []

    finally:
        if cursor:
            cursor.close()

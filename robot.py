import random
import pymysql
import time

# Establishing a connection to the database
connection = pymysql.connect(
    host='68.178.151.243',
    user='achha',
    password='achha@123',
    db='skilancersolar',
    connect_timeout=30
)

# Creating a cursor object
cursor = connection.cursor()

# Creating a table for storing sensor data
table_create_query = '''
    CREATE TABLE IF NOT EXISTS sensor (
        ID INT NOT NULL AUTO_INCREMENT,
        total_runs INT NOT NULL,
        runtime_today INT NOT NULL,
        V_panel FLOAT NOT NULL,
        V_battery FLOAT NOT NULL,
        temperature FLOAT NOT NULL,
        PRIMARY KEY (ID)
    )
'''
cursor.execute(table_create_query)

# Inserting random sensor data into the table
add_data=True
while add_data:
    total_runs = int(input("Enter the total run"))
    runtime_today = int(input("Enter the runtime today"))
    V_panel = int(input("Enter the v_panel in interger"))
    V_battery = int(input("Enter the  v_battery in integer"))
    temperature = int(input("Enter the temperature in integer"))
    
    insert_query = f"""
        INSERT INTO sensor (
            total_runs,
            runtime_today,
            V_panel,
            V_battery,
            temperature
        ) VALUES (
            {total_runs},
            {runtime_today},
            {V_panel},
            {V_battery},
            {temperature}
        )
    """
    cursor.execute(insert_query)
    connection.commit()
    print("Data added to the sensor_data table.")
    choice = input("Do you want to add another person? (y/n): ")
    if choice.lower() == "n":
        add_data = False
    time.sleep(1)
# Closing the cursor and connection
cursor.close()
connection.close()

import os
from azure.data.tables import TableServiceClient
import pandas as pd
from dotenv import load_dotenv
load_dotenv(override=True)
# Make sure your connection string is set in the environment
connection_string = os.getenv("AZURE_TABLES_CONNECTION_STRING")
table_name = os.getenv("AZURE_TABLES_TABLE_NAME")

# Create the TableServiceClient from the connection string
service_client = TableServiceClient.from_connection_string(conn_str=connection_string)
table_client = service_client.get_table_client(table_name=table_name)

def get_table_data():
    # List entities from the table and convert them into a pandas DataFrame
    entities = list(table_client.list_entities())
    df = pd.DataFrame(entities)
    
    # Export the DataFrame to a CSV file
    df.to_csv("azure_table_export.csv", index=False)
    print("Data exported successfully using connection string!")
    return df

# if __name__ == "__main__":
#     get_table_data()

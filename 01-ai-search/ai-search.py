from openai import AzureOpenAI
import pandas as pd
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient 
from utils.storage_functions import get_table_data
import requests
import json
import os
from dotenv import load_dotenv
import traceback

load_dotenv(override=True)

SEARCH_ENDPOINT = os.getenv("SEARCH_ENDPOINT")
INDEX_NAME = os.getenv("INDEX_NAME")
SEARCH_KEY = os.getenv("SEARCH_QUERY_KEY")
AOAI_API_KEY = os.getenv("AOAI_API_KEY")
AOAI_ENDPOINT = os.getenv("AOAI_ENDPOINT")
AOAI_API_VERSION = os.getenv("AOAI_API_VERSION")
AOAI_MODEL = os.getenv("AOAI_MODEL")
SEARCH_ADMIN_KEY = os.getenv("SEARCH_ADMIN_KEY")
STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")

def get_embeddings(text):
  # print(f"Getting embeddings for text: {text}")
  try:
    openai_client = AzureOpenAI(
      api_key = AOAI_API_KEY,
      api_version = AOAI_API_VERSION,
      azure_endpoint = AOAI_ENDPOINT
    )
    
    embedding = openai_client.embeddings.create(
      input = text,
      model= AOAI_MODEL
    ).data[0].embedding
  except Exception as e:
    print(f"Error getting embeddings for text: {text}")
    print(f"Error: {e}")
  
  return embedding

def createIndex(index_name):
  print("Creating index...")
  print(f"SEARCH_ADMIN_KEY = {SEARCH_ADMIN_KEY}")
  headers = {
    "Content-Type": "application/json",
    "api-key": SEARCH_ADMIN_KEY
  }

  with open("index_definition.json", "r", encoding="utf-8") as f:
    index_definition = json.load(f)

  index_definition["name"] = index_name
  print(f"Current api-key: {index_definition['vectorSearch']['vectorizers'][0]['azureOpenAIParameters']['apiKey']}")
  index_definition['vectorSearch']['vectorizers'][0]['azureOpenAIParameters']['apiKey'] = AOAI_API_KEY
  print(f"Updated api-key: {index_definition['vectorSearch']['vectorizers'][0]['azureOpenAIParameters']['apiKey']}")
  endpoint = f"{SEARCH_ENDPOINT}/indexes/{index_name}?api-version=2024-11-01-Preview"
  # Send the PUT request to create or update the index
  response = requests.put(endpoint, headers=headers, data=json.dumps(index_definition))
  
  if 200 <= response.status_code < 300:
    print("Index created or updated successfully!")
  else:
    print(f"Failed to create or update index. Status code: {response.status_code}")


def uploadIndexContent():
  # Creates an index over a CSV that follows the schema of the ServiceCatalogData.csv
  # Manually creates index rather than using the Indexer API

  credential = AzureKeyCredential(SEARCH_ADMIN_KEY)
  search_client = SearchClient(SEARCH_ENDPOINT, INDEX_NAME, credential)

  docs_to_upload = []

  # df = pd.read_csv(file_path)
  df = get_table_data()

  print(df.head())
  print(df.columns)
  count = 0
  metadata_storage_path = f"https://{STORAGE_ACCOUNT_NAME}.table.core.windows.net/DSWtest"


  BATCH_SIZE = 100
  for i, row in df.iterrows():
    
    # if i<152 or i>155:
    #   continue
    #Skip headers
    try:
      doc = {
        "id": str(i),
        "category": row["Category"],
        "categoryVector": get_embeddings(row["Category"]),
        "categoryDescription": row["CategoryDescription"],
        "categoryDescriptionVector": get_embeddings(row["CategoryDescription"]),
        "DefaultTeam": row["DefaultTeam"],
        "defaultTeamVector": get_embeddings(row["DefaultTeam"]),
        "Organization": row["Organization"],
        "organizationVector": get_embeddings(row["Organization"]),
        "Service": row["Service"],
        "serviceVector": get_embeddings(row["Service"]),
        "metadata_storage_path": metadata_storage_path
      }

      # print(f"{i}: {doc}")
      # print(f"Uploading document {i}...{doc}")
      docs_to_upload.append(doc)

      #Uncomment to test with a small number of documents
      # if count>5:
      #   break
      # count += 1

      if len(docs_to_upload) == BATCH_SIZE:
          response = search_client.upload_documents(documents=docs_to_upload)
          print(f"Uploaded a batch of {BATCH_SIZE} documents. Response: {response}")
          docs_to_upload = []  # Clear the list for the next batch

    except Exception as e:
      print(f"Error uploading document {i}: {e}:\n")
      continue
      

  # Upload the documents to the index
  response = search_client.upload_documents(documents=docs_to_upload)
  print(response)
if __name__ == '__main__':
  createIndex(INDEX_NAME)
  uploadIndexContent()
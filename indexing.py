from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import pandas as pd
import re
import json

# define azure search settings
service_name = '<service_name>'
index_name = '<index_name>'
admin_key = '<admin_key>'
endpoint = f"https://{service_name}.search.windows.net/"
credential = AzureKeyCredential(admin_key)

# load data into a dataframe

filepath = 'db/customer_support_tickets.csv'
df = pd.read_csv(filepath)

#initialize the search client
search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=credential)

# upload data to the index
data = []

for _, row in df.iterrows():
    data.append({
        "@search.action": "upload",
        "TicketID": str(row['Ticket ID']),
        "TicketType": row['Ticket Type'],
        "TicketSubject": row['Ticket Subject'],
        "TicketDescription": row['Ticket Description'],
        "TicketStatus": row['Ticket Status'],
        "TicketPriority": row['Ticket Priority'], 
        "TicketChannel": row['Ticket Channel']     
    })

result = search_client.upload_documents(data)
print("Upload result: ",result)
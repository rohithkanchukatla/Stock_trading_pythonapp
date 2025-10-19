import requests
import openai
import os
import csv
from dotenv import load_dotenv
load_dotenv()

def run_job():
    
    POLYGON_API_KEY=os.getenv("POLYGON_API_KEY")

    url=f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit=100&sort=ticker&apiKey={POLYGON_API_KEY}"

    response=requests.get(url)
    data=response.json()
    ticker_list=[]

    # print(len(ticker_list))
    while 'next_url' in data:
        response=requests.get(data['next_url']+f'&apikey={POLYGON_API_KEY}')

        data = response.json()
        # print(data)
        if 'results' in data and isinstance(data['results'], list):
            for ticker in data['results']:
                ticker_list.append(ticker)
        else:
                # Handle cases where the request was 200 but the body is unexpected (e.g., end of data)
            # print("Response is missing the 'results' key or it's not a list. Stopping pagination.")
            # print("Last received data:", data) # Print to debug the final response
            break # Exit the loop safely
    print(len(ticker_list))
    
# field_names=ticker_list[0].keys()

# print(field_names)

# with open("tickers.csv",mode="a",newline="") as file:

#     writer=csv.DictWriter(file,field_names)
    
#     for t in ticker_list:
#         writer.writerow(t)


if __name__=="main":
    run_job()


    









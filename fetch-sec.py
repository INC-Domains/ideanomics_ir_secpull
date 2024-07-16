import requests
import json

# Function to fetch SEC filings data
def fetch_sec_data(cik):
    base_url = f'https://data.sec.gov/submissions/CIK{cik}.json'
    headers = {'User-Agent': 'Intercap cristy@intercap.com'}
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        filings = data['filings']['recent']
        filing_data = []
        for i in range(len(filings['accessionNumber'])):
            form_and_file = filings['form'][i]
            file_date = filings['filingDate'][i]
            reporting_date = filings['reportDate'][i] if 'reportDate' in filings else 'N/A'
            form_and_file_reporting_date = f"{form_and_file} ({reporting_date})"
            file_link = f"https://www.sec.gov/Archives/edgar/data/{cik}/{filings['accessionNumber'][i].replace('-', '')}/{filings['primaryDocument'][i]}"
            
            # Ensure no duplicate keys
            filing_entry = {
                'Form & File': form_and_file,
                'File date': file_date,
                'Reporting for date': reporting_date,
                'Filing Type': form_and_file_reporting_date,
                'File link': file_link  # Ensure only one 'File link' key
            }
            filing_data.append(filing_entry)
        return filing_data, response.status_code
    else:
        print(f"Failed to fetch SEC data. Status code: {response.status_code}")
        return None, response.status_code

# Function to update Google Sheet with all data at once
def update_google_sheet(data):
    api_url = "https://script.google.com/macros/s/AKfycbxFYoa1afrynauW72fhn7jkkC5S0xT86zfK03g0XZugJwAma2hu9aMy4fbhtRVlD1tW/exec"  # Replace with your API URL
        # Convert data to JSON format
    json_data = json.dumps(data)
    # Set headers with content type
    headers = {'Content-Type': 'application/json'}
    print("Sending the following data to Google Sheets API:")
    
    try:
        # Send POST request with headers and JSON data
        response = requests.post(api_url, headers=headers, data=json_data)
        
        # Check response status
        if response.status_code == 200:
            print('Data inserted successfully.')
        else:
            print(f'Failed to insert data. Status Code: {response.status_code}')
            print('Response Text:', response.text)
            
    except requests.exceptions.RequestException as e:
        print('Error occurred:', e)

# Main function
def main():
    # Define the CIK for the company (IDEANOMICS, INC.)
    cik = '0000837852'
    data, status_code = fetch_sec_data(cik)
    if status_code == 200:
        print("Data fetched successfully from SEC.")
        print("Data to be sent to Google Sheets API:")
        update_google_sheet(data)
    else:
        print(f"Failed to fetch data: {status_code}")

if __name__ == '__main__':
    main()

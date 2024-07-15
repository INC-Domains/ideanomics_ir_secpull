import requests
import pandas as pd

# Define the CIK for the company (IDEANOMICS, INC.)
cik = '0000837852'
# Define the base URL for the EDGAR API
base_url = f'https://data.sec.gov/submissions/CIK{cik}.json'

# Fetch the data from the EDGAR API
headers = {'User-Agent': 'Intercap cristy@intercap.com'}
response = requests.get(base_url, headers=headers)

# Check if the request was successful
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

        filing_data.append({
            'Form & File': form_and_file,
            'File date': file_date,
            'Reporting for date': reporting_date,
            'Filing Type': form_and_file_reporting_date,
            'File link': file_link
        })

    # Save the scraped data to an Excel file
    df = pd.DataFrame(filing_data)
    df.to_excel('sec_filings.xlsx', index=False)
    print('Data saved to sec_filings.xlsx')
else:
    print(f"Failed to fetch data: {response.status_code}")


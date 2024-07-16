# ideanomics_ir_secpull
Python code to pull SEC filings from EDGAR for ideanomics

1. In your google sheet, go to Extensions -> App Script
2. Add the scripts from gsheet-appscript folder
3. Create a button in the sheet and assign it to clearSheet
4. Deploy app script : Deploy -> New Development -> Select type -> Web app 
5. Set "Who has access" to Anyone
6. Authorize
7. Copy Web App Url (will serve as API)
8. Use the API url in python code
9. Run fetch-sec.py

NOTE: Click the button previously created in the sheet to remove the contents before adding new set of data.
